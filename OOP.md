# Classes

Classes should start with a capital letter!

Assign a class:
```python
class Melissa:
    pass
```
Assign class to variable:
```python
melissa_one = Melissa()
```
Looking at the class:
```python
print(type(melissa_one))

<class '__main__.Melissa'>
```
In this case, __main__ refers to the current file that is running.

Assign the type to a variable:
```python
melissa_one_type = type(melissa_one)
```
## Class variables

The same for every instance of the class.

Define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
```python
class Musician:
  title = "Rockstar"

#in the obejct.varibale syntax, the object is something that has been assigned to that class and the variable is that which is defined within the class - in this case, title.
```
## Instantiation:
```python
drummer = Musician()
print(drummer.title)

#here, we accessed the class attribute using the object.varibale syntax to yeild:
'Rockstar'
```
## Methods:

Methods are functions that are defined as part of a class.

The first argument in a method is the is always the object that is callign the methdod.

Convention recommends that we name this first argument **self**. Methods always have at least this one argument.

We define methods similarly to functions, except that they are indented to be part of the class.
```python
class Rules():  
  def washing_brushes(self):
   return "Point bristles towards the basin while washing your brushes."

```
**Note** - When you call a method it automatically passes the object calling the method as the first argument!

## Methods with Arguments

```python
class Circle():
  def area(self, radius):
    pi = 3.14
    return pi*radius**2

circle = Circle()
```
Then to use the method:
```python
#In each, we were given a diameter. It needed to be divided by 2 to get the radius before the method could be called on it. The radius is the argument being passed; self was default

pizza_area = (circle.area(12/2))
print(pizza_area)

teaching_table_area = (circle.area(36/2))
print(teaching_table_area)

round_room_area = (circle.area(11460/2))
print(round_room_area)
```
## Constructors:

Methods that are used to prepare an object being instantiated are called constructors. 

**Magic** or **Dunder** methods behave differently than normal methods. They are denoted by '__' on either side.

**Initialize:** or:
```python
__init__
```
This method is used to initialize a newly created object. It is called every time the class is instantiated, or runs every time you create a new object.

```python
class Person():
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name

        def speak(self)
        print(self.name)
    
p = Person('Melissa', 'Munz')

#when you call above, under the hood it is calling that init method and passing it that 'self' thing that is a reference to the person being created.

p.speak() #Melissa Munz
```
Another example:
```python
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)
```
## Instance variables

So far we know that a class is a schematic for a data type and an object is an instance of a class.

 But why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.

Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
```python
class Store:
  pass
```
Add instance attributes
```python
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices.store_name = "Isabelle's Ices"
```
## Attribute Functions

Instance variables and class variables are both accessed similarly in Python. Both are considered **attributes** of a object.

If youre not sure if an object has an attribute you can use hasattr and getattr.

What if we only really care whether the attribute exists? hasattr() will return True if an object has a given attribute and False otherwise.

**hasattr**
```python
hasattr(attributeless, "fake_attribute")
# returns False
```
getattr() is a Python function that works a lot like the usual dot-syntax (i.e., object_name.attribute_name) but we can supply a third argument that will be the default if the object does not have the given attribute. 

**getattr**
```python
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value because there are no other attributes for other types present.
```
Putting it all together:
```python
#below is a series of types, starting with a dictionary, a string, an integer, and a list. The forloop below shows how the hasattr function determines if each type has the atrribute "count" and then returns the count of 's's in it  
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

#First, the for loops skips the dictionary because dictionaries do not have a 'count' attribute
5 #number of 's' in 'sassafrass', a string which does have a 'count' attribute.
#Then it skips 18, which is a integer and does not have a 'count' attribute.
2 #number of 's' in the list of letters. Lists have a 'count' attribute.
```

## Self

Secure Methods: 

