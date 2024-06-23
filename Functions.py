import pandas as pd
import re

def generate_email(name):

    name_parts = re.sub(r"[^\w\s]", "", name).lower().split()  # Remove special characters and split name
    first_initial = name_parts[0][0] if name_parts else ""
    last_name = name_parts[-1] if name_parts else ""
    email = f"{first_initial}.{last_name}@gmail.com"
    return make_unique(email)

def make_unique(email):

    count = 1
    seen_emails = set()
    while email in seen_emails:
        email = f"{email.split('@')[0]}.{count}@{email.split('@')[1]}"
        count += 1
    seen_emails.add(email)
    return email

def separate_genders(data):

    male_students = data[data['Gender'] == 'Male']['Student Name'].tolist() if 'Gender' in data else []
    female_students = data[data['Student Name'] != '']['Student Name'].tolist()  # Exclude empty names
    return male_students, female_students

def find_special_characters(names):

    pattern = r"[^\w\s]"  # Matching characters that are not alphanumeric or whitespace
    special_names = [name for name in names if re.search(pattern, name)]
    return special_names

def shuffle_data(data):

    shuffled_data = data.sample(frac=1).reset_index(drop=True)  # Shuffle and reset index
    shuffled_data.to_json('all_students_shuffled.json', orient='records')

def log_message(message):

    with open('logs.txt', 'a') as f:
        f.write(f"{message}\n")
