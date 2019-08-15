MATH STUFF

For example, we can say the following:

f(x)=3x
f(x)=3x
 
The expression above means that there is an output that equals 3 times  xx.

Can be expressed in Python like:
```python
def f(x):
    return 3*x
f(3)
9
```
It is not just a specific input of  xx  that returns the same input, but specific inputs of  xx  and  yy that always return the same output. We indicate this like so:

f(x,y)=3x+y
```python
def f(x,y):
    return 3*x + y
```
**Multivariable Functions:** To indicate that we are evaluating the function at specific values of  xx  and  yy for the problem: 

f(x,y)=3x+y

If x,y = 3,4

f(3,4)=3∗3+4=13

We write the following:
```python
def f(x,y):
    return 3*x + y
#in code, we can now ask:
f(3, 4)
13
```
Functions depending on other functions:

```python
def squared_error(actual, expected): #(4,2)
    return (actual - expected)**2

squared_error(4, 2)
4

#This can also be defined:

def error(actual, expected): #(4,2)
    return actual - expected
    
def squared_error(actual, expected): #(4,2)
    return error(actual, expected)**2

squared_error(4, 2)
4
```
**Expressing Functions**

Let's represent the _function error_ as:

 g(x,y)=x−y
 
 Where  xx  represents **actual** and  yy  represents **expected**.
 
 Now we can represent _squared error_ as the following.

f(g(x,y))=g(x,y)<sup>2</sup>

The important thing to remember: is that to determine what the above function will output, we need to know the variables  xx  and  yy  as well as the **function**  g(x,y). 

**Derivatives of Straight Lines**

_Here is what we know so far:_

How to apply gradient descent by using the slope of the cost curve to determine the direction and magnitude of the next **step** for updating the parameter of a **regression line**.

_Here is what we need to learn:_

How to find that **slope** or _rate of change_ of a function at a given point.
The **instantaneous rate of change at a given point** is called the **derivative**.

Derivatives are important because they tell us how a function is changing at any given point. Derivatives allow us to see what is coming next.

**Understanding the rate of change**

Miles per hour is just one example of rate of change. Anytime we come across the word **per**, we know this is a form of rate of change. All forms of rate of change are calculated the same way: **the change in y divided by the change in x.**

Another way of expressing change in y is:

y2−y1 or  Δy , read delta y

Likewise, another way of expressing change in x is:

x2−x1 or  Δx , read delta x

**Derivatives** 

a specific kind of rate of change -- the rate of change of a function at a given point.

If we are given a function  f(x) , we say the derivative of that function is  **f′(x)** -- read f primed of x.

In this example, we replaced  y2−y1 with  f(x2)−f(x1). This makes sense, because really when we say  y2y2  and  y1y1 , we mean the **function's output** at the first x value and the **function's output** at the second x value.

So  f(x)  equals the output at a given point. And  f′(x)  is the rate of change at a given point. So then:

f(1)
means the output at  x=1 , or in our example, the distance at hour one, and

f′(1)
means the rate of change at  x=1 , or in our example, the speed at hour one

This is the definition that we will often see. It expresses our technique for calculating the derivative.

**General Formula for calculating a Derivative:** 

Subtract the output at one input, x, from the output at that initial input plus a change in x.

Then divide that difference by the change in x.
In summation, that is the derivative of a line, or the rate of change of a linear function. 

_The rate of change answers how much is our output changing at a given point._



**Derivatives Lab**

This is our technique: write the formula as a list of tuples.

A tuple is a list whose elements cannot be reassigned. But everything else, for our purposes, is the same.
```python

tuple = (7, 3)
tuple[0] # 7
tuple[1] # 3
#We get a TyperError if we try to reassign the tuple's elements.

tuple[0] = 7
# TypeError: 'tuple' object does not support item assignment
```
Take the following function as an example:

f(x)=2x^2+4x−10

of a line, or the rate of change of a linear function. 

The rate of change answers how much is our output changing at a given point.

**Set the tuples as a list:**
```python
four_x_squared_plus_four_x_minus_ten = [(4, 2), (4, 1), (-10, 0)]
```
So each tuple in the list represents a different term in the function. 

The first element of the tuple is the term's constant and the second element of the tuple is the term's exponent. 

Thus f(x)=4x^2+4x-10 translates to (4, 2) and  −10− translates to (-10, 0) because  −10  is the same as  −10∗x^0.


**EXAMPLE**

If you start with the formula:

3x^2

When x=2

The full answer will be **12**

3x^2 is represented in code as  (3,2), or the (term constant, term exponent)

The full term output would be: 

term_output=((3,2),2) which should return 12 

```python
def term_output(term, input_value):
    return term[0]*input_value**term[1]
    pass

term_output((3, 2), 2) # 12
12
```
**EXAMPLE 2**

Write a function called output_at, when passed a list_of_terms and a value of  x, calculates the value of the function at that value.

f(x)=3x^2−11

output_at([(3, 2), (-11, 0)], 2)

