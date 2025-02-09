# 🌍 AI-Powered Multilingual Email Responder
## Respond to Customers in Seconds

AI-Powered Multilingual Email Responder is a FastAPI-based web application that utilizes the OpenAI API (model: GPT-3.5-turbo)  to generate automated email responses. The application provides a simple interface for users to input customer emails, generate AI-powered replies, and translate responses into multiple languages. It also integrates with Gmail for quick email replies, making customer communication more efficient and streamlined.

## Features
- Generate AI-powered email responses using OpenAI API.
- Automatically detect and extract the subject line.
- Preserve email formatting with proper spacing.
- Translate responses into multiple languages (English, Hindi, Urdu, Arabic, French, Spanish).
- One-click integration with Gmail for replying to customers.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.10+
- FastAPI
- Uvicorn
- OpenAI API key

## Installation

### 1. Clone the Repository
```
git clone https://github.com/saqiba123/AI-Email-Responder.git
cd auto-email-responder
```
### 2. Create python environment
```
python -m venv email_env
source email_env/bin/activate  # On macOS/Linux
email_env\Scripts\activate     # On Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Start the FastAPI server
```
  uvicorn main:app --reload
```



