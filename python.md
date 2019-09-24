# Python
LESSON 1: Introduction to Python

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
```
Change an element from the middle of the list, we can access and then reassign that element. For example, let's change 'Walla Walla Valley' to the number 4.
```python
top_travel_cities[4]
'Walla Walla Valley'
top_travel_cities[4] = 4
top_travel_cities
['Solta',
 'Greenville',
 'Buenos Aires',
 'Los Cabos',
 4,]
 ```
 Determining difference between unique varibles and original list. Convert all back to list from set first. Then, output is the different in unique values. In this example there are 13 countries and we found 10 unique_countries after converting the 'list' to 'set'.
 ```python
 len(countries)-len(unique_countries)
 3
 ```
 For data visualization: First we download a mapping library with 'pip'. Pip is another tool that allows us to easily download various Python libraries from the Internet.
 ```python
 !pip install folium
 ```
 Using 'pip': our folium library is available to us. Now we just tell Python that we will be using folium in our codebase by writing import folium in the next cell. (In this example we already assigned coordinates to the latitude and longitude variables below. Reminder that quotes are not necessary when assigning integer variables).
 ```python
 import folium
buenos_map = folium.Map([ba_latitude, ba_longitude])
buenos_map
```
Add a marker to the map. In this case we used the folium library to create a marker and specified coordinates of the marker as a list. Add the marker to our map with the 'add_to' function.
```python
buenos_marker = folium.Marker([ba_latitude, ba_longitude])
buenos_marker.add_to(buenos_map)
 ```
 Matching coordinates on a Map using Folium
 ```python
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
marker_one = folium.Marker([-34.5711, -58.4233])
marker_two = folium.Marker([-34.5895, -58.3974])
marker_three = folium.Marker([-34.6212, -58.3731])
marker_four = folium.Marker([-34.6177, -58.3621])
marker_five = folium.Marker([-34.603722,  -58.381592])
marker_six = folium.Marker([-34.6037, -58.3816])
neighborhood_markers = [marker_one, marker_two, marker_three, marker_four, marker_five, marker_six]
```
Assign a marker to one of the above coordinates
```python
la_boca_marker = folium.Marker([-34.6037, -58.3816])
```
View the map (with Zoom) to see Marker:
```python
import folium
buenos_map = folium.Map([ba_latitude, ba_longitude], zoom_start = 12)
la_boca_marker.add_to(buenos_map)
buenos_map
```
LESSON 2: Dictionary

Creating a direct association between the attribute or key and its correlated value (i.e. {'key': "value"}). This datatype makes it easier to store and access information, such as the attributes of a person or other entity. Always start and end a Dictionary with curly brackets {}.
```python
terrance = {'name': "Terrance", 'age': 25, 'weight': 72, 'height': 165, 'fav_lang': "Python"}
```
If a dictionary is: friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}

Retreiving a Dictionary:
```python
friends
{'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
```
OR: Retreiving information from a Dictionary
```python
friends['no_of_seasons']
10
```
Add to a Dictionary
``python
friends['no_of_episodes'] = 236
friends
{'name': 'Friends',
 'genre': 'sitcom',
 'no_of_seasons': 10,
 'no_of_episodes': 236}
 ```
 Delete from a Dictionary using 'del'
 ```python
 friends[Test] = 'some value'
 del friends[Test]
 ```
Lists within a Dictionary: If there are more than one value/variable associated with an item. This example uses the two co-creators of Friends:
 ```python
 creators = ['David Crane', 'Marta Kauffman']
 friends['creators'] = ['David Crane', 'Marta Kauffman']
 ```
 NOW the Dictionary looks like this:
 ```python
 friends
{'name': 'Friends',
 'genre': 'sitcom',
 'no_of_seasons': 10,
 'no_of_episodes': 236,
 'creators': ['David Crane', 'Marta Kauffman']}
 ```
 To see just ONE item or list from the dictionary, ask:
 ```python
 friends['creators']
 ['David Crane', 'Marta Kauffman']
 ```
 Store one of the list items as a single variable:
 ```python
 david = friends['creators'][0]
 ```
(In above line, we referenced the dictionary, then got to the list of creators through using the key creators. And now that we are pointing to that list, we use the brackets to reference the string at index zero.) If we wanted Marta Kaufmann, it would be:
```python
Marta = friends['creators'][1]
```
Nested Structures! 
After creating a Dictionary for Seinfeld that mimics the structure of the Friends Dictionary, we now have...a 'list' of TV Shows! 
INPUT is here:
```python
tv_shows = [friends, seinfeld]
tv_shows
```
The nested OUTPUT is here:
```python
[{'name': 'Friends',
  'genre': 'sitcom',
  'no_of_seasons': 10,
  'no_of_episodes': 236,
  'creators': ['David Crane', 'Marta Kauffman']},
 {'name': 'Seinfeld',
  'creators': ['Larry David', 'Jerry Seinfeld'],
  'genre': 'sitcom',
  'no_of_seasons': 10,
  'no_of_episodes': 180}]
  ```
To select specific information from a nested structure, follow this format. 

You start by selecting which of the TV shows (in this case, 'Friends' is 0 and 'Seinfeld' is 1, per output above).
  ```python
  tv_shows[1]
 {'name': 'Seinfeld',
 'creators': ['Larry David', 'Jerry Seinfeld'],
 'genre': 'sitcom',
 'no_of_seasons': 10,
 'no_of_episodes': 180}
 ```
 Then, choose the rest of the information you are looking for (in this case, it's Jerry), and then assigning that pathway as the variable 'jerry'.
 ```python
 tv_shows[1]['creators']
 ['Larry David', 'Jerry Seinfeld']
 tv_shows[1]['creators'][1]
 'Jerry Seinfeld'
 jerry = tv_shows[1]['creators'][1]
jerry
 ```
 Importing Dictionaries:
 
 How to move an .xlsx (Excel) file into Python! 
 ```python
 import pandas
travel_df = pandas.read_excel('./cities.xlsx')
cities = travel_df.to_dict('records')
cities[0]
#OR
import pandas as pd
file_name = './cities.xlsx'
travel_df = pd.read_excel(file_name)
cities = travel_df.to_dict('records')
```
Here is that same code with comments for context:
```python
# Here we use a library, which is some code not part of standard Python, to make this process easier 
import pandas
# If we use the `import pandas` we have access to the pandas library 
travel_df = pandas.read_excel('./cities.xlsx')
# We call the pandas.read_excel method and pass through the string './cities.xlsx' as the file is called cities.xlsx.  By saying './' we are saying 
# go to the current folder, lists-lab, and find the 'cities.xlsx' file there
cities = travel_df.to_dict('records')
# now the whole excel spreadsheet is in Python!!
 ```
 To see only the keys in a Dictionary. You don't need to see all the associated values if you're looking for just the types of information that the Dictionary has present.
 ```python
 cities[0].keys()
 dict_keys(['City', 'Country', 'Population', 'Area'])
 # Note that the keys() function returns a dict_keys object. It's a little tricky to work with that type of object, so let's coerce it into a list:
 list(cities[0].keys()) 
 ['City', 'Country', 'Population', 'Area']
 ```
 To see just the values in a Dictionary, and not keys, try this:
 ```python
 cities[0].values()
 dict_values(['Solta', 'Croatia', 1700, 59])
 #Or again, even simpler, try using a list funtion:
 list(cities[0].values())
 ['Solta', 'Croatia', 1700, 59]
 ```
Two ways of creating Dictionaries:
```python
#The 1st Way:
philadelphia = {'City': 'Philadelphia'}
#The 2nd Way:
pittsburgh = dict(city='Pittsburgh')
pittsburgh
#Python knows how to convert the string to the dictionary. Here's the same structure with more keys and variables:
dict(city="Las Vegas", state="Nevada")
{'city': 'Las Vegas', 'state': 'Nevada'}
```
DATA VISUALIZATION
There are various Python visualization tools we can use to display our data. In this lesson, we will be using Plotly, as it produces nice looking graphs and is easy to work with.

We can easily download the plotly library with the use of 'pip'.
```python
!pip install plotly==3.3.0
#In this case we are using plotly offline account.
import plotly
plotly.offline.init_notebook_mode(connected=True)
```
Building a graph using Plotly:
Create a new dictionary and assign it to 'trace0'. Then set 'x' key that points to a list of xx values, and create a 'y' key with a value of a list of yy values.
```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 10]}
trace0
#In this case, the type of graph is a 'bar', and there are three variables assigned to each the X axis and the Y axis.
```
Plot the graph!  ( This graph has only ONE x and ONE y variable, with three data points in each)
```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy'], 'y': [8, 11, 10]}

plotly.offline.iplot([trace0])
# Notice in this code strucuture the 'trace0' described above is now embedded in the offline Plotly account also described above.
```
Understanding 'Plot' vs 'Trace0'. (Unlike the one above, this graph has 2 sets or 'Traces' of data for each x and y 'key' , with four 'variable' data points on available in each)
```python
trace0 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy', 'blaise'], 'y': [8, 11, 8, 13, 6, 4]}
trace1 = {'type': 'bar', 'x': ['jack', 'jill', 'sandy', 'gob'], 'y': [4, 12, 3, 14, 8, 1]}

plotly.offline.iplot([trace0, trace1])
#this data visulualization is represented as a bar graph, as noted in the trace.
```
Building a 'trace': build a trace. A trace is a dictionary with a key of x and a key of y. We have set up a trace to look like the following: trace_first_three = {'x': x_values, 'y': y_values}. 
```python
#First define x_values so that it is a list of names of the first three cities, 
x_values = [cities[0]['City'], cities[1]['City'], cities[2]['City']]
#and y_values as those city's populations.
y_values = [cities[0]['Population'], cities[1]['Population'], cities[2]['Population']]
#And then Plot!
trace_first_three_pops = {'x': x_values, 'y': y_values}

plotly.offline.iplot([trace_first_three_pops])
#This time, data is represented in a line graph (Line is the default!)
```
Modifying a Trace: The default is a line graph. We can our trace a bar trace by setting the 'type' key equal to 'bar'.
```python
example_trace = {'type': 'bar', 'x': x_values, 'y': y_values, 'text': ["label_1", "label_2", "label_3"]}
#In this case, we have also added labels to the graph!
```
Creating a single trace:
```python
bar_trace_first_three_pops = {'type': 'bar', 'x': x_values, 'y': y_values, 'text':["Buenos Aires", "Toronto", "PyeongChang"]}
```
Adding a second trace to plot side by side

Ok, now let's plot two different traces side by side. First, create another trace called bar_trace_first_three_areas that is like our bar_trace_first_three_pops except the values are a list of areas. We will display this side by side along our bar_trace_first_three_pops in the plot below.
```python
y_values2 = [cities[0]['Area'], cities[1]['Area'], cities[2]['Area']]
#First, I created a new variable for Area which I called y_values2.
bar_trace_first_three_pops = {'type': 'bar', 'x': x_values, 'y': y_values, 'text': ["Buenos Aires", "Toronto", "Pyeongchang"]}
bar_trace_first_three_areas = {'type': 'bar', 'x': x_values, 'y': y_values2, 'text': ["Buenos Aires", "Toronto", "Pyeongchang"]}
#This graph compares the overall population of each city to the overall area. Clearly, Toronto has much more space for its population than the other two cities.
``` 
Summary of Plotly:
In this section, we saw how we use data visualizations to better understand the data. We do the following. Import plotly:
```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
#Then we define a trace, which is a Python dictionary.

trace = {'x': [], 'y': [], 'text': [], 'type': 'bar'}
#Finally, we display our trace with a call to the following method:

plotly.offline.iplot([trace])
#the end!
```
INTRO TO LOOPS

A 'for' loop in Python is primarily used for going through elements of a list one by one. 
```python
#Using Loops, instead of doing this:
zero_to_three = [0, 1, 2, 3]
print(zero_to_three[0])
print(zero_to_three[1])
print(zero_to_three[2])
print(zero_to_three[3])
0
1
2
3
#This code performs the exact same function:
for number in zero_to_three:
    print(number)
0
1
2
3
```
***Breaking down components of a for loop***: A for loop essentially has two necessary components, which we'll refer to as arguments. 

The first argument is the variable name we are assigning to an element, or in this case, `number`. 

The second argument is the collection we are iterating over, or in this case, the list `zero_to_three`.

We can give any name to the variable. The important thing to understand here is **it is the reference** to each **element** in the collection. So, when we print `number`, we are printing an element of the collection `zero_to_three`. 

**Undersanding indentation and blocks**: Every for loop needs to end the first line with a colon `:`. This indicates the start of the **block** of code. 

The **block** is simply the code that we want executed in each iteration of our loop. So, if all we want to do is print each element, then the line that prints the element is our block. Our block is indicated by indenting. So the first line after the colon `:` should be indented. When we want to end our block, we simply stop indenting. Any code follwing the for loop will only be executed after the for loop finishes.
```python
iteration_count = 0
for whatever_we_want in zero_to_three:
    iteration_count += 1
    print("This is iteration:", iteration_count)
    print(whatever_we_want)
print("The for loop is finished now! I am not in the for loop block, which is why I only printed once!")
This is iteration: 1
0
This is iteration: 2
1
This is iteration: 3
2
This is iteration: 4
3
The for loop is finished now! I am not in the for loop block, which is why I only printed once!
```
To perform mutliple funtions, follow this format:
```python
for index in [0,1,2,3,4,5,6,7]:
    print(index)
    print(countries[index])
0
Croatia
1
USA
2
Argentina
3
France
4
Brazil
5
Japan
6
Vietnam
7
Israel
#In this case we are still using the elements in the list of numbers from 0 to 7 in our for loop, but we are instead using them to access each element of another list. 
```
 For two lists that are ordered correctly and have information like the capital cities in one list and the the corresponding countries in another. To print them both out in the same line:
 ```python
 countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam', 'Israel']
cities = ['Zagreb', 'Distric of Columbia', 'Buenos Aires', 'Paris', 'Rio de Janeiro', 'Tokyo', 'Hanoi', 'Tel Aviv']
for index in [0,1,2,3,4,5,6,7]:
    print(cities[index]+",", countries[index])
Zagreb, Croatia
Distric of Columbia, USA
Buenos Aires, Argentina
Paris, France
Rio de Janeiro, Brazil
Tokyo, Japan
Hanoi, Vietnam
Tel Aviv, Israel
#note that this will NOT work if your number of iterations does not match up with the size of our list.
```
To make sure you have the correct length of list to execute, use the **len** function!
```python
len(countries)
8
#Then create a range object:
range(0, len(countries))
range(0, 8)
#And then convert this into a list:
list(range(0, len(countries)))
#Note that the range object is marking the starting and ending point, and excluding the end. Now this works:
for index in list(range(0, len(countries))):
    print(cities[index] + ",", countries[index]) #In this example, the plus sign provides the concatination of the lists.
Zagreb, Croatia
Distric of Columbia, USA
Buenos Aires, Argentina
Paris, France
Rio de Janeiro, Brazil
Tokyo, Japan
Hanoi, Vietnam
Tel Aviv, Israel
#To add and subtract countries, we will still be iterating through our list elements.
countries.append('Mexico')
cities.append('Mexico City')
for index in list(range(0, len(countries))):
    print(cities[index] + ",", countries[index])
```
**Looping different datatypes**: A loop variable can represent any data type, not just an element of a list that is a number. Here's a for loop with **dictionaries**:
```python
example_dictionary = {'first_name': "Terrance", 'last_name': "KOAR", 'favorite_language': "Python"}
print(example_dictionary.items())
type(example_dictionary.items())
#Output follows:
dict_items([('first_name', 'Terrance'), ('last_name', 'KOAR'), ('favorite_language', 'Python')])
dict_items
```
Here we can see this dict_items object looks almost like a list, but each item has two parts, the key and value. 
```python
#So, in our first iteration, the first key will be first_name, and the first value will be Terrance.
for key, value in example_dictionary.items():
    print("this is the key:", key)    
    print("this is the value:", value, "\n")
#In the example, the "\n" causes the paragraph breaks.
this is the key: first_name
this is the value: Terrance 

this is the key: last_name
this is the value: KOAR 

this is the key: favorite_language
this is the value: Python 
```
Output and formatting for specific information or keys from a dictionary. In this case, we're looking for First and Last name, displayed in normal formatting.
```python
first_name = ""
favorite_language = ""
#Above provides the formatting. In this case, making it standard instead of all caps.
for key, value in example_dictionary.items():
    if key == "last_name": 
        last_name = value.title()
    if key == "first_name":
        first_name = value
#Above section connects to the key. If you change to 'favorite_language', that will be in the output instead of 'first_name'.
print(first_name, last_name)
#This just tells it how to display the output.
#Output:
Terrance Koar
```
Here's a great **for loop** example!
```python
ice_cream_flavors = ['Mint Chocolate Chip', 'Coffee', 'Cookie Dough', 'Fudge Mint Brownie', 'Vanilla Bean']
for ice_cream_flavor in ice_cream_flavors:
    print('I love ' + ice_cream_flavor + ' ice cream!!')
I love Mint Chocolate Chip ice cream!!
I love Coffee ice cream!!
I love Cookie Dough ice cream!!
I love Fudge Mint Brownie ice cream!!
I love Vanilla Bean ice cream!!
#note the naming convention above - when the key is named 'ice_cream_flavor' in 'ice_cream_flavors' which is a universal naming convention.
```
PROJECT TEST 1: Your task is to assign the variable names_and_ranks to a list, with each element equal to the city name and it's corresponding rank. For example, the first element would be, "1. Buenos Aires" and the second would be "2. Toronto". Use a for loop and the lists city_indices and city_names to accomplish this. We'll need to perform some nifty string interpolation to format our strings properly. Check out f-string interpolation to see how we can pass values into a string. Remember that list indices start at zero, but we want our names_and_ranks list to start at one!
```python
names_and_ranks = [] #What does it mean for it to equal '[]'?
for index in city_indices: 
    names_and_ranks.append(f"{index + 1}. {city_names[index]}")
 # THIS WAS DIFFICULT! I did not know the 'f' string syntax used. Also, need recall use of index, definition below, for these functions.   
names_and_ranks
['1. Buenos Aires',
 '2. Toronto',
 '3. Pyeongchang',
 '4. Marakesh',
 '5. Albuquerque',
 '6. Los Cabos',
 '7. Greenville',
 '8. Archipelago Sea',
 '9. Walla Walla Valley',
 '10. Salina Island',
 '11. Solta',
 '12. Iguazu Falls']
```
**Index**: The index() method searches an element in the list and returns its index. In simple terms, index() method finds the given element in a list and returns its position. However, if the same element is present more than once, index() method returns its smallest/first position. 

Reminder: Index in Python starts from 0 not 1.

PROJECT TEST 2: Create a new variable called `city_populations`.  Use a `for` loop to iterate through `cities` and have `city_populations` equal to each of the populations.
```python
city_populations = []
for city in cities:
    city_populations.append(city['Population'])
city_populations
#What exactly is the 'append' doing here? ALSO, how did it know how to rank them?
2891000,
 2800000,
 2581000,
 928850,
 559277,
 287651,
 84554,
 60000,
 32237,
 4000,
 1700,
 0]
 ```
Plotting the data on Plotly:
First create a trace of our populations and set it to the variable 'trace_populations'.

Note that the items below are all ones we created throughout the lesson:
```python
trace_populations = {'x': names_and_ranks, 
                     'y': city_populations, 
                     'text': names_and_ranks, 
                     'type': 'bar', 
                     'name': 'populations'}

#Now import Plotly:
import plotly
plotly.offline.init_notebook_mode(connected=True)
plotly.offline.iplot([trace_populations])
#looks like the only thing that changes here is the final item, in this case pulling on the 'trace_populations' which we set above.
```
FUNCTIONS!!!

Here's an example of converting some loop code into a function. Start with the regular for loop:
```python
#Here's the data set:
new_employees = ['steven', 'jan', 'meryl']
#Here's the code for a welcome message to those new employees
welcome_messages = []
for new_employee in new_employees:
    welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )
    
welcome_messages
["Hi Steven, I'm so glad to be working with you!",
 "Hi Jan, I'm so glad to be working with you!",
 "Hi Meryl, I'm so glad to be working with you!"]
```
Now make it into a function:
```python
def greet_employees():
    welcome_messages = []
    for new_employee in new_employees:
        welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

    return welcome_messages
```
**There are two steps to using a function:**

1: **Define**(or Declare): Defining a function happens first, more on this below. In this example, it was def greet_employees()

2: **Execute**: Executing a function is fairly simple, just type the function's name followed by parentheses. Now when we call greet_employees() we execute the function. 

**Now if some new employees arrive, I can just execute the function I defined:**
```python
new_employees = ['Jan', 'Joe', 'Avi']
greet_employees()
["Hi Jan, I'm so glad to be working with you!",
 "Hi Joe, I'm so glad to be working with you!",
 "Hi Avi, I'm so glad to be working with you!"]
 ```
**Declaring a Function**: There are two components to declaring a function: the **function signature** and the **function body**.

**Function Signature**: The function signature is the first line of the function. It follows the pattern of def, function name, parentheses, colon.
```python
def name_of_function():
```
_The def is there to tell Python that you are about to declare a function. The name of the function indicates how to reference and execute the function later. The colon is to end the function signature and indicate that the body of the function is next. The parentheses are important as well, and we'll explain their use in a later lesson._

**Function Body**:
The body of the function is what the function does. This is the code that runs each time we execute the function. We indicate that we are writing the function body by going to the next line and indenting after the colon. To complete the function body we stop indenting.
```python
def name_of_function(): 
    words = 'function body' # function body
# no longer part of the function body
```
Here's the full function, with return statement to produce the desired output.
```python
def greet_employees(): # function signature
    welcome_messages = [] # begin function body
    for new_employee in new_employees:
        welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

    return welcome_messages # return statement

# no longer in function body
```
Function Practice: Write amfunction which iterates through the list of destinations and capitalizes the first letter of each word. It should return a list of capitalized destinations.
```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
def capitalize_countries():
    travel_destinations = []
    for travel_destination in travel_destinations:
      travel_destinations.append(travel_destination.title())
    pass
```
**Return Statements:**
Variables declared inside a function cannot be retreived globally unless you are using a return statement. The example below shows how this plays out:
```python
def return_full_name():
    first_name = 'bob'
    last_name = 'smith'
    full_name = first_name + ' ' + last_name
    return full_name
return_full_name()
'bob smith'

'Hello ' + return_full_name()
'Hello bob smith'
```
**Predictability with arguments**:

**dependencies**: When code requires something to work, we call that something a dependency. 

Example: This function requires a dependency that is not present. We have not yet defined 'traveller' variable.

```python

def meet_traveller(): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message # return statement

NameError: name 'traveller' is not defined
```
Let's try the same function, with 'traveller' better defined.
```python
def meet(traveller): 
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
meet()
#In the code above we changed the first line of the function, the function signature, to the following:

def meet(traveller):

#This tells us, and Python, to not even run the code unless the proper data to the function is provided
```
By using an **argument**, the function signature tells us how to run this function. We refer to the function by it's name and then pass through a string representing the 'traveller'.

Quick Dictionaries reminder:
 
 Look at the keys of a dictionary to quickly view the attributes of that dictionary.
```python
fork_fig.keys()
#'fork_fig' is a yelp review for a restarant. This reveals:
dict_keys(['categories', 'coordinates', 'display_phone', 'distance', 'id', 'image_url', 'is_closed', 'location', 'name', 'phone', 'price', 'rating', 'review_count', 'transactions', 'url'])
```
To check if keys between two dictionaries are the same (and thus comparible):
```python
fork_fig.keys() == frontier_restaurant.keys()
True
```
Write a function called restaurant_name that, provided a dictionary representing a restaurant like you saw above, returns that restaurant's name.
```python
def restaurant_name(restaurant):
    return restaurant['name']
```
Now for restaurant rating. This is good practice with **dictionaries** and **functions**.
```python
def restaurant_rating(restaurant):
    return restaurant['rating']
```
**Comparing statements**:

Now let's write a function called is_better that returns True if a restaurant has a higher rating than an alternative restaurant. The first argument should be called restaurant and the second argument should be called alternative. The function returns False if the two ratings are equal.
```python
def is_better(restaurant, alternative):
    if restaurant['rating'] > alternative['rating']:
        return True
    return False
#What exactly does the indentation here mean? In this example, 'True' if higher rating, 'False' if the same rating
```
In the one below, returns True if a restaurant has a lower price, that is the restaurant has fewer '$' signs. The function returns False if the two prices are equal.

Because the 'price' is determined in '$-$$$', used 'len' of the price string.
```python
def is_cheaper(restaurant, alternative):
    if len(restaurant['price']) < len(alternative['price']):
        return True
    return False
#output
is_cheaper(fork_fig, frontier_restaurant)
False
```
Testing greater or equal to a specific number, in this case a rating:
```python
def high_rating(restaurant, rating):
    if restaurant['rating'] >= rating:
        return True
    return False
    pass
#output
high_rating(fork_fig, 4)
True
```
**If Statement and Execution Flow**:

The **+=** is used to increment. consider:

```python
vacation_days = 0
vacation_days += 1
vacation_days += 1
vacation_days
#output
2
```
The statement vacation_days += 1 can be thought of as vacation_days = vacation_days + 1. 

On line 2, vacation_days is 0. Then we reassign vacation_days to equal the previous value of vacation_days, which is 0, plus 1. 

Again we increment vacation_days on line 3, which would now equate to 1 + 1, 

and finally we output the new value of vacation_days, 2.
```python
vacation_days = 1
if False:
    # code does not run as conditional argument False
    vacation_days += 1
vacation_days
1
#Since the condition following the if equals False, the code directly underneath is not run. Vacation_days stays assigned to the number 1.
```
Here, see how the indentation tell the function when it is conditional:
```python
vacation_days = 1
if False:
    # if block begins
    vacation_days += 1
# if block ends
vacation_days += 2
vacation_days
3
#So in the above cell, the last two lines are run because they are not part of the if block.
```
When the conditional argument is True, the code in the conditional block does run.
```python
vacation_days = 1
if True:
    # code in if block runs, as True
    vacation_days += 1
vacation_days
2
```
**Code that sometimes runs:**
```python
def long_vacation(number_of_days):
    if number_of_days > 4:
        return 'that is a long vacation'
long_vacation(5)
'that is a long vacation'
long_vacation(3)  
#Our if argument is the expression number_of_days > 4, which sometimes evaluates to True and sometimes False, it depends on the number of days.
```
**When something is True do one thing, and when not True do something else.**
```python
def vacation_length(number_of_days):
    if number_of_days > 4:
        return 'that is a long vacation'
    else:
        return 'not so long'
vacation_length(3) 
'not so long'
vacation_length(5)
 'that is a long vacation'
 ```
 **Truthiness and falsiness**:  
 Conditionals also consider some values True if they are truthy and False if they are falsy. Take a look at the following:
 ```python
 vacation_days = 1
if vacation_days:
    # this is run
    vacation_days += 1
vacation_days
2
#Even through vacation_days did not equal True above, it still ran the code in the if block because the value for vacation_days was 1, which is considered truthy.
```
What is and isn't truthy?

**Zero** is falsy, and **None** is falsy. Also falsy is anything where len of that thing returns False, so '', [] are both falsy. Let's see that.
```python
#Here's that last example:
greeting = ''
if greeting:
    greeting += 'Hello'
else:
    greeting += 'Goodbye'
greeting

'Goodbye'
```
To know if something is truthy or falsy, use a Bool test:
```python
bool(0) 
false
bool(1)
true
```
**Conditionals in Loops**
```python
greetings = ['hello', 'bonjour', 'hola', 'hallo', 'ciao', 'ola', 'namaste', 'salam']

def starts_with_h(words):
    selected = []
    for word in words:
        if word.startswith('h'):
            selected.append(word)
    return selected 

starts_with_h(greetings)
['hello', 'hola', 'hallo']
```
The above starts_with_h function uses a for loop to move through the list of words one by one. 

For each word, it checks if the word starts with h and if it does, it adds that word to the selected list. 

Finally, the function returns that list of selected elements. So by using the for loop combined with if we can choose elements of a list based on a specific criteria.



More on **Conditionals**: Writing functions with conditionals

Let's write a function called better_restaurant that provided two restaurants, returns the restaurant with the better rating. The first argument is restaurant and the second argument is alternative.
```python
def better_restaurant(restaurant, alternative):
    if restaurant['rating'] > alternative['rating']:
        return restaurant
    return alternative
print(better_restaurant(frontier_restaurant, fork_fig)['name']) # 'Fork & Fig'
print(better_restaurant(fork_fig, frontier_restaurant)['name']) # 'Fork & Fig'
```
Let's write a function called cheaper_restaurant that returns the restaurant with the lower price, that is the restaurant that has fewer '$' signs. The first argument should be named restaurant and the second argument should be named alternative.
```python
def cheaper_restaurant(restaurant, alternative):
    if len(restaurant['price']) < len(alternative['price']):
        return restaurant
    return alternative
 print(cheaper_restaurant(fork_fig, frontier_restaurant)['name'])
#output
Frontier Restaurant
```
Test: Let's continue our work of conditionals by seeing how they can be combined with loops. Let's write a function called open_restaurants that takes in a list of restaurants as an argument and returns a list of only the restaurants that are not closed.
```python
def open_restaurants(restaurants):
    selected = []
    for restaurant in restaurants:
          if restaurant['is_closed'] == False:
            selected.append(restaurant)
    return selected
open_restaurants(restaurants)[0]['name']
'Fork & Fig'
```
First solve it for one element
Before determining how to categorize all elements in a list, let's just answer the question of whether one element is even. We can do so by making use of the modulo operator, %. The % returns the **remainder** resulting from dividing a number by another. For example:
```python
7 % 3
1
#7 divided by 3 is 2, with a remainder of 1, which is the output here.
6%3
0
#When it divides evenly, there is no remainder so the output is 0.
```
Note that the above line effectively asks (and answers) whether 4 is even. This is because the statement 4 % 2returns a zero, which means that four divided by two has a remainder of zero, and as we know, any number that is divisible by two with no remainder leftover is an even number.

**Even and Odd**
Note that the above line effectively asks (and answers) whether 4 is **even**. 
Similarly, if a number is **odd**, then dividing by the number two results in a remainder of one.
```python
def is_even(number):
    return number % 2 == 0
print(is_even(3)) # False
print(is_even(100)) # True
False
True
```
Here’s a function:
```python
def select_even(elements):
    selected = []
    for element in elements:
        if is_even(element):
            selected.append(element)
    return selected

numbers = list(range(0, 11))
numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

select_even(numbers)
[0, 2, 4, 6, 8, 10]
```
**Returning a subset of elements that meet a specific criteria is something commonly done in Python.** And the procedure looks pretty much the same regardless of what we are selecting. For example, let's now select words that end with 'ing'.
```python
#What exactly is this section at the top? Why would you not be able to start with the function below?
def ends_ing(word):
    return word.endswith('ing')

def select_ing(elements):
    selected = []
    for element in elements:
        if ends_ing(element):
            selected.append(element)
    return selected

words = ['camping', 'biking', 'sailed', 'swam']
select_ing(words)
['camping', 'biking']
```
Notice that our two functions **select_ing** and **select_even** share a lot of similarity. Below, let's just highlight the differences.
```python
def select_ing(elements):
#     selected = []
#     for element in elements:
        if ends_ing(element):
#             selected.append(element)
        #return selected

def select_even(elements):
#     selected = []
#     for element in elements:
        if is_even(element):
#             selected.append(element)
# return selected
```
Essentially, the only thing different between the functions is the criteria of how we are selecting. The **filter()** function allows us to filter for specific elements, so long as it knows the criteria and the elements.

The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
The general syntax of a filter() function is given as:
```python
filter ( function, iterable )
```
Apply this to filter the even numbers as we did above with a condition and loop:
```python
filter(is_even,numbers) #filter ( function, iterable )
<filter at 0x7f89f44e6a20>
#This doesnt really mean anything. It needs to be coerced by a list in order to produce a meaningful result:
list(filter(is_even, numbers))
[0, 2, 4, 6, 8, 10]
```
The filter function takes two arguments, the first is the function itself. The function goes through each element, and passes that element into the criteria function. 
If that criteria function returns a truthy value, the element is selected. 
If not, the element is not selected.
**Note that when passing through the function, no parentheses are added at the end of the function. This is important. If we pass through the parentheses the filtering will not occur.

**Filter WITHOUT a Function**
Passing the list to the filter without supplying a first argument
```python
random_list = [0,'0','python', 2, True, 'flatiron', False, 38.9]
```
Our random_list above contains a number of different data types. Let's pass this list through function()and use None for filter function.
```python
list(filter(None, random_list))
['0', 'python', 2, True, 'flatiron', 38.9]
#filter function as None, the function defaults to Identity function i.e. each element in random_list is checked to see if it is true or not. So in the output, we only get the elements which are true. Numbers and strings are always true (this includes '0' as a string), whereas 0 and False return a False value and hence are not included in the output.
```
**Map with Python**
Use the map function not to return a subset of elements, but to alter each element in a similar manner.
```python
#list of names
names = ['Homer', 'Marge', 'Bart', 'Maggie', 'Lisa']
```
We would like to add the name Simpson to the end of each name. Just as we did with filter, we can start by writing a function that solves the problem for one element.
```python
#In this example, HOW  does it know to call upon the ‘name’ list above??
def add_simpson(name):
    return name + " Simpson"
add_simpson("Homer")
'Homer Simpson'
#our method add_simpson successfully takes in a string, name, and returns that string with the added last name, Simpson.
```
Solve for all: iterate through the names one by one, and for each name we perform the same operation -- add the last name "Simpson".
```python
#Does it need this section to work? I’ve added it in here. I assume that this means it can 
def add_simpson(name):
    return name + " Simpson"

#Here is the function
def add_simpsons(elements):
    altered = []
    for element in elements:
        altered.append(add_simpson(element))
    return altered
```
Let's write a function that derives the initials of each person's name.
```python
def find_initial(name): # name = 'Michael Prude'
    names = name.split(' ') # ['Michael', 'Prude']
    first_name = names[0] #'Michael'
    last_name = names[1] # 'Prude'
    return first_name[0] + last_name[0] # 'M' + 'P'
  
homer = simpsons[0]
find_initial(homer)
'HS'
```
And to apply it to the whole list:
```python
def find_initials(elements):    
    altered = []
    for element in elements:
        altered.append(find_initial(element))
    return altered

find_initials(simpsons) 
['HS', 'MS', 'BS', 'MS', 'LS']
```
Again, Our two functions, are quite similar.
```python
def add_simpsons(elements):
#     altered = []
#     for element in elements:
        altered.append(add_simpson(element))
#     return altered

def find_initials(elements):    
#     altered = []
#     for element in elements:
        altered.append(find_initial(element))
#     return altered
```
**Map Function**: The map function allows us to apply the same operation to each element and return a new list of elements receiving the modified elements from this operation.

A map() function is defined in python like this:
```python
map(Function, Sequence)
```
Just as the filter function returns a filter object, the map function returns a map object. 

In order to get our desired list back, we need to coerce the map object to a list:
```python
list(map(add_simpson, names))
['Homer Simpson',
 'Marge Simpson',
 'Bart Simpson',
 'Maggie Simpson',
 'Lisa Simpson']
 ```
 OR:
 ```python
 list(map(find_initial, simpsons))
 ['HS', 'MS', 'BS', 'MS', 'LS']
 ```
The **pow** built-in python function takes in two numbers as arguments and calculates the result by setting second number as power of first number. 
```python
pow(2,4)
16

#another example:

list(map(pow, [2, 4, 8], [3, 5, 7]))
[8, 1024, 2097152]
```
Summary of Map:
Map function which takes in two arguments.

 The **first argument** is the altering function, which operates on each element by passing through the element as an argument and returning a value. 
 
 The **second argument** is the list of elements to be iterated through and operated on. 
 
 The return values of the altering function are appended to a new list, which is returned after we coerce our map object into a list.

 **Practice**
 ```python
 def extract_name(thing_with_a_name):
    return thing_with_a_name['name']

names = list(map(extract_name, restaurants))
names
# ['Fork & Fig',
#  'Salt And Board',
#  'Frontier Restaurant',
#  'Nexus Brewery',
#  "Devon's Pop Smoke",
#  'Cocina Azul',
#  'Philly Steaks',
#  'Stripes Biscuit']
```
OR: For review counts:
```python
def extract_review(review):
    return review['review_count']
        
review_counts = list(map(extract_review, restaurants))
review_counts
[610, 11, 1373, 680, 54, 647, 25, 20]
```
TIPS! Using the socks@

```python
def pillow_doubler(sock):
    return sock * 2

def double_socks(list_of_socks):
    # map(function_to_apply_to_each_item, list_of_items)
    return list(map(lambda sock: pillow_doubler(sock), list_of_socks))

sock_list = [1,2,3]
double_socks(sock_list)

2,4,6
```
More Python Work:

Write a function called get_boundaries() that takes in two parameters, a number called target and a number called margin.

Call the function on the target 100 with a margin of 20. Save the returned values to variables called low and high.
```python

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

#This is another way to call the function:
low, high = get_boundaries(100,20)
print(low)
print(high)
80
120
```
## Using range in for loops

Notice that we need to iterate through a list of length 3, but we don’t care what’s in the list. To create these lists of length n, we can use the range function. range takes in a number n as input, and returns a list from 0 to n-1.
```python
zero_thru_five = range(6)
# zero_thru_five is now [0, 1, 2, 3, 4, 5]
zero_thru_one = range(2)
# zero_thru_one is now [0, 1]

for i in range(3):
  print("WARNING!")
#which will print WARNING! three times
```
Example:
```python
promise = "I will not chew gum in class"

for i in range(5):
	print(promise)
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
```
Infinite Loops:
```
Append in for loops
```python
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)
  
print(students_period_B)
```
Break in for loops

You can stop a for loop from inside the loop by using break. When the program hits a break statement, control returns to the code outside of the for loop. For example:
```python
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
#output
Checking the sale list!
blue_shirt
striped_socks
knit_dress
End of search!
```
Another example of break:
```python
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
  	break
print("They have the dog I want!")
french_bulldog
dalmatian
They have the dog I want!
```
Dictionary notes:
Notice that:

1. A dictionary begins and ends with curly braces ({ and }).

2. Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)

3. Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)

4. It’s considered good practice to insert a space () after each comma, but your code will still run without the space.

Dictionaries provide us with a way to map pieces of data to each other, so that we can quickly find values that are associated with one another.
```
Nested Loops:
```python
#I have a dictionary called 'users'

def get_street(list_of_users):
  streets_list = []
  for person in list_of_users:
    streets_list.append(person['address']['street'])
  return streets_list

print(get_street(users))
['Park Place', 'Nowhere', 'The north pole']
```
Dictionaries: Adding two dictionaries together

```python
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

```
Remember that **zip()** combines two lists into a list of pairs. This list comprehension:

1. Takes a pair from the zipped list of pairs from names and heights
2. Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
3. Creates a key : value item in the students dictionary
4. Repeats steps 1-3 for the entire list of pairs


When retrieving a collection of information about a dictionary. Use the appropriate dictionary function to return a list of values in the dictionary regarding Pyeongchang. Assign the list to the variable pyeongchang_values.
```python

pyeongchang_values = list(cities[11].values())

print(pyeongchang_values) 
['PyeongChang', 'South Korea', 2581000, 3194]

type(pyeongchang_values) # list
```
A **trace** is a dictionary! 

used for Plotly

```python
trace = {'x': [], 'y': [], 'text': [], 'type': 'bar'}
```
More practice with Dictionaries:
```python
users = [
  {
    'id': 1,
    'email': 'devilchick182@hotmail.com',
    'address': {
      'street': 'Park Place',
      'number': 123
    },
    'age': 10
  },
  {
    'id': 3,
    'email': 'sporkler@biz.co',
    'address': {
      'street': 'Nowhere',
      'number': 100000000
    },
    'age': 99,
  },
  {
    'id': 2,
    'email': 'surfingbear10@chillers.bro',
    'address': {
      'street': 'The north pole',
      'number': 55
    },
    'age': 3
  },
]

bear = users[2]
print(bear)

melissa = users[0]
print(melissa)

melissa_email = users[0]['email']
print(melissa_email)

boring_person_address = users[1]['address']
print(boring_person_address)

melissa_values = list(users[0].values())
print(melissa_values)

melissa_keys = list(users[0].keys())
print(melissa_keys)
```
Pythagorian Theorum:

```python
neighbors = [{'name': 'Fred', 'avenue': 4, 'street': 8}, {'name': 'Suzie', 'avenue': 1, 'street': 11}, 
             {'name': 'Bob', 'avenue': 5, 'street': 8}, {'name': 'Edgar', 'avenue': 6, 'street': 13},
             {'name': 'Steven', 'avenue': 3, 'street': 6}, {'name': 'Natalie', 'avenue': 5, 'street': 4}]

fred = neighbors[0]
natalie = neighbors[5]

import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = dict(x=list(map(lambda neighbor: neighbor['avenue'],neighbors)), 
              y=list(map(lambda neighbor: neighbor['street'],neighbors)),
              text=list(map(lambda neighbor: neighbor['name'],neighbors)),
              mode='markers')
plotly.offline.iplot(dict(data=[trace0], layout={'xaxis': {'dtick': 1}, 'yaxis': {'dtick': 1}}))
```
Write a function called street_distance that calculates how far in streets two neighbors are from each other. So for example, with Natalie at street 4, and Fred at street 8, our street_distance function should return the number 4.

```python
def street_distance(first_neighbor, second_neighbor):
    return first_neighbor['street']-second_neighbor['street']
    pass

street_distance(fred, natalie) # 4
```
Write a function called avenue_distance that calculates how far in avenues two neighbors are from each other. The distance should always be positive.

```python
def avenue_distance(first_neighbor, second_neighbor):
    return abs(first_neighbor['avenue']-second_neighbor['avenue'])
    pass

avenue_distance(fred, natalie) #  1
```
Now let's begin writing functions involved with calculating that hypotenuse of our right triangle. Using the Pythagorean Theorem, a^2+b^2=c^2, write a function called distance_between_neighbors_squared that calculates 
c^2, the length of the hypotenuse squared.

```python
def distance_between_neighbors_squared(first_neighbor, second_neighbor):
    return street_distance(first_neighbor, second_neighbor)**2 + avenue_distance(first_neighbor, second_neighbor)**2
    pass
distance_between_neighbors_squared(fred, natalie) # 17
```
Now let's move onto the next step and write a function called distance, that given two neighbors returns the distance between them.
```python
import math 
from math import sqrt
def distance(first_neighbor, second_neighbor):
    return sqrt(distance_between_neighbors_squared(first_neighbor, second_neighbor))
    pass

distance(fred, natalie) # 4.123105625617661
```

## Nearest Neighbors

Writing Our **"Nearest Neighbors"** Functions


We first need to calculate the distances between one neighbor and then all of the others. Next, we sort those neighbors by their distance from the selected_neighbor. Finally, we select a given number of the closest neighbors. Let's work through it.

What we already have a function that calculates the distance between two neighbors. We may think we could simply use this function to loop through our neighbors, but that would just return a list of distances.
```python
distances = []
for neighbor in neighbors:
    distance_between = distance(fred, neighbor)
    distances.append(distance_between)

distances
```
The returned list from the above procedure isn't super helpful. We need to know the person associated with each distance.


So let's accomplish this by writing a function called distance_with_neighbor that works like our distance function but instead of returning a float, returns a dictionary representing the second_neighbor, and also adds in the a key value pair indicating distance from the first_neighbor.
```python
import math
from math import sqrt

def distance_with_neighbor(first_neighbor, second_neighbor):
    nearby_neighbor = second_neighbor.copy()
    distance = sqrt(distance_between_neighbors_squared(first_neighbor, second_neighbor))
    nearby_neighbor['distance'] = distance
    return(nearby_neighbor)
    Pass

```
Now write a function called distance_all that returns a list representing the distances between a first_neighbor and the rest of the neighbors. The list should not return the first_neighbor in its collection of neighbors.
```python
import math
def distance_with_neighbor(first_neighbor, second_neighbor):
    neighbor_with_distance = second_neighbor.copy()
    distance = math.sqrt(distance_between_neighbors_squared(first_neighbor, second_neighbor))
    neighbor_with_distance['distance'] = distance
    return neighbor_with_distance

distance_with_neighbor(fred, natalie)
# {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4}

def distance_all(first_neighbor, neighbors):
    rest_of_neighbors = list(filter(lambda neighbor: neighbor != first_neighbor, neighbors))
    return list(map(lambda neighbor: distance_with_neighbor(first_neighbor, neighbor), rest_of_neighbors))
    pass

distance_all(fred, neighbors)

# [{'avenue': 1, 'distance': 4.242640687119285, 'name': 'Suzie', 'street': 11},
#  {'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
#  {'avenue': 6, 'distance': 5.385164807134504, 'name': 'Edgar', 'street': 13},
#  {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6},
#  {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4}]
```
Finally, write a function called nearest_neighbors that given a neighbor, returns a list of neighbors, ordered from closest to furthest from the neighbor. The function should take an optional third argument that specifies how many "nearest" neighbors are returned.
```python

nearest_neighbors(fred, neighbors, 2)
# [{'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
#  {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6}]

#Write the algorithm for Nearest Neighbors

To write a nearest_neighbors function, we break this into steps:
Write a function to calculate the distance of one neighbor from another
Write a function that returns the distance between one neighbor and all others (using map)
Return a selected number of nearest neighbors
Calculating the distance of one neighbor from another
First, we write a function that calculates the distance between one individual and another. This function is a translation of our Pythagorean Theorem, which says that given a first individual with coordinates 
```python
import math
def distance(selected_individual, neighbor):
   distance_squared = (neighbor['x'] - selected_individual['x'])**2 + (neighbor['y'] - selected_individual['y'])**2
   return math.sqrt(distance_squared)
```
And…
```python
def distance_between_neighbors(selected_individual, neighbor):
    neighbor_with_distance = neighbor.copy()
    neighbor_with_distance['distance'] = distance(selected_individual, neighbor)
    return neighbor_with_distance
 
distance_between_neighbors(bob, suzie)
{'name': 'Suzie', 'x': 1, 'y': 11, 'distance': 4.242640687119285}
```
 
The distance_between_neighbors function makes a copy of the neighbor object and then adds a new attribute called distance using the previous distance function. So now we have associated a neighbor with his/her distance from a given point.
 
**Creating a list of neighbors with distances**

Next, we write a distance_all function to calculate the distance between a selected_individual, and all of the other neighbors. We do this by calling our distance_between_neighbors function with the selected_individual and each of the rest of the neighbors.

In the distance_all function, we first filter out the selected_individual as we don't want to return the selected individual as a neighbor. Then we calculate the distance between the selected_individual and the rest of the individuals. Finally, for each of the remaining neighbors, we use our distance_between_neighborsmethod to add in a distance attribute to each of the neighbors.
```python
def distance_all(selected_individual, neighbors):
    remaining_neighbors = filter(lambda neighbor: neighbor != selected_individual, neighbors)
    return list(map(lambda neighbor: distance_between_neighbors(selected_individual, neighbor), remaining_neighbors))
```
**Return selected number of nearest neighbors**

Finally, we write our nearest_neighbors function. The function takes an optional argument of number, which represents the number of "nearest" neighbors to return. When set to None, number is reassigned to equal the length of the neighbors list. The nearest_neighbors function finishes by sorting the the "neighbors" by their distance and then slicing the list to return the correct number of neighbors.
```python
def nearest_neighbors(selected_individual, neighbors, number = None):
    number = number or len(neighbors)
    neighbor_distances = distance_all(selected_individual, neighbors)
    sorted_neighbors = sorted(neighbor_distances, key=lambda neighbor: neighbor['distance'])
    return sorted_neighbors[:number]
 
nearest_neighbors(bob, neighbors)
nearest_neighbors(bob, neighbors, 2)
```
Python's sorted method lets us sort a list of dictionaries by a certain value. We do so by telling the sortedmethod to compare the values specified in the lambda function, in this case neighbor['distance'].

We have seen how to access elements from a list by explicitly providing the starting element and stopping element in the following manner: sorted_neighbors[0:number]. Above, we implicitly select the first numberof elements from our list by leaving out the starting element.

**Summary**
In this lesson, we reviewed the nearest neighbors function and saw how it derives from calculating the distance using the Pythagorean Theorem to then sorting neighbors by that interest.

**Nearest Neighbors Overview:** 

Apply our nearest neighbors algorithm
Here is the nearest neighbors algorithm once again. The code below reflects the following steps:

Write a function to calculate the distance of one neighbor from another
Write a function that returns the distance between one neighbor and all others (using map)
Return a selected number of nearest neighbors
Ok once again, here is the code.
```python
import math

def distance(selected_individual, neighbor):
   distance_squared = (neighbor['x'] - selected_individual['x'])**2 + (neighbor['y'] - selected_individual['y'])**2
   return math.sqrt(distance_squared)

def distance_between_neighbors(selected_individual, neighbor):
    neighbor_with_distance = neighbor.copy()
    neighbor_with_distance['distance'] = distance(selected_individual, neighbor)
    return neighbor_with_distance

def distance_all(selected_individual, neighbors):
    remaining_neighbors = filter(lambda neighbor: neighbor != selected_individual, neighbors)
    return list(map(lambda neighbor: distance_between_neighbors(selected_individual, neighbor), remaining_neighbors))

def nearest_neighbors(selected_individual, neighbors, number = None):
    number = number or len(neighbors)
    neighbor_distances = distance_all(selected_individual, neighbors)
    sorted_neighbors = sorted(neighbor_distances, key=lambda neighbor: neighbor['distance'])
    return sorted_neighbors[:number]

bob = neighbors[0]
nearest_neighbor_to_bob = nearest_neighbors(bob, neighbors, 1)
nearest_neighbor_to_bob
 ```
We try our nearest_neighbors function on a known piece of data, bob. When we ask our function to return only the closest neighbor, it returns Fred and tells us his number of purchases. Perhaps we can expect Bob's number of purchases to be similar to Fred's. We also can apply the function to a customer at new location to predict this customer's number of purchases.
```python
nearest_neighbor_to_new = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 1)
nearest_neighbor_to_new
```
**Row, row, row your boat** - in python:
```python
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats 

