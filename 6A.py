import re

def validate_phone_number(phone_number):

    ## Validates a phone number.
    ## Valid formats: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890

    pattern = re.compile(r'^(\+?\d{1,2}[\s-]?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone_number))

def validate_ssn(ssn):

   ## Validates a Social Security Number (SSN).
   ## Valid format: 123-45-6789

    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

def validate_zip_code(zip_code):

   ## Validates a US ZIP code.
   ## Valid formats: 12345, 12345-6789

    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

def main():
    phone_number = input("Enter a phone number: ")
    ssn = input("Enter a social security number: ")
    zip_code = input("Enter a ZIP code: ")

    if validate_phone_number(phone_number):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    if validate_ssn(ssn):
        print("The social security number is valid.")
    else:
        print("The social security number is invalid.")

    if validate_zip_code(zip_code):
        print("The ZIP code is valid.")
    else:
        print("The ZIP code is invalid.")

if __name__ == "__main__":
    main()