Answer will be f(2)=3x^2−11=1

```python
# REVIEW THIS AGAIN
def output_at(list_of_terms, x_value):
    outputs = list(map(lambda term: term_output(term, x_value), list_of_terms))
    return sum(outputs)

#Define the terms of the function
three_x_squared_minus_eleven = [(3, 2), (-11, 0)]

#Put it all together:
output_at(three_x_squared_minus_eleven, 2) # 1 

#try with x=3
output_at
(three_x_squared_minus_eleven, 3) # 16
```
**Graph it!**
 we can use our output_at function to display our function graphically. We simply declare a list of x_values and then calculate output_at for each of the x_values.
```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import plot, trace_values

x_values = list(range(-30, 30, 1))
y_values = list(map(lambda x: output_at(three_x_squared_minus_eleven, x),x_values))

three_x_squared_minus_eleven_trace  = trace_values(x_values, y_values, mode = 'lines')
plot([three_x_squared_minus_eleven_trace], {'title': '3x^2 - 11'})
```
**Derivatives of linear functions**

f(x)=4x+15 
```python
four_x_plus_fifteen = [(4, 1), (15, 0)]
```
Plot it using:
```python
import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import plot, trace_values, build_layout

x_values = list(range(0, 6))
# layout = build_layout(y_axis = {'range': [0, 35]})


four_x_plus_fifteen_values = list(map(lambda x: output_at(four_x_plus_fifteen, x),x_values))
four_x_plus_fifteen_trace = trace_values(x_values, four_x_plus_fifteen_values, mode = 'lines')
plot([four_x_plus_fifteen_trace])
```
**Writing a function for a derivative**

Start by writing a function for **change in f** or **delta_f** which will be used in the full derivative function

(**change in f/change in x**)

For now, focusing on change in f which is
Δf=f(x+Δx)−f(x)

Write a function called delta_f that, given a list_of_terms, an x_value, and a value  Δx , returns the change in the output over that period.

f(x)=4x+15

```python
four_x_plus_fifteen = [(4, 1), (15, 0)]
```
Again solving for:
Δf=f(x+Δx)−f(x)

When f(x)=4x+15
```python
def delta_f(list_of_terms, x_value, delta_x):
    return output_at(list_of_terms, x_value + delta_x) - output_at(list_of_terms, x_value)
#For:
four_x_plus_fifteen = [(4, 1), (15, 0)]
#output:
delta_f(four_x_plus_fifteen, 2, 1) # 4
4
```
Now we have Δf!

**In sum:**  for f(x)=4x+15, when x = 2, and  Δx=1,  Δf is 4

**TO GRAPH**
```python
def delta_f_trace(list_of_terms, x_value, delta_x):
    initial_f_value = output_at(list_of_terms, x_value)
    delta_f_value = delta_f(list_of_terms, x_value, delta_x)
    if initial_f_value and delta_f_value:
        trace =  trace_values(x_values=[x_value + delta_x, x_value + delta_x], 
                              y_values=[initial_f_value, initial_f_value + delta_f_value], mode = 'lines',
                              name = 'delta f = ' + str(delta_x))
        return trace

trace_delta_f_four_x_plus_fifteen = delta_f_trace(four_x_plus_fifteen, 2, 1)
```
Let's add another function that shows the delta x.
```python
from graph import plot, trace_values

trace_delta_x_four_x_plus_fifteen = delta_x_trace(four_x_plus_fifteen, 2, 1)
if four_x_plus_fifteen_trace and trace_delta_f_four_x_plus_fifteen and trace_delta_x_four_x_plus_fifteen:
    plot([four_x_plus_fifteen_trace, trace_delta_f_four_x_plus_fifteen, trace_delta_x_four_x_plus_fifteen], {'title': '4x + 15'})
```
**Calculating the derivative**

Write a function, **derivative_at** that calculates  Δf/Δx  when given a list_of_terms, an x_value for the value of (x) the derivative is evaluated at, as well as delta_x, which represents  Δx .

Let's try this again for f(x)=4x+15, using the delta_f function we created above. 
```python
def derivative_of(list_of_terms, x_value, delta_x):
    delta = delta_f(list_of_terms, x_value, delta_x)
    return delta/delta_x

#to round to 3 decimal places, just format the return: round(delta/delta_x, 3)

derivative_of(four_x_plus_fifteen, 3, 2) # 4.0
4.0
```
Showing all this on a graph:

```python
def derivative_trace(list_of_terms, x_value, line_length = 4, delta_x = .01):
    derivative_at = derivative_of(list_of_terms, x_value, delta_x)
    y = output_at(list_of_terms, x_value)
    if derivative_at and y:
        x_minus = x_value - line_length/2
        x_plus = x_value + line_length/2
        y_minus = y - derivative_at * line_length/2
        y_plus = y + derivative_at * line_length/2
        return trace_values([x_minus, x_value, x_plus],[y_minus, y, y_plus], name = "f' (x) = " + str(derivative_at), mode = 'lines')
```
**derivative_trace function** 
shows the rate of change, or slope, for the function between initial x and initial x plus delta x. 

