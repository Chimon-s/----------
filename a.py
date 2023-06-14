import copy
a = [7,2,1,4,6,0,8,5,9,3]

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2 #分割を行う
        left = a[:mid]
        right = a[mid:]
        left = merge_sort(left) #再帰を利用して再度分割していく
        right = merge_sort(right) #再帰を利用して再度分割していく
        merged = merge(left, right)
        return merged #mergedに結合しているのでそれをreturnでmergeを再帰する
    return a

def merge(left, right):
    merged = []
    l_i, r_i =0, 0

    while l_i < len(left) and r_i < len(right): #ソート済みの配列をマージする為にそれぞれ左から見ていく
        if left[l_i] <= right[r_i]: 
            merged.append(left[l_i])
            l_i = l_i + 1
        else:
            merged.append(right[r_i])
            r_i = r_i + 1
            
    # 上のwhile文のどちらかがFalseになった場合終了する為、あまりをextendで追加する
    if l_i < len(left): 
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

b = merge_sort(a)
