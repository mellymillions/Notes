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
# Partial Derivatives

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



# Linear Regression

## Single variable Regression

Where:

y = dependent variable

m = slope

x = input variable

b = y intercept

Full single linear regression equation:
**y = mx+b**

Using Python:
```python
def y(x):
    return m*x + b

print y(x) #For any input of  x  our function returns the value of  y  along that line.
```
## Calculating Slope

**Rise over run**. We can determine the slope by taking any two points along the line and looking at the ratio of the vertical distance travelled to the horizontal distance travelled. 


Given a beginning point  (x0,y0) and an ending point  (x1,y1) along any segment of a straight line, the slope of that line  m  equals the following:

Full slope equation: **m=(y1−y0)/(x1−x0)**

In python:
```python
def slope(x_values, y_values):
    return (y_values[1]-x_values[1])/(y_values[0]-x_values[0])
```

## Calculating Y-Intercept

First, let's figure out the slope of our line.

Then plug in our value of  m  into our formula.

Full y-intercept equation: **y=3x+b**

**LAB**

The comedy show is trying to figure out how much money to spend on advertising in the student newspaper. The newspaper tells the show that

1. For every two dollars spent on advertising, three students attend the show.

2. If no money is spent on advertising, no one will attend the show.

Write a linear regression function called attendance that shows the relationship between advertising and attendance expressed by the newspaper.

m = 3/2 (3 students / $2 on advertising) 

b = 0 (because $0 advertising = 0 attendees)

```python
def attendance(advertising):
    return (3/2)*advertising + 0

attendance(100) # 150
```
When the advertising budget is zero, 20 friends still attend
Three additional people attend the show for every two dollars spent on advertising.

The additional 20 friends is the y-intercept, which is now 20.
```python
def attendance(advertising):
    return (3/2)*advertising + 20

attendance(100) # 170
```
PLOT IT!

initial_sample_budgets = [0, 50, 100]

attendance_values = [20, 95, 170]

First we **import the necessary plotly library**, and **graph_obs function**, and setup plotly to be used without uploading our plots to its website.

Finally, we plot out our regression line using our attendance_with_friends function. 

Our x values will be the budgets. 

For our y values, we need to use our attendance_with_friends function to create a list of y-value attendances for every input of x.
```python
import plotly
from plotly import graph_objs
plotly.offline.init_notebook_mode(connected=True)

trace_of_attendance_with_friends = graph_objs.Scatter(
    x=initial_sample_budgets,
    y=attendance_values,
)

plotly.offline.iplot([trace_of_attendance_with_friends])

#run it, output
trace_of_attendance_with_friends
Scatter({
    'x': [0, 50, 100], 'y': [20, 95, 170]
})
```
DONE!

## Functions for Linear Regression

Now let's write a couple functions that we can use going forward. 

We'll write a function called m_b_data that give:
1. a slope of a line (m)  
2. a y-intercept (b) 
3. will return a dictionary that has a key of (x) pointing to a list of x_values
4. a key of y that points to a list of y_values. 

Each  y  value should be the output of a regression line for the provided  m  and  b  values, for each of the provided x_values.
```python
def m_b_data(m, b, x_values):
    y_values = list(map(lambda x: m*x + b, x_values))
    return {'x': x_values, 'y': y_values}

m_b_data(1.5, 20, [0, 50, 100]) 
# {'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
```
Now let's write a function called **m_b_trace** that uses our **m_b_data** function to return a dictionary that includes keys of name and mode in addition to x and y. 

The values of mode and name are provided as arguments. When the mode argument is not provided, it has a default value of **lines** and when name is not provided, it has a default value of **line function**.
```python
def m_b_trace(m, b, x_values, mode = 'lines', name = 'line function'):
    values = m_b_data(m, b, x_values)
    values.update({'mode': mode, 'name': name})
    return values

m_b_trace(1.5, 20, [0, 50, 100]) 
{'x': [0, 50, 100],
 'y': [20.0, 95.0, 170.0],
 'mode': 'lines',
 'name': 'line function'}
 ```

**LAB**
```python
first_show = {'budget': 200, 'attendance': 400}
second_show = {'budget': 400, 'attendance': 700}

def marginal_return_on_budget(first_show, second_show):
    return (second_show['attendance'] - first_show['attendance'])/(second_show['budget'] - first_show['budget'])
```
Define a **slope function**:
```python
def slope(x_values, y_values):
    return (y_values[1]-x_values[1])/(y_values[0]-x_values[0])
    pass
```
OR!!
```python
def slope(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    x1 = sorted_values[0][0]
    y1 = sorted_values[0][1]
    x2 = sorted_values[-1][0]
    y2 = sorted_values[-1][1]
    m = (y2 - y1)/(x2 - x1)
    return m
```
Now write a function called **y_intercept:** 

