import pandas as pd
import string
import random

def generate_unique_email(name, data):


    # Extract first letter and full last name
    names = name.rstrip().split()
    first_letter = names[0][0].lower()
    last_name = names[1] if len(names) > 1 else names[0]

    base_email = f"{first_letter}{last_name}"
    random_number = ""
    while base_email in data['Email Address'].tolist():
        random_number = f"{random.randint(1, 99)}"  # Random number 1-99 (inclusive)

    # Combine email address with random number (if needed) and domain
    email = f"{random_number}{base_email}@gmail.com"

    return email

def read_data(file_path):

        return pd.read_excel(file_path)

def write_data(data, output_file):


    try:
        data.to_excel(output_file, index=False)
        print(f"Email addresses generated and saved to: {output_file}")
    except PermissionError:
        print(f"Error: Cannot write to: {output_file}")

#def fix_date_format(data):

    # Fixes the format of the DoB column
    #if 'DoB' in data.columns:  # Check if DoB column exists
     #   data['DoB'] = pd.to_datetime(data['DoB']).dt.strftime('%Y-%m-%d')  # Remove time that appears in the DOB column

    return data