Since the self keyword refers to the object and not the class being called, we can define a secure method on the class.
```python
class Circle:
  pi = 3.14
  def __init__(self, diameter):
   print("Creating circle with diameter {d}".format(d=diameter))

 #radius is going to be a secure method:   
   self.radius = diameter/2

 #Each item in the method to define circumferance needs to relate to the 'self'.   
  def circumference(self):
    return 2 * self.pi * self.radius

#Define three new circles with their respective diameters.    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

#Print the circumference of those pizzas based on the functions above. make sure to add those final '()'!
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#Here's the output to all that:
Creating circle with diameter 12
Creating circle with diameter 36
Creating circle with diameter 11460
37.68
113.04
35984.4
```
## Dir()

Everything is an object!

Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. We can use the dir() function to investigate an object’s attributes at runtime. 
```python

print(dir(5))

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__'...'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
#This output is QUITE LONG so it's been shortened here, but the point is that the single integer '5' has a ton of attirbutes under the hood!


def this_function_is_an_object():
  pass
#You can also call 'dir' on a function, because a function is also an object!

print(dir(this_function_is_an_object))

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```
#String Representation (__repr__)

Now, we will learn another magic/dunder method called __repr__. 

This is a method we can use to tell Python what we want the string representation of the class to be. __repr__ can only have one parameter, self, and must return a string.

```python
#See this explained using the Circle class example

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def __repr__(self):
    return(f'Circle with radius {self.radius}')
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

#output
Circle with radius 6.0
Circle with radius 18.0
Circle with radius 5730.0
```
Making classes talk to eachother~

```python
class Student:
  def __init__(self, name, year):
   self.name = name
   self.year = year
   self.grades = []

#Below method updates the .grades list with a new grade.
  def add_grade(self, grade):
   if type(grade) == Grade:
    self.grades.append(grade)
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#The new class, Grade, provides parameters for determining if a student's grade is passing or not
class Grade:
 minimum_passing = 65
 def __init__(self, score):
  self.score = score

#This will provide a way to show the output that is readable and clean. It needs the 'str'!
 def __repr__(self):
  print('This is the score:')
  return str(self.score)
  
#Create a new instance, 'instantiating'
grade = Grade(100)

#Bring it all together: For the individual Student, Pieter, we will determine if he has a passing grade, and if yes, add it to the empty list, .grades from Grades,.
(pieter.add_grade(grade))

print(pieter.grades)
#Output
This is the score:
[100]

print(repr(pieter.grades[0]))
#Output (this one looks a little cleaner)
This is the score:
100
```
# Inheritance

For when we need a class that looks a lot like a class we already have.

Sometimes a **base class** is called a **parent class**. In these terms, the class inheriting from it, the **subclass**, is also referred to as a **child class**.

##Crating a subclass
```python

class SubClass(ParentClass):
    pass
```
## Exceptions

```python
# Define your exception up here:
class OutOfStock(Exception):
  pass
# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] == False:
      raise OutOfStock
    else:
      self.stock[color] = self.stock[color] - 1
      print(f"There are now {self.stock[color]} left in stock.")
      

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})

candle_shop.buy('blue')
#Output from 'blue':
There are now 5 left in stock.


candle_shop.buy('green')
#Output from green - OutOfStock Exception error
Traceback (most recent call last):
  File "script.py", line 22, in <module>
    candle_shop.buy('green')
  File "script.py", line 12, in buy
    raise OutOfStock
__main__.OutOfStock
```
## Overriding Methods


**Inheritance** is a useful way of creating objects with different class variables, but is that all it’s good for? What if one of the methods needs to be implemented differently?

All we have to do to override a method definition is to offer a new definition for the method in our subclass.
```python

#For the following classes:
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

 #Here is the override method. In this example, we've created an Admin override which can edit ANY message, not ont messages that arise from a particular sender like in the method above.     
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text
```
 ## Super()
 Sometimes we want to add some extra logic to the existing method. In order to do that we need a way to call the method from the parent class. Python gives us a way to do that using super().

 super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super():

