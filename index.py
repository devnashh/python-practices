from data import datas

id = datas(input("Enter Name: "), input("Enter Age: "), input("Enter Gender: "), input("Enter Address: "), input("Enter Contact: "))

while True:

 print("Select action: ")
 print("View name | View age | View Gender | View Address | View Contact")
 select = input("Select: ")

 if select == "name":
     id.view_name()
 elif select == "age":
    id.view_age()
 elif select == "gender":
    id.view_gender()
 elif select == "address":
    id.view_address()
 elif select == "contact":
    id.view_contact()
 else:
   print("Error")
   continue
 con = input("Continue?: ")
 if con != "yes":
   break