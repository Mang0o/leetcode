def quick_sort(l,left,right):
    if left >= right:
        return
    low = left
    high = right
    k = l[low]
    while(low < high):
        while(low<high and l[high]>=k):
            high -= 1
        l[low] = l[high]
        while(low<high and l[low]<=k):
            low += 1
        l[high] = l[low]
    l[low] = k
    quick_sort(l,left,low-1)
    quick_sort(l,low+1,right)

def my_sort(l):
    quick_sort(l,0,len(l)-1)

if __name__ == '__main__':

    l = [1,23,24,346,467,5,5,32,323,56,35]
    my_sort(l)
    print(l)