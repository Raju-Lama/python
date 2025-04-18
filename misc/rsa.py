# n = 340282366920938460843936948965011886881
# p = 18446744073709551613
# q = 18446744073709551557

# p = 18446744073709551613
# q = 18446744073709551557
# # assert p * q == n  # True

# phi = (p - 1) * (q - 1)  # φ(n) = 340282366920938460843936948963950166656

# e = 65537
# d = pow(e, -1, phi)  # d = 254555347062646534839222900590099449313

# def decrypt(ciphertext, d, n):
#     return pow(ciphertext, d, n)

# # Example for a ciphertext integer "ct":
# plaintext = decrypt(ct, d, n)

# d = 254555347062646534839222900590099449313
# n = 340282366920938460843936948965011886881

# ct = 123456789  # Replace with actual ciphertext
# plaintext = decrypt(ct, d, n)
# print(bytes.fromhex(hex(plaintext)[2:]).decode())


aes_key = bytes.fromhex("a0e74456a8fcb71354fd081fff10b1b8")
print(aes_key)