print((repeat_stuff("Row ", 3)) + "Your Boat")

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

song = repeat_stuff(lyrics)
print(song)

Row Row Row Your Boat
Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. Row Row Row Your Boat. 
```
Age in dog years function:
```python
# Write your dog_years function here:
def dog_years(name, age):
  dog_age = str(age*7)
  string1 = ", you are "
  string2 = " years old in dog years"
  return name + string1 + dog_age + string2

print(dog_years("Michael", 32))

Michael, you are 224 years old in dog years
```
Physics function project:
```python
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = ((f_temp - 32)*(5/9))
  return c_temp

f100_in_celcius = (f_to_c(100))

print(f100_in_celcius)

def c_to_f(c_temp):
  f_temp = ((c_temp * (9/5))+32)
  return f_temp

print(c_to_f(0))

c0_in_fahrenheit = (c_to_f(0))

def get_force(mass, acceleration):
  return mass*acceleration

print(get_force(train_mass, train_acceleration))

train_force = (get_force(train_mass, train_acceleration)) 

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=(3*10**8)):
  return mass*c

print(get_energy(bomb_mass))

bomb_energy = (get_energy(bomb_mass))

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  force = (mass*acceleration)*distance
  return force

print(get_work(train_mass, train_acceleration, train_distance))

train_work = (get_work(train_mass, train_acceleration, train_distance))

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
```
## Allow or Don't Allow - using IF and ELSE

```python
banned_users = ['Melissa', 'Michael', 'Ted', 'Mari', 'Eyeball Monster']
user = 'Unbridled Optimism Monster'

