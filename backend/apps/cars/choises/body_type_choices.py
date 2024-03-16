import os

# Set the path to the `choices` directory
choices_dir = '/path/to/your/project/apps/cars/choices'

# Create the `body_type_choices.py` file
body_type_file = os.path.join(choices_dir, 'body_type_choices.py')
with open(body_type_file, 'w') as f:
    f.write('BODY_TYPE_CHOICES = (\n')
    f.write('    ("SEDAN", "Sedan"),\n')
    f.write('    ("HATCHBACK", "Hatchback"),\n')
    f.write('    ("COUPE", "Coupe"),\n')
    f.write('    ("CONVERTIBLE", "Convertible"),\n')
    f.write('    ("SUV", "SUV"),\n')
    f.write('    ("TRUCK", "Truck"),\n')
    f.write('    ("VAN", "Van"),\n')
    f.write(')\n')