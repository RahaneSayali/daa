#include <iostream>
using namespace std;

void fibonacciIterative(int n) {
    int num1 = 0;
    int num2 = 1;
    int step_count = 0;
    int fib = 0;
    
    cout << "Fibonacci Iteratively:\n";
    for (int i = 0; i < n; i++) {
        cout << num1 << " ";  // Print the Fibonacci number
        fib = num1 + num2;
        num1 = num2;
        num2 = fib;
        step_count++;
    }
    cout << "\nNumber of steps (Iteratively): " << step_count << endl;
}

int fibonacciRecursive(int n, int& step_count) {
    step_count++; 
    if (n <= 1)
        return n;
    else
        return fibonacciRecursive(n - 1, step_count) + fibonacciRecursive(n - 2, step_count);
}

int main() {
    int n;
    cout << "Enter the number of terms:\n";
    cin >> n;

    // Iterative calculation
    fibonacciIterative(n);

    // Recursive calculation with step count
    cout << "\nFibonacci Recursively:\n";
    int step_count = 0;
    for (int i = 0; i < n; i++) {
        cout << fibonacciRecursive(i, step_count) << " ";
    }
    cout << "\nNumber of steps (Recursively): " << step_count << endl;

    return 0;
}
