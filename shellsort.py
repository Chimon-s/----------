import time
import numpy as np
import matplotlib.pyplot as plt

def isSorted(a):
    b = a[0]
    for x in a:
        if b > x:
            return False
        b = x 
    return True

def insertion_sort(a):#挿入ソート
    for i in range(len(a)):
        j = i
        while j >= 1 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def shell_sort(a):
    gap = len(a)//2
    while gap > 0:
        for i in range(gap, len(a)):
            j = i
            while j >= gap and a[j-gap] > a[j]:
                a[j], a[j-gap] = a[j-gap], a[j]
                j -= gap
        gap //= 2
    return print("shell_sort", a)

def qsort(a, l, r):
    if l >= r:
        return
    
    pivot = a[r]
    i,j = l,r
    
    while i < j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            if a[i] == a[j]:
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
    qsort(a, l, i-1)
    qsort(a, j+1, r)
    

a = [8,27,1,2,39,36,14,19,4,30]
shell_sort(a)


num = 3 
qtimes = []
nums = [10**i for i in range(num)]
for i in range(num):
    a = np.random.rand(10**i) #10**1以上、10**i未満
    length = len(a) 
    start = time.time()
    print("qsort", qsort(a, 0, length-1))
    end = time.time()
    print(isSorted(a))
    print(end - start)
    qtimes.append(end - start)
    
print(qtimes)
print(nums)
plt.title("Quick Sort Time Comparison")
plt.xlabel("# of date")
plt.ylabel("Time")

plt.plot(nums, qtimes, marker = "o", label = "Quick")

plt.legend()

print(plt.show())