if user not in banned_users:
		print(f"{user.title()}, do whatever the fuck you want!!!!")
else: 
		print(f"{user.title()}, get OUT of here you jerk!!!")

#Unbridled Optimism Monster, do whatever the fuck you want!!!!
```
Another example of IF, ELIF, ELSE:
```python
print("This is how cool you are at every age:")
age = 40

if age <5:
  price = 0
  print("You literally don't care and you're too young still to be cool.")
elif age <10:
  price = .50
  print("If you own a video game console you're cool.")
elif age <14:
  price = 7
  print("Have you ever gotten drunk? No? Not cool.")
elif age <20:
  price = 60
  print("You are a teenager. Pretty much cool by definition.")
else:
  price = 50000
  print("It is all downhill from here coolness wise.")

print(f"It will cost you ${price} to be cool at that age.")
```
Showing all the options using IF, ELSE!
```python
alien_colors = ["silver glitter", "green slime", "matte black sandpapery", "lumpy booger"]

for alien_color in alien_colors:
	if alien_color == "matte black sandpapery":
		print(f"Sorry, {alien_color} aliens don't breathe oxygen and will die here.")
	else:
		print(f"Good news, {alien_color} aliens should be able to survive on earth if you let them eat kittens!")

print("We all live happily ever after maybe!")

