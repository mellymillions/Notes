# Python
This is how you capitalize first letters
```python
string = "art vandelay" # 'Art Vandelay'
(string.title())
```
This is how you make it all uppercase
```python
string = "Ceo" # 'CEO'
(string.upper())
```
This is how you validate if a string ends correctly
```python
string = "art.vandelay@vandelay.co" # False
(string.endswith('.com'))
```
This is how you validate if a string starts correctly
```python
'vandelay.com' # 'www.vandelay.com'
(string.startswith('www.'))
```
String Slicing: Isolate the area code
```python
string = "7285553334" # 728
"7285553334"[:3]
```
String Slicing: Isolate the phone number
```python
string = "7285553334" # 728
"7285553334"[4:10]
```
Making a List. We indicate that we are initializing a list with an opening bracket, [, and we end the list with a closing bracket ]. We separate each list item, also called an element, with a comma.
```python
top_travel_cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls']
```
Accessing List Elements: So to access the second element we write top_travel_cities[1], and the third element is top_travel_cities[2].
```python
top_travel_cities[2]
'Buenos Aires'
```
`slice`: Accessing multiple elements of a list
```python
top_travel_cities[0:2]
['Solta', 'Greenville']
```
Storing and assigning a `slice`
```python
top_two = top_travel_cities[0:2]
top_two
['Solta', 'Greenville']
```
append - Adding to the list
```python
top_travel_cities.append('San Antonio')
```
pop - Removing the last element from a list
```python
top_travel_cities.pop()
'San Antonio'
```
`set` Function: see a unique list of the elements. The set function is non-destructive on our list.A set is just like a list, except elements do not have order and each element appears just once.
```python
unique_travel_cities = set(top_travel_cities)
```
Convert a set into a List and test it:
```python
unique_travel_cities = list(unique_travel_cities)
type(unique_travel_cities)
list
```
Use `len` to check length of a list. Helpful to determine if your conversion from set to list or back worked correctly.
```python
len(unique_travel_cities)
unique_travel_cities
