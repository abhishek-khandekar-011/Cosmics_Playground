
#include <iostream>

int main() {
    std::cout << "Welcome to C++ Programming!\n";
    int num1, num2, sum;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;

    sum = num1 + num2;
    std::cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << std::endl;
    return 0;
}
