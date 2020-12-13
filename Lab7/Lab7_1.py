# Операції з бінарним деревом пошуку в Python
import time

time_start = time.time()

# Створіть вузол
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Внутрішній обхід
def inorder(root):
    if root is not None:
        # Спуск ліворуч
        inorder(root.left)

        # Прихід до кореня
        print(str(root.key) + "->", end=' ')

        # Спуск праворуч
        inorder(root.right)


# Вставте вузол
def insert(node, key):

    # Поверніть новий вузол, якщо дерево порожнє
    if node is None:
        return Node(key)

    # Поверніться в потрібне місце і вставте вузол
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Знайдіть наступника в порядку
def minValueNode(node):
    current = node

    # Знайдіть крайній лівий лист
    while(current.left is not None):
        current = current.left

    return current


# Видалення вузла
def deleteNode(root, key):

    # Поверніть, якщо дерево порожнє
    if root is None:
        return root

    # Знайдіть вузол, який потрібно видалити
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # Якщо вузол має лише одну дитину або її немає
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Якщо вузол має двох дітей,
        # розмістіть наступника inorder у позиції вузла, який потрібно видалити
        temp = minValueNode(root.right)

        root.key = temp.key

        # Видалити наступника inorder
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Внутрішній обхід: ", end=' ')
inorder(root)

print("\nВидалити 10")
root = deleteNode(root, 10)
print("Внутрішній обхід: ", end=' ')
inorder(root)
print("\n", str((time.time() - time_start) * 1000).replace(".", ","), "ms")