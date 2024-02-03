#include <iostream>
#include namespace std;
#include <cmath>

int main() {
    std::cout << "Enter your first digit: ";
    std::cin >> num1;

    std::cout << "Enter an operation (+ , - , * , /): ";
    std::cin >> operation;

    std::cout << "Enter your second digit: ";
    std::cin >> num2;

    switch (operation) {
    case ' + ' :
        result = num1 + num2;
        std::cout << "Result of Operation is: " << result << std::endl;
        break;
    case ' - ' :
        result = -num1 - num2;
        std::cout << "Result of Operation is: " << result << std::endl;
        break;
    case  ' * ':
        result = num1 * num2;
        std::cout << "Result of Operation is: " << result << std::endl;
        break;
    case ' / ':
        if (num2 != 0) {
                result = num1 / num2;
                std::cout << "Result: " << result << std::endl;
            } else {
                std::cout << "Error: Division by zero is not allowed." << std::endl;
            }
        break;
    default:
        std::cout << "Error: Invalid operation." << std::endl;
        break;
  
    }

    return 0;     
}
