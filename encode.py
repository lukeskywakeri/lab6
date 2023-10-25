#Carlos Benavides

def password_encoder(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

# Autumn Nix's decoding
def decode(encoded_password):
    split_password = []
    split_password.extend(encoded_password)
    decoded_password = ''
    for element in split_password:
        element = int(element)
        if element <= 2:
            if element == 2:
                element = 9
            elif element == 1:
                element = 8
            elif element == 0:
                element = 7
        else:
            element -= 3
        element = str(element)
        decoded_password += element
    return decoded_password

while True:
    print('Menu')
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))
    if option == 1:
        input_password = input("What's the password you want to encode?: ")
        encoded_password = password_encoder(input_password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        decoded_password = decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
    elif option == 3:
        pass
