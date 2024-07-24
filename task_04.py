class Comment:
    def __init__(self, text, author):
        self.text = text  # The text of the comment
        self.author = author  # The author of the comment
        self.replies = []  # List to store replies to this comment
        self.is_deleted = False  # Flag to indicate if the comment is deleted

    # Method to add a reply to the comment
    def add_reply(self, reply):
        self.replies.append(reply)  # Add the reply to the replies list

    # Method to remove a reply from the comment
    def remove_reply(self):
        self.text = "This comment has been deleted."  # Change the text to indicate deletion
        self.is_deleted = True  # Set the deletion flag to True

    # Method to display the comment and its replies recursively
    def display(self, level=0):
        indent = " " * 4 * level  # Create indentation based on the level
        if self.is_deleted:
            print(f"{indent}{self.text}")  # Print deleted comment text
        else:
            print(f"{indent}{self.author}: {self.text}")  # Print the author and text of the comment

        for reply in self.replies:  # Iterate over each reply
            reply.display(level + 1)  # Recursively display the reply with increased indentation


# Example usage
if __name__ == "__main__":
    root_comment = Comment("What a wonderful book!", "Bodia")
    reply1 = Comment("The book is a complete disappointment :(", "Andrii")
    reply2 = Comment("What's so wonderful about it?", "Maryna")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Not a book, just a waste of paper...", "Serhii")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
