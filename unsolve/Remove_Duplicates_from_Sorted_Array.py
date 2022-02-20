from distutils.log import ERROR


def searchInsert( nums, target):
    if nums[-1] <= target:
        return  len(nums)
    elif nums[0] >= target:
        return 0
    
    for i in  nums:
        if nums[i+1] >= target and target >= nums[i]:
            return  i  , i+1
        else:
            return 'None'


data = searchInsert([1,2,4,5,9,12],6)
print(data)


    