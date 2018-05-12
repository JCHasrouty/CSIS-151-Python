def main():
    upper_chars = 0
    lower_chars = 0
    num_digits = 0
    whitespace_chars = 0
    
    file = open('text.txt', 'r')
    file_info = file.read()
    for line in file_info:
        if line.isupper():
            upper_chars += 1
        if line.islower():
            lower_chars += 1
        if line.isdigit():
            num_digits += 1
        if line.isspace():
            whitespace_chars += 1

    print("Uppercase letters:", upper_chars)
    print("Lowercase letters:", lower_chars)
    print("Digits:", num_digits)
    print("Spaces:", whitespace_chars)

main()
