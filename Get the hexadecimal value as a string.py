# Get the hexadecimal value as a string
hex_value = "0x746e6153"

# Remove the "0x" prefix and convert to an integer
integer_value = int(hex_value, 16)

# Convert the integer value to ASCII
ascii_string = bytearray.fromhex(format(integer_value, "x")).decode("utf-8")

# Print the resulting ASCII string
print("ASCII String: " + ascii_string)

# Start with the input hexadecimal value "0x746e6153".
# Remove the "0x" prefix and convert it to an integer, resulting in 1959379843.
# Convert the integer back to a hexadecimal string, which is "746e6153".
# Create a bytearray from the hexadecimal string, resulting in bytearray(b'tanS').
# Decode the bytearray to get the ASCII string "tanS".

#     I apologize for any confusion. In Python, when you use the int() function with a string that starts with "0x," it is automatically recognized as a hexadecimal number, and the "0x" prefix is ignored. So, in the line integer_value = int(hex_value, 16), the "0x" prefix is not actually included in the conversion to an integer.

# Here's how it works:

#     You start with the input hexadecimal string "0x746e6153".
#     When you use int(hex_value, 16), Python recognizes that it's a hexadecimal string and ignores the "0x" prefix. It then converts the characters following "0x" (i.e., "746e6153") into an integer.

# This is why it doesn't affect the end result, and you still get the correct integer value, which is 1959379843, and then subsequently the ASCII string "tanS" after converting it to a bytearray and then decoding it.
