**Plotting and Maps in Python**

A common problem
Imagine that Molly is selling cupcakes out of her kitchen. She gains more and more customers, so she decides to hire a delivery person, Bob. Molly asks us to calculate which customers are closest to and furthest from Bob. This way, she can pay him appropriately.

Molly gives us a list of all of the customer locations, along with Bob's. Here they are:

Name	Avenue #	Block #
Bob	4	8
Suzie	1	11
Fred	5	8
Edgar	6	13
Steven	3	6
Natalie	5	4

```Python

!pip install plotly

import plotly

plotly.offline.init_notebook_mode(connected=True)
# use offline mode to avoid initial registration

import plotly
plotly.offline.init_notebook_mode(connected=True)
# we repeat these first lines just to keep the code together  

trace0 = dict(x=[4, 1, 5, 6, 3, 2], y=[8, 11, 8, 13, 6, 4])

# too many lines, doesnt make sense
plotly.offline.iplot([trace0])
```
The points were plotted correctly, but they are connected by a line, which doesn't represent anything in particular.

The lines are getting in the way. Let's remove all of the connecting lines by setting mode = "markers". Then, let's also set labels to each of the dots, by setting text equal to a list of our names.
```python
trace1 = dict(x=[4, 1, 5, 6, 3, 2],
              y=[8, 11, 8, 13, 6, 4], 
              mode="markers", 
              text=["bob", "suzie", "fred", "edgar", "steven", "natalie"],)


plotly.offline.iplot([trace1])

# lines have been removed.
```
So if you move your mouse over the dots, you can see the names that correspond to each point. 

**Here's the Summary**

To display the data with plotly we need to do a couple of things. First, we install plotly by going to our terminal and running pip install plotly. 

Then to use the library, we import the plotly library into our notebook. 

Once the library is loaded in our notebook, it's time to use it. We create a new dictionary with keys of  x  and  y , with each key pointing to a list of the  x  or  y  values of our points. 

To clean up the appearance we set the mode attribute equal to 'markers'.

**Calculating Distance**

 this is the formula for calculating the lengths of the sides of a right triangle, called the Pythagorean Theorem:

a^2+b^2=c^2


**Absolute value**

 of a number means to not consider whether a number is negative. So the absolute value of -100 is 100, and the absolute value of -20 is 20. We indicate the we are taking the absolute value of a number with the use of pipes. So we can say  |−20|=20

a^2+b^2=c^2
 
we have that:

a=(x1−x2)=∣3−4∣=1

b=(y1−y2)=∣8−6∣=2
 
c^2=a^2+b^2=12+22=5

c^2=5

Now just take the sqaure root of 5

**Squares, Square Roots, and Inverses**

**Squares** 

- Squaring something simply means multiplying something by itself. So for example, 5 squared equals 5  ×  5. Four squared equals 4  ×  4. We denote four squared with the a raised number 2, as in  42 . The two is the number of times we are multiplying four by itself.

**Square Roots**

 - Now we can go from a number's square back to the original square with the square root. For example, the square of 4 is 4  ×  4, which equals 16. And the square root of 16 should undo the operation of squaring, so the square root of 16 equals four, and we denote the square root of 16 as  16⎯⎯⎯⎯√16 .

**Inverses** 

- In mathematics, the inverse is anything that undoes the operation. So the inverse of squaring is taking the square root. The inverse of multiplying by ten is dividing by ten. Here is a question:


**Solving the pythagorian theorum**

Now that we have seen how to solve for distance between two points in our example above, let's make sure we know how to do this in general. We start with the formula:

a^2+b^2=c^2
 
and putting this formula in terms of our two points,  x  and  y , we have :

(x1−x2)^2+(y1−y2)^2=c^2
 
and solving for  cc  we have

c=square root (x1−x2)^2+(y1−y2)^2

Where  c  is the length of the hypotenuse, or the shortest distance between our two points.

So given two points,  (x1,y1)  and  (x2,y2)  we can plug them into our formula above to solve for the distance between them,  c .

**LAB**
```python
neighbors = [{'name': 'Fred', 'avenue': 4, 'street': 8},                  {'name': 'Suzie', 'avenue': 1, 'street': 11}, 
             {'name': 'Bob', 'avenue': 5, 'street': 8}, {'name': 'Edgar', 'avenue': 6, 'street': 13},
             {'name': 'Steven', 'avenue': 3, 'street': 6}, {'name': 'Natalie', 'avenue': 5, 'street': 4}]

fred = neighbors[0]
natalie = neighbors[5]
```
Import Plotly:
```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = dict(x=list(map(lambda neighbor: neighbor['avenue'],neighbors)), 
              y=list(map(lambda neighbor: neighbor['street'],neighbors)),
              text=list(map(lambda neighbor: neighbor['name'],neighbors)),
              mode='markers')
plotly.offline.iplot(dict(data=[trace0], layout={'xaxis': {'dtick': 1}, 'yaxis': {'dtick': 1}}))
```
We'll start by focusing on the neighbors Fred and Natalie, and points (4, 8) and (5, 4) respectively.

Write a function called street_distance that calculates how far in streets two neighbors are from each other. So for example, with Natalie at street 4, and Fred at street 8, our street_distance function should return the number 4.
```python