Use the slope function to calculate the slope if it isn't provided as an argument. Then we will use the slope and the values of the point with the highest x value to return the y-intercept.
```python
def y_intercept(x_values, y_values, m = None):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    if m == None:
        m = slope(x_values, y_values)
    offset = highest[1] - m*highest[0]
    return offset
```
Now write a function called **build_starting_line** that given a list of x_values and a list of y_values returns:
1.  a dictionary with a key of m 
2.  a key of b to return the m and b values of the calculated regression line. 

Use the slope and y_intercept functions to calculate the line.
```python
def build_starting_line(x_values, y_values):
    sorted_values = sorted_points(x_values, y_values)
    highest = sorted_values[-1]
    lowest = sorted_values[0]
    m = slope(x_values, y_values)
    b = y_intercept(x_values, y_values, m)
    return {'m': m, 'b': b}
```
Now, put them all together into the full equation!
```python
def expected_value_for_line(m, b, x_value):
    return m*x_value + b
```
PLOT IT! 

As we can see above, we built a "starting" regression line out of the points with the lowest and highest x values. We will learn in future lessons how to improve our line so that it becomes the "best fit" given all of our dataset, not just the first and last points. For now, this approach sufficed since our goal was to practice working with and plotting line functions.

# Evaluation of Regression Lines

**Series and Summations**

One of the nice things about data science is that it allows us to explore the symmetry between mathematics and coding. We saw this with translating equations into functions. For example, we have now seen how to translate something like this:  

y=1.3x+20

into code like this:
```python
def y(x):
    return 1.3*x + 20
```
**Sequences in code** OR **Sigma Notation**

Consider this list:
```python
my_list = [1, 6, 11, 16, 21]
```
Looking at the numbers above, you can see that these numbers start at one and increment by five for every number. So below we generate these numbers with code, and also use code to express how these numbers increment.
```python
initial_i = 0
ending_i = 4

terms = []
for i in range(initial_i, ending_i + 1):
    current_element = 5*(i) + 1
    terms.append(current_element)
terms
```
Our code above expresses a pattern in the numbers:

1. initialize a number (our index) at zero
2. increase the index until it reaches four
3. Each element in the list equals  5∗i+1 for the index 0 up to and including 4

**Sequences in math**
In Python we call this ordered collection a **list**. In math, an ordered list of numbers is called a **sequence**. 

We express sequences not with [], but with parentheses or curly brackets. For example:

(1, 6, 11, 16, 21) or
{1, 6, 11, 16, 21}

Each component of a sequence is called an element, or a term. So in our sequence above, 1 is a term, as is 6 and 21.

CONSIDER: (xi)4 as i=0  where  xi=5∗i+1

Read the above line as the following: 
1. A sequence of numbers
2. from the indices of 0 to 4 (i=0 being the starting point of the range/indices and 4 being the stopping point)
3. where  sum of xi or Sigma equals 5∗i+1 (meaning this equation is applied to each number in the sequence, then summed)

Again, this gives us {1, 6, 11, 16, 21}

In describing a sequence in math, the initial index is placed at the bottom, and the stopping point at the top. And the common term for the sequence is also described.

**A mathematical series**
(xi)4 i=0 where xi=5∗i+1=1+6+11+16+21=55

Let's see how we would write something like this using Python. Here is the sequence that we previously generated written another way. 

Python's range function can accept a third argument, **which tells it how much to increment each element**. In other words, we start at 1, increment each element by 5, then stop at 21 because 26 < 22 is False.
```python
num_range = list(range(1, 22, 5))
num_range

#[1, 6, 11, 16, 21]
```
Now to turn this into a series, we just add up those terms
```python
total = 0
for i in num_range:
    total += i
total

#55
```
Or we can use Python's built-in sum function to add up the elements in num_range.
```python
num_range
sum(num_range)

#55
```
All this is the same as using SIGNA NOTATION!!

## Evaluating Regression Lines

