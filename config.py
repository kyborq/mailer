import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SMPT_SERVER = os.getenv('SMPT_SERVER')
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