#Good news, silver glitter aliens should be able to survive on earth if you let them eat kittens!
#Good news, green slime aliens should be able to survive on earth if you let them eat kittens!
#Sorry, matte black sandpapery aliens don't breathe oxygen and will die here.
#Good news, lumpy booger aliens should be able to survive on earth if you let them eat kittens!
#We all live happily ever after maybe!
```

Multiple Dictionaries - Aliens:
```python
alien_1 = {"color":"silver glitter", "points":15}  
alient_2 = {"color":"green slime","points": 10}
alien_3 = {"color":"matte black sandpapery","points": 5} 
alien_4 = {"color":"lumpy booger","points": 1}
           
new_points = alien_1["points"]
print(f'You won {new_points} points!')

alien_3["x_position"] = 0
alien_3["y_position"] = 25
print(alien_3)

print(f"The alien is {alien_3['color']}, so it can't breath oxygen.")
#The alien is matte black sandpapery, so it can't breath oxygen.
```
Changing something in the dictionary:
```python
alien_3['color'] = 'translucent yellow'
print(f"The alien is now {alien_3['color']}, so it can breathe oxygen!")
#The alien is now translucent yellow, so it can breathe oxygen!
```
**ALIEN GAME**

Moving the position based on a dictionary!

```python
alien_1 ={'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_1['x_position'], alien_1['y_position']}")

#Move the alien to the right
#Determine how far ot move based on current speed:
      
if alien_1['speed'] =='slow':
  x_increment = 1
elif alien_1['speed'] == 'medium': 		x_increment = 2
else:
  x_increment = 3

#this is the new position of the alien:
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"The new position is {alien_1['x_position']}.")

