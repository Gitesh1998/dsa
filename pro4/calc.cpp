#include <cmath>
#include <ctype.h>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;
#include "dstack.h"

// function checking char is operation from +,-,*,/,^
// input char
// output boolean
bool isOperation(char c)
{
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

// function do operation on 2 operands
// input is operand and stack frame
void doOperation(char op, Dstack &stack)
{
    if (stack.size() < 2)
    {
        cerr << "Error: Invalid expression." << endl;
        exit(1);
    }
    double fir, sec;
    stack.pop(sec);
    stack.pop(fir);

    switch (op)
    {
    case '+':
        stack.push(fir + sec);
        break;
    case '-':
        stack.push(fir - sec);
        break;
    case '*':
        stack.push(fir * sec);
        break;
    case '/':
        stack.push(fir / sec);
        break;
    case '^':
        stack.push(pow(fir, sec));
        break;
    default:
        break;
    }
    return;
}

// check value is double or not
// input double value as string
// return double value
double isDouble(string digit)
{
    int dot = 0;
    for (char c : digit)
    {
        if (c == '.')
            dot++;
    }
    if (dot > 1)
    {
        cerr << "Error: Invalid expression." << endl;
        exit(1);
    }
    return stof(digit);
}

int main()
{
    Dstack stack;

    while (cin.peek() != EOF)
    {
        // check input value is space or not
        if (isspace(cin.peek()))
        {
            cin.ignore();
            continue;
        }

        // check input value is operation or not
        if (isOperation(cin.peek()))
        {
            char op;
            cin >> op;
            doOperation(op, stack);
            continue;
        }

        string oper;

        // if value is digit then get that digit and convert to double
        while (!isspace(cin.peek()) && (isdigit(cin.peek()) || (cin.peek() == '.')))
        {
            char nextChar;
            cin >> nextChar;
            oper += nextChar;
        }
        double data = isDouble(oper);
        stack.push(data);
    }
    double result;
    stack.pop(result);

    // check is empty or not
    if (!stack.empty())
    {
        cerr << "Error: Invalid expression." << endl;
        exit(1);
    }

    // print result
    cout << result << endl;
    return 0;
}