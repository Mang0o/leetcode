def percolateDown(a,hole,size):
    tmp = a[hole]
    while(hole*2+1<size):
        child = hole*2+1
        if child!=size-1 and a[child+1]>a[child]:
            child+=1
        if a[child]>tmp:
            a[hole] = a[child]
        else:
            break
        hole = child
    a[hole] = tmp


def heapSort(nums):
    for i in range(len(nums)//2-1,-1,-1):
        percolateDown(nums,i,len(nums))
    for i in range(len(nums)-1,-1,-1):
        nums[0],nums[i] = nums[i],nums[0]
        percolateDown(nums,0,i)

if __name__ == '__main__':

    l = [1,23,24,346,467,5,5,32,323,56,35]
    heapSort(l)
    print(l)