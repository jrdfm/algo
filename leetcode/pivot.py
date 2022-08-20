#!/usr/bin/python3

def findt(nums, target):
    def find(nums,l,r,target):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if target >= nums[l] and target <= nums[mid]:
                return find(nums, l,mid - 1 , target)
            else:
                return find(nums, mid + 1, r, target)
        if target >= nums[mid] and target <= nums[r]:
            return find(nums, mid + 1, r , target)
        else:
            return find(nums, l,mid - 1, target)

    return find(nums,0,len(nums) - 1, target)
    
def findmin(nums):
    def find(nums,l,r):
        if l > r:
            return nums[0]
        if r == l:
            return nums[l]
        mid = (l + r) // 2
        print(f'mid {mid}')
        if nums[mid - 1] > nums[mid]:
            return nums[mid] 
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] < nums[l]:
            print(f'>')     
            return find(nums,l,mid-1)
        else:
            print(f'<')     
            return find(nums,mid + 1,r)
    return find(nums,0,len(nums) - 1)

if __name__ == "__main__":
    nums = [[6,7,8,1,2,3,4,5],[4,5,6,7,8,1,2,3],[5,6,7,8,1,2,3,4]]

    for i in nums:
        print(i)
        print(findt(i,1))
        print(findmin(i))

    print(f'\n{findmin(nums[0])}')