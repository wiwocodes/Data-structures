class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinaryTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinaryTree(value)
            
    def pre_order(self):
        if self ==None:
            return
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()
    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None
        
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        
        return print(value == self.value)
        
    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node() #use clear node
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True
bst = BinaryTree(4)
bst.insert_node(5)
bst.insert_node(34)
bst.insert_node(50)
bst.insert_node(67)
bst.insert_node(99)
bst.insert_node(100)
bst.insert_node(105)
x, y, z = map(int, input().split())
A, B, C = map(int, input().split())
bst.pre_order()
bst.find_node(x)
bst.find_node(y)
bst.find_node(z)
bst.remove_node(A, None)
bst.remove_node(B, None)
bst.remove_node(C, None)
bst.pre_order()