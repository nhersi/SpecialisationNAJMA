# TASK 1
class CashRegister:

    def __init__(self, total_items,total_price,discount):
        self.total_items = total_items  # {'item': 'price'}
        self.total_price = total_price
        self.discount = discount

    def add_item(self):
        self.total_items += 1

    def remove_item(self):
        self.total_items -= 1

    def apply_discount(self):
        self.total_price *= 0.8

    def get_total(self):
        print("the total price is {}".format(self.total_price))

    def show_items(self):
        print("the total number of items is {}".format(self.total_items))

    def reset_register(self):
        self.total_price == 0

# Examples of how my code works:
# I will create some objects

first_add_item = CashRegister(4,100,0.2)
first_add_item.add_item()
print(first_add_item.total_items)

first_remove_item = CashRegister(4,100,0.2)
first_remove_item.remove_item()
print(first_remove_item.total_items)

first_apply_discount = CashRegister(4,100,0.2)
first_apply_discount.apply_discount()
print(first_apply_discount.total_price)

first_getting_total = CashRegister(4,100,0.2)
first_getting_total.get_total()
# i don't need a print statement here as i already have one in my method

first_showing_items = CashRegister(4,100,0.2)
first_showing_items.show_items()
# again no print statement needed

first_reset_register = CashRegister(4,100,0.2)
first_reset_register.reset_register()
print(first_reset_register.reset_register())

# TASK 2
class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = []

    # here is the child class

class CFGStudent(Student):

    def __init__(self, name, age, id):
        super().__init__(name, age, id)

    def all_subject(self,subjects):
        print(self.subjects)

Bob = CFGStudent('Bob',20,111)
Bob.all_subject('Maths')

print(Bob.all_subject())

