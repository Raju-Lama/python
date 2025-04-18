# # Function to convert hex to bytes
# def hex_to_bytes(hex_string):
#     return bytes.fromhex(hex_string)

# # Function to XOR two byte sequences
# def xor_bytes(byte_sequence, key):
#     return bytes([b ^ key[i % len(key)] for i, b in enumerate(byte_sequence)])

# # Define the intercepted message (hexadecimal)
# ciphertext1 = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
# ciphertext2 = "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"

# # Convert hex ciphertext to bytes
# ciphertext_bytes1 = hex_to_bytes(ciphertext1)
# ciphertext_bytes2 = hex_to_bytes(ciphertext2)

# # Define the header (the message starts with this)
# header = "ORDER:"

# # Convert header to bytes
# header_bytes = header.encode()

# # Determine the key by XORing the first bytes of the ciphertext with the header
# key = xor_bytes(ciphertext_bytes1[:len(header_bytes)], header_bytes)

# # Decrypt the entire message by XORing the ciphertext with the repeating key
# decrypted_message1 = xor_bytes(ciphertext_bytes1, key)
# decrypted_message2 = xor_bytes(ciphertext_bytes2, key)

# # Combine the decrypted parts
# decrypted_message = decrypted_message1 + decrypted_message2

# # Print the decrypted message as a string
# print(decrypted_message.decode('utf-8', errors='ignore'))


# import base64

# # Target string to decode
# target_string = "ICIqfbxTlkqa{bjcfsBcmmzy~cke~w3"

# # try:
#     # Attempt to decode the target string as Base64
# # decoded_bytes = base64.b64decode(target_string)
# # decoded_string = decoded_bytes.decode('utf-8')
# # print("Decoded string (Base64):", decoded_string)
# # except Exception as e:
# #     print("Base64 decoding failed:", e)

# def caesar_cipher_decrypt(text, shift):
#     decrypted = ''
#     for char in text:
#         if char.isalpha():  # Only shift alphabetic characters
#             start = 65 if char.isupper() else 97
#             decrypted += chr((ord(char) - start - shift) % 26 + start)
#         else:
#             decrypted += char  # Non-alphabetic characters remain the same
#     return decrypted

# # Target string
# target_string = "ICIqfbxTlkqa{bjcfsBcmmzy~cke~w3"

# # Try all shifts from 1 to 25 and see if we get a readable message
# for shift in range(1, 26):
#     print(f"Shift {shift}: {caesar_cipher_decrypt(target_string, shift)}")


# Convert the hex ciphertext into bytes
hex_str = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
ciphertext = bytes.fromhex(hex_str)

# Determine the key using the known header "ORDER:"
header = b"ORDER:"
key = bytes([ciphertext[i] ^ header[i] for i in range(len(header))])

# Decrypt the entire ciphertext using the repeating key
plaintext = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])

# Print the decrypted message
print(plaintext.decode('ascii'))