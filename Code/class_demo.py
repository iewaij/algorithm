"""
Class and Trees
"""

# Sometimes you want a object which is more flexible
jiawei = {"student_id": 1656, "first_name": "jiawei", "last_name": "li", "grade": 100}

# So you create a object, named Student. 
# In Python it is a common practice to name the class FirstLetterCapitalized.
class Student:
    def __init__(self, any_name_id, any_first_name, any_last_name):
        self.student_id = any_name_id
        self.first_name = any_first_name
        self.last_name = any_last_name
        self.grade = 100

    def __repr__(self):
        return self.student_id

    def grade_divide_by(self, a_number):
        return self.grade / a_number

student_0 = Student(77667, "Vivian", "Last")
print(student_0.grade_divide_by(4))

# Tree
#         10("any_name")
#      /       \
#     5        15
#    / \       / \
#   3   8    None None

tree = Tree(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(3)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.left is None:
            self.left = Node(key)
        elif self.right is None:
            self.right = Node(key)
        else:
            print("the tree is full.")

# Tree
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if self.key > key and self.left is None:
            self.left = Node(key, data)
        elif self.key > key and self.left is not None:
            self.left.insert(key, data)
        elif self.key < key and self.right is None:
            self.right = Node(key, data)

    def get(self, key):
        if key == self.key:
            return self.data
        if key < self.key:
            pass

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# Tree
#         10
#      /       \
#     1           15
#    / \         / \ 
#  None 3    None    None

root = Node(10, "Vivian")
root.insert(15, "Jiawei")
root.insert(1, "Nasim")
root.insert(3, "Prashant")
root.display()
print(root.get(10))
