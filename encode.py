#Carlos Benavides

def password_encoder(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

def main():
    input_password = input("What's the password you want to encode?: ")
    encoded_password = password_encoder(input_password)
main()