It takes as arguments list_of_terms, x_value, which is where our line should be tangent to our function, line_length as the length of our tangent line, and delta_x which is our  Δx.

The return value of derivative_trace is a dictionary that represents tangent line at that values of  x. It uses the **derivative_of** function you wrote above to calculate the slope of the tangent line. 

Once the slope of the tangent is calculated, we stretch out this tangent line by the line_length provided. The beginning x value is just the midpoint minus the line_length/2 and the ending x  value is midpoint plus the line_length/2. 

Then we calculate our  y  endpoints by starting at the  y along the function, and having them ending at line_length/2*slope in either direction.

```python
tangent_line_four_x_plus_fifteen = derivative_trace(four_x_plus_fifteen, 2, line_length = 4, delta_x = .01)
tangent_line_four_x_plus_fifteen
#ouput:
{'x': [0.0, 2, 4.0],
 'y': [15.0, 23, 31.0],
 'mode': 'lines',
 'name': "f' (x) = 4.0",
 'text': []}
 ```
 Now we provide a function that simply returns all three of these traces.
 ```python
 def delta_traces(list_of_terms, x_value, line_length = 4, delta_x = .01):
    tangent = derivative_trace(list_of_terms, x_value, line_length, delta_x)
    delta_f_line = delta_f_trace(list_of_terms, x_value, delta_x)
    delta_x_line = delta_x_trace(list_of_terms, x_value, delta_x)
    return [tangent, delta_f_line, delta_x_line]
```
Below we can plot our trace of the function as well:
 ```python
 delta_x = 1

# derivative_traces(list_of_terms, x_value, line_length = 4, delta_x = .01)

three_x_plus_tangents = delta_traces(four_x_plus_fifteen, 2, line_length= 2*1, delta_x = delta_x)

# only plot the list of traces, if three_x_plus_tangents, does not look like [None, None, None]
if list(filter(None.__ne__, three_x_plus_tangents)):
    plot([four_x_plus_fifteen_trace, *three_x_plus_tangents])
```
So that function highlights the rate of change is moving at precisely the point x = 2. 

```python
#Using plotly, there would be a graph here showing both the slope, and a graph next to it showing the rate of change (which is constant in the case of a straight line).

from graph import make_subplots, trace_values, plot_figure

def function_values_trace(list_of_terms, x_values):
    function_values = list(map(lambda x: output_at(list_of_terms, x),x_values))
    return trace_values(x_values, function_values, mode = 'lines')
    
def derivative_values_trace(list_of_terms, x_values, delta_x):
    derivative_values = list(map(lambda x: derivative_of(list_of_terms, x, delta_x), x_values))
    return trace_values(x_values, derivative_values, mode = 'lines')

def function_and_derivative_trace(list_of_terms, x_values, delta_x):
    traced_function = function_values_trace(list_of_terms, x_values)
    traced_derivative = derivative_values_trace(list_of_terms, x_values, delta_x)
    return make_subplots([traced_function], [traced_derivative])

four_x_plus_fifteen_function_and_derivative = function_and_derivative_trace(four_x_plus_fifteen, list(range(0, 7)), 1)

plot_figure(four_x_plus_fifteen_function_and_derivative)

#output
This is the format of your plot grid:
[ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
#AND A GRAPH!!!
```


## Fun Facts:
### Lambdas:
```python
def double(x):
    return x * 2
# is equivalent to
labda x: x * 2
```

```python
# multiply_list takes a list of integers and returns a list of integers multiplied by the second argument
# e.g. multiply_list([1,2], 2) == [2,4]
def multiply_list(list_of_items, multiplier):
    return list(map(lambda item: item * multiplier, list_of_items))

multiply_list([1,2] 3) # [3, 6]
```
This use of lambda is equivalent to defining a function _inside the scope_ of the `multiply_list` function. 
```python
def multiply_list(list_of_items, multiplier):
    def multiply_item(item):
        return item * multiplier
    return list(map(multiply_item, list_of_items))

multiply_list([1,2] 3) # [3, 6]
```
`multiply_item` (or its lambda equivalent) must be deinfed within `multiply_list` so that it can take only one argument (a requirement for `map`) but still have access to the `multiplier` variable. 

### For loops vs. maps
Using a **For Loop** in a function VS using **List(Map(Lambda...)**
```python
def output_at(list_of_terms, x_value):
    final_answer = 0
    for term in list_of_terms:
        final_answer = final_answer+ term_output(term, x_value)
    return(final_answer)

three_x_squared_minus_eleven = [(3, 2), (-11, 0)]

output_at(three_x_squared_minus_eleven, 2) # 1 
```

THIS IS THE SAME AS:

```python
def term_output(term, input_value):
    return term[0]*input_value**term[1]

def output_at(list_of_terms, x_value):
    outputs = list(map(lambda term: term_output(term, x_value), list_of_terms))
    return sum(outputs)

three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
output_at(three_x_squared_minus_eleven, 2) 
#output
1
```
**Derivatives of non-linear functions**

Once again, use:

f′(x)=Δf/Δx

f′(x)=f(x+Δx)−f(x)/Δx

we do the following:

*Set  x=2, as that's the point we want to calculate the rate of change at

*Set  Δx=1, as that's the number of seconds that elapsed on our stopwatch

We saw multiple ways of calculating this rate of change.

**RECAP**

**derivative** is the rate of change of a function.

Graphically this is rise over run

Which can be calculated by taking two points (x1,y1) and x2,y2)and calculating:  

