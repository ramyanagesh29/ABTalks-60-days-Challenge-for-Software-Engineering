# Day 18 - Ancient Bracket Decoder

## Problem

The task is to determine whether a message contains properly balanced
and correctly ordered brackets.

The supported bracket types are:

- ()
- []
- {}

## Approach

I used a stack to validate the brackets.

A stack follows the LIFO principle:

Last In, First Out.

When an opening bracket is found, it is pushed onto the stack.

When a closing bracket is found, the top element of the stack is checked.

If the opening and closing brackets match, the opening bracket is removed.

If they do not match, the sequence is invalid.

At the end, the stack must be empty for the sequence to be valid.

## Example

For:

([{}])

The stack changes as follows:

(
([
([{ 
([
(
[]

The brackets are matched in reverse order, which is why a stack is useful.

## Edge Cases

The program handles:

- Empty input
- Only opening brackets
- Only closing brackets
- Mismatched brackets
- Nested brackets
- Multiple bracket types

## Complexity

Time Complexity: O(N)

Space Complexity: O(N)

## Real-World Applications

Stacks are commonly used in:

- Compilers
- HTML/XML validation
- IDE syntax checking
- Expression parsing
- Function call management
- Parsing engines

## Key Learning

I learned how stacks use LIFO behavior and how they can be used
to validate nested and structured data.
