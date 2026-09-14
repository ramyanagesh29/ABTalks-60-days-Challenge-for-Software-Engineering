# Day 20 - Robot Calculator Arena

## Problem

Evaluate mathematical expressions written in Reverse Polish Notation (RPN).

In RPN, operators appear after their operands.

Example:

2 3 +

means:

2 + 3

## Approach

I used a stack to evaluate the expression.

### Number

When a number is encountered, it is pushed onto the stack.

### Operator

When an operator is encountered:

1. Pop the second operand.
2. Pop the first operand.
3. Perform the operation.
4. Push the result back onto the stack.

The final value remaining in the stack is the answer.

## Example

Expression:

5 2 + 3 *

Stack flow:

5
[5]

2
[5, 2]

+
[7]

3
[7, 3]

*
[21]

Final result:

21

## Important Detail

For subtraction and division, operand order matters.

If:

first = 5
second = 2

Then:

first - second = 3

and:

first / second = 2.5

The implementation truncates division toward zero as required by the
standard RPN problem.

## Complexity

Time Complexity: O(N)

Space Complexity: O(N)

## Edge Cases

The implementation handles:

- Addition
- Subtraction
- Multiplication
- Division
- Negative numbers
- Multiple operations
- Nested calculation sequences

## Real-World Applications

Expression evaluation using stacks is used in:

- Compilers
- Calculators
- Query engines
- Programming language interpreters
- Parsing systems

## Key Learning

I learned how stacks can be used to evaluate expressions sequentially.

RPN is especially suitable for stack-based evaluation because each
operator works on the most recently available operands.