y2−y1/x2−x1

Finally, we said that when we have a function  f(x) , we can calculate the derivative with knowing the starting point and the change in our input, x:

f(x1+Δx)−f(x1)/Δx

**Calculating speed at a certain point:**
Using a track star. We want to know how our track star does at one part of the race, say the starting point, versus another point later in the race. We can imagine the distance travelled by our track star's distance through time as represented by the function  f(x)=x^2

We measure the change at second two by starting our stopwatch at second 2 and stopping it one second later. So turning this into our formula for calculating a derivative of:

f′(x)=f(x+Δx)−f(x)/Δx

Set  x=2 , as that's the point we want to calculate the rate of change at

Set  Δx=1 , as that's the number of seconds that elapsed on our stopwatch

f′(2) = f(2+1)−f(2)/1 = f(3)−f(2)/1

So our rate of change at second number 2, with a  Δx=1  is calculated by subtracting the function's output at second 2 from the function's output at second 3 and dividing by delta x, one.

Simplifying our calculation of f′(x) further by calculating the outputs at x = 2 and x = 3 we have:

f(3) = (3)^2 = 9f(3) = (3)2 = 9  is the output at **x = 3** 

f(2) = (2)^2 = 4f(2) = (2)2 = 4  is the output at **x = 2** so

f′(2) = 9−4/1 = 5/1 = **5**

**The problem with our derivative formula**
That straight line is a supposed to be the rate of change of the function at the point  x=2. On our plot, the orange line quickly begins to move above the blue line, indicating that it has a faster rate of change than the blue line at  x=2. This means that our calculation that  f′(1)=5  is a little high.

**Here is the problem:** in our formula of  

f′(x)=f(x1+Δx)−f(x1)/Δx 

We are seeing the rate of change not just where x = 2, but from the period from  x=2  to  x=3.

A mathematician would make the  point that we are not actually calculating the derivative:

Our derivative means we are calculating **how fast a function is changing at any given moment, and precisely at that moment**. And unlike in where our functions were linear, here the rate of change of our function is always changing. The larger our value of Δx, the less our derivative reflects the rate of change at just that point.

**The solution: Decrease the change in x**

To calculate the rate of change at precisely one point, the solution is to use our imagination. We calculate the derivative with a Δ of 1, then calculate it again with a Δx  of .1, then again with Δx of .01, then again with Δ .001. Our derivative calculation should show convergence on a single number as our Δ approaches zero and that number is our derivative.

_That is, the derivative of a function is a change in the function's output across  Δx, as  Δx  approaches zero_

Another way to see how we approach the derivative is by seeing how a line becomes more **tangent** to the curve as delta x decreases.

In our example, as  Δx approaches zero,  f′(2) approaches  4. This convergence around one number as we change another number, is the **limit**.

**Approaching our formula for a derivative**

So the derivative is the change in output as we just nudge our input. That is how we calculate instantaneous rate of change. We can determine the runners speed at precisely second number 2, by calculating the runner's speed over shorter and shorter periods of time, to see what that number approaches.

**Derivative Rules**

1: To calculate that slope of the function at a given point, we make  Δx value smaller until it approaches zero, and see what our  Δf/Δx  converges upon.

2: This convergence around one number is called the limit.

3: **The power rule**

Given the following:

f(x)=x^r
 
Then, the **derivative** is:
f′(x) = r∗x^(r−1)

This says that if a variable,  x , is raised to a exponent  r ,then the derivative of that function is the exponent  r  multiplied by the variable, with the variable raised to the original exponent minus one.

**Example:** If f(x)=3∗x, there is no exponent so we know immediately that it is a linear function!

In this example, the rate of change of our linear function f(x)=3x was always 3. Since the rate of change is constant for linear functions, the derivative will be the same across all values of x.

Now let's see how this works with our power rule:

f(x)= 3∗x = 3∗x^1
 
Now applying our rule that for a function with

f(x)=x^r
 
f′(x)=r∗x^(r−1)
 
we see that in this case  r=1 . So applying our power rule we have:

f′(x) = r∗3∗x^(r−1) = 1∗3∗x^(1−1) = 3∗x^0 = 3

**Another example**
Let's apply the power rule with another example to make sure that we understand it.

f(x)=x^2
 
f′(x)= 2∗x^(2−1) = 2∗x^1 = 2∗x


