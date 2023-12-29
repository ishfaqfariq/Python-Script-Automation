# # Create a list of Hexadecimal Values
hex_values = ["0x746e6153", "0x33323161"]

combined_string = ""

for hex_value in hex_values:
    integer_value = int(hex_value, 16)
    ascii_string = bytearray.fromhex(format(integer_value, "x")).decode("utf-8")
    print("ASCII String: " + ascii_string)
    print("Reversing Start------- ")
    reverse_string = ascii_string[::-1]
    print("Reversed String is: " + reverse_string)

#     # Handle both hex values together.

#     combined_string += ascii_string
# reversed_string = combined_string[::-1]

# print("Combined String is: " + combined_string)
# print("Reversed String is: " + reversed_string)


# Chat GPT Version

# hex_values = ["0x746e6153", "0x33323161"]

# combined_string = ""

# for hex_value in hex_values:
#     integer_value = int(hex_value, 16)
#     ascii_string = bytearray.fromhex(format(integer_value, "x")).decode("utf-8")
#     combined_string += ascii_string

# reversed_string = combined_string[::-1]

# print("Combined String is: " + combined_string)
# print("Reversed String is: " + reversed_string)
