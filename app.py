import random, string


def main():
    print("Welcome to Shimmy's password generator")
    generate_password()
    
def generate_password():
    lenght = input("Enter desired lenght of the password: ")

    if lenght.isnumeric():
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        combined = uppercase + lowercase + digits + special

        temp = random.sample(combined, int(lenght))
        password = "".join(temp)

        print(f"Your password is: {password}")
    else:
        print("Password lenght needs to be a number :)")
        generate_password()

if __name__ == "__main__":
    main()
