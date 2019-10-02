
# Gradient Descent with Partial Derivatives

## Gradient ASCENT

Here in finding gradient ascent, our task is not to calculate the gain from a move in either the  x  or  y  direction. Instead our task is to find some combination of a change in  x , y  that brings the largest change in output.

**Calculating the gradient using Partial Derivatives**

As we know, the partial derivative  df/dx calculates the change in output from moving a little bit in the  x  direction, and the partial derivative  df/dy  calculates the change in output from moving in the  y  direction. 

Because with gradient ascent our goal is to make a nudge in  x,y  that produces the **greatest change in output, if  df/dy>df/dx** , we should make that move more in the  y  direction than the  x  direction, and vice versa

## Derivative Chain Rule

 Chain Rule allows us to see how a function's output changes as we change a variable that the function does not directly depend on.

 Start with the function:

 f(x)=(0.5x+3)^2

 **Step 1: Break the function down**

g(x)=0.5x+3 

```python
#We call  f(x)  the outer function, and  g(x)  the inner function.

def g_of_x(x):
    return 0.5*x + 3
```
f(x)=(g(x))^2

```python
def f_of_x(x): #outer function
    return (g_of_x(x))**2 #inner function
```
**Step 2: Take the derivatives of those functions**

Start with the inner function, and use the power rule:

g(x)=0.5x+3

g′(x)= 1∗0.5x^0+0 = **0.5**

Then take the derivative of the outer function. Not that it's derivative does not tie to change in x or y, but to change in the inner function
, whose output depends on x:

  f′g((x)) = 2∗(g(x))^1 = 2∗g(x)

**Step 3: Apply the chain rule!**

**The chain rule**: In taking the derivative,  df/dx  of an outer function,  f(x), which depends on an inner function g(x), which depends on x, **the derivative equals the derivative of the outer function times the derivative of the inner function.**

f′(g(x)) = f′g(x) ∗ g′(x)

Then substituting for  g(x) , which we already defined, we have:

f′(g(x)) = g(x) = 0.5x+3

So the derivative of the function f(x)=(0.5x+3)^2
is: **f′(x) =0.5x+3**

Summary: 

Remember that The chain rule is allows us to determine the rate of change of a function that does not directly depend on a variable,  x , but rather depends on a separate function that depends on  x .

Remember, taking a derivative means changing a variable  x  a little, and seeing the change in the output. The chain rule allows us to solve the problem of seeing the change in output when our function does not directly depend on that changing variable, but depends on a function that depends on a variable.

We can take the derivative of a function that indirectly depends on  x , by taking the derivative of the outer function and multiplying it by the derivative of the inner function.

One more example:

f(x)=(3x2+10x)^3

1. Divide the function into two components

Inner:
g(x)=3x^2+10x

Outer: 
f(x)=(g(x))^3

2. Take the derivative of each of the component functions

g′(x)=6x+10
 
f′(x)=3(g(x))^2

Substitution

f′(x)=f′(g(x))∗g′(x)=3(g(x))2∗(6x+10)
 
Then substituting in  g(x) = 3x^2+10x we have:

f′(x) = 3 ∗ (3x^2+10x)^2 ∗ (6x+10)


## Gradient to Cost Function

In the previous lessons:
1. We saw that the gradient of a function was a combination of our partial derivatives with respect to each variable of that function. 

2. We saw the process of gradient descent involves moving in the negative direction of the gradient. For example, if the direction of ascent of a function is a move up and to the right, the descent is down and to the left. 

In this lesson we will apply gradient descent to our cost function to see how we can move toward a best fit regression line by changing the variables of  m  and  b .

**RSS Review:**

RSS takes the difference between  mxi+b, which is  yi^  (the  yi value our regression line predicts), and our actual  yi , represented by the length of the red lines. Then we square this difference, and sum up these squares for each piece of data in our dataset. That is the residual sum of squares.

**Calculating the Gradient of a Cost Function:**

Now that we are applying gradient descent to our cost curve  J(m,b) , the technique should answer how much to move the  mm  variable and the  bb  variable to produce the greatest decrease in cost, or RSS. 

In other words, when altering our regression line, we want to know how much of this change should be derived from a move in the slope versus how much should be derived from a change in the y-intercept.

## Gradient Descent of Cost Function Equations

