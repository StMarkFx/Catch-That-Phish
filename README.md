# 🎣 Catch That Phish 

Catch That Phish is a sophisticated email monitoring and classification service that helps protect against phishing attacks. This service combines real-time email monitoring with machine learning to automatically detect and respond to potential phishing attempts.

## 🌟 Features

- **Real-time Email Monitoring**: Automatically scans incoming emails for phishing attempts
- **ML-Powered Classification**: Utilizes machine learning to accurately identify phishing emails
- **Automatic Responses**: Sends immediate classification results to email senders
- **REST API Integration**: Provides an HTTP endpoint for external service integration
- **Detailed Logging**: Comprehensive logging system for monitoring and debugging

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Outlook email account
- Trained ML model files (`phishing_detection_model.pkl` and `vectorizer.pkl`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/catch-that-phish.git
   cd catch-that-phish
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   Create a `.env` file:
   ```env
   CATCH_EMAIL_USER=your-outlook-email@outlook.com
   CATCH_EMAIL_PASS=your-email-password
   ```

## 💻 Usage

### Starting the Service

Run the main application:
```bash
python catch_that_phish.py
```

The service will:
- Start monitoring your email inbox
- Check for new emails every minute
- Launch the API server on port 8080

### API Documentation

#### Classify Email Content

**Endpoint:**
```
POST /classify
```

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "email_content": "Email content to classify"
}
```

**Response:**
```json
{
  "result": "phishing",
  "confidence": 1.0
}
```

## 🏗️ Architecture

The service consists of three main components:

1. **Email Monitor**
   - Connects to Outlook email server
   - Processes unread emails
   - Sends automatic responses

2. **Classification Engine**
   - Uses pre-trained ML model
   - Vectorizes email content
   - Provides binary classification (phishing/legitimate)

3. **Web API**
   - RESTful endpoint for classification
   - CORS-enabled for cross-origin requests
   - Error handling and logging

## 🔒 Security Considerations

- Store sensitive credentials in `.env` file
- Never commit `.env` file to version control
- Regularly update dependencies
- Monitor API access patterns
- Review email server security settings

## 🛠️ Development

### Project Structure
catch-that-phish/
├── catch_that_phish.py
├── requirements.txt
├── .env
├── .gitignore
├── phishing_detection_model.pkl
└── vectorizer.pkl

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Submit a pull request

## 📝 Logging

The service includes comprehensive logging:
- Email processing status
- Classification results
- Error tracking
- API request handling

Logs are formatted with timestamps and severity levels.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

St. Mark Adebayo - stmarkadebayo@gmail.com
Catch me on [X](https://x.com/_calvaryforex) and
[LinkedIn](https://www.linkedin.com/in/stmarkadebayo)

Project Link: [https://github.com/your-username/catch-that-phish](https://github.com/your-username/catch-that-phish)

## 🙏 Acknowledgments
- Al-Subaiey, A., Al-Thani, M., Alam, N. A., Antora, K. F., Khandakar, A., & Zaman, S. A. U. (2024, May 19). Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection. ArXiv.org. https://arxiv.org/abs/2405.11619
- scikit-learn for ML capabilities
- Flask for web framework
- APScheduler for task scheduling
