from dotenv import load_dotenv
import os

# Call load_dotenv function from dotenv module to load environment variables
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    
    # Mail configuration
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True") == "True"
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "False") == "True"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    MAIL_DEBUG = os.environ.get("MAIL_DEBUG", "False") == "True"
    MAIL_SUPPRESS_SEND = os.environ.get("MAIL_SUPPRESS_SEND", "False") == "True"
    MAIL_ASCII_ATTACHMENTS = os.environ.get("MAIL_ASCII_ATTACHMENTS", "False") == "True"   