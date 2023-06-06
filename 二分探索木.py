class BSTNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val


    def insert(self, val):
        if not self.val: #1回目はself.valに何もなくNoneな為実行される。
            self.val = val #下に連ねるための親
            # print("1")
            return
        
        if self.val == val: #あっても無くても
            # print("2")
            return
        
        if val < self.val: #1つ目に入れたのよりvalが小さければ19行目へ
            if self.left: #leftは1回目はNoneとして扱われ、2回目以降は数字が入るのでTrueを返す。
                self.left.insert(val) #self.leftの中でinsert関数が呼び出されて(再帰)、self.val = self.leftになり、仮想的な親として扱われる。
                # print("3")
                return
            self.left = BSTNode(val) #self.leftにvalを代入
            return 
            
        if self.right:
            self.right.insert(val) #rightも1回目はNoneとして扱われ、2回目以降は数字が入るのでTrueを返す。
            # print("4")
            return
        self.right = BSTNode(val) #self.rightに代入

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
        if self.right is None: 
            return self.left #左下の数をselfに持ってくる。
        if self.left is None:
            return self.right #右下の数をselfに持ってくる。
        #子供が2人だったら下に行く
        min_larger_Node = self.right #
        while min_larger_Node.left: #Nodeに持ってきた値の左下を探すプログラム
            min_larger_Node = min_larger_Node.left #Nodeの一番左下がくるまで上に上げてく
        self.val = min_larger_Node.val #一番左の数をvalに持ってくる
        self.right = self.right.delete(min_larger_Node.val) #min_larger_Node.valが2つ出来上がっているから消す
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