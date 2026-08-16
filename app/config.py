import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env file from the project root
load_dotenv(BASE_DIR / ".env")

# Read the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Validate the API key
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

if not VIRUSTOTAL_API_KEY:
    raise ValueError("VIRUSTOTAL_API_KEY not found. Please check your .env file.")

# Default Gemini model
DEFAULT_MODEL = "models/gemini-flash-latest"