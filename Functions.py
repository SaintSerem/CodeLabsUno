import pandas as pd
import string
import random

def generate_unique_email(name, data):
    """Generates a unique email address for a student in the format 'FirstLetter.lastname@gmail.com'.

    Args:
        name (str): Student's name.
        data (dict): Dictionary containing student data (including existing emails).

    Returns:
        str: Unique email address for the student.
    """

    # Extract first letter (capitalized) and full last name
    names = name.rstrip().split()
    first_letter = names[0][0].upper()  # Get first letter of first name (uppercase)
    last_name = names[1] if len(names) > 1 else names[0]  # Full last name (single or double names)

    # Combine and generate unique email address
    base_email = f"{first_letter}.{last_name}"  # Reintroduce the dot (.)
    random_number = ""
    while base_email in data['Email Address'].tolist():
        random_number = f"{random.randint(1, 99)}_"  # Random number 1-99 (inclusive) with underscore

    # Combine email address with random number (if needed) and domain
    email = f"{random_number}{base_email}@gmail.com"

    return email

def read_data(file_path):


    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def write_data(data, output_file):


    try:
        data.to_excel(output_file, index=False)
        print(f"Email addresses generated and saved to: {output_file}")
    except PermissionError:
        print(f"Error: Cannot write to: {output_file}")

# Optional function for DoB handling
def fix_date_format(data):

    # Fixes the format of the DoB column
    if 'DoB' in data.columns:  # Check if DoB column exists
        data['DoB'] = pd.to_datetime(data['DoB']).dt.strftime('%Y-%m-%d')  # Remove time component

    return data
