class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val


    def insert(self, val):
        if not self.val:
            self.val = val
            # print("1")
            return
        
        if self.val == val:
            # print("2")
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val) 
                # print("3")
                return
            self.left = BSTNode(val)
            return 
            
        if self.right:
            self.right.insert(val)
            # print("4")
            return
        self.right = BSTNode(val)

    def delete(self, val):
        if self is None:
            return self
        print("あああ",self.val)
        if val < self.val:
            print("<")
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            print(">")
            self.right = self.right.delete(val)
            return self
        print("nama", 1)
        if self.right is None:
            return self.left
        print("nama", 2)
        if self.left is None:
            return self.right
        print("nama", 3)
        min_larger_Node = self.right #valの値が一致したらその右下の値をNodeに持ってくる
        print("aaaa", min_larger_Node)
        while min_larger_Node.left: #Nodeに持ってきた値の左下があったら実行
            min_larger_Node = min_larger_Node.left #Nodeの一番左下がくるまで上に上げてく
        #     print("aa", min_larger_Node)
        # print(min_larger_Node.val)
        self.val = min_larger_Node.val
        print("nama", 4)
        self.right = self.right.delete(min_larger_Node.val)
        return self
    
    def exists(self, val): #existsは木の中にval(数字)があるかどうか確かめる
        if val == self.val:
            return True
        
        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val) #左の子まで下がる
        
        if self.right is None:
            return False
        return self.right.exists(val) #右の子まで下がる

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

def main():
    nums = [12,6,18,19,21,11,3,5,4,24,18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
        
    # print("inorder:")
    # print(bst.inorder([]))
    # print("#")

    nums = [5]
    print("deleting" + str(nums))
    for num in nums:
        if bst.exists(num): #木の中に数字があれば実行
            print(str(bst.delete(num).val))
            print(bst.inorder([]))
            
    print("#")

    # print("4 exists.")
    # print(bst.exists(4))
    # print("6 exists.")
    # print(bst.exists(6))

if __name__ ==  "__main__":
    main()