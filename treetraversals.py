    def inoder(self,curr_node):
        if self.root==None:
            return "No tree"
        else:
            if curr_node.left!=None:
                self.inoder(curr_node.left)
            print(curr_node.data)
            if curr_node.right!=None:
                self.inoder(curr_node.right)
    def preoder(self,curr_node):
        if self.root==None:
            return "No tree"
        else:
            print(curr_node.data)
            if curr_node.left!=None:
                self.inoder(curr_node.left)
            if curr_node.right!=None:
                self.inoder(curr_node.right)
    def inoder(self,curr_node):
        if self.root==None:
            return "No tree"
        else:
            if curr_node.left!=None:
                self.inoder(curr_node.left)
            if curr_node.right!=None:
                self.inoder(curr_node.right)
            print(curr_node.data)
    