import math


while True:
 FirstNumber = float(input("Enter First Number: "))
 SecondNumber = float(input("Enter Number Number: "))

 print(f"|_________________________|")
 print("+ | - | / | x")
 print(f"")
 print("|__________________________|")
 op = input(f"| Select Operator: ")

 if op == "+":
    result = FirstNumber + SecondNumber
    print(f"| TOTAL = "+ str(math.floor(result)))
    print("|____________________________________|")
 elif op == "-":
    result = FirstNumber - SecondNumber
    print(f"| TOTAL = "+ str(math.floor(result)))
    print("|____________________________________|")
 elif op == "x":
    result = FirstNumber * SecondNumber
    print(f"| TOTAL = "+ str(math.floor(result)))
    print("|____________________________________|")
 elif op == "/":
    result = FirstNumber / SecondNumber
    print(f"| TOTAL = "+ str(math.floor(result)))
    print("|____________________________________|")
 else:
    print("Error Try Again")
    continue

 con = input("Continue? ")
 if con != "no":
    continue
 else:
    break
