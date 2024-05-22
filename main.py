import pandas as pd
import re

def generate_email(name):
    """Generates a unique email address in the format 'firstinitial.lastname@gmail.com'."""
    name_parts = re.sub(r"[^\w\s]", "", name).lower().split()  # Remove special characters and split name
    first_initial = name_parts[0][0] if name_parts else ""
    last_name = name_parts[-1] if name_parts else ""
    email = f"{first_initial}.{last_name}@gmail.com"
    return make_unique(email)

def make_unique(email):
    """Ensures email address uniqueness by appending a number if duplicates exist."""
    count = 1
    seen_emails = set()
    while email in seen_emails:
        email = f"{email.split('@')[0]}.{count}@{email.split('@')[1]}"
        count += 1
    seen_emails.add(email)
    return email

def separate_genders(data):
    """Separates students into male and female lists based on a gender column (if present)."""
    male_students = data[data['Gender'] == 'Male']['Student Name'].tolist() if 'Gender' in data else []
    female_students = data[data['Student Name'] != '']['Student Name'].tolist()  # Exclude empty names
    return male_students, female_students

def find_special_characters(names):
    """Identifies names containing special characters using regular expressions."""
    pattern = r"[^\w\s]"  # Match characters that are not alphanumeric or whitespace
    special_names = [name for name in names if re.search(pattern, name)]
    return special_names

def shuffle_data(data):
    """Shuffles the data using Pandas and saves it as a JSON file."""
    shuffled_data = data.sample(frac=1).reset_index(drop=True)  # Shuffle and reset index
    shuffled_data.to_json('all_students_shuffled.json', orient='records')

def log_message(message):
    """Appends messages to the log file."""
    with open('logs.txt', 'a') as f:
        f.write(f"{message}\n")

def main():
    try:
        # Read data from Excel file (replace with your actual reading logic)
        data = pd.read_excel('C:\\Users\\brian\\OneDrive\\Documents\\Test Files.xlsx')

        # Validate data
        validate_data(data)

        # Generate email addresses
        data['Email Address'] = data['Student Name'].apply(generate_email)

        # Save student names and email addresses
        data[['Student Name', 'Email Address']].to_csv('C:\\Users\\brian\\OneDrive\\Documents\\Test Files\\email_output.tsv', index=False, sep='\t')

        # Identify names with special characters
        special_characters_names = find_special_characters(data['Student Name'].tolist())
        log_message(f"Number of students with special characters: {len(special_characters_names)}")

        # Save male and female students to TSV files (optional, commented out)
        # male_students.to_csv('male_students.tsv', index=False)
        # female_students.to_csv('female_students.tsv', index=False)

        # Save names with special characters to a text file (optional, commented out)
        # with open('special_characters_names.txt', 'w') as f:
        #     f.writelines(name + '\n' for name in special_characters_names)

        # Shuffle all student data (including names and emails)
        shuffle_data(data.copy())

        log_message("Data processing completed successfully.")

    except Exception as e:
        log_message(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
