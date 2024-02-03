#include <iostream>
#include <vector>

std::string decrypt(const std::vector<unsigned char> &ciphertext)
{
    // Step 1: Create a new list of values in the right order
    std::vector<unsigned char> new_list;
    for (int i = 0; i < ciphertext.size(); i++)
    {
        new_list.push_back(ciphertext[i]);
        if ((i + 1) % 5 == 0)
        {
            for (int j = i - 4; j <= i; j++)
            {
                new_list.push_back(ciphertext[j]);
            }
        }
    }

    // Step 2: Shift four positions to the left (mod 26)
    std::string decrypted;
    for (int i = 0; i < new_list.size(); i++)
    {
        decrypted += (new_list[i] - 4 + 26) % 26 + 'A';
    }

    // Step 3: Convert back to characters using UTF-8 encoding
    return decrypted;
}

int main()
{
    std::vector<unsigned char> ciphertext = {0x4C, 0x50, 0x53, 0x53, 0x50, 0x49, 0x50, 0x41, 0x56, 0x48};
    std::string decrypted = decrypt(ciphertext);
    std::cout << decrypted << std::endl;
    return 0;
}
