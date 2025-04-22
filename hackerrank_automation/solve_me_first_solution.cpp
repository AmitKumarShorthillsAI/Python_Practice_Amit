#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solveMeFirst(int a, int b) {
    return a + b;  // Solution for solving the problem by summing the two inputs
}

int main() {
    int num1, num2;
    int sum;
    cin >> num1 >> num2;  // Taking two integer inputs
    sum = solveMeFirst(num1, num2);  // Calling the solveMeFirst function
    cout << sum;  // Output the sum
    return 0;
}
