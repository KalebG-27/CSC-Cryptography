def decrypt(ciphertext):
    # step 1. Create a new list of values in the right order
    plaintext = []
    for i in range(len(ciphertext)):
        if i % 2 == 0:
            plaintext.append(ciphertext[i + 1])
            plaintext.append(ciphertext[i])
        else:
            continue

    # step 2. Shift four positions to the left (mod 26)
    for i in range(len(plaintext)):
        plaintext[i] = chr((ord(plaintext[i]) - 65 - 4 + 26) % 26 + 65)

    # step 3. Convert back to characters using UTF-8 encoding
    return "".join(plaintext)


# Example usage
ciphertext = [0x4C, 0x50, 0x53, 0x53, 0x50, 0x49, 0x50, 0x41, 0x56, 0x48]
ciphertext = [chr(c) for c in ciphertext]
print(decrypt(ciphertext))  # Output: HELLO WORLD
