# Import the 'settings' module from the parent directory
import os
import sys
from settings import DATABASES
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Define the database configuration
DATABASE_CONFIG = DATABASES['default']


class Model:
    pass


class Column:
    pass


def session():
    return None


class String:
    pass


class Integer:
    pass


class ForeignKey:
    pass


def backref(param, lazy):
    return None


def relationship(param, backref):
    return None