This line says: “call the constructor (the function called __init__) of the class that is this class’s parent class.
 
 ```python
#Basically, calling a super() allows the parent method to fullfill it's duty, and then executes a new duty. It differs from Override Method in that Override will only filfill it's new duty.
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
   self.potatoes = potatoes
   self.celery = celery
   self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
   super().__init__(potatoes, celery, onions)
   self.raisins = 40
#Here, we've allowed the full potato salad to be constructed before executing super() to add the raisins.
```
## Interfaces

When two classes have the same method names and attributes, we say they implement the same interface. An interface in Python usually refers to the names of the methods and the arguments they take. 

It basically means that different objects from different classes can perform the same operation (even if it is implemented differently for each class).

```python
#Insurance Policy is the parent class:
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

#Now we definte two child classes; Vehicle and Home. Each has the same method definited within it, 'get_rate', with slightly different parameters.
   
class VehicleInsurance(InsurancePolicy):
  pass

  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  pass 

  def get_rate(self):
    return self.price_of_insured_item * .00005
```

##Polymorphism

Polymorphism is the term used to describe the same syntax (like the + operator being used to add integers, floats, strings, etc -  but it could also be a method name) doing different actions depending on the type of data.

Defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.

Here is a classic example of Polymorphism in action, using the built in 'len' function!
```python
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))
```
## Polymorphism and Magic/Dunder Methods

Here is an example of another Magic Method that is also an example of Polymorphism using the '__add__' method.
```python
class Atom:
  def __init__(self, label):
    self.label = label

#Here, we added a '__add__' dunder method that creates a Molecule by adding together two atoms.
  def __add__(self,other):
    return Molecule([self, other])
  
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
```
In our UserGroup class above we defined three methods:

`__init__`, our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup.

`__iter__`, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. For more information on iterators, review Python’s documentation of Iterator Types.

`__len__`, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.

`__contains__`, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.

```python
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
    
  def __len__(self):
    return len(self.lawyers)
  
  #The __contains__ magic method defines True or False membership to a list. In this case, we are checking in an indiviudal 'lawyer' is a member of the self.lawyers.
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
```
## Review - putting it all together

Here's an example using the built-in type 'List'.
```python
class SortedList(list):
  pass

#Here we use the 'super()' method to override the 'List' type and append the list with values, and then sort it.

  def append(self, value):
    super().append(value)
    self.sort()

#In this case, we can call 'self' again to refer back to the list, and call 'sort' on self!
```
We subclassed a Python primitive and introduced new behavior to it.

Some things to consider:

When a SortedList gets initialized with unsorted values (say if you call SortedList([4, 1, 5])) those values don’t get sorted! How would you change SortedList so that the list is sorted right after the object gets created?

What other Python builtins have functionality “missing”? Could you write a new dictionary that uses a fallback value when it tries to retrieve an item and can’t?

# Steps for Creating Classes and Hierachy

This example shows step by step how to create and use classes.

In this case, we are creating a restaraunt.

## 1. Create the class:
```python
class Menu:
```
## 2. Assign a constructor.

In this case, we are using the "__init__" construtor and passing in several arguments, including: self, name, items, start_time, end_time

Before moving on, we want to assign each of these arguments to a **self.** variable to make them usable later:

```python
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
```
## 3. Assign instances (instantiate). 

The prompt here reads: "Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch: (and it provides a dictionary)

Here, we assign the dictionary of brunch items to a variable name, and then instantiate it using the arguments needed for the "__init__" method.

```python
#First we assign the dictionary to a variable name:
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#Then, we instantiate this menu by assigning it to the 'Menu' class and passing in the necessary arguments that are needed for __init__ - in this case 'name', 'items', 'start_time', 'end_time'. 'Self' is inherent.
brunch = Menu('Brunch', brunch_items, 1100, 1700)

#Note that here we also need to assign time type to the start and end times, decided to use a 24hr clock.
```
In this case, we're also going to define a couple more instances of the 'Menu' class:

