from dotenv import load_dotenv
import os
#Call load_dotenv function from dotenv module to load environment variables in env in os
load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") #use os module to get database uri value 
    