def decrypt(ciphertext):
    # step 1. Create a new list of values in the right order
    plaintext = [None]*10 
    for i in range(5):
        plaintext[i*2]=ciphertext[i]
        plaintext[i*2+1]=ciphertext[i+5]

    # step 2. Shift four positions to the left (mod 26)
    for i in range(len(plaintext)):
        plaintext[i] = (chr((plaintext[i] - 65 - 4 + 26) % 26 + 65))

    # step 3. Convert back to characters using UTF-8 encoding
    return "".join(plaintext)
ciphertext = [0x4C, 0x50, 0x53, 0x53, 0x50,
0x49, 0x50, 0x41, 0x56, 0x48]
print(decrypt(ciphertext))