Think about what our calculation for  f′(x) is saying about our function. It says, for our function  f(x)=x2 , a small change in  x  produces an increase in  f(x)  equal to 2 times the  x  value. Or, in other words:

f′(x)=2∗x
 
So when  x=2 then  f′(2)=2∗2=4 
When  x=3 , then  f′(3)=2∗3=6 
When  x=−1 , then  f′(−1)=2∗(−1)=−2
And when  x=10 , then  f′(10)=2∗10=20

**The constant factor rule**
The constant factor addresses how to take the derivative of a function multiplied by a constant.

In the general case, we can say, consider the function  a∗f(x) where  a  is a constant (that is, is a number and not a variable).

 The rule simply says if a variable is multiplied by a constant (i.e. a number), then to take the derivative of that term, apply our familiar power rule to the variable and multiply the variable by that same constant.

**The addition rule**

So far, all of our functions consisted of only one term. Remember that a term is a constant or variable that is separated by a plus or minus sign. For example, the function  f(x) below has three terms:

f(x)= 4x^3−x^2+3x

To take a derivative of a function that has multiple terms, simply take the derivative of each of the terms individually. So for the function above,
 
f′(x)=12x^2−2x+3

 We simply applied our previous rules to each of the terms individually and continued to add or subtract the terms accordingly.

 **Derivatives Drill**
 Let's take the last few lines of this lesson to practice these derivative rules.

1: f(x)=3x^5

2: g(x)=10x

3: z(x)=10

Answers:

1:

f(x)=3x^5

f′(x)=15x^4
 
2:

g(x)=10x

g′(x)=10

3:

z(x)=10

z(x)=10∗(x^0)

z′(x)=0∗10x^(0−1)=0

So as you can see, we are just applying our rule:

f(x)=x^r
 
f′(x)=r∗x^(r−1)
 
And note that whenever we take the derivative of a constant like the number 10, then the derivative of that constant is 0.

A couple more derivatives, using the **Power Rule**, **Constant Rule**, and **Addition Rule**:

1:

f(x)=3x^3+8x+12
 
f′(x)=9x2+8
 
2:

g(x)=12x^2+4x^2+2

g′(x)=24x+8x=32x

**Derivatives Rules Lab:**

As you know we can represent polynomial functions as a list of tuples.

Each term is represented as a single tuple, for example,  2x3  is expressed as (2, 3).

And an entire function is expressed as a list of tuples, like  f(x)=2x3+7x is expressed as [(2, 3), (7, 1)].

Between elements in our list, we imagine there is a plus sign. To subtract elements we simply place a negative sign before the first element in the tuple. For example,  f(x)=x2−4x is represented as [(1, 2), (-4, 1)].

**Remember:** tuples are just like lists except that they are immutable. We can access elements of a tuple just as we do a list.

two_x_cubed = (2, 3)

two_x_cubed[1] # 3

**Writing our derivative functions**

The function takes the derivative of one term represented as a tuple, say  (1,3) , and returns its derivative, also represented as a tuple. 

For example, if the function is  f(x)=2x^4 so its derivative is  f′(x)=2x^3 , then our function find_term_derivative should take an input of (2, 4) and return (2, 3).

Find_term_derivative, let's first consider the function  f(x)=x^3

```python
one_x_cubed = (1, 3)

def find_term_derivative(term):
    return (term[1]*term[0], term[1]-1)

find_term_derivative(one_x_cubed) # (3, 2)
(3, 2)
```
Let's try the function with  f(x)=2x^2 
```python
two_x_squared = (2, 2)
find_term_derivative(two_x_squared) # (4, 1)
(4, 1)
```
**Multi-termed Function**

If the derivative of a function  f(x)  is  f′(x)=2x^3+4x^2, then the function find_derivative should return [(2, 3), (4, 2)].

Note: Imagine that a plus sign separates each of our terms. Again, if we need a negative term, then we add a minus sign to the first element of the tuple.

Let's apply this function to  f(x)=4x^3−3x
```python

def find_derivative(function_terms):
    return list(map(lambda function_term: (function_term[1]*function_term[0], function_term[1]-1), function_terms))

four_x_cubed_minus_three_x = [(4, 3), (-3, 1)]
find_derivative(four_x_cubed_minus_three_x)  # [(12, 2), (-3, 0)]
[(12, 2), (-3, 0)]
```
One **gotcha** to note is when one of our terms is a constant, when taking the derivative, the constant is removed. 

For example, when  f(x)=3x^2−11 , the derivative  f′(x)=6x. 

The reason why is because 11 is the same as  11∗x^0  which is also  11∗1 , as anything raised to the zero power equals 1. And so the derivative of the term  11x^0  equals  0∗11∗x^(−1)=0. 

Our **find_derivative** function should return, using **filter**, only the terms whose derivatives are not multiplied by zero.

```python
def find_derivative(function_terms):
    derivatives = list(map(lambda function_term: (function_term[1]*function_term[0], function_term[1]-1), function_terms))
    return list(filter(lambda derivative: derivative[0] !=0, derivatives))

three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
find_derivative(three_x_squared_minus_eleven) # [(6, 1)]
[(6,1)]
```
**PUT IT ALL TOGETHER**

