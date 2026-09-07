# Day 13 - Valid Anagram Using Hashing

## Problem

The goal is to determine whether two strings are anagrams.

Two strings are anagrams if they contain the same characters with the same frequency, even if the order of characters is different.

### Example

Input:

s = "anagram"  
t = "nagaram"

Output:

Valid Anagram

---

## Approach

I used a hashmap (Python dictionary) to count the frequency of characters.

First, I counted every character in the first string.

Then, I processed the second string and decreased the count of each character.

If both strings are anagrams, all character counts will become zero.

---

## Hashing Concept

A hashmap stores data as key-value pairs.

Example:

```text
a -> 3
n -> 1
g -> 1
r -> 1
m -> 1
