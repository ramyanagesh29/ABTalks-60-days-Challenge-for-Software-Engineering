# Day 26 - The Secret Message Decoder

## Objective
Remove the nth node from the end of a linked list using two pointers.

## Strategy
Use `fast` and `slow` pointers. Move `fast` n positions ahead, then move
both pointers together until `fast` reaches the last node. Now `slow.next`
is the node to remove.

```python
slow.next = slow.next.next
```

A dummy node before the head makes the edge case of removing the first
node work with the same logic.

## Example

```text
A -> B -> C -> D -> E -> None
```

For `n = 2`, remove `D`:

```text
A -> B -> C -> E -> None
```

## Complexity
- Time: O(N)
- Extra Space: O(1)

## Why Single-Pass?
A length-counting approach requires a separate traversal to count nodes
before locating the target. The two-pointer method keeps a fixed n-node
gap between the pointers and finds the target during one traversal.

## Test Cases

Test 1:
```text
A -> B -> C -> D -> E -> None
n = 2
Result: A -> B -> C -> E -> None
```

Test 2:
```text
HELLO -> FROM -> RAMYA -> None
n = 3
Result: FROM -> RAMYA -> None
```

## Interview Explanation
"I use two pointers, fast and slow. I first move fast n positions ahead.
Then I move both together until fast reaches the end. Slow is then
immediately before the node to remove. I bypass that node using
slow.next = slow.next.next. A dummy node handles removal of the head.
The algorithm uses O(N) time and O(1) extra space."

