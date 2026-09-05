Day 11 - Move Zeroes Using Two Pointers
Problem

The goal is to move all zeroes to the end of the array while maintaining the original order of the non-zero elements.

Example:

Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Approach

I used the Two Pointers technique.

index scans through every element in the array.
position keeps track of where the next non-zero element should be placed.

First, all non-zero elements are moved to the front while maintaining their original order.

Then, the remaining positions are filled with zeroes.

Time Complexity
O(N)

The array is processed using two loops, but both loops together process the elements a constant number of times.

Space Complexity
O(1)

No extra array is created. The original array is modified directly.

Real-World Usage

The Two Pointers technique is useful in memory-efficient systems and large-scale data processing where modifying data in-place helps avoid unnecessary memory usage.

Key Learning

I learned how two pointers can work together: one pointer scans the data while another pointer tracks the correct position for placing elements.

3️⃣ Run the code

In the VS Code terminal:

python day11_move_zeroes.py

Expected output:

[1, 3, 12, 0, 0]
4️⃣ Push to GitHub
git status
git add .
git commit -m "Day 11 Move Zeroes Using Two Pointers"
git push origin main