Using a dictionary, converting movie data into variables:
```python

movies[0]
{'budget': 13000000, 'domgross': 25682380.0, 'title': '21 &amp; Over'}

#converting to manageable numbers because amounts are in millions.
movies[0]['budget']/1000000

#using map to convert all of them to meaningful scles numbers.
scaled_movies = list(map(lambda movie: {'title': movie['title'], 'budget': round(movie['budget']/1000000, 0), 'domgross': round(movie['domgross']/1000000, 0)}, movies))
scaled_movies[0]

{'title': '21 &amp; Over', 'budget': 13.0, 'domgross': 26.0}
```
As a first task, convert the budget values of our scaled_movies to x_values, and convert the domgross values of the scaled_movies to y_values.
```python
x_values = list(map(lambda movies: movies['budget'], scaled_movies))

y_values = list(map(lambda movies: movies['domgross'], scaled_movies))

#Assign a variable called titles equal to the titles of the movies.
titles = list(map(lambda movies: movies['title'], scaled_movies))
```
Using Plotly to plot these points on a graph:
```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, plot

movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')

plot([movies_trace])
```
**Plotting a regression Line**
Now let's add a regression line to make a prediction of output (revenue) based on an input (the budget). We'll use the following regression formula:

ŷ =1.7x+10
```python
def regression_formula(x):
    return 1.7*x + 10
```
Use Plotly to create the regression line:
```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, m_b_trace, plot

if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace])
```
## Calculating Error of regression line

First, We provide a function called y_actual that given a data set of x_values and y_values, finds the actual y value, provided a value of x.
```python
def y_actual(x, x_values, y_values):
    combined_values = list(zip(x_values, y_values))
    point_at_x = list(filter(lambda point: point[0] == x,combined_values))[0]
    return point_at_x[1]

x_values and y_values and y_actual(13, x_values, y_values) # 26.0
```
Then we write an error function:

 Given a list of x_values, and a list of y_values, the values m and b of a regression line, and a value of x, returns the error at that x value. Remember  εi=yi−ŷ 
 ```python
 def error(x_values, y_values, m, b, x):
    expected = (m*x + b)
    return y_actual(x, x_values, y_values) - expected
```
Ok, so the function error_line_trace takes our dataset of x_values as the first argument and y_values as the second argument. It also takes in values of  mm  and  bb  as the next two arguments to represent the regression line we will calculate errors from. Finally, the last argument is the value  xx  it is drawing an error for.

The return value is a dictionary that represents a trace, and looks like the following:

{'marker': {'color': 'red'},
 'mode': 'lines',
 'name': 'error at 120',
 'x': [120, 120],
 'y': [93.0, 214.0]}

The trace represents the error line above. The data in x and y represent the starting point and ending point of the error line. 

Note that the x value is the same for the starting and ending point, just as it is for each vertical line. It's just the y values that differ - representing the actual value and the expected value. The mode of the trace equals 'lines'.
```python
def error_line_trace(x_values, y_values, m, b, x):
    y_hat = m*x + b
    y = y_actual(x, x_values, y_values)
    name = 'error at ' + str(x)
    return {'x': [x, x], 'y': [y, y_hat], 'mode': 'lines', 'marker': {'color': 'red'}, 'name': name}
```
From there, we can write a function called error_line_traces, that takes in a list of x_values as an argument, y_values as an argument, and returns a list of traces for every x value provided.
```python
def error_line_traces(x_values, y_values, m, b):
    return list(map(lambda x_value: error_line_trace(x_values, y_values, m, b, x_value), x_values))
```
Now when we run this in Plotly we'll see the error (in lines) of all the plots and their relationship to the line of best fit.
```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import trace_values, m_b_trace, plot

if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace, *errors_for_regression])
```
It looks really cool!

# Evaluating Linear Regression 

## Regression formula

Now let's add a regression line to make a prediction of output (revenue) based on an input (the budget). We'll use the following regression formula:

ŷ =mx+b 

with m=1.7, and b=10

ŷ =1.7x+10

Write a function called regression_formula that calculates our ŷ for any provided value of x.
```python
def regression_formula(x):
    return 1.7*x + 10
```    

## Calculating errors of a regression Line

First, here is the **y-actual** function, provided by the 'Lab' aka by Flatiron. 
```python
def y_actual(x, x_values, y_values):
    combined_values = list(zip(x_values, y_values))
    point_at_x = list(filter(lambda point: point[0] == x,combined_values))[0]
    return point_at_x[1]

x_values and y_values and y_actual(13, x_values, y_values) # 26.0
```
Write a function called **error**, that given a list of x_values, and a list of y_values, the values m and b of a regression line, and a value of x, returns the error at that x value. 

