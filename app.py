import random, string

def main():
    print("\nWelcome to Shimmy's password generator")
    generate_password() 

def generate_password():
    combined = string.ascii_uppercase + string.ascii_lowercase + string.digits
    specialcombined = combined + string.punctuation
    length = ''
    while not length.isnumeric():
        length = input("\nEnter desired length of the password: ")

    strength = ''
    while strength not in { '1', '2' }:
        strength = input("\nPassword strength \n1: weak\n2: strong ")

    if strength == '1':
        temp = random.sample(combined, int(length))
    else:
        temp = random.sample(specialcombined, int(length))

    password = "".join(temp)
    print(f"Your password is: {password}")
                

if __name__ == "__main__":
    main()
