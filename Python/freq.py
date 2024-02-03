cipher = "lcllewljazlnnzmvyiylhrmhza"
list_ciphertext = [cipher]
freq_dictionary = {}

for ciphertext in list_ciphertext:
    for letter in ciphertext:
        if letter.isalpha():
            if letter in freq_dictionary.keys():
                freq_dictionary[letter] += 1
else:
    freq_dictionary[letter] = 1
print(freq_dictionary)
