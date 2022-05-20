# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
Car1 = Vehicle()
Car1.name = 'Fer'
Car1.kind = 'convertible'
Car1.color = 'red'
Car1.value = 60000.00

Car2 = Vehicle()
Car2.name = 'Jump'
Car2.kind = 'van'
Car2.color = 'blue'
Car2.value = 10000.00


# test code
print(Car1.description())
print(Car2.description())