Original position: (0, 25)
The new position is 2.
```
## Looping in Dictionaries:
```python 
favorite_aliens = {
  'Ted': 'green slimy',
  'Michael':'green slimy',
  'Melissa': 'matte black sandpapery',
  'Mari': 'translucent yellow',
  'Berit': 'fleshy teal',
  'Adam': 'lumpy booger',
  'Gray': 'matte black sandpapery',
}
  
for key,value in favorite_aliens.items():
  print(f"\nName: {key}")
  print(f"Alien: {value}")
  
for name in favorite_aliens.keys():
  print(name.title())

for alien in favorite_aliens.values():
  print(alien.title())

#THIS IS HOW YOU LOOP THROUGH EACH OF THEM! if you forget the items part, then it will just list the last person in the list - it needs to be able to convert the dictionary into a list in order to properly iterate through it.

for name, alien in favorite_aliens.items():
  print(f"{name.title()}'s favorite alien is {alien.title()}.")
  
Ted's favorite alien is Green Slimy.
Michael's favorite alien is Green Slimy.
Melissa's favorite alien is Matte Black Sandpapery.
Mari's favorite alien is Translucent Yellow.
Berit's favorite alien is Fleshy Teal.
Adam's favorite alien is Lumpy Booger.
Gray's favorite alien is Matte Black Sandpapery.
```
## Sets 

Pulls all values from a list without repeats!
```python
favorite_aliens = {
  'Ted': 'green slimy',
  'Michael':'green slimy',
  'Melissa': 'matte black sandpapery',
  'Mari': 'translucent yellow',
  'Berit': 'fleshy teal',
  'Adam': 'lumpy booger',
  'Gray': 'matte black sandpapery'
}