Remember  εi=yi−ŷ  
```python
def error(x_values, y_values, m, b, x):
    expected = (m*x + b)
    return y_actual(x, x_values, y_values) - expected

error(x_values, y_values, 1.7, 10, 13) # -6.099999999999994
```
Ok, so the function error_line_trace takes our dataset of x_values as the first argument and y_values as the second argument. It also takes in values of  m  and  b  as the next two arguments to represent the regression line we will calculate errors from. Finally, the last argument is the value  x  it is drawing an error for.

The return value is a dictionary that represents a trace, and looks like the following:

{'marker': {'color': 'red'},
 'mode': 'lines',
 'name': 'error at 120',
 'x': [120, 120],
 'y': [93.0, 214.0]}

The trace represents the error line above. The data in x and y represent the starting point and ending point of the error line. Note that the x value is the same for the starting and ending point, just as it is for each vertical line. It's just the y values that differ - representing the actual value and the expected value. The mode of the trace equals 'lines'.
```python
error_line_trace(x_values, y_values, m, b, x):
    y_hat = m*x + b
    y = y_actual(x, x_values, y_values)
    name = 'error at ' + str(x)
    return {'x': [x, x], 'y': [y, y_hat], 'mode': 'lines', 'marker': {'color': 'red'}, 'name': name}

error_at_120m = error_line_trace(x_values, y_values, 1.7, 10, 120)
```

## Calculating Residual Sum of Squares in Python:

Now write a function called **squared_error**, that given a value of x, returns the squared error at that x value.

```python
def squared_error(x_values, y_values, m, b, x):
    return error(x_values, y_values, m, b, x)**2
    pass

x_values and y_values and squared_error(x_values, y_values, 1.7, 10, x_values[0]) # 37.20999999999993
```
Now write a function that will iterate through the x and y values to create a list of **squared_errors** at each point,  (xi,yi) of the dataset.
```python
def squared_errors(x_values, y_values, m, b):
    return list(map(lambda x: squared_error(x_values, y_values, m, b, x), x_values))
    pass
# Note that this differs from above sqaured_error function in that it uses that function and iterates through each point of the dataset.

x_values and y_values and squared_errors(x_values, y_values, 1.7, 10)
```
Next, write a function called **residual_sum_squares** that, provided a list of x_values, y_values, and the m and b values of a regression line, returns the sum of the squared error for the movies in our dataset.
```python
def residual_sum_squares(x_values, y_values, m, b):
    return sum(squared_errors(x_values, y_values, m, b))
    pass
# Note that this function takes the sum of all the sqaured errors from the previous function.

residual_sum_squares(x_values, y_values, 1.7, 10) # 327612.2800000001
```
Finally, write a function called **root_mean_squared_error** that calculates the RMSE for the movies in the dataset, provided the same parameters as RSS. 

Remember that root_mean_squared_error is a way for us to measure the **approximate error per data point**.
```python
import math
def root_mean_squared_error(x_values, y_values, m, b):
    return math.sqrt(residual_sum_squares(x_values, y_values, m, b)/len(x_values))

root_mean_squared_error(x_values, y_values, 1.7, 10) # 104.50076235766578
```
That is it! You have calculted the RSS!

## More Functions - for RSS

Note that we can represent multiple regression lines by a list of m and b values:
```python
regression_lines = [(1.7, 10), (1.9, 20)]
```
Then we can return a list of the regression lines along with the associated RMSE.
```python
def root_mean_squared_errors(x_values, y_values, regression_lines):
    errors = []
    for regression_line in regression_lines:
        error = root_mean_squared_error(x_values, y_values, regression_line[0], regression_line[1])
        errors.append([regression_line[0], regression_line[1], round(error, 0)])
    return errors
```
Now let's generate the RMSE values for each of these lines.
```python
x_values and y_values and root_mean_squared_errors(x_values, y_values, regression_lines)

[[1.7, 10, 105.0], [1.9, 20, 120.0]]
```
1. function called **trace_rmse**, that builds a bar chart displaying the value of the RMSE. 

