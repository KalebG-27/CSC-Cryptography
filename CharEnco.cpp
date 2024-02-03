#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
#include <vector>
using namespace std;
using namespace boost;      // so that we can use erase() 

//Remove whitesaces from a string
int main(){
    // creating a string containing multiple whitespaces 

    string s = "";
    cin >> s;
    cout << "The string before removing whitespaces: " << s << endl;
    

    /** Using the erase, remove_if, and ::isspace functions.
    // erase() function takes two arguments: the iterator's starting position and ending position
    //remove_if() brings all the non-whitespace characters to the beginning of the string and 
    //returns an iterator pointing at the start of the whitespace characters. 
    **/

    s.erase(std::remove_if(s.begin(), s.end(), ::isspace), 
        s.end());

    cout << "String s after removing whitespaces: " << s << endl;
    return 0;



//Remove all punctuation from a string
{
//string s = ""

    remove = remove_if(s.begin(), s.end(), []
    (char const &s)
    {
        return ispunct(s);
    });

s.erase(remove, s.end());

cout<< s << endl;        

    return 0;
}


//Convert all alphabetic characters to lower case
string s = tolower(s);

    cout<<"String in lowercase:" << s << endl;
return 0;

//Perform a shift of +4 (mod 26) on each character, and convert it to upper case
string caesar_cipher(string input)
{
string output = "";
for (char c : input)
{
    if (isalpha(c))
    {
        char shifted = toupper(c) + 4;
        if (shifted > 'Z')
        {
            shifted = shifted - 26;
        }
        output += shifted;
    }
    else
    {
        output += c;
    }
}
return output;
cout << "Input: " << s << endl;
cout << "Output: " << caesar_cipher(s) << endl;
return 0;
}
//Create an output array/list that contains the ordinal values of all characters at even positions

vector<int> ordinal_values(string input)
{
vector<int> output;
for (int i = 0; i < input.length(); i++)
{
    if (i % 2 == 0)
    {
        output.push_back((int)input[i]);
    }
}
return output;
}

int main()
{
string input = "the quick brown fox";
cout << "Input: " << input << endl;
vector<int> output = ordinal_values(input);
cout << "Output: [";
for (int i = 0; i < output.size(); i++)
{
    cout << output[i];
    if (i < output.size() - 1)
    {
        cout << ", ";
    }
}
cout << "]" << endl;
return 0;
}
}
