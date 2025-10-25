[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BE_csc8S)
# Serialize / Deserialize a Binary Tree

## Story
Your settings tree must sync across devices. You’ll **serialize** it to a compact string and **deserialize** it back to the exact same shape.

## Task (What to Build)
In `src/serialize.py`, implement:
- `serialize(root) -> str`: **preorder** traversal with `#` sentinels for `None`, space-separated.
- `deserialize(s) -> Node`: rebuild the identical tree from the string.

**Node API:** `Node(val, left=None, right=None)`  
Values may be numbers or strings; store them as strings during serialization and restore numbers if token is an integer.

## Hints
- Preorder pattern: write `val`, then left, then right.
- In `deserialize`, consume tokens from an iterator so the position moves naturally.
- On `#`, return `None` immediately.

## Run Tests Locally
```bash
python -m pytest -q
```

## Common Problems

- Forgetting to include # for None → ambiguous shapes.
- Not advancing the token index (stuck recursion).
- Mixing traversal orders (must be preorder for both directions).

## Complexity
- Both serialize and deserialize: O(n) time, O(h) space (recursion).

## Example
```bash    

   1
  / \
 2   3

serialize -> "1 2 # # 3 # #"
deserialize(serialize(tree)) reproduces the same shape.
```