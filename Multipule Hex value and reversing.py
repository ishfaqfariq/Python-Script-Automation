hex_values = ["0x746e6153", "0x33323161"]

reversed_strings = []

for hex_value in hex_values:
    integer_value = int(hex_value, 16)
    ascii_string = bytearray.fromhex(format(integer_value, "x")).decode("utf-8")
    reversed_string = ascii_string[::-1]
    reversed_strings.append(reversed_string)

combined_string = "".join(reversed_strings)

print("Reversed String 1: " + reversed_strings[0])
print("Reversed String 2: " + reversed_strings[1])
print("Reversed Combined String: " + combined_string)