The return value is a dictionary with keys of x and y, both which point to lists. The  x  key points to a list with one element, a string containing each regression line's m and b value. The  y  key points to a list of the RMSE values for each corresponding regression line.
```python
import plotly.graph_objs as go

def trace_rmse(x_values, y_values, regression_lines):
    errors = root_mean_squared_errors(x_values, y_values, regression_lines)
    x_values_bar = list(map(lambda error: 'm: ' + str(error[0]) + ' b: ' + str(error[1]), errors))
    y_values_bar = list(map(lambda error: error[-1], errors))
    return dict(
        x=x_values_bar,
        y=y_values_bar,
        type='bar'
    )


x_values and y_values and trace_rmse(x_values, y_values, regression_lines)
```
Once this is built, we can create a subplot showing the two regression lines, as well as the related RMSE for each line.
```python
import plotly
from plotly.offline import iplot
from plotly import tools
import plotly.graph_objs as go

def regression_and_rss(scatter_trace, regression_traces, rss_calc_trace):
    fig = tools.make_subplots(rows=1, cols=2)
    for reg_trace in regression_traces:
        fig.append_trace(reg_trace, 1, 1)
    fig.append_trace(scatter_trace, 1, 1)
    fig.append_trace(rss_calc_trace, 1, 2)
    iplot(fig)
```
AND...
```python
### add more regression lines here, by adding new elements to the list
regression_lines = [(1.7, 10), (1, 50)]

if x_values and y_values:
    regression_traces = list(map(lambda line: m_b_trace(line[0], line[1], x_values, name='m:' + str(line[0]) + 'b: ' + str(line[1])), regression_lines))

    scatter_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    rmse_calc_trace = trace_rmse(x_values, y_values, regression_lines)

    regression_and_rss(scatter_trace, regression_traces, rmse_calc_trace)
```
In the plot shown with this function, we can see above, the second line (m: 1.0, b: 50) has the lower RMSE. 

We thus can conclude that the second line "fits" our set of movie data better than the first line. Ultimately, **our goal will be to choose the regression line with the lowest RSME or RSS**. We will learn how to accomplish this goal in the following lessons and labs.

# Gradient Descent

## First reviewing RSS and RSME:

Difference etween RSS, TSS, ESS explained: https://www.youtube.com/watch?v=I8cRj0wefi8

First:

Evaluate the regression line again by first displaying errors in the graph:
```python
def y_actual(x, x_values, y_values):
    combined_values = list(zip(x_values, y_values))
    point_at_x = list(filter(lambda point: point[0] == x,combined_values))[0]
    return point_at_x[1]

def error_line_trace(x_values, y_values, m, b, x):
    y_hat = m*x + b
    y = y_actual(x, x_values, y_values)
    name = 'error at ' + str(x)
    error_value = y - y_hat
    return {'x': [x, x], 'y': [y, y_hat], 'mode': 'lines', 'marker': {'color': 'red'}, 'name': name, 'text': [error_value], 'textposition':'top right'}

def error_line_traces(x_values, y_values, m, b):
    return list(map(lambda x_value: error_line_trace(x_values, y_values, m, b, x_value), x_values))

errors = error_line_traces(budgets, revenues, 1.417, 133.33)
plot([scatter_trace, regression_trace, *errors])
```
From there, we calculate the **residual sum of squared errors** and the **root mean squared error**:
```python
import math
def error(x_values, y_values, m, b, x):
    expected = (m*x + b)
    return (y_actual(x, x_values, y_values) - expected)

def squared_error(x_values, y_values, m, b, x):
    return round(error(x_values, y_values, m, b, x)**2, 2)

def squared_errors(x_values, y_values, m, b):
    return list(map(lambda x: squared_error(x_values, y_values, m, b, x), x_values))

def residual_sum_squares(x_values, y_values, m, b):
    return round(sum(squared_errors(x_values, y_values, m, b)), 2)

def root_mean_squared_error(x_values, y_values, m, b):
    return round(math.sqrt(sum(squared_errors(x_values, y_values, m, b))/len(x_values)), 2)

squared_errors(budgets, revenues, 1.417, 133.33) #[0.0, 13625.89, 3896.26, 4741.01, 0.02]
residual_sum_squares(budgets, revenues, 1.417, 133.33) # 22263.18
root_mean_squared_error(budgets, revenues, 1.417, 133.33) # 66.73
```
## Best Fit Line - Moving towards gradient descent

Now that we have the residual sum of squares function to evaluate the accuracy of our regression line, we can simply try out different regression lines and use the regression line that has the lowest RSS. 

The regression line that produces the lowest RSS for a given dataset is called the **"best fit" line** for that dataset.

So this will be our technique for finding our "best fit" line:

1. Choose a regression line with a guess of values for  m  and  b 
2. Calculate the RSS
3. Adjust  m  and  b , as these are the only things that can vary in a single-variable regression line.
4. Again calculate the RSS
5. Repeat this process
6. The regression line (that is, the values of  b  and  m ) with the **smallest RSS is our best fit line**!

We'll eventually tweak and improve upon that process, but for now it will do. 

In fact, we will make things even easier at first by holding  m  fixed to a constant value while we experiment with different  b  values. In later lessons, we will change both variables.

**Updating the regression line to improve accuracy**

