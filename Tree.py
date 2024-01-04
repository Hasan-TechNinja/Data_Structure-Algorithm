class Node:
    def __int__(self, data):
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node