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

# Plotly Lab  - Install and Types
Install Plotly:
```python
!pip install plotly
```
Import Plotly librbary
```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

plotly.offline.iplot([
    {}
])
```
We reference the plotly library, which we imported above. Then we pass a list containing a dictionary to the iplot method. That dictionary can represent a scatter trace, a line trace, or other types of traces.
We pass the trace into a list because we can have more than one trace in the same graph - for example two bar traces displayed side by side or a scatter trace underneath a line trace.
```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]}

plotly.offline.iplot([
    trace
])
```
The plot above has one trace which is a line trace. However, this type of trace is just the default. Note, that we did not specify any particular type.
 
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4]}
We can change it by changing the mode to markers. While we are at it, let's also change the color of the markers.
```python
trace = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4], 'mode': 'markers', 'marker': {'color': 'rgba(255, 182, 193, .9)'}}

plotly.offline.iplot([
    trace
])
```
Now let's add **more than one trace** to a given graph. We'll keep the first trace largely the same by using the same data, and color of markers. We'll name our trace 'Some dots' by adding the name attribute and set it equal to the corresponding string.
```python
trace0 = {'x': [1, 2, 3, 4], 'y': [1, 2, 3, 4], 
          'mode': 'markers', 'marker': {'color': 'rgba(255, 182, 193, .9)'}, 
          'name': 'Some dots'}
```
In the second trace, we have some new data, and set the color as blue. Because we did not specify a mode, it defaults to connecting the points as a line. And we name our trace as "Our nice line".
```python
trace1 = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 
          'marker': {'color': 'blue'},
          'name': 'Our nice line'}
```
Finally, we create a plot of the two traces.
```python
plotly.offline.iplot([
    trace0, trace1
])
```
THE END!

## Working with Types
For example, we can make a bar chart, simply by specifying the in our dictionary that the type is bar for a bar trace.

```python
bar_trace = {'type': 'bar', 'x': ['bobby', 'susan', 'eli', 'malcolm'], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice bar trace'}

plotly.offline.iplot([
    bar_trace
])
```
Another way to create a bar chart is to use the constructor provided by plotly. It's not too tricky to do so. First, we import our **graph_objs** library from Plotly. And then we call the bar chart constructor.
```python
from plotly import graph_objs 

bar_trace_via_constructor = graph_objs.Bar(
            x=['bobby', 'susan', 'eli', 'malcolm'],
            y=[3, 5, 7, 9]
    )

bar_trace_via_constructor
```
We refer to the function **graph_objs.Bar** as a constructor because it literally constructs python dictionaries with a key of type that equals bar. Then, we can pass this dictionary to our iplot method to display our bar chart.
```python
bar_trace_via_constructor = graph_objs.Bar(
            x=['bobby', 'susan', 'eli', 'malcolm'],
            y=[3, 5, 7, 9]
    )


plotly.offline.iplot([
    bar_trace_via_constructor
])
```
Now let's look at some constructors for make other traces.

SCATTER PLOT
```python
graph_objs.Scatter()
```
PIE CHART
```python
graph_objs.Pie()
```
DICTIONARY CONSTRUCTOR
```python
pie_trace = dict(type="pie", labels=["chocolate", "vanilla", "strawberry"], values=[10, 5, 15])

plotly.offline.iplot([
    pie_trace
])
```
## Modifying the layout

So far we have seen how to specify attributes of traces or charts, which display our data. Now let's see how to modify the overall layout in our chart.

Note that the format of our traces will not change.
```python
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 
                 'marker': {'color': 'blue'},
                 'name': 'Our nice line'}
```
However, instead of passing to our iplot function a list of traces, we pass our iplot function a dictionary with a data key, which has a value of a list of traces. The layout key points to a dictionary representing our layout.
```python
layout = {'title': 'Scatter Plot'}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```
So above we used the layout to name our plot's title. Now that we have used layout to specify our chart's title, let's also use it to specify the range of our x axis and y axis. Previously, we were allowing Plotly to automatically set the range. We can also adjust the range to meet our specifications.
```python
layout = {'title': 'Scatter Plot', 'xaxis': {'range': [1, 10]}, 'yaxis': {'range': [1, 10]}}
trace_of_data = {'x': [1.5, 2.5, 3.5, 4.5], 'y': [3, 5, 7, 9], 'marker': {'color': 'blue'}, 'name': 'Our nice line'}

figure = {'data': [trace_of_data], 'layout': layout}

plotly.offline.iplot(figure)
```
# LAB - A function to create traces

And returns data like the commented out dictionary below:

data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
build_trace(data)

So **build_trace** that takes in a list of data points as arguments and returns a dictionary with a key of x that points to a list of x values, and a key of y that points to a list of y values.

**Note:** Look at the parameters provided for build_trace. The arguments mode = 'markers' and name = 'data' may seem scary since we haven't seem them before. No need to worry! These are **default arguments**.

If no argument for mode or name is provided when we call the build_trace function, Python will automatically set these parameters to the value provided, which, in this case would be 'markers' for the mode and 'data' for the name.