```python
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird = Menu('Early_Bird', early_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu('Kids', kids_items, 1100, 2100)
```
## 4. Create a string representation 

Now, we need to create a string repesentation for the 'Menu' class. 

Remember that right now, it you try to print out any of specific instatnce of 'Menu', you get this:
```python
print(brunch)
<__main__.Menu object at X0Fch4igo>

#total gobblygook. Instead, we want to create a string that prints when the intance is called that tells us something about the instance.
```
We need to use '__repr___':

```python
 def __repr__(self):
   return(f"The {self.name} menu is available from {self.start_time} to {self.end_time} and contains the following items: {self.items}")

#In this case, I included a string that provided information about all the variables, but you could only use a few.
```
Now, when we call any of the menus, we get:
```python
print(brunch)

The Brunch menu is available from 1100 to 1600 and contains the following items: {'pancakes': 7.5, 'waffles': 9.0, 'burger': 11.0, 'home fries': 4.5, 'coffee': 1.5, 'espresso': 3.0, 'tea': 1.0, 'mimosa': 10.5, 'orange juice': 3.5}
```
A much better representation of the instance!

## 5. Create a new method for the Class

In this case, the instructions want us to: "Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items. Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items."

This method is created within the Class - Menu.
```python
 def calculate_bill(self, purchased_items):
   #Here, we set the bill to '0' so that there is something to add to going forward. we know we will call 'bill' in the return.
   bill = 0
   #Now we make a for loop:
   for purchased_item in purchased_items:
     #The if statement below allows it to loop through each item and determine if it is indeed in the list of items. If it is, then that item will be added to the bill using '+='.
    if purchased_item in self.items:
      bill += self.items[purchased_item]
   return bill

#Putting it all together, the method looks like this:
 def calculate_bill(self, purchased_items):
   bill = 0
   for purchased_item in purchased_items:
    if purchased_item in self.items:
      bill += self.items[purchased_item]
   return bill
```
Call the new method to make sure that it works!

Here, we're printing an instance of the class (brunch) dot class method (calculate_bill), and then passing arguments needed for that method. In this case (purchased items), which we called as a list.
```python
print(brunch.calculate_bill(['pancakes', 'espresso']))
10.5
#It added the prices for pancakes and espresso!
```
Now we can use the 'calculate_bill' method for ANY of the menus!

```python
print(early_bird.calculate_bill(['salumeria plate', 'mushroom raviolli']))
8.0
#It calcuated this order was $8, even though it was a totally different menu!
```
## 6. Create a new Class

In this example, we are now opening restaraunt franchises, which we will represent with a new class.

First, create the subclass:
```python
class Franchise:
  pass
```
Then, define a constructor method. This one takes self, address, and menus. Assign them variables just as you did before.

```python
class Franchise:
  def __init__(self, address, menus):
   self.address = address
   self.menus = menus
```
## Create instances of the new class

Here, we're actually already going to start linking these classes together.

The Franchise class takes menus, and address.

First, we can assign all the menus to a single 'menus' variable:
```python
menus = [brunch, dinner, kids, early_bird]
```
Then, we can instiate the two new franchises by passing in the addresses (which the program has provided here), and the new variable 'menus'.)
```python
flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)
```
## Give the new Class a String Representation

Use '__repr__' again:
```python
 def __repr__(self):
    return (f"The franchise at {self.address} serves the following menus: {self.menus}")

print(flagship_store)
#output
The franchise at 1232 West End Road serves the following menus: brunch, dinner, kids, early_bird
```

## Provide a method for the new class

```python
def available_menus(self, time):
  available_menus = []
  for menu in self.menus:
   if time >= menu.start_time and time <= menu.end_time:
    available_menus.append(menu)
  return available_menus
```