We want to our partial derivatives of the following:
```python
∂J/∂m J(m,b) = ∂J/∂m(y−(mx+b))^2
 ```
 AND
 ```python
∂J/∂b J(m,b) = ∂J/∂b(y−(mx+b))^2
```
**We start by taking the partial derivative of the first, with resepct to (m):**

∂J/∂m J(m,b) = ∂J/∂m(y−(mx+b))^2

1. Break it into:
```python
g(m,b) = y−(mx+b)

J(g(m,b)) = (g(m,b))^2
```
2. Use the chain rule to find the partial derivative with respect to a change in the slope:
```python
∂J/∂mJ(g) = ∂J/∂g J(g(m,b)) ∗ ∂g/∂m g(m,b)
```
3.  Solve these derivatives individually
```python
∂J/∂g J(g(m,b)) = ∂J/∂g g(m,b)2 = 2∗g(m,b)

∂g/∂m g(m,b) = ∂g/∂m (y−(mx+b)) = ∂g/∂m y−∂g/∂m mx−∂/g∂ mb = −x
```
4. Now plugging these back into our chain rule we have:
```python
∂J∂gJ(g(m,b))∗∂g∂mg(m,b)=(2∗g(m,b))∗−x=2∗(y−(mx+b))∗−x

∂J/∂m J(m,b) =2∗(y−(mx+b))∗−x=−2x∗(y−(mx+b))
```
**Now, we take the partial derivative of the second equation, with respect to y-intercept:**
```python
∂J/∂b J(m,b) = ∂J/∂b(y−(mx+b))^2
```
1. Break into two functions:
```python
g(m,b)=y−(mx+b)

J(g(m,b))=(g(m,b))^2

```
2. Apply chain rule, to this same function composition, we get:

```python
∂J/∂bJ (g(m,b)) = ∂J/∂g J(g(m,b)) ∗ ∂g/∂bg(m,b)
```
3. Calculate these partial derivatives individually.

From our earlier calculation of the partial derivative, we know that:
```python
 ∂J/∂g J(g(m,b)) = ∂J/∂g g(m,b)^2 = 2∗g(m,b)
 ```
 The only thing left to calculate is 
 ```python
 ∂g/∂b g(m,b)

∂g/∂bg(m,b) = ∂g/∂b(y−(mx+b)) = −1
```
4. Now we plug our terms into our chain rule and get:
```python
∂J/∂g J(g) ∗ ∂g/∂bg(m,b) = 2∗g(m,b)∗−1 = −2∗(y−(mx+b))
```
**Using both of our partial derivatives for gradient descent**

Now we have our two partial derivatives for  
```python
∇J(m,b) :

#partial derivative 'm'
∂J/∂m J(m,b) = −2∗x(y−(mx+b))

#partial derviative 'b'
∂J/∂b J(m,b) = −2∗(y−(mx+b))

#Since 'mx+b' is just the regression line, and error = actual - expected, we can replace  y−ŷ  with  'ϵ' , our error. These can also be expressed like this:

∂J/∂m J(m,b) = −2∗x(y−ŷ) = −2x∗ϵ

∂J/∂b J(m,b) = −2∗(y−ŷ) = −2ϵ

# Since -2 is constant it can stay outside
```

In the context of gradient descent, we use these partial derivatives to take a step size. Remember that our step should be in the opposite direction of our partial derivatives as we are descending towards the minimum. So to take a step towards gradient descent we use the general formula of:
```python
current_m = old_m  −∂J/∂mJ(m,b)

current_b = old_b  −∂J/∂bJ(m,b)
```
## Applying Gradient Descent to Code

Starting with data:

```python
# our data
first_show = {'x': 30, 'y': 45}
second_show = {'x': 40, 'y': 60}
third_show = {'x': 100, 'y': 150}

shows = [first_show, second_show, third_show]
```
Now we set our initial regression line by initializing  m  and  b  to zero. 

Then to update our regression line, we iterate through each of the points in the dataset, and at each iteration, 

change our **update_to_b** by  2∗ϵ  

and 

change our **update_to_m** by  2∗x∗ϵ 

