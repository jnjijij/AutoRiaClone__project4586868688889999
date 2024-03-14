# Import the 'settings' module from the parent directory
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import DATABASES

# Define the database configuration
DATABASE_CONFIG = DATABASES['default']