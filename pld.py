def pal(word):
    left = 0
    right = len(word) -1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

print(pal("racecar"))
print(pal("madam"))
print(pal("apple"))
print(pal("level"))
print(pal("noon"))