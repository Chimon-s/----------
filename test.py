def isSorted(a):
    b = a[0]
    for x in a:
        if b > x:
            return False
        b = x
    return True

def qsort(a, l, r):
    if l >= r: 
        return

    pivot = a[r]
    print("rの値", r)
    print(pivot)

    i,j =l, r #リストの1つ目の値をi, 後ろから一つ目をjとする
    while i < j: #i(最初は0が入る)がjより小さいと入る
        print("①", i, j)
        print(pivot)
        while a[i] < pivot: #a[i]がより小さかったらi+1
            i += 1
            print("②",i, j, a)      
        print(pivot)
        while a[j] > pivot: #j番目の値がpivotより小さければpivotより、小さくなるまで探す。
            j -= 1
            print("③",i, j, a)
        if i < j:
            print("あいうえお")
            if a[i] == a[j]: 
                j -= 1
            else:
                a[i], a[j] = a[j], a[i] #iとjが違う値だった場合、iとjの値を変える。(マイナスの値がない場合は、i=0なので最初に来る。)
                print("④",i, j, a)
    print("呼び出し番号：⑤", l, i-1, r)
    qsort(a, l, i-1) #i-1番目の値がjになり、再度繰り返される。
    print("呼び出し番号：⑥", j+1, r)
    qsort(a, j+1, r) #j+1番目の値がiになり、再度繰り返される。
    


a = [5,2,4,6,1,3]
lenght = len(a)
print(a)
qsort(a, 0, lenght- 1)
print(isSorted(a))
print(a)