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

If youre not sure if an object has an attribute:

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
# returns 800, the default value
```
Putting it all together:
```python
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))
```