## Build_trace function:
```python
def build_trace (data, mode = 'markers', name = 'data'):
    x_values = list(map(lambda datapoint: datapoint['x'], data))
    y_values = list(map(lambda datapoint: datapoint['y'], data))
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name}
```
So by default, if we just call build_trace(data) without specifying either a mode or a name, the function will automatically set these parameters to 'markers' and 'data' respectively.
```python
data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
build_trace(data)
# {'x': [1, 3, 2], 'y': [1, 2, 5], 'mode': 'markers', 'name': 'data'}
```
If we want our build_trace function to take a different mode arguement, we add a second argument when we call the function which will overwrite the mode's default argument.

In this case, **SCATTER**
```python
build_trace(data, 'scatter')

# {'x': [1, 3, 2], 'y': [1, 2, 5], 'mode': 'scatter', 'name': 'data'}
```
We could do the same thing with the name of the plot. This is useful for when we have more than one trace in the same plot.

**Order matters!** The value passed through as the name argument, should correspond to the value of the name key in our returned dictionary.

```python
build_trace(data, 'markers', 'sample plot')
# {'x': [1, 3, 2], 'y': [1, 2, 5], 'mode': 'markers', 'name': 'sample plot'}
```
## trace_values function
Now let's write another function to create a trace called trace_values. It works just like our build_trace function, except that it takes in a list of x_values and a list of y_values and returns our trace dictionary. We will use default argument again here in the same manner as before.
```python
def trace_values(x_values, y_values, mode = 'markers', name="data"):
    return {'x':x_values,'y':y_values, 'mode': mode, 'name': name}

trace_values([1, 2, 3], [2, 4, 5])

# {'x': [1, 2, 3], 'y': [2, 4, 5], 'mode': 'markers', 'name': 'data'}
```
Now let's try to build a line trace with our newly defined trace_values function. We will set mode to 'lines' and the name of our trace to 'line trace'.
```python
trace_values([1, 2, 3], [2, 4, 5], 'lines', 'line trace')
# {'x': [1, 2, 3], 'y': [2, 4, 5], 'mode': 'lines', 'name': 'line trace'}
```
From there, we can use our trace_values function to plot our chart.
```python
trace2 = trace_values([1, 2, 3], [2, 4, 5], 'lines', 'line trace')
plot({'data': [trace2]})

#IT IS PLOTTED!!
```
## Creating layouts

Ok, now that we have built some functions to create traces, let's write a function to create a layout. Remember that our layout also can be passed to our plot function.

```python
plot({'data': [trace0, trace2], 'layout': {'title': 'Sample Title'}})
```
Our layout function should return a dictionary, just as it's defined in the above plot. We'll start by returning an empty dictionary then below we'll walk through building out the rest of the function.

## layout function
```python
def layout(x_range = None, y_range = None, options = {}):
    layout = {}
    if isinstance(x_range, list): layout.update({'xaxis': {'range': x_range}})
    if isinstance(y_range, list): layout.update({'yaxis': {'range': y_range}})
    layout.update(options)
    return layout
```
Setting the xaxis and yaxis range:

Oftentimes in building a layout, we want an easy way to set the range for the x and y axis. To set a range in the x-axis of  1  through  4  and a range of the y-axis of  2  through  5 , we return a layout of the following structure.

{'xaxis': {'range': [1, 4]}, 'yaxis': {'range': [2, 5]}}

Let's start with adding functionality to the layout() function so it can set the range for the x-axis. 

(Hint: Google search Python's built-in isinstance() and update() functions.)

Add an argument of x_range returns a dictionary with a range set on the xaxis.

```python
layout([1, 4])
# {'xaxis': {'range': [1, 4]}}
```
We want to ensure that when an x_range is not provided, an empty dictionary is still returned.
```python
layout()
  {}
```
The x_range should be a default argument that sets x_range to None. Then, only add a key of xaxis to the dictionary layout when the x_range does not equal None.

Now let's provide the same functionality for the y_range. When the y_range is provided we add a key of yaxis which points to a dictionary that expresses the y-axis range.
```python
layout([1, 3], [4, 5])
# {'xaxis': {'range': [1, 3]}, 'yaxis': {'range': [4, 5]}}
```
Adding layout options

Now have the final argument of our layout function be options. The options argument should by default point to a dictionary. And whatever is provided as pointing to the options argument should be updated into the returned dictionary.
```python
layout(options = {'title': 'foo'})

layout([1, 3], options = {'title': 'chart'})

# {'xaxis': {'range': [1, 3]}, 'title': 'chart'}

```
Ok, now let's see this layout function in action.
```python
another_trace = trace_values([1, 2, 3], [6, 3, 1])
another_layout = layout([-1, 4], [0, 7], {'title': 'Going Down...'})
# plot({'data': [another_trace], 'layout': another_layout})
```
Finally, we'll modify the plot function for you so that it takes the data, and the layout as arguments.
```python
def plot(traces = [], layout = {}):
    if not isinstance(traces, list): raise TypeError('first argument must be a list.  Instead is', traces)
    if not isinstance(layout, dict): raise TypeError('second argument must be a dict.  Instead is', layout)
    plotly.offline.iplot({'data': traces, 'layout': layout})
```
PLOT IT:
```python
trace4 = trace_values([4, 5, 6], [10, 5, 1], mode = 'lines')
last_layout = layout(options = {'title': 'The big picture'})
plot([trace4], last_layout)
```
