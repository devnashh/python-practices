def pair(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        csum = numbers[left] + numbers[right]

        if csum == target:
            return [left + 1, right + 1]
        elif csum < target:
            left += 1
        else:
            right -= 1
        
    return False

result = pair([1, 2 ,3 , 4 ,5], 6)
print(result)

