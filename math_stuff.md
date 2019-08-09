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

**Derivatives** are a specific kind of rate of change -- the rate of change of a function at a given point.

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

In summation, that is the derivative of a line, or the rate of change of a linear function. The rate of change answers how much is our output changing at a given point.
