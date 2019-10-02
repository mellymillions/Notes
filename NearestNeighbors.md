#Locations and Plotly Practice 

##Pythagorian Theorum:

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
```
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
