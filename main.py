import pandas as pd
from functions import generate_email, separate_genders, find_special_characters, shuffle_data, log_message
from constraints import validate_data

def main():
    try:
        # reading the test files
        data = pd.read_excel('C:\\Users\\brian\\OneDrive\\Documents\\Test Files.xlsx')

        # data validation
        validate_data(data)

        # Separate male and females
        male_students, female_students = separate_genders(data.copy())

        #Generation of emails
        data['Email Address'] = data['Student Name'].apply(generate_email)


        special_characters_names = find_special_characters(data['Student Name'].tolist())
        log_message(f"Number of students with special characters: {len(special_characters_names)}")


        male_students.to_csv('male_students.tsv', index=False)
        female_students.to_csv('female_students.tsv', index=False)


        with open('special_characters_names.txt', 'w') as f:
            f.writelines(name + '\n' for name in special_characters_names)


        shuffle_data(data.copy())

        log_message("Daata processing completed successfully.")

    except Exception as e:
        log_message(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
