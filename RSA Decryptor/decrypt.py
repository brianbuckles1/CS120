def rsa_decrypt(c, d, n):
    return chr(pow(c, d, n))

ciphertext_blocks = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]
d = 595
n = 1079

plaintext_blocks = [rsa_decrypt(c, d, n) for c in ciphertext_blocks]
print(plaintext_blocks)