```python
# initial variables of our regression line
b_current = 0
m_current = 0

# amount to update our variables for our next step
update_to_b = 0
update_to_m = 0 

#We define a function called error_at, which we can use in the error component of our partial derivatives above.
def error_at(point, b, m):
    return (m*point['x'] + b - point['y'])

for i in range(0, len(shows)):
    update_to_b += -2*(error_at(shows[i], b_current, m_current))
    update_to_m += -2*(error_at(shows[i], b_current, m_current)*shows[i]['x'])

# We calculate our new_b and new_m values by updating our current values and adding our respective updates.
new_b = b_current - update_to_b
new_m = m_current - update_to_m

```
Remember:  The code above represents **just one** update to our regression line and, therefore, **just one step towards our best fit line**. 

We'll just repeat the process to take multiple steps. 

**Making some tweaks to our equations!**

1. Tweak 1:  **Apply Learning Rate!** Think about what it means to change each of our  m  and  b  variables by at least the sum of all of the errors (the  yi  values that our regression line predicts and our actual data). That would be an enormous change!

 To ensure that we do not drastically update our regression line after each step, we **multiply each of these partial derivatives by a learning rate**. 
 
 As we have seen before, the learning rate is just a small number, like  0.0001, which **controls how large our updates to the regression line will be**. 
 
 The learning rate is represented by the Greek letter eta,  η , or alpha  α . We'll use eta, so  η=0.0001 means the learning rate is  0.0001.

**Just make sure to update BOTH partial derivatives with the SAME learning rate!**

```python
#amount to update our variables for our next step
update_to_b = 0
update_to_m = 0 

#applying the learning rate!
learning_rate = .0001
n = len(shows)

for i in range(0, n):  
    update_to_b += -(1/n)*(error_at(shows[i], b_current, m_current))
    update_to_m += -(1/n)*(error_at(shows[i], b_current, m_current)*shows[i]['x'])

#Update the current b and m values with the new learning rate.
new_b = b_current - (learning_rate*update_to_b)
new_m = m_current - (learning_rate*update_to_m)
```
Putting the step_gradient formula into action, with the movie data set from above!

```python
#Here's that movie data recreated
first_show = {'x': 30, 'y': 45}
second_show = {'x': 40, 'y': 60}
third_show = {'x': 100, 'y': 150}

shows = [first_show, second_show, third_show]

#Defining the step_gradient function. Remember all code below is within the function!

def step_gradient(b_current, m_current, points):
    b_gradient = 0 
    m_gradient = 0
    learning_rate = .0001
    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i]['x']
        y = points[i]['y']
        b_gradient += -(1/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(1/N) * x * (y - ((m_current * x) + b_current))

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return {'b': new_b, 'm': new_m}

#We begin by setting  b and  m  to 0, 0. Then from our step_gradient function, we receive new values of  b  and  m  of .0085 and .6245 in the output below when the function is called.

b = 0
m = 0

step_gradient(b, m, shows) 
# {'b': 0.0085, 'm': 0.6249999999999999}
```
Now what we need to do is take another step in the correct direction by calling our step gradient function with our updated values of b and  m!
```python
#Call the function again using those updated b and m values to take the next step:

updated_b = 0.0085
updated_m = 0.6249

step_gradient(updated_b, updated_m, shows) 
# {'b': 0.01345805, 'm': 0.9894768333333332}
```
Now, do it 10 more times to take ten more steps using a for loop!

```python
# set our initial step with m and b values, and the corresponding error.
b = 0
m = 0
iterations = []
for i in range(10): #range is how you tell it to do 10 more iterations
    iteration = step_gradient(b, m, shows)
    # {'b': value, 'm': value}
    b = iteration['b']
    m = iteration['m']
    # update values of b and m
    iterations.append(iteration) #onto the empty iteration list called above the for loop.

#Now, it cycles through and creates the list of new steps below:
iterations
[{'b': 0.0085, 'm': 0.6249999999999999},
 {'b': 0.013457483333333336, 'm': 0.9895351666666665},
 {'b': 0.016348771640555558, 'm': 1.20215258815},
 {'b': 0.018034938763874835, 'm': 1.3261630333815368},
 {'b': 0.01901821141416974, 'm': 1.398492904819568},
 {'b': 0.019591516465717437, 'm': 1.4406797579467343},
 {'b': 0.019925705352372706, 'm': 1.4652855068756228},
 {'b': 0.020120428242875608, 'm': 1.4796369666804499},
 {'b': 0.02023380672219544, 'm': 1.4880075481368862},
 {'b': 0.020299740568747532, 'm': 1.4928897448417577}]
```
As you can see, our  m  and  b  values both update with each step. Not only that, but with each step, the size of the changes to  m  and  b  decrease. This is because they are approaching a best fit line!

