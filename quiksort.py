import time

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

    #pivot = a[l + int((r-l)/2)]
    pivot = a[r]

    i,j =l, r #リストの1つ目の値をi, 後ろから一つ目をjとする
    
    while i < j: #i(最初は0が入る)がjより小さいと入る
        while a[i] < pivot: #a[i]がより小さかったらi+1
            i += 1    
        while a[j] > pivot: #j番目の値がpivotより小さければpivotより、小さくなるまで探す。
            j -= 1
        if i < j:
            if a[i] == a[j]: 
                j -= 1
            else:
                a[i], a[j] = a[j], a[i] #iとjが違う値だった場合、iとjの値を変える。(マイナスの値がない場合は、i=0なので最初に来る。)
    qsort(a, l, i-1) #i-1番目の値がjになり、再度繰り返される。
    qsort(a, j+1, r) #j+1番目の値がiになり、再度繰り返される。
    

a = [7,2,1,4,6,0,8,5,9,3]
lenght = len(a)
print(a)
start = time.time()
qsort(a, 0, lenght- 1)
end = time.time()
print(end-start)
print(isSorted(a))
print(a)

#実行結果
# [7, 2, 1, 4, 6, 0, 8, 5, 9, 3]
# 2.5033950805664062e-05
# True
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
