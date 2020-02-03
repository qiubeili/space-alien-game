##Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Dog is-a animal :)
class Dog(Animal):

    def __init__(self, name):
    ## dog class has-a __init__ that takes self and name parameters
        self.name=name

## cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
    ## cat class has-a __init__ that takes self and  name parameters
        self.name=name
    def count(self, name):
        return len(self.name)

##Person is-a object
class Person(object):
    def __init__(self, name):
    ## person class has-a __init__ that takes self a nd name parameters
        self.name = name
    #person has-a pet of some kind
    ## none makes sure that self.pet is DEFAULT NONE :D
        self.pet = None

#employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
    ## ?? hmmm what is this strange magic?
    ## SEARCH IT UP :D
    ## super() returns a proxy object that delegates method call to a parent or sibling of class type
    ## basically you can use rectange function to find area/permeter and use super to simplify code for doing the same for square cause they are  very similar :)
        super(Employee,self).__init__(name)
    ## employee has a salary :)
        self.salary= salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("rover")

##satan is a cat
satan = Cat("Satan")

#mary is a person
mary=Person("Mary")

##mary is a person and has a pet satan (Cat)
mary.pet = satan

##frank is a Employee
frank = Employee("Frank", 120000)

##frank has a pet rover(dog)
frank.pet = rover

##flipper is-a instance of Fish
flipper = Fish()

##crouse is-a instance of salmon
crouse= Salmon()

##harry is-a instance of Halibut
harry= Halibut()

print(satan.count)
