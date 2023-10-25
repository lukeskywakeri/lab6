#Carlos Benavides

def password_encoder(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

def main():
    print('Menu')
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))
    if option == 1:
        input_password = input("What's the password you want to encode?: ")
        encoded_password = password_encoder(input_password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        pass
    elif option == 3:
        pass


main()