## Visualizing with Plotly
```python
def to_line(m, b):
    initial_x = 0
    ending_x = 100
    initial_y = m*initial_x + b
    ending_y = m*ending_x + b
    return {'data': [{'x': [initial_x, ending_x], 'y': [initial_y, ending_y]}]}

frames = list(map(lambda iteration: to_line(iteration['m'], iteration['b']),iterations))
frames[0]
#Ouput
{'data': [{'x': [0, 100], 'y': [0.0085, 62.508499999999984]}]}
```
Now we can see how our regression line changes, and approaches a better model of our data, with each iteration using an animation!
```python
#YIKES

from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

init_notebook_mode(connected=True)

x_values_of_shows = list(map(lambda show: show['x'], shows))
y_values_of_shows = list(map(lambda show: show['y'], shows))
figure = {'data': [{'x': [0], 'y': [0]}, {'x': x_values_of_shows, 'y': y_values_of_shows, 'mode': 'markers'}],
          'layout': {'xaxis': {'range': [0, 110], 'autorange': False},
                     'yaxis': {'range': [0,160], 'autorange': False},
                     'title': 'Regression Line',
                     'updatemenus': [{'type': 'buttons',
                                      'buttons': [{'label': 'Play',
                                                   'method': 'animate',
                                                   'args': [None]}]}]
                    },
          'frames': frames}
iplot(figure)
```
# Applying Gradient Descent LAB

This is our task: We are an employee for Good Lion Studios. For Good Lion, our job is first to gather, explore, and format our data so that we can build a regression line of this data. Then we will work through various attempts of building out these regression lines. By the end of this lab, we should have a working version that we can proudly show to our manager.

We will have access to functions in the error, graph and linear equations libraries that we previously wrote.

Learning Objectives:
1. Review how to use built-in functions, like filter and map, to clean data
2. Evaluate the quality of regression lines using Residual Sum of Squares (RSS)
3. Review how RSS changes with varying values of the slope and y-intercept of a regression line
4. Implement gradient descent to find a "best fit" regression line

## Retreive the data:
```python
import pandas

def parse_file(fileName):
    movies_df = pandas.read_csv(fileName)
    return movies_df.to_dict('records')

movies = parse_file('https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv')

type(movies) # list
len(movies) # 1794
```
## Explore the data:
```python
movies[0]

{'year': 2013,
 'imdb': 'tt1711425',
 'title': '21 &amp; Over',
 'test': 'notalk',
 'clean_test': 'notalk',
 'binary': 'FAIL',
 'budget': 13000000,
 'domgross': 25682380.0,
 'intgross': 42195766.0,
 'code': '2013FAIL',
 'budget_2013$': 13000000,
 'domgross_2013$': 25682380.0,
 'intgross_2013$': 42195766.0,
 'period code': 1.0,
 'decade code': 1.0}
 ```
 Here we can see the data available for each movie. The information most relevant for our task is:

1. **budget_2013** is the budget adjusted for inflation in 2013 dollars
2. **domgross_2013** is the domestic revenue adjusted for inflation in 2013 dollars
3. **intgross_2013** is the international revenue adjusted for inflation in 2013 dollars

## Clean the Data

### Handle missing data
Look at the values associated with these attributes. The first movie looks good since it has nice data for each of these attributes, but this is likely not the case for all movies in the set.

Let's remove the movies whose domgross_2013 points to values of __nan__, which stands for "not a number", which means this data is missing. There are only a few pieces of missing data here, so we can safely remove these movies without causing too much damage.
```python
import math
list(filter(lambda movie: math.isnan(movie['domgross_2013$']), movies))
```
Write a function called remove_movies_missing_data that returns the subset of movies that don't have **nan**.
```python
import math

def remove_movies_missing_data(movies):
    return [movie for movie in movies if not math.isnan(movie['domgross_2013$'])]

parsed_movies = remove_movies_missing_data(movies) or []

```
Now check number of movies in the pared down list:
```python
len(parsed_movies) 
# 1776
```
Check that no movies with a domgross_2013 value of nan are included.
```python
list(filter(lambda movie: math.isnan(movie['domgross_2013$']),parsed_movies)) 
# []
```


### Changing the Scale of the Data

In this example, the movie budgets are saved as very large numbers - in the millions!