Ok, so we have a regression line of  ŷ =mx+b, and we started with values of  m=1.417  and  b=133.33. 

Then seeing how well this regression line matched our dataset, we calculated that  RSS=22,263.18. 

Our next step is to plug in different values of  b  and see how RSS changes. Let's try  b  = 140 instead of  133.33.
```python
residual_sum_squares(budgets, revenues, 1.417, 140)
#output
24130.78
```
Now let's the RSS for a **variety of  b  values**:
```python
def residual_sum_squares_errors(x_values, y_values, regression_lines):
    errors = []
    for regression_line in regression_lines:
        error = residual_sum_squares(x_values, y_values, regression_line[0], regression_line[1])
        errors.append([regression_line[0], regression_line[1], round(error, 0)])
    return errors

b_values = list(range(70, 150, 10))

m_values = [1.417]*8
regression_lines = list(zip(m_values, b_values))
regression_lines

#output
[(1.417, 70),
 (1.417, 80),
 (1.417, 90),
 (1.417, 100),
 (1.417, 110),
 (1.417, 120),
 (1.417, 130),
 (1.417, 140)]

 rss_lines = residual_sum_squares_errors(budgets, revenues, regression_lines)
rss_lines
#output
[[1.417, 70, 26696.0],
 [1.417, 80, 23330.0],
 [1.417, 90, 20963.0],
 [1.417, 100, 19597.0],
 [1.417, 110, 19230.0],
 [1.417, 120, 19864.0],
 [1.417, 130, 21497.0],
 [1.417, 140, 24131.0]]
```
(These values were added to a chart). While keeping our value of  m  fixed at 1.417, we moved towards a smaller residual sum of squares (RSS) by changing our value of  b , our y-intercept.

**Important!** Setting  b  to 130 produced a lower error than at 140. We kept moving our  bb  value lower until we set  b  = 100, at which point our error began to increase. 

Therefore, we know that a value of  b  between 110 and 100 produces the smallest RSS for our data while  m=1.417.

This changing output of RSS based on a changing input of different regression lines is called our **cost function**. Let's plot this chart to see it better.

## Cost Function, or Cost Curve
We set:

1. b_values as the input values (x values)
2. rss_errors as the output values (y values)

```python
b_values = list(range(70, 150, 10))

# remember that each element in rss_lines has the m value, b value, and related rss error
# rss_lines[0] => [1.417, 70, 26696.0]
# so we collect the rss errors for each regression line  
rss_errors = list(map(lambda line: line[-1], rss_lines))
```
Plot it!
```python
import plotly
from plotly.offline import init_notebook_mode, iplot
from graph import m_b_trace, trace_values, plot
init_notebook_mode(connected=True)


cost_curve_trace = trace_values(b_values, rss_errors, mode="lines")
plot([cost_curve_trace])
```
The graph created above is called the **cost curve**. It is a plot of the RSS for different values of  b. 

The curve demonstrates that when  b  is between 100 and 120, the RSS is lowest. This technique of optimizing towards a minimum value is called **gradient descent**. 

Here, we descend along a cost curve. As we change our variable, we need to stop when the value of our RSS no longer decreases.

## Gradient Descent Step Sizes

Summary explanation of Gradient Descent:

1. We quantify the accuracy of the regression line by squaring all of the errors (to eliminate negative values) and adding these squares together to get our residual sum of squares (RSS).

2. Armed with a number that describes the line's accuracy (or goodness of fit), we iteratively try new regression lines by adjusting our y-intercept value,  b , or slope value,  m , and then comparing these RSS values. 

3. By finding the values  m  and  b  that minimize the RSS, we can find our "best fit line".

In our cost function below, you can see the sequential values of  b  and the related RSS values (given a constant value  m ).

```python
#Cost Curve
import plotly
from plotly.offline import init_notebook_mode, iplot
from graph import m_b_trace, trace_values, plot, build_layout
init_notebook_mode(connected=True)
b_values = list(range(70, 150, 10))
rss = [10852, 9690, 9128, 9166, 9804, 11042, 12880, 15318]

layout = build_layout(options = {'title': 'RSS with changes to y-intercept', 'xaxis': {'title': 'y-intercept value'}, 'yaxis': {'title': 'RSS'}})
cost_curve_trace = trace_values(b_values, rss, mode="lines")
plot([cost_curve_trace], layout)
```
** Thinking in 3 Dimensions**
So far, we have held one variable constant in order to experiment with the other. 

**We need an approach that will continue to work as we change both of the variables in our regression line.** 

