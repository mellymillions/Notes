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

