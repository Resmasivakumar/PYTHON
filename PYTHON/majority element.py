def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    count=0
    for num in nums:
        if num == candidate:
            count+=1
    if count > len(nums) // 2:
        return candidate
    else:
        return None  

# Example usage
arr = [3, 2, 3]
print(majority_element(arr))  # Output: 3
