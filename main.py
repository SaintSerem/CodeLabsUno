import pandas as pd

from Functions import generate_unique_email, read_data, write_data, fix_date_format
from Constraints import validate_data,is_valid_email_format
# Replace with your actual file path
input_file = "C:\\Users\\brian\\OneDrive\\Documents\\Test Files.xlsx"
output_file = "output.xlsx"

# Read data from the excel (Test Files)
data = read_data(input_file)

# Optional: Fix DoB format (if DoB column exists)
# Uncomment the following line if you want to fix the DoB format
data = fix_date_format(data)

# Check if data was read successfully
if data is not None:
    # Adding the email addresses to the column
    data['Email Address'] = data['Student Name'].apply(generate_unique_email, args=(data,))

    # Write modified data to a new Excel file
    write_data(data, output_file)
else:
    print("Error: Unable to read data from the input file.")
