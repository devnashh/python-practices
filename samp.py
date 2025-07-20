class cellphone:

    def __init__(act, brand, ram, rom, cpu):
        act.brand = brand
        act.ram = ram
        act.rom = rom
        act.cpu = cpu

    def turn_on(act):
        print(f"Phone "+act.brand+" was turned on")
    def turn_off(act):
        print(f"Phone "+act.brand+" was turned off")
    def __add__(act, other):
        return f'{act.cpu} + {other.cpu}'

vivo: cellphone = cellphone("vivo", "8gb", "128gb", "Snapdragon560")
samsung: cellphone = cellphone("samsung", "6gb", "128gb", "Snapdragon456")

print(vivo + samsung)