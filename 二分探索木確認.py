class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val: #1回目はself.valに何もなくNoneな為実行される。
            self.val = val #下に連ねるための親
            print(str(val)+", 1")
            return
        
        if self.val == val: #あっても無くても
            print(str(val)+", 2")
            return
        
        if val < self.val: #1つ目に入れたのよりvalが小さければ19行目へ
            if self.left: #leftは1回目はNoneとして扱われ、2回目以降は数字が入るのでTrueを返す。
                print(str(val)+", 3")
                self.left.insert(val) #self.leftの中でinsert関数が呼び出されて(再帰)、self.val = self.leftになり、仮想的な親として扱われる。
                return
            self.left = BSTNode(val) #self.leftにを代入
            print(str(val)+", 4")
            return
            
        if self.right:
            self.right.insert(val) #rightも1回目はNoneとして扱われ、2回目以降は数字が入るのでTrueを返す。
            print(str(val)+", 5")
            return
        self.right = BSTNode(val) #self.rightに代入
        print(str(val)+", 6")

    def delete(self, val):
        if self is None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_Node = self.right
        while min_larger_Node.left:
            min_larger_Node = min_larger_Node.left
        self.val = min_larger_Node.val
        self.right = self.right.delete(min_larger_Node.val)
        return self
    
    def exists(self, val):
        if val == self.val:
            return True
        print("これは", val, self.val)
        
        if val < self.val:
            if self.left is None:
                return False 
            return self.left.exists(val)
        
        if self.right is None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

def main():
    nums = [6,4,8,5,2,12]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
        
    print("inorder:")
    print(bst.inorder([]))
    print("#")

    nums = [2,6,20]
    print("deleting" + str(nums))
    for num in nums:
        if bst.exists(num):
            bst.delete(num)
    print("#")

    print("4 exists.")
    print(bst.exists(4))
    print("6 exists.")
    print(bst.exists(6))

if __name__ ==  "__main__":
    main()