Altering the second variable makes things far more complicated. Exploring both variables, the slope and the y-intercept, requires plotting the second variable along the horizontal axis and turning our graph into a three-dimensional representation. And in the future we'll be able to change more than just that.

Going forward, rather than arbitrarily changing our variables, as we have done by decrementing the y-intercept by 10 in the example above, we need to move carefully down the cost curve to be certain that our changes are reducing the RSS.

## Step Sizes - Step-by-step

We want an approach that lets us be certain that we're moving in the right direction with every change. Also, we want to know how much of a change to make to minimize RSS.

Let's call each of these changes a **step**, and the size of the change our **step size**.

1. **The slope of the cost curve tells us our step size**

    If the slope tilts downwards, then we should walk forward to approach the minimum.

    And if the slope tilts upwards, then we should point walk backwards to approach the minimum.

    The steeper the tilt, the further away we are from our cost curve's minimum, so we should take a larger step.

2. **Tangent Lines** - the line that just barely touches the curve at that point

    We can follow our technique with more precision by adding some numbers to our slope. 
    
    The slope of the curve at any given point is equal to the slope of the tangent line at that point.  

How it works:

We use the following procedure to find the ideal b :

Randomly choose a value of  b , and
Update  b  with the formula  

b=(−.1)∗slopeb=i+bi

The formula above tells us which  b  value to look at next. We start by choosing a random  b  value that we can plug into our formula. We take the slope of the curve at that  b  value and multiply it by  −.1  then add it to our original  b  value to produce our next  b  value.

As we can surmise, the larger the slope, the larger the resulting step to the next  b  value.

Here's an example. We randomly choose a  b  value of 70. Then:

b=70

b=(−.1)∗−146.17+70=14.61+70=84.61

b=(−.1)∗−58.51+85=5.851+85=90.85

b=(−.1)∗−21.07+90.85=90.851+2.11

**Learning Rate** - Notice that we don't update our values of  b  by just adding or subtracting the slope at that point. The reason we multiply the slope by a fraction like .1 is so that we avoid the risk of **overshooting the minimum.** 

This fraction is called the **learning rate**. Here, the fraction is negative because we always want to move in the opposite direction of the slope. 

When the slope of the cost curve points downwards, we want to move to a higher y-intercept. Conversely, when we are on the right side of the curve and the slope is rising, we want to move backwards to a lower y-intercept.

**Note** This technique is pretty magical. By looking at the tangent line at each point, we no longer are changing our  b  value and just hoping that it has the correct impact on our RSS. 

This is because, for one, the slope of the tangent line points us in the right direction. And as you can see above, our technique properly adjusts the amount to change the  b  value  without even knowing the ideal  b  value. When our  b  was far away from the ideal  b  value, our formula increased  b  by over 14. By the third step, we were updating our  b  value by only 2 because we were closer to the ideal slope for minimizing the RSS.

HERE is a good link to how RMSE is calculated:
https://www.freecodecamp.org/news/machine-learning-mean-squared-error-regression-line-c7dde9a26b93/


## Gradient Descent Steps LAB

1. Setting up initial regression line:

Dictionary with info on movies:
```python
first_show = {'budget': 100, 'revenue': 275}
second_show = {'budget': 200, 'revenue': 300}
third_show = {'budget': 400, 'revenue': 700}

shows = [first_show, second_show, third_show]
```
Start with some values for an initial not-so-accurate regression line,  

y=.6x+133.33
```python
from linear_equations import build_regression_line

#Assign variables to lists from the dictionary above

budgets = list(map(lambda show: show['budget'], shows))
revenues = list(map(lambda show: show['revenue'], shows))

#Provide the regression equation function:
def regression_line(x):
    return .6*x + 133.33
```
Using the residual_sum_squares function we calculate the RSS to measure the accuracy of the regression line to our data. Let's take another look at that function:
```python
#Here is the function for the squared error of a single data point
def squared_error(x, y, m, b):
    return (y - (m*x + b))**2

#Here is the function for the squared error of multiple data points. In the mathematical equation, RSS is the sum of the true values of Y minus the fitted values of Y, representing what is 'left over' from our best fit model and the actual data points.

def residual_sum_squares(x_values, y_values, m, b):
    data_points = list(zip(x_values, y_values))
    squared_errors = map(lambda data_point: squared_error(data_point[0], data_point[1], m, b), data_points)
    return sum(squared_errors)
```
Now we plot this:
```python
from plotly.offline import iplot, init_notebook_mode
from graph import plot, m_b_trace
import plotly.graph_objs as go

init_notebook_mode(connected=True)

from graph import trace_values, plot

data_trace = trace_values(budgets, revenues)
regression_trace = m_b_trace(.6, 133.33, budgets)
plot([data_trace, regression_trace])
```
## Building a cost curve:

