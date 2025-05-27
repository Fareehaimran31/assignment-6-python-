class Empolyee:

    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Empolyee("Mus'haf", 50000, "123-45-6789")
print(emp.name)  # Public attribute
print(emp._salary)  # Protected attribute
print(emp._Empolyee__ssn)  # Private attribute accessed using name mangling