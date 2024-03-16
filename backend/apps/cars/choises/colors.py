import os

# Set the path to the `choices` directory
choices_dir = '/path/to/your/project/apps/cars/choices'


init_file = os.path.join(choices_dir, '__init__.py')
with open(init_file, 'w') as f:
    pass

# Create the `colors.py` file
colors_file = os.path.join(choices_dir, 'colors.py')
with open(colors_file, 'w') as f:
    f.write('COLORS = (\n')
    f.write('    ("BLACK", "Black"),\n')
    f.write('    ("WHITE", "White"),\n')
    f.write('    ("RED", "Red"),\n')
    f.write('    ("BLUE", "Blue"),\n')
    f.write('    ("GREEN", "Green"),\n')
    f.write('    ("YELLOW", "Yellow"),\n')
    f.write('    ("SILVER", "Silver"),\n')
    f.write('    ("GRAY", "Gray"),\n')
    f.write(')\n')