```python
movies[0]['budget']
13000000
```
To make the data more manageable, we need to scale the data.

To make things simpler, let's divide both our budget and revenue numbers for each movie by 1 million. It will make some of our future calculations easier to interpret. The attributes that we can scale down are budget, budget_2013$, domgross, domgross_2013$, intgross, and intgross_2013$.
```python
def scale_down_movie(movie):
    movie_copy = dict(movie)    
    movie_copy.update({'budget': round(movie['budget']/1000000, 2), 'budget_2013$': round(movie['budget_2013$']/1000000, 2), 
                       'intgross': round(movie['intgross']/1000000, 2), 'intgross_2013$': round(movie['intgross_2013$']/1000000, 2),
                       'domgross': round(movie['domgross']/1000000, 2), 'domgross_2013$': round(movie['domgross_2013$']/1000000, 2)
                      })
                      #Each key in the movie dictionary is divided by 100000 and rounded, and added to the new dictionary movie_copy
    return movie_copy
```
Test it:
```python

movies[0]
{'year': 2013,
 'imdb': 'tt1711425',
 'title': '21 &amp; Over',
 'test': 'notalk',
 'clean_test': 'notalk',
 'binary': 'FAIL',
 'budget': 13000000,
 'domgross': 25682380.0,
 'intgross': 42195766.0,
 'code': '2013FAIL',
 'budget_2013$': 13000000,
 'domgross_2013$': 25682380.0,
 'intgross_2013$': 42195766.0,
 'period code': 1.0,
 'decade code': 1.0}

 scale_down_movie(movies[0])

 {'year': 2013,
 'imdb': 'tt1711425',
 'title': '21 &amp; Over',
 'test': 'notalk',
 'clean_test': 'notalk',
 'binary': 'FAIL',
 'budget': 13.0,
 'domgross': 25.68,
 'intgross': 42.2,
 'code': '2013FAIL',
 'budget_2013$': 13.0,
 'domgross_2013$': 25.68,
 'intgross_2013$': 42.2,
 'period code': 1.0,
 'decade code': 1.0}
 ```
Now that we have a function to scale down our movies, lets map through all of our parsed_movies to return a list of scaled_movies.

 ```python
 def scale_down_movies(movies):
    scaled_movies = list(map(lambda movie:scale_down_movie(movie), movies))
    return scaled_movies
    
```
Then, test it:
```python
first_ten_movies = parsed_movies[0:10]
first_ten_scaled = scale_down_movies(first_ten_movies) or []
first_ten_scaled[-2:]
```
It if works, you can move forward.

## Now we Plot the data!

To do so, set budget_2013$ as the  x  values, and the domgross_2013$ as the  y  values. 

Set the text of the trace equal to a list of the movie titles, so that we can see which movie is associated with each point. All of the data should be coming from our scaled_movies variable.

```python
budgets = list(map(lambda movie: movie['budget_2013$'], scaled_movies))
domestic_revenues = list(map(lambda movie: movie['domgross_2013$'], scaled_movies))
titles = list(map(lambda movie: movie['title'], scaled_movies))
```
Check the first ten values of the budgets, domestic_revenues, and titles lists, but your trace should have an element for each of the scaled_movies in the dataset.
```python
budgets[0:10]

domestic_revenues[0:10]

titles[0:10] 
#I havent included the output here, but you would want to check it.

```
Once we have lists of these values, we are ready to create a trace. The following code creates a trace with the x values set as the budgets, the y values set as the domestic_revenues, and the text set as each of the movie titles.

```python
from graph import trace_values
revenues_per_budgets_trace = trace_values(budgets, domestic_revenues, text = titles)

#Now we can Plot!
from graph import plot
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

plot([revenues_per_budgets_trace])
```
Check an outlying value using the __max__ function:

```python
def highest_domestic_gross(movies):
    return max(movies, key=lambda movie: movie['domgross_2013$'])

max_movie = highest_domestic_gross(scaled_movies) or {'title': 'some non movie'}
max_movie['title'] # 'Star Wars'
```
 Let's zoom in on our dataset so that our plot no longer expands for just a few of the outliers. 
 
 We will set the x-axis of our plot to go from zero to 300 million dollars, and the y-axis of our plot to go from zero to one billion dollars.
 ```python
 from graph import build_layout
revenues_per_budgets_trace = trace_values(budgets, domestic_revenues, text = titles)
revenues_layout = build_layout(x_range = [0, 300], y_range = [0, 1000])
plot([revenues_per_budgets_trace], revenues_layout)
```
## Building our models