print("The following aliens have been mentioned:")
for alien in set(favorite_aliens.values()):
  print(alien.title())
```
## Sorted

Provides all keys or values in alphabetical order.
```python
print("Here are the people who took the alien quiz:")
for name in sorted(favorite_aliens.keys()):
  print(name)

Here are the people who took the alien quiz:
Adam
Berit
Gray
Mari
Melissa
Michael
Ted
```
## Comparing list and dictionary using a For Loop:

In this case, comparing a list of Friends to a Favorite Alien poll:
```python
favorite_aliens = {
  'Ted': 'green slimy',
  'Michael':'green slimy',
  'Melissa': 'matte black sandpapery',
  'Mari': 'translucent yellow',
  'Berit': 'fleshy teal',
  'Adam': 'lumpy booger',
  'Gray': 'matte black sandpapery'
}

friends = ['Ted', 'Michael', 'Mari','Sara', 'Sabina']

for name in friends:
	if name in favorite_aliens:
		print(f"Thank you {name.title()} for taking the quiz!")
	else:
 	 print(f"{name.title()}, take the favorite aliens poll!")

Thank you Ted for taking the quiz!
Thank you Michael for taking the quiz!
Thank you Mari for taking the quiz!
Sara, take the favorite aliens poll!
Sabina, take the favorite aliens poll!
```
# Nesting

## Making a list of dictionaries!
```python
#back to the alien game!

