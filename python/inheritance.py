class Parent:
    pass


# Single Inheritance
class Child(Parent):
    pass


# --------------------------------------------------
# Multiple Inheritance

class Parent1:
    pass


class Parent2:
    pass


class Child1(Parent1, Parent2):
    pass


# ---------------------------------------------------
# Multi-Level Inheritance

class Class1:
    pass


class Child1(Class1):
    pass


class Child2(Child1):
    pass
