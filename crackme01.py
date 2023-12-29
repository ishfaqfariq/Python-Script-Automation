username = "ishfaqfariq"
number = 3

password = ""

for letter in username:
    password_letter = ord(letter) + number
    password += chr(password_letter)
print(password)