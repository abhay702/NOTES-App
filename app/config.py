from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Database connection
try:
    conn = MongoClient("mongodb+srv://abhayrathore487:Pass%4012345678@notepadapp.zzw2pcu.mongodb.net/")
    db = conn.Notebook  
    notes_collection = db.Notes  
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    raise e
