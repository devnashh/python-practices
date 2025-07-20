def water(find):
    left = 0
    right = len(find) -1

    while left < right:
        
        if find[left] > find[right]:
            print("Left is greater than Right")
        else:
            print("Right is Greater than left")

    return find

water1 = 50
water2 = 10