Here is our starting equation, provided by an 'outside consultant':

R(x)=1.5∗budget+10

where  x is a movie's budget in 2013 dollars, and R(x) is the expected revenue in 2013 dollars.

Write a function called outside_consultant_predicted_revenue that, provided a budget, returns the expected revenue according to the outside consultant's formula.

```python
def outside_consultant_predicted_revenue(budget):
    return 1.5 * budget + 10
```
Plot it:
```python
budgets = list(map(lambda movie: movie['budget_2013$'], scaled_movies))
domestic_revenues = list(map(lambda movie: movie['domgross_2013$'], scaled_movies))
titles = list(map(lambda movie: movie['title'], scaled_movies))

consultant_estimated_revenues = list(map(lambda budget: outside_consultant_predicted_revenue(budget),budgets))
consultant_estimated_revenues_trace = trace_values(budgets, consultant_estimated_revenues, mode='lines', name = 'external consultant estimate')
```
then:
```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import trace_values, m_b_trace, plot

plot([revenues_per_budgets_trace, consultant_estimated_revenues_trace], revenues_layout)
```
## Calculate RSS

The line based on the model equation doesnt look too bad, but we should test it! can calculate the RSS to quantify how accurate his model really is.

Let's write a method called error_for_consultant_model which takes in a budget of a movie in our dataset, and returns the difference between the movie's gross domestic revenue in 2013 dollars, and the prediction from the consultant's model.

```python
#remember, error is calculated:
def error(x_values, y_values, m, b, x):
    expected = (m*x + b)
    return (y_actual(x, x_values, y_values) - expected)

#Again, here's mx+b according to the 'consultant's formula.
def outside_consultant_predicted_revenue(budget):
    return 1.5 * budget + 10

#So for this example, we want to plug in the movie budget into mx+b provided by the 'consultant's formula' and see how it compares to the real domestic gross, using the function for 'error'.
def error_for_consultant_model(movie):
    expected = outside_consultant_predicted_revenue(movie['budget_2013$'])
    return movie['domgross_2013$'] - expected
```
Now, test it out:
```python
american_hustle = {'binary': 'PASS', 'budget': 40.0, 'budget_2013$': 40.0, 'clean_test': 'ok',
         'code': '2013PASS', 'decade code': 1.0, 'domgross': 148.43, 'domgross_2013$': 148.43, 'imdb': 'tt1800241',
         'intgross': 249.48, 'intgross_2013$': 249.48, 'period code': 1.0, 'test': 'ok-disagree',
         'title': 'American Hustle', 'year': 2013}
error_for_consultant_model(american_hustle) # 78.43
```
Once we have written a formula that calculates the error for the consultant's model provided a budget, we can write a method that calculates the RSS for the consultant's model. W

hen we move on to compare our consultant's model with others, we'll then have a metric for comparison.

```python
#Here are the formulas for:
def squared_error(x_values, y_values, m, b, x):
    return round(error(x_values, y_values, m, b, x)**2, 2)

def squared_errors(x_values, y_values, m, b):
    return list(map(lambda x: squared_error(x_values, y_values, m, b, x), x_values))

def residual_sum_squares(x_values, y_values, m, b):
    return round(sum(squared_errors(x_values, y_values, m, b)), 2)

#To convert this situation into RSS. I dont really understand thow this works but here it is.

def rss_consultant(movies):
    return round(sum(list(map(lambda movie: error_for_consultant_model(movie)**2, movies))), 2)

rss_consultant(scaled_movies) 
# 23234357.68
```

We'll find out if this number is any good later, but for right now let's just say that our RSS is good enough. 

##Using the Deriviative Function for a New Model

Use the derivative to write a function that provided a budget, returns the  ΔR/Δx according to the consultant's model. 

Remember that our consultant's model is  R(x)=1.5x+10  where  x  is a budget, and  R(x)  is an expected revenue.

So the data scientist comes up with a new model, to indicate a movie's expected revenue is 1.5 million for every year after 1965 plus 1.1 times the movie's budget. Write a function called revenue_with_year that takes as arguments budget and year and returns expected revenue.
```python
def revenue_with_year(budget, year):
    return 1.1*budget + 1.5*(year-1965)

revenue_with_year(25, 1997) # 75.5
revenue_with_year(40, 1983) # 71.0
```

