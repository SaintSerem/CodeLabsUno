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


def separate_and_format_data(input_file):

    try:
        # Read the Excel file using pandas
        data = pd.read_excel(input_file)

        # Separate students by gender (assuming columns named 'Gender' and 'Name')
        male_students = data[data['Gender'].str.lower() == 'male']['Name']
        female_students = data[data['Gender'].str.lower() == 'female']['Name']

        # Function to remove special characters from names (optional)
        def remove_special_chars(name):
            allowed_chars = set('abcdefghijklmnopqrstuvwxyz ')
            return ''.join([char for char in name.lower() if char in allowed_chars])

        # Filter names with special characters (optional)
        students_with_special_chars = data[data['Name'].str.contains(r"[^\w\s]", case=False)]['Name']

        # Calculate total male and female students
        num_male_students = len(male_students)
        num_female_students = len(female_students)

        # Create TSV and CSV files with informative headers
        male_students.to_csv('male_students.csv', index=False, header=['Name'])
        female_students.to_csv('female_students.csv', index=False, header=['Name'])
        male_students.to_csv('male_students.tsv', index=False, header=['Name'], sep='\t')
        female_students.to_csv('female_students.tsv', index=False, header=['Name'], sep='\t')


import re  # used to remove special characters
import pandas as pd


def process_stud_data(firstname, lastname):
    email = generate_email(firstname, lastname)
    return firstname, lastname, email


def generate_email(firstname, lastname):
    # Concatenate the first letter of the name and the full last name
    email = f"{firstname[0]}{lastname.split()[0]}@gmail.com"

    # Remove any special characters from the email address
    email = re.sub(r'[^a-zA-Z0-9@.]', '', email)
    return email.lower()


def main():
    input_file = 'Test Files.xlsx'
    output_csv_file = 'output.csv'
    output_tsv_file = 'output.tsv'

    # Read data from the Excel file
    df = pd.read_excel('Test Files.xlsx')

    processed_data = []

    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        firstname, lastname = row['firstname'].strip(), row['lastname'].strip()
        firstname, lastname, email = process_stud_data(firstname, lastname)
        processed_data.append({'firstname': firstname, 'lastname': lastname, 'email': email})

    # Create a new DataFrame from the processed data
    processed_df = pd.DataFrame(processed_data)

    # Save the DataFrame to CSV and TSV files
    processed_df.to_csv(output_csv_file, index=False)
    processed_df.to_csv(output_tsv_file, sep='\t', index=False)

    print(f"Data saved to {output_csv_file} and {output_tsv_file}")


import re  # used to remove special characters
import pandas as pd


def process_stud_data(firstname, lastname):
    email = generate_email(firstname, lastname)
    return firstname, lastname, email


def generate_email(firstname, lastname):
    # Concatenate the first letter of the name and the full last name
    email = f"{firstname[0]}{lastname.split()[0]}@gmail.com"

    # Remove any special characters from the email address
    email = re.sub(r'[^a-zA-Z0-9@.]', '', email)
    return email.lower()


def main():
    input_file = 'Test Files.xlsx'
    output_csv_file = 'output.csv'
    output_tsv_file = 'output.tsv'

    # Read data from the Excel file
    df = pd.read_excel('Test Files.xlsx')

    processed_data = []

    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        firstname, lastname = row['firstname'].strip(), row['lastname'].strip()
        firstname, lastname, email = process_stud_data(firstname, lastname)
        processed_data.append({'firstname': firstname, 'lastname': lastname, 'email': email})

    # Create a new DataFrame from the processed data
    processed_df = pd.DataFrame(processed_data)

    # Save the DataFrame to CSV and TSV files
    processed_df.to_csv(output_csv_file, index=False)
    processed_df.to_csv(output_tsv_file, sep='\t', index=False)

    print(f"Data saved to {output_csv_file} and {output_tsv_file}")


if _name_ == "_main_":
    main()