alien_1 = {"color":"silver glitter", "points":15}
alien_2 = {"color":"green slime","points": 10}
alien_3 = {"color":"matte black sandpapery","points": 5} 
alien_4 = {"color":"lumpy booger","points": 1}

aliens = [alien_1, alien_2, alien_3, alien_4]

for alien in aliens:
  print(alien)

{'color': 'silver glitter', 'points': 15}
{'color': 'green slime', 'points': 10}
{'color': 'matte black sandpapery', 'points': 5}
{'color': 'lumpy booger', 'points': 1}
```
## Generating a list

In this example, we will CREATE a list based on criteria specied in For Loop:
```python
#Make a list for storing aliens:
aliens = []

#Make 30 aliens
for alien_number in range(30):
  new_alien = {'color': 'green slime', 'points': 10, 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green slime':
		alien['color'] = 'silver glitter'
		alien['speed'] = 'medium'
		alien['points'] = 15
	elif alien['color'] =='silver glitter':
		alien['color'] = 'matte black sandpapery'
		alien['speed'] = 'fast'
		alien['points'] = 20
    
#show first 5 aliens
for alien in aliens[:5]:
  print(alien)
print("...")

#total aliens created:
print(len(aliens))

{'color': 'silver glitter', 'points': 15, 'speed': 'medium'}
{'color': 'silver glitter', 'points': 15, 'speed': 'medium'}
{'color': 'silver glitter', 'points': 15, 'speed': 'medium'}
{'color': 'green slime', 'points': 10, 'speed': 'slow'}
{'color': 'green slime', 'points': 10, 'speed': 'slow'}
...
30
```
## A List in a Dictionary

```python
zombie_pizza = {
  'crust': 'moldy', 
  'toppings':['ears', 'blood', 'green peppers']
}

#summarize the order
print(f"You ordered a {zombie_pizza['crust']}-crust zombie pizza"" with the following toppings:")
#Here we needed a break in the print line
      
for topping in zombie_pizza['toppings']:
	print("\t" + topping)
#the \t in this example makes it into a table.

You ordered a moldy-crust zombie pizza with the following toppings:
	ears
	blood
	green peppers
```
## Nesting lists in dictionaries:
```python
favorite_aliens = {
  'Michael':['green slimy'],
  'Melissa': ['matte black sandpapery'],
  'Mari': ['translucent yellow'],
  'Berit': ['fleshy teal'],
  'Sara': ['green slimy'],
  'Adam': ['lumpy booger', 'matte black sandpapery'],
   'Ted': ['green slimy','fleshy teal'],
  'Gray': ['matte black sandpapery', 'translucent yellow'],
}

for name, aliens in favorite_aliens.items():
	print(f"\n{name.title()}'s favorite aliens are:")
	for alien in aliens:
		print(f"\t{alien}")
  
  Michael's favorite aliens are:
	green slimy

Melissa's favorite aliens are:
	matte black sandpapery

Mari's favorite aliens are:
	translucent yellow

Berit's favorite aliens are:
	fleshy teal

Sara's favorite aliens are:
	green slimy

Adam's favorite aliens are:
	lumpy booger
	matte black sandpapery

Ted's favorite aliens are:
	green slimy
	fleshy teal

Gray's favorite aliens are:
	matte black sandpapery
	translucent yellow
```
# While Loops

Need to revisit this!!

```python
responses = {}
#set a flag to indicate polling is active
polling_active = True

while polling_active:
  #prompt for the persons name and response
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to live on one day?")

#store the response in a dictionary
	responses[name] = response

#Find out if anyone else is going to take the poll
	repeat = input("Would you like to let the person respond? (yes/no)")
	if repeat == 'no':
		polling_active = False

#Polling is complete. Show results
	print("\n---Polling Results---")
	for name, response in responses.items():
		print(f"\n{name} would  like to live on {response}.")
```
## Functions and While Loops

```python
def get_formatted(first,last):
 full_name = f"{first}{last}"
 return full_name.title()

while True:
 print("n\Tell me your name!!!")
 print("(enter 'q' at any time to quit.)")
  
 f_name = input("first name:")
 if f_name == 'q':
  break
    
 l_name = input("last name:")
 if l_name == 'q':
   break
  
 formatted_name = get_formatted(f_name, l_name)
 print(f"\nHello, {formatted_name}!")
```
# Function Practice

## Returning a dictionary with a function:
```python
def build_person(first, last):
  person = {'first': first, 'last': last}
  return person

melissa_munz = build_person('Melissa', 'Munz')
print(melissa_munz)

{'first': 'Melissa', 'last': 'Munz'}
```
## Passing a list through a function
```python
def greet_users(names):
 for name in names:
  message = f"Hi {name.title()}, do you like aliens?"
  print(message)
  

friends = ['Michael', 'Sara', 'Berit']
greet_users(friends)

Hi Michael, do you like aliens?
Hi Sara, do you like aliens?
Hi Berit, do you like aliens?
```
## Modifying a list in a Function
```python
unprinted_designs = ['phone case', 'robot', 'alien']
completed_models = []

while unprinted_designs:
  current_design = unprinted_designs.pop()
  print(f"Printing model:{current_design}") 
  completed_models.append(current_design)
  
print("\nThe following models have been printed:")
for completed_model in completed_models:
  print(completed_models)

Printing model:alien
Printing model:robot
Printing model:phone case

The following models have been printed:
['alien', 'robot', 'phone case']
['alien', 'robot', 'phone case']
['alien', 'robot', 'phone case']
```
# Game of Chance
```python
import random

money = 100

#Write your game of chance functions here

def game_of_chance(guess, bet):
 num = random.randint(1, 10)
 if num == guess:
  bank = money+bet
  return(f"You guessed {guess}. The number was {num}. You are correct! You now have {bank}!")
 elif num != guess:
  bank = money-bet
  return (f"You guessed {guess}, which is the wrong guess. The correct answer was {num}. You suck! You're the worst! You now have {bank}.")

print(game_of_chance(11,10))
```
# Heads or Tails
```python
import random

money = 100

#Write your game of chance functions here

heads_or_tails = {
  1: "heads",
  2: "tails",
}

def game_of_chance(guess, bet):
  num = random.randint(1,2)
  result = heads_or_tails[num]
  if result == guess:
    bank = money+bet 
    return(f"You guessed {guess},and the answer was {result} which is correct! You now have {bank}!")
  else:
    bank = money-bet
    return (f"You lose. You guessed {guess} but the answer is {heads_or_tails[num]}. You bet {bet}, so now you have {bank}.")
  
print(game_of_chance('heads',10))

You lose. You guessed heads but the answer is tails. You bet 10, so now you have 90.
```
Cleaned up version: Heads or Tails
```python
import random

money = 100

#Write your game of chance functions here

heads_or_tails = {
  1: "heads",
  2: "tails",
}

def game_of_chance(guess, bet):
  global money
  num = random.randint(1,2)
  result = heads_or_tails[num]
  if result == guess:
    money = money+bet 
    return(f"You guessed {guess},and the answer was {result} which is correct! You now have {money}!")
  else:
    money = money-bet
    return (f"You lose. You guessed {guess} but the answer is {heads_or_tails[num]}. You bet {bet}, so now you have {money}.")
  
print(game_of_chance('heads',10))
print(game_of_chance('heads',10))
print(game_of_chance('heads',10))

You guessed heads,and the answer was heads which is correct! You now have 110!
You lose. You guessed heads but the answer is tails. You bet 10, so now you have 100.
You lose. You guessed heads but the answer is tails. You bet 10, so now you have 90.
```





 
 