Now let's use the **residual_sum_squares** function to build a cost curve. Keeping the  b  value fixed at  133.33 , write a function called **rss_values**.

1. rss_values passes our dataset with the x_values and y_values arguments.
2. It also takes a list of values of  mm , and an initial  bb  value as arguments.
3. It outputs a dictionary with keys of m_values and rss_values, with each key pointing to a list of the corresponding values.

```python
#First import the residual_sum_squares
from error import residual_sum_squares

#Function uses the RSS equation and iterates across all values:
def rss_values(x_values, y_values, m_values, b):
    rss_values = list(map(lambda m_value:residual_sum_squares(x_values, y_values, m_value, b), m_values))
    return {'m_values':m_values,'rss_values':rss_values}
```
In this case, the function is called like so:
```python
#Variables first, from above:
budgets = list(map(lambda show: show['budget'] ,shows))
revenues = list(map(lambda show: show['revenue'] ,shows))

#Scaling the m-values:
initial_m_values = list(range(8, 19, 1))
scaled_m_values = list(map(lambda initial_m_value: initial_m_value/10,initial_m_values))

#B stays the same becasue it is the y-intercept which is constant.
b_value = 133.33

#Finally, calling the function we just wrote with the above value lists:
rss_values(budgets, revenues, scaled_m_values, b_value)

# {'m_values': [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],
#  'rss_values': [64693.76669999998,
#   45559.96669999998,
#   30626.166699999987,
#   19892.36669999999,
#   13358.5667,
#   11024.766700000004,
#   12890.96670000001,
#   18957.166700000016,
#   29223.36670000002,
#   43689.566700000025,
#   62355.76670000004]}
```
From here it can be plotted and made into a table to help calculate gradient descent:


## Looking at the slope of our cost curve

In this section, we'll work up to building a gradient descent function that **automatically changes our step size**. 

To get you started, we'll provide a function called slope_at that calculates the slope of the cost curve at a given point on the cost curve. Here it is in action:

```python
from helper import slope_at

slope_at(budgets, revenues, .6, 133.33333333333326)

slope_at(budgets, revenues, 1.6, 133.33333333333326)
```
So the slope_at function takes in our dataset, and returns the slope of the cost curve at that point.

So now let's write a function called **updated_m**. 

The function will tell us the step size and direction to move along our cost curve. The updated_m function takes as arguments an initial value of  m , a learning rate, and the slope of the cost curve at that value of  m . Its return value is the next value of m that it calculates.

```python
from error import residual_sum_squares

# I couldnt quite find an equivalent mathimatical formula to go along with this function. Should revisit.
def updated_m(m, learning_rate, cost_curve_slope):
    change_to_m = -1 * learning_rate * cost_curve_slope
    return change_to_m + m
```
This is what our function returns.
```python
current_slope = slope_at(budgets, revenues, 1.7, 133.33333333333326)['slope']
updated_m(1.7, .000001, current_slope)
# 1.5343123333335096

current_slope = slope_at(budgets, revenues, 1.534, 133.33333333333326)['slope']
updated_m(1.534, .000001, current_slope)
# 1.43803233333338

current_slope = slope_at(budgets, revenues, 1.438, 133.33333333333326)['slope']
updated_m(1.438, .000001, current_slope)
# 1.3823523333332086
```
## Gradient Descent Function

Now let's write another function called gradient_descent. 


1.  The inputs of the function are x_values, y_values, steps, the b we are holding constant, the learning_rate, and the current_m that we are looking at. 
2. The steps arguments represents the number of steps the function will take before the function stops. 
3. We can get a sense of the return value in the cell below. It is a list of dictionaries, with each dictionary having a key of the current m value, the slope of the cost curve at that m value, and the rss at that m value.
```python
def gradient_descent(x_values, y_values, steps, b, learning_rate, current_m):
    cost_curve = []
    for item in range(steps):
        current_cost_slope = slope_at(x_values, y_values, current_m, b)['slope']
        current_rss = residual_sum_squares(x_values, y_values, current_m, b)
        cost_curve.append({'m': current_m, 'rss': current_rss, 'slope': current_slope})
        current_m = updated_m(current_m, learning_rate, current_cost_slope) 
    return cost_curve

#output
descent_steps = gradient_descent(budgets, revenues, 12, 133.33, learning_rate = .000001, current_m = 0)
descent_steps
```
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