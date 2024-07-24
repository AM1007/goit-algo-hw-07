from main import AVLNode, insert

def sum_values(node):
    if not node:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)

# Приклад використання
if __name__ == "__main__":
    root = None
    keys = [10, 20, 5, 6, 15, 30, 25, 35]
    
    for key in keys:
        root = insert(root, key)
    
    print("Сумма всех значений в AVL-дереве:", sum_values(root))
