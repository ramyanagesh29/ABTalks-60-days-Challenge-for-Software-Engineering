# Day 12 - Reverse String Using Two Pointers

## Problem

The goal is to reverse a string efficiently.

Example:

Input: hello  
Output: olleh

## Approach

I used the Two Pointers technique to reverse the string.

- `left` starts from the beginning of the string.
- `right` starts from the end of the string.
- The characters at both positions are swapped.
- `left` moves forward.
- `right` moves backward.
- The process continues until both pointers meet.

Since Python strings are immutable, I converted the string into a list before swapping the characters. After reversing, I used `join()` to convert the list back into a string.

## Time Complexity

O(N)

Each character is processed while the two pointers move toward the center.

## Space Complexity

O(N)

Extra space is used to convert the string into a list because Python strings cannot be modified directly.

## Real-World Usage

String reversal and string manipulation are useful in text processing systems, chat applications, search engines, log processing, and data validation.

## Key Learning

I learned how the Two Pointers technique can be used for efficient string manipulation and why Python string immutability affects memory usage.
