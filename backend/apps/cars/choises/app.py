import os

# Set the path to the parent directory of the `choices` directory
parent_dir = '/path/to/your/project/apps/cars'

# Create the `choices` directory
choices_dir = os.path.join(parent_dir, 'choices')
os.makedirs(choices_dir, exist_ok=True)