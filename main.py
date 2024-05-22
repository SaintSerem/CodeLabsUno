# Importing  libraries

import pandas as pd
from functions import generate_unique_email, read_data, write_data



input_file = "C:\\Users\\brian\\OneDrive\\Documents\\Test Files.xlsx"
output_file = "output.xlsx"

# Read data from the excel (Test Files)
data = read_data(input_file)


data = (data)


if data is not None:
    # Adding the email addresses to the column
    data['Email Address'] = data['Student Name'].apply(generate_unique_email, args=(data,))

    # Write modified data to a new Excel file
    write_data(data, output_file)
else:
    print("Error: Unable to read data from the input file.")
