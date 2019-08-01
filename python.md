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












 
 
