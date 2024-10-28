import os
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import joblib
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import logging

# Load environment variables from .env file
load_dotenv()

# Get environment variables
EMAIL_USER = os.getenv('CATCH_EMAIL_USER')  # Your catch email
EMAIL_PASS = os.getenv('CATCH_EMAIL_PASS')  # Your email password

# Load your trained model and vectorizer
model = joblib.load('phishing_detection_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def classify_email(email_content):
    """Classifies the email content as phishing or legitimate."""
    email_vectorized = vectorizer.transform([email_content])
    prediction = model.predict(email_vectorized)
    return prediction[0]  # 0 for legitimate, 1 for phishing

def check_email():
    """Checks the inbox for unread emails and classifies them."""
    try:
        mail = imaplib.IMAP4_SSL('outlook.office365.com')
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select('inbox')

        # Search for all unread emails
        result, data = mail.search(None, 'UNSEEN')
        email_ids = data[0].split()

        for email_id in email_ids:
            # Fetch the email
            result, msg_data = mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Get email content
            email_content = ''
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        email_content = part.get_payload(decode=True).decode()
                        break
            else:
                email_content = msg.get_payload(decode=True).decode()

            # Classify the email
            is_phishing = classify_email(email_content)
            
            # Prepare the response
            response = MIMEMultipart()
            response['From'] = EMAIL_USER
            response['To'] = msg['From']
            response['Subject'] = 'Email Classification Result'

            if is_phishing == 1:
                body = "The email provided is a phishing email."
            else:
                body = "The email provided is legitimate."
            
            response.attach(MIMEText(body, 'plain'))
            
            # Send the response
            with smtplib.SMTP('smtp.outlook.com', 587) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                server.send_message(response)
                
            logging.info(f'Response sent to: {msg["From"]} - Classification: {"Phishing" if is_phishing == 1 else "Legitimate"}')

    except Exception as e:
        logging.error(f'Error checking emails: {str(e)}')
    
    finally:
        mail.logout()

def start_email_checking():
    """Starts the email checking scheduler."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_email, 'interval', minutes=1)  # Check every minute
    scheduler.start()
    logging.info("Started email checking scheduler.")

# Flask app initialization
app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

@app.route('/classify', methods=['POST'])
def classify_endpoint():
    """Endpoint to classify email content provided in the request body."""
    try:
        data = request.get_json()
        email_content = data.get('email_content')
        
        if not email_content:
            return jsonify({'error': 'No email content provided'}), 400
            
        prediction = classify_email(email_content)
        
        return jsonify({
            'result': 'phishing' if prediction == 1 else 'legitimate',
            'confidence': float(prediction)
        })
        
    except Exception as e:
        logging.error(f'Error in classify_endpoint: {str(e)}')
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    start_email_checking()
    app.run(host='0.0.0.0', port=8080)
