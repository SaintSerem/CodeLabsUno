from Functions import generate_unique_email, read_data, write_data
from Constraints import validate_data, is_valid_email_format

# Replace with your actual file path
input_file = "C:\\Users\\brian\\OneDrive\\Documents\\Test Files.xlsx"
output_file = "output.xlsx"

# Read data from Excel file
data = read_data(input_file)

# Validate data (placeholder for more checks)
validate_data(data)

# Add a new column for email addresses
data['Email Address'] = data['Student Name'].apply(generate_unique_email, args=(data,))

# Basic check for valid email format after generation (optional)
for email in data['Email Address']:
    if not is_valid_email_format(email):
        print(f"Warning: Email '{email}' might have an invalid format.")

# Write modified data to a new Excel file
write_data(data, output_file)

print(f"Email addresses generated and saved to: {output_file}")
