class datas:

    def __init__(infos, name, age, gender, address, contact):
        infos.name = name
        infos.age = age
        infos.gender = gender
        infos.address = address 
        infos.contact = contact

    def view_name(infos):
        print("The name of this data is: "+infos.name)
    def view_age(infos):
        print("The age of it is: ", infos.age)
    def view_gender(infos):
        print("the gender is: "+infos.gender)
    def view_address(infos):
        print("The address is: "+infos.address)
    def view_contact(infos):
        print("The contact number is: ", infos.contact)
    def __add__(infos, other):
        return f'{infos.name} + {other.name}'
    
