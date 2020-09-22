class Node:
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def insert(self, key, data):
        if self.left is None:
            self.left = Node(key, data)
        elif self.left is not None:
            self.left.insert(key, data)
        else:
            print("The node if full.")

    def get(self, key):
        if key == self.key:
            return self.data

# Tree
#                      13,"Anna"
#     8:"Ramsey"                          88, "Bob"
# 1,"Sam"        None                  23, "David"       None

