# num=[3,2,2,3]
# val=3
# num1=num.copy()
# num1.pop()
# num1.pop(0)
# print(num1)

# def Remove(num):
#     val=2
#     num1=num.copy()
#     for i in num1:
#         if i==val:
#             num.remove(val)
#         else:
#             continue

# print(num)
        
# num=[0,1,2,2,3,0,4,2]
       
def remove(nums):
    n=len(nums)
    val=2
    left=0
    right=n-1
    while(left<=right):
        if nums[left]==val:
            nums.remove(nums[left])
            nums.append("_")
        else:
            left+=1
    print(nums)
nums=[0,1,2,2,3,0,4,2]        
remove(nums)


def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while(left<=right):
            if nums[left]==val:
                nums.remove(nums[left])
                right-=1
                # nums.append("_")
            else:
                left+=1
        print(nums213)



