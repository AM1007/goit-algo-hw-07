# Trees and Balancing

## Task 1

Write an algorithm (function) to find the maximum value in a binary search tree or an AVL tree. Use any tree implementation from your notes or another source.

## Task 2

Write an algorithm (function) to find the minimum value in a binary search tree or an AVL tree. Use any tree implementation from your notes or another source.

## Task 3

Write an algorithm (function) to find the sum of all values in a binary search tree or an AVL tree. Use any tree implementation from your notes or another source.

## Task 4 (Optional Task)

Implement a data structure for a comment system where comments can have replies, and those replies can also have replies, thus forming a hierarchical structure.

#### Also, consider the following requirements:

- Implement a Comment class that represents an individual comment. It should store the text of the comment, the author, and a list of replies.
- The add_reply method should add a new reply to the comment.
- The remove_reply method should remove a reply from the comment. This should change the text of the comment to a standard message (e.g., "This comment has been deleted.") and set the is_deleted flag to True.
- The display method should recursively print the comment and all its replies, using indentation to represent the hierarchical structure.

  **Example of Expected Output:**

```python
root_comment = Comment("What a great book!", "Bodhi")
reply1 = Comment("The book is a complete disappointment :(", "Andrew")
reply2 = Comment("What’s great about it?", "Marina")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Not a book, just a pile of paper for nothing...", "Sergey")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
```

**Output:**

```yaml
Bodhi: What a great book!
    This comment has been deleted.
        Sergey: Not a book, just a pile of paper for nothing...
    Marina: What’s great about it?

```
