# Import the 'settings' module from the parent directory
import os
import sys
from settings import DATABASES
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Define the database configuration
DATABASE_CONFIG = DATABASES['default']