Although the internal consultant model isn't a line, it still seems to match our data fairly well. Let's find out how well. Even though it is not a line, we can still calculate the RSS for this model. Write a function called rss_revenue_with_year that returns the Residual Sum of Squares associated with the revenue_with_year model for the scaled_movies dataset. The squared_error_revenue_with_year function can be used to return the squared error of the model associated with just a single movie.
```python
def squared_error_revenue_with_year(movie):
    actual = movie['domgross_2013$']
    expected = revenue_with_year(movie['budget_2013$'], movie['year'])
    return (actual - expected)**2

def rss_revenue_with_year(movies):
    squared_errors = list(map(
        lambda movie: squared_error_revenue_with_year(movie), 
        movies))
    return round(sum(squared_errors), 2)

#The RSS here is  $25,364,329.23  as opposed to the RSS of  $23,234,357.68 from the external consultant's model. 
```
According to RSS, this model isn't as accurate as the previous model. Still, it isn't bad enough to ignore completely.

##Improving on the initial regression line

We have our dataset. Let's begin with an initial regression line that sets  b=0.5  and  m=1.79 .
```python
from linear_equations import build_regression_line
budgets = list(map(lambda movie: movie['budget_2013$'], scaled_movies)) or [1, 2]
domestic_revenues = list(map(lambda movie: movie['domgross_2013$'], scaled_movies)) or [1, 2]

initial_regression_line = {'b': 0.5, 'm': 1.79}
```
Using values for  mm  and  bb  from our initial regression line, we can write expected_revenue_per_budget that returns the expected revenue provided a budget.
```python
#Still not sure what the '1' at the end is here!
def expected_revenue_per_budget(budget):
    return round(budget*initial_regression_line['m'] + initial_regression_line['b'], 1)

budget = american_hustle['budget_2013$'] # 40.0
expected_revenue_per_budget(budget) # 72.1
```
Now this initial regression line was not very sophisticated. We simply drew a line between the points with the lowest and highest  xx  values.

Let's plot our initial regression line along our dataset to get a sense of the accuracy of this first line.
(plotted)

By now we should be able to guess the next step: quantify how well this line matches our data. We'll write a function called regression_revenue_error that, provided a movie and an m and b value of a regression line, returns the difference between our initial_regression_lines's expected revenue and the actual revenue error.
```python
def regression_revenue_error(m, b, movie):
    expected = (m * movie['budget_2013$'] + b)
    actual = movie['domgross_2013$']
    return round(actual - expected, 2)

initial_regression_line
{'b': 0.5, 'm': 1.79}
```
Ok, now plot the cost curve from changing values of  mm  from  1.0  to  1.9 .

We don't ask you to write a function for calculating the RSS, as you already wrote one in the error library which is available to you, and you can see used here.
```python
from error import residual_sum_squares
residual_sum_squares(budgets, domestic_revenues, initial_regression_line['m'], initial_regression_line['b'])
```
But we do ask you to plot a cost curve from 1.0, to 1.9 using that residual_sum_squares function. We start off with a list of values of m from 1.0 to 1.9, assigned to m_range below.
```python
large_m_range = list(range(10, 20))
m_range = list(map(lambda m_value: m_value/10,large_m_range))
```
Now we need to calculate a list of RSS values associated with each value in the m_range.
```python
cost_values = list(map(lambda m_value: round(residual_sum_squares(budgets, domestic_revenues, m_value, initial_regression_line['b']), 2),m_range))

from graph import trace_values
rss_trace = trace_values(x_values=m_range, y_values=cost_values, mode = 'lines')

plot([rss_trace])
```
Ok, so based on this, it appears that with our  b=0.5 , the slope of our regression line that produces the lowest error is between  1.3 and  1.4 . 

In fact if we replace our initial line value of  mm  with  1.3, we see that our RSS does in fact decline from our previous value of 24,179,824.

```python
residual_sum_squares(budgets, domestic_revenues, 1.3, initial_regression_line['b'])

22066076.55
```
## Changing multiple variables using Gradient Descent

Now it's time to move beyond testing the accuracy of the line with changing only a single variable. We need to play with both variables to find the 'best fit regression line'. As we know, the technique for that is to use **gradient descent**.