(in this case, we're importing the function output_at from above...)
```python
def output_at(list_of_terms, x_value):
    outputs = list(map(lambda term: term_output(term, x_value), list_of_terms))
    return sum(outputs)
```
THEN...
```python

def derivative_at(terms, x):
    # terms [(3, 2), (-11, 0)]
    derivative_terms = find_derivative(terms) # [(6, 1)]
    return output_at(derivative_terms, x)

find_derivative(three_x_squared_minus_eleven) # [(6, 1)]
derivative_at(three_x_squared_minus_eleven, 2) # 12
12
```
ORRRR....
```python
def derivative_at(terms, x):
    derivative_fn = find_derivative(terms)
    total = 0 #creating a for loop
    for term in derivative_fn:
        total += term[0]*x**term[1] #this is the same as output_at from above!
    return total

find_derivative(three_x_squared_minus_eleven) # [(6, 1)]
derivative_at(three_x_squared_minus_eleven, 2) # 12
12
```
**Graphing the derivative across a range of values**

We can also write a function that given a list of terms can plot the derivative across multiple values. After all, the derivative is just a function. For example, when  f(x)=3x^2−11, the derivative is  f′(x)=6x . And we know that we can plot multi-term functions with our function_values_trace.

This is what function_values_trace looks like:
```python
from calculus import function_values_trace

three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
function_values_trace(three_x_squared_minus_eleven, list(range(-5, 5)))

#output
{'x': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],
 'y': [64, 37, 16, 1, -8, -11, -8, 1, 16, 37],
 'mode': 'lines',
 'name': 'data',
 'text': []}
```
This is what function_values_trace looks like:
```python
    def function_values_trace(list_of_terms, x_values):
        function_values = list(map(lambda x: output_at(list_of_terms, x),x_values))
        return trace_values(x_values, function_values, mode = 'line')#this is new, but comes from function_values_trace output above.
```
Solve for derivative_function_trace:
```python
def derivative_function_trace(terms, x_values):
    derivative_terms = find_derivative(terms)
    return function_values_trace(derivative_terms, x_values)

#Call it
three_x_squared_minus_eleven_derivative_trace = derivative_function_trace(three_x_squared_minus_eleven, list(range(-5, 5)))

three_x_squared_minus_eleven_derivative_trace

{'x': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],
 'y': [-30, -24, -18, -12, -6, 0, 6, 12, 18, 24],
 'mode': 'lines',
 'name': 'data',
 'text': []}
```
So now that we can plot a nonlinear function with our function_values_trace and plot that function's derivative with the derivative_function_trace trace, we can now plot these traces side by side!

**Multivariable Functions**

We want to approach our best fit line in an efficient manner, so we look to the slope of our **cost curve** at at a specific value to tell us whether to increase or decrease our y-intercept variable and how large of a change to make. 

We can make this change even without knowing what the rest of our cost function looks like, and just look to the slope at the current value. This technique is called **gradient descent**.

**Explaining 3D graphing:** Multiple Variables

For our function f(x,y)=y∗x^2 , this parabola is multiplied by the value of  y. 

1: So, for example, when  y=2 ,  f(x,2)=2x^2 means the parabola is twice as steep as each output doubles. The further  y moves away from zero the steeper the parabola.

2: And a negative  y  in the function  f(x,y)=y∗x^2  flips our parabola upside down.

**Reminder:** The output for multivairate functions looks something like this:

For function:

f(x,y) = x^2 + y^2

For input (x,y) = (1,2)

Plug it in to the function, output is: 

f(1,2) = 1^2 + 2^2 = 5

Now if you want to plot this, the original tuple turns into:

**(1,2,5)** -> three variables in space!

**Gradient Descent** and **Partial Derivatives**

1: For a two-dimensional regression line:

When changing just one variable,  m  or  b , **gradient descent** means stepping forwards or backwards along the cost curve and and taking a **specific step size.** 

To determine whether to move forwards or backwards (as well as the step size) we imagine standing ON the two-dimensional curve and feeling the slope of our cost curve to tell us how to move. A step in a direction means **a change in one of our regression variables**.

2: For THREE dimensions:

In three dimensions, we once again choose an initial regression line, which means that we are choosing a point on the graph and begin taking steps towards the minimum. 

But now, we are now able to walk not just forwards and backwards but left and right as well -- as we now **can alter two variables.**

Imagine our initial regression line places us at the back-left corner of the graph above, with a slope of 50, and y-intercept of negative 20. Now imagine that we cannot see the rest of the graph - yet we still want to approach the minimum. How do we do this?


So this is our approach: We shift horizontally a little bit to determine the change in output in right-left direction, and then shift forward and back to determine the change in output in that direction. From there **we take the next step in the direction of the steepest descent.**

**Taking this mathematically:** It means we determine the slope in one dimension, then the other. Then, we move where that that slope is steepest downwards. This moves us towards our minimum.

This leads up to....**PARTIAL DERIVATIVES!**

To measure the slope in each dimension, one after the other, we'll:

1: take the derivative with respect to one variable, and then, 

2: take the derivative with respect to another variable. 

What it means to take a partial derivative with respect to a variable:

f(x,y)=y∗x^2

1: First, we nudge only in the x direction. This is expressed : lowercasedelta f / lowercasedelta x

2: Then, nudge only in the y direction. This is expressed: lowercasedelta f / lowercasedelta y

What this means is calculating **the change in output as we nudge our input over** in the  x or y  direction.

**What does a partial derivative look like?**

1: Remember the standard derivative of one variable function is determined: f(x)=x^2

In two dimensions, to take the derivative at a given point, we simply calculate the slope of the function at that x value. 

2: For multiple varibales, it's **equal to the slope of the tangent line at a specific  x value AND a specific y value.** 

Let's do it for the 3-d graph of  

f(x,y)=yx^2

First let's understand our plots below -- they may be surprising. 

Starting at the top left quadrant the graph of the function  f(x,y)  makes sense as when  x=−1 then the function is just f(y)=−1∗y

And moving down to the bottom left,  f(2,y)= 2^2∗y = 4y

And we know that the derivative of a line is always just equal to the line's slope. 

So, for f(1,y) that slope, and thus the derivative, is always 1

For f(2,y) it's 4

_Again, reviewing the process:_

So that is our technique for a partial derivative. For  df/dy we move to a slice of the curve at a specific value of x , move to the point for y, and then calculate the change in output as we nudge in the  y direction.

For  df/dx , we move to a slice of a curve of a specific value of y , move the correct value of  x and then calculate how much the output changes as we nudge in the y  direction. 

_Just think slide, slide then nudge. That's a partial derivative._

**Rule for partial derivatives:**

 For any multivariable function, the variables that you are not taking the derivative with respect to, can just be treated as a constant.

We calculated that  df/dy f(x,y) = x^2 , and that is what the graphs show. 

When  x=2 our derivative is always 4.  

When  x=3  the derivative is always 9. 

So even though we are taking  **df/dy**, the  x value is influencing the steepness of that line. 

But by the time we get to our **nudge**, that value of  x is constant, it's influence has already been applied. Then we are seeing how the output changes as we nudge in the  y  direction.

It can also be switched around, where y can be treated as the constant, such as in f(x,y)=y∗x^2

**Summary:**

For the partial derivative, we say we are taking the derivative with respect to a variable.

So for example, we can say for the function f(x,y), take the partial derivative with respect to the variable x. This means we are assessing the output after nudging in the x direction.

Basically, youre looking for a tiny change in the output thats caused by a tiny change in the input. And that change is dependent on where you start, in this case, x.

You're trying to find how that nudge influences the function itself. You can almost imagine it as mapping from a x line onto a new, f line to show how this change manifests.

If, say, the dx nudge for df that's four times as big, or 4, which means your derivative is 4 at that point.

Our rule for taking the partial derivative is **to treat the variables that we are not taking the derivative with respect to as constants**. 

 This makes sense because at the time that we are taking the derivative by making our "nudge" the only variable that is changing is the variable we are taking the derivative with respect to.

 **PARTIAL DERIVATIVES LAB**

   f(x,y)=3xy

First break this function down into it's equivalent of different slices. We'll do this by taking different slices of the function, stepping through various values of y .

Instead of considering the entire function,  f(x,y)=3xy  we can think about the function  f(x,y) evaluated at various points, where  y=1,  y=3,  y=6, and  y=9.

First, write the Python functions that return the values  f(x,y)  for:
f(x,1),  
f(x,3),  
f(x,6),  
f(x,9)  

For the function  f(x,y)=3xy.
```python
def three_x_y_at_one(x):
    y = 1
    return 3*x*y

def three_x_y_at_three(x):
    y = 3
    return 3*x*y

def three_x_y_at_six(x):
    y = 6
    return 3*x*y

def three_x_y_at_nine(x):
    y = 9
    return 3*x*y
three_x_y_at_one(3) # 9
three_x_y_at_three(3)# 27
three_x_y_at_six(1) # 18
three_x_y_at_nine(2) # 36
```
Now that we have our functions written, we can write functions that provided an argument of x_values, return the associated y_values that our four functions return.
```python
def y_values_for_at_one(x_values):
    return list(map(lambda x: three_x_y_at_one(x), x_values))

def y_values_for_at_three(x_values):
    return list(map(lambda x: three_x_y_at_three(x), x_values))
    
def y_values_for_at_six(x_values):
    return list(map(lambda x: three_x_y_at_six(x), x_values))

def y_values_for_at_nine(x_values):
    return list(map(lambda x: three_x_y_at_nine(x), x_values))

zero_to_ten = list(range(0, 11))
zero_to_four = list(range(0, 5))

y_values_for_at_one(zero_to_four) # [0, 3, 6, 9, 12]
y_values_for_at_one(zero_to_ten) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

y_values_for_at_three(zero_to_four) # [0, 9, 18, 27, 36]
y_values_for_at_three(zero_to_ten) # [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]

y_values_for_at_six(zero_to_four) # [0, 18, 36, 54, 72]
y_values_for_at_six(zero_to_ten) # [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180]

y_values_for_at_nine(zero_to_four) # [0, 27, 54, 81, 108]
y_values_for_at_nine(zero_to_ten) #[0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270]
```
Now we are ready to plot the function  f(x)=x ,  f(x)=3x,  f(x)=6x and  f(x)=9x
```python
from graph import trace_values

y_at_one_trace = trace_values(zero_to_ten, y_values_for_at_one(zero_to_ten), mode = 'lines', name = 'f(x, y) at y=1') or {}

y_at_three_trace = trace_values(zero_to_ten, y_values_for_at_three(zero_to_ten),  mode = 'lines',  name = 'f(x, y) at y=3') or {}

y_at_six_trace = trace_values(zero_to_ten, y_values_for_at_six(zero_to_ten),  mode = 'lines', name = 'f(x, y) at y=6') or {}

y_at_nine_trace = trace_values(zero_to_ten, y_values_for_at_nine(zero_to_ten),  mode = 'lines', name = 'f(x, y) at y=9') or {}
```
## **Using our partial derivative rule**

Now let's consider the function  f(x,y)=4x^2y+3x+y. 

Now soon we will want to take the derivative of this function with respect to x . We know that in doing something like that, we will need to translate this function into code, and that when we do so, we will need to capture the exponent of any terms as well as.

four_x_squared_y_plus_three_x_plus_y = [(4, 2, 1), (3, 1, 0), (1, 0, 1)]

Let's get started by writing a function multivariable_output_at that takes in a multivariable function and returns the value  f(x,y) evaluated at a specific value of  x  and  y  for the function.
```python
def multivariable_output_at(list_of_terms, x_value, y_value):
    value_holder = 0
    for term in list_of_terms:
        total = term[0]*x_value**term[1]*y_value**term[2]
        value_holder += total
    return value_holder

multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1) # 8
8
```
So now we want to write a Python function that calculates  δf/δx of a multivariable function. Let's start by writing a function that just calculates  δf/δx of a single term.
```python
def term_df_dx(term):
    constant = term[0]
    exponent_x = term[1]
    exponent_y = term[2]
    return (constant*exponent_x, exponent_x - 1, exponent_y)

four_x_squared_y = (4, 2, 1)
term_df_dx(four_x_squared_y) # (8, 1, 1) 
(8, 1, 1)
#This solution represents  8xy
```
Now write a function that finds the derivative of all terms,  δf/δx of a function  f(x,y).
```python
def df_dx(list_of_terms):
    value_holder = []
    for term in list_of_terms:
        constant = term[0]
        exponent_x = term[1]
        exponent_y = term[2]
        equation = (constant*exponent_x, exponent_x - 1, exponent_y)
        value_holder += [equation]
    return value_holder

df_dx(four_x_squared_y_plus_three_x_plus_y)
[(8, 1, 1), (3, 0, 0), (0, -1, 1)]
```
ANOTHER way to do it:
```python
def df_dx(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dx(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] > 0, derivative_terms))
#This way provides a filter which removes the final thruple when it equals 0.

df_dx(four_x_squared_y_plus_three_x_plus_y)
[(8, 1, 1), (3, 0, 0)]
```
Now that we have done this for  δf/δx , lets work on taking the derivative  δf/δy. 

Once again, we can use as an example our function  

f(x,y)=4x^2y+3x+y

Let's start with writing the function term_df_dy, which takes the partial derivative  δf/δy  of a single term.
```python
def term_df_dy(term):
    constant = term[0]
    exponent_x = term[1]
    exponent_y = term[2]-1
    return (constant, exponent_x, exponent_y)

four_x_squared_y # (4, 2, 1)
term_df_dy(four_x_squared_y) # (4, 2, 0)
```
Another way:
```python

def term_df_dy(term):
    constant = term[0]*term[2]
    exponent = term[2] - 1
    return (constant, term[1], exponent)

#In these examples, the x or y value not currently being used is referred to simply as '[term]'

four_x_squared_y
(4, 2, 1)
```
FINISH IT! Use the df/dy function to determine the derivative:
```python
def df_dy(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dy(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] > 0, derivative_terms))

df_dy(four_x_squared_y_plus_three_x_plus_y)
[(4, 2, 0), (3, 1, -1), (1, 0, 0)]

two_x_cubed_y_plus_three_y_x_plus_x = [(2, 3, 1), (3, 1, 1), (1, 1, 0)]
df_dy(two_x_cubed_y_plus_three_y_x_plus_x)
[(2, 3, 0), (3, 1, 0), (1, 1, -1)]
```
THAT IS HOW YOU GET THE DERIVATIVE OF A MUTLIVARIABLE FUNCTION!!!!!!