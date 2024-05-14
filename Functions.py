import pandas as pd
import string
import random

def generate_unique_email(name, data):
    """
    Generates a unique email address in the format "firstname.lastname@gmail.com".
    Handles single or double names and avoids special characters.

    Args:
        name (str): The student's name.
        data (pandas.DataFrame): The data containing student information.

    Returns:
        str: The generated email address.
    """

    # Extract first and last names (handle single or double names)
    names = name.split()
    first_name = names[0].lower()
    last_name = (names[1].lower() if len(names) > 1 else first_name)

    # Generate random characters for uniqueness
    random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

    # Combine and format email address
    email = f"{first_name}.{last_name}{random_chars}@gmail.com"

    # Check for uniqueness and regenerate if necessary
    while email in data['Email Address'].tolist():
        email = generate_unique_email(name, data)  # Pass data again

    return email

def read_data(file_path):
    """
    Reads data from an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        pandas.DataFrame: The DataFrame containing the data.
    """

    return pd.read_excel(file_path)

def write_data(data, output_file):
    """
    Writes data to an Excel file.

    Args:
        data (pandas.DataFrame): The data to write.
        output_file (str): The path to the output Excel file.
    """

    data.to_excel(output_file, index=False)
