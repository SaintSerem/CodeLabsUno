import pandas as pd
import random
import string


def generate_unique_email(name, data):

    # Extract first initial and lowercase the entire last name
    names = name.rstrip().split()
    first_initial = names[0][0].lower()
    last_name = names[-1].lower()  # Lowercase the entire last name

    base_email = f"{first_initial}{last_name}"
    random_number = ""

    # Check for uniqueness and append random number if needed
    while base_email in data['Email Address'].tolist():
        random_number = f"{random.randint(1, 99)}"  # Random number 1-99 (inclusive)
        base_email = f"{random_number}{base_email}"

    # Combine email address with domain in lowercase
    email = f"{base_email}@gmail.com".lower()

    return email



def read_data(file_path):

        return pd.read_excel(file_path)

def write_data(data, output_file):


    try:
        data.to_excel(output_file, index=False)
        print(f"Email addresses generated and saved to: {output_file}")
    except PermissionError:
        print(f"Error: Cannot write to: {output_file}")

    return data
