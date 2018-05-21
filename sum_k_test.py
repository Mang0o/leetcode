def find_sub_elements(nums,k):
    d = {}

    sum = 0
    d[0] = [-1]


    ret = []
    for index,value in enumerate(nums):
        sum+=value
        if sum-k in d:
            for j in d[sum-k]:
                ret.append((j+1+1,index+1))
        if sum in d:
            d[sum].append(index)
        else:
            d[sum] = [index]

    print(ret)


if __name__ == '__main__':
    find_sub_elements([1,2,3,4,5,6,7,8],15)

        
