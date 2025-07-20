from car_function import function

carr = function(input("input brand: "),input("Input Model: "))

while True:
 action = input("action: ")

 if action == "forward":
    print(carr.brand)
    carr.move_forward()
 elif action == "left":
    carr.move_left()
 elif action == "right":
    carr.move_right()
 elif action == "backward":
    carr.move_backward()
 else:
    print("Error! Invalid Input")
    break




