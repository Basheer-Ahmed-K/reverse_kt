class Class:
    def __init__(self, my_name, my_address):
        self.name = my_name
        self.address = my_address

    def print_details(self):
        print(self.name)
        print(self.address)


Object = Class("this is name", "this is address")
Object.print_details()
print(Object.print_details())











# print(type(diggibyte_1.name))
# print(diggibyte_1.name)
# print(type(diggibyte_1.address))
# print(diggibyte_1.address)

# def __init__(): # It will throw error  TypeError: Diggibyte.__init__() takes 0 positional arguments but 1 was given
#     pass        # Because we are not passing self or any parameter to it

# print(type(diggibyte_1))