Remember that we derived our gradient formulas by starting with our cost function, and saying the RSS is a function of our  m  and  b  variables:

From the formula for our cost curve (not pictured), we found the gradient descent of the cost function, as that is used to find the incremental changes to decrease RSS. We do this mathematically, by taking the partial derivative with respect to  m  and  b .

Looking at our top function  ∂J/∂m , we see that it equals negative 2, multiplied by the sum of the errors for a provided  m  and  b  values relative to our dataset. And luckily for us, we already have a function called r**egression_revenue_error** that returns the error at a given point when provided our  m  and  b  values.

Recall, that we learned that **the factor of 2** can be discarded since it is present in both formulas. 

Additionally, recall that the error needs to be scaled by the size of the dataset to prevent larger datasets from having larger errors.

Our task now is two write a function called b_gradient that takes in values of  m ,  b  and our (scaled) movies, and returns the b gradient.


```python
def b_gradient(m, b, movies):
    n = len(movies)
    errors = list(map(lambda movie: regression_revenue_error(m, b, movie), movies))
    return round(-1 * sum(errors)/n, 2)

 b_gradient(1.79, 0.50, scaled_movies) # 5.37
```
Now do the same for the m_gradient:

```python
def m_gradient(m, b, movies):
    n = len(movies)
    errors_times_x = list(map(lambda movie: regression_revenue_error(m, b, movie)*movie['budget_2013$'], movies))
    return round(-1 * sum(errors_times_x)/n, 2)

m_gradient(1.79, 0.50, scaled_movies) # 2520.59

#Notice that the m_gradient is significantly larger than the b_gradient. This makes sense since the m_gradient formula is similar to the b_gradient formula, except that its output is also multiplied by the corresponding  xx  value.
```
Ok, now we just wrote two functions that tell us how to update the corresponding values of  mm  and  bb . Our next step is to write a function called step_gradient that will use these functions to take the step down along our cost curve.

Remember that with each step we want to move our current_b value in the negative direction of calculated b_gradient, and want to move our current_m value in the negative direction of the calculated m_gradient.

current_m = old_m  −η(−1/n∗∑ni=1 (xi∗ϵi)
current_b = old_b  −η(−1/n∗∑ni=1 (ϵi)

The step_gradient function would take as arguments:
 1. b_current
 2. m_current
 3. the list of scaled movies
 4. a learning rate
 
 and returns a newly calculated b_current and m_current with a dictionary of keys b and m that point to the current values.
```python
def step_gradient(b_current, m_current, movies, learning_rate):
    b_change = b_gradient(m_current, b_current, movies)
    m_change = m_gradient(m_current, b_current, movies) 
    new_b = round(b_current - (learning_rate * b_change), 2)
    new_m = round(m_current - (learning_rate * m_change), 2)
    return {'b': new_b, 'm': new_m}

initial_regression_line # {'b': 0.5, 'm': 1.79}

{'b': 0.5, 'm': 1.79}
```
Generate steps:
```python
def generate_steps(m, b, number_of_steps, movies, learning_rate):
    for i in range(number_of_steps):
        iteration = step_gradient(b, m, movies, learning_rate)
        # {'b': value, 'm': value}
        b = iteration['b']
        m = iteration['m']
        # update values of b and m
        iterations.append(iteration)
    return iterations

iterations = generate_steps(initial_regression_line['m'], initial_regression_line['b'], 100, scaled_movies, .0001) or [{'m': 'uncomment generate_steps method', 'b': 'uncomment generate_steps method '}]

```
Finally, let's calculate the RSS associated with our formula as opposed to the other.
```python
iterations[-1] # {'b': 0.5, 'm': 1.38}

residual_sum_squares(budgets, domestic_revenues, iterations[-1]['m'], iterations[-1]['b'])

22052973.85
```
Using this last iteration, we have an RSS  22052973.85 , better than all previous models - and we have the data, and knowledge to prove it:
```python
external_consultant_model = rss_consultant(scaled_movies)
internal_consultant_model = rss_revenue_with_year(scaled_movies)
our_regression_model = residual_sum_squares(budgets, domestic_revenues, iterations[-1]['m'], iterations[-1]['b'])
```
Compare:
```python
external_consultant_model # 23234357.68
internal_consultant_model # 25364329.23
our_regression_model      # 22052973.85
```
The End!
