def bitwise_encrypt(plaintext):
    # combine the two bytes of plaintext into a single value
    p1 = (plaintext >> 14 << 6) | (((plaintext >> 10) & 0b11) << 4) | (((plaintext >> 6) & 0b11) << 2) | ((plaintext >> 2) & 0b11) 
    p2 = (((plaintext >> 12) & 0b11)<< 6) | (((plaintext >> 8) & 0b11) << 4) | (((plaintext >> 4) & 0b11) << 2) | (plaintext & 0b11) 
    encrypted= (p1,p2)
    return encrypted

# test the implementation with the plaintext data 0xADE1

encrypted = bitwise_encrypt(0xADE1)
print(encrypted)
