
#Export Learn to Jupyter:

Git icon
copy
go to notes in Terminal
fork
git clone #paste
jupyter notebook
click the py thing

# Quick Intro to Jupyter Notebook:

##Adding cells

If you wish to quickly add a new cell you can do so using the following steps:

Make sure you are not in insert mode
Remember you can tell you are in insert mode when you have a green border around the cell
To get out of insert mode, press shift + enter. Another option is to press the escape key
You will no longer see a cell bordered in green
Then press the letter b to create a new cell

## Deleting cells
To delete a cell you once again should be in escape mode, and then press the x key.

Of course, you'll want a way to undo your deletion. From escape mode, you can press z to undo deletion of a cell. Note that this is different from cmd + z. Pressing cmd + z while in insert mode undoes any changes inside of a cell while, whether these changes be deletions or text insertions. Pressing z from escape mode undoes the deletion of a cell.

Go to escape mode and press x. This cell disappears!

Then bring it back with z.

## Change between cell types:

A cell must either be of type markdown or of type code, in which case all of the contents must be valid Python. It cannot be both. We can quickly change a cell from markdown to code with some keyboard shortcuts.

From escape mode, you can change a cell to type code by pressing the letter y
From escape mode, you can change a cell to type markdown by pressing the letter m
Anytime you create a new cell, say with the shortcut key b, the new cell will default to code mode. You can switch to escape mode and press the letter m to change the cell from code to markdown.

## View All Shortcuts
Press the key h while in escape mode to view the menu for all of Jupyter's shortcuts.

## Summary
In this lesson, you learned about the command line, cloning GitHub repositorites, and working with Jupyter notebooks. You saw that in Jupyter notebooks, you can either be in insert mode or escape mode. While in insert mode, you can edit the cells and undo changes within that cell with cmd + z on a Mac or ctl + z on Windows. In escape mode, you can add cells with b, delete a cell with x, and undo deletion of a cell with z. You can also change the type of a cell to markdown with m and to Python code with y.

Then you saw how to work with Python code in Jupyter notebooks. You saw that to execute your code in the cell, you need to press shift + enter. If you do not do this, then the variables that you assigned in Python are not going to be recognized by Python later on in the notebook.

# Jupyter Notebook Cell Types¶
You might have started to notice that the code blocks have little notes that say In [ ]: before you run them, and then are filled with a number after you run them. This is important, as it tells you in what order the cell blocks were run. (Which can affect how a program runs.)

You may also notice that other cell blocks, such as this one, do not have the In [ ]: label as with the code blocks. This is because this cell block is formatted as Markdown rather than code. The details of Markdown are not important here but just know you can use markdown cell blocks to display text. They are really useful for embedding notes and explanations in your Jupyter Notebook. You can see (and change) what type of cell is by clicking the dropdown menu at the top:

## Command Versus Edit Mode
You should also start to notice that when you are in a cell writing code (or notes), the cell is highlighted in green meaning you are in edit mode.

Alternatively, if you press esc, the cursor will be in blue inidicating that you are in command mode.

## Edit Mode
Edit mode is the standard mode for editing cells, whether it's writing code or notes. To enter edit mode from command mode simply hit enter, or double click on a cell.

## Command Mode
In command mode, you can delete cells, add cells, copy cells, paste cells, change cell types, and more. You can also do these tasks in a more cumbersome (and time consuming) manner by using the various headers in the menu bar at top.

## Shortcuts

Keyboard shortcuts available under "Help"

# Running Bash Commands
We can also run bash commands just as we did before from the terminal directly within Jupyter Notebooks!
(Note: bash commands cannot be mixed with Python and must be in their own cell block.)

# Loading a Dataframe

```python
df = pd.read_csv('lego_sets.csv') #Loads the dataframe in
print(len(df)) #Prints the length of the dataframe
df.head() #Uses a built in method common to all Pandas Dataframes
```

# Accessing Methods from Packages and Objects

When we loaded in packages in our first cell block (using the import commands), we loaded code into memory. That code included functions, variables, and other objects. Collectively, all of these items are loaded under the package name or alias.

We demonstrated this when we used the pd.read_csv() method above.

This also demonstrates the dot notation in Python, which is how we access built in methods or attributes of a given object. Similar to what we saw with bash in the command line, we can also use tab completion to preview methods available in packages or other objects.

In the cell below, navigate your cursor to the right of pd.
Press tab to see a list of available methods/attributes
```python
pd.#start the thing you want and press tab and you'll get a dropdown menu
```

# Pulling up Docstrings

Even better, you can even see how a method works by pulling up its docstring!
You can do this by writing ? after the method and running the cell.

```python
pd.read.csv?
#This provides a new window with the docstring
```
OR:
```python
pd.read.csv() 
#if your cursor is in the () then you can view docstring a dropdown

# Variables
The other thing that happened in our block of code above was that we defined a variable.

This happened in this line of code:
```python
df = pd.read_csv('lego_sets.csv')
```
As we saw, we used the built in read_csv method from the pandas package which we imported under the alias pd.

The output of this method was then assigned to the variable df. This is the standard syntax for declaring any variable. You do not have to specify variable types, as in many other programming languages. Simply:
```python
variable_name = what_to_store_in_the_variable
```

**Remeber to make sure not to name variables the same as built-in varibles. You can check type by calling 'type(xxx)' on that item!**

## Common DataFrame Methods

As you can see, the variable df is a DataFrame object (which is part of the Pandas core package). Here's some other common methods you will want to become familiar with when working with Pandas dataframes:
```python
df.head()
#Preview the first 5 rows of a dataframe. Pass a number for more/less rows
df.head(2) #or just two...
df.ages.head() #a spreadsheet with ages as a columb will show just that data
df.ages[:5] #Here we introduce another new syntax the list slice [:5] this limits us to the first 5 items
```
```python
df.tail(10)
#Preview last 10 rows (default 5 if no number given)
df.info()
#Returns column names and details about each column
df.columns
#Return column names. Note that there is no parentheses for this. This is becuase this is an attribute as opposed to a method - it returns a list of column names instead!
```

# Pandas Series

Pandas Series
While the entire spreadsheet is called a dataframe, each individual column is known as a series. You can access a specific column of a pandas dataframe one of two ways:
```python
df['col_name']
```
or
```python
df.col_name
```
First note that in df['col_name'] we need 'quotations' around the column name. The quotations denote the column name is a string, Python's built in variable type for storing text. This can alternatively be replaced with double quotes df["col_name"]. In general, anything in quotations is a string in Python code. Occasionally, with very ill formatted column names with quotations in the names themselves, you may even need to wrap a name in triple quotes df["""col_name"""] . This will rarely happen in this particular context, but it's the general pattern for dealing with messy strings.

Note that the second way, df.col_name, will only work if there are no spaces within the name of the column. Similar to tab completion with the command line, this is a primary reason why programmers use dashes (-) and underscores (_) in lieu of whitespace in their variable and file names. Also note that no quotations are used when using this format. (The column names have been stored as attributes of the DataFrame object!)

# Slices!
List and Series Slices
Above, we introduced an entirely new programming pattern called a slice which subsets the data into smaller pieces.

```python
#The syntax for a slice is 
[start:end]
```

You can also pass an additional third parameter 
```python
[start:end:count_by] 
```
which will allow you to:
count every other: 
```python
[start:end:2]
```
count backwards: 

```python
start:end:-1]
```
or potentially much more cryptic patterns, depending on what you pass.

While we could have also used df.State.head(), slicing works for many more datatypes. This includes the previously mentioned strings as well as lists and other iterable objects. Series, the columns of the pandas DataFrame, are similar to Python's built in lists, but also have additional methods built in to them that we will continue to investigate.

Common Series Methods
Some very useful series methods include those for obtaining basic summary statistics:
```python

series.mean()
series.median()
series.min()
series.max()
```
Series references
https://pandas.pydata.org/pandas-docs/stable/reference/series.html

# Importing Matlobplot
```python
#import a subset of the matplotlib package under the alias 'plt'
import matplotlib.pyplot as plt

#ipython magic command for displaying graphs within the notebook
%matplotlib inline

#Then:
to_graph = df.theme_name.value_counts()[:5]
to_graph.plot(kind='barh')
```
## Adding labels

The graph above is a good start, but we should be sure to add some labels! To do this we make successive calls to the plt package we imported. Some common methods you should be familiar with include:
```python
plt.title()
plt.xlabel()
plt.ylabel()

#which aloow:
to_graph = df.theme_name.value_counts()[:5]
to_graph.plot(kind='barh') #lots of other optional parameters can be passed such as color
plt.title('Top 5 Lego Themes', fontsize=16) #add a title and adjust font size (optional)
plt.xlabel('Number of Lego Sets') #you could also pass in fontsize if you wanted here
plt.ylabel('Theme')
```

## Scatter plot

Take a minute to try chaining some of these methods together to create a few of your own visuals for practice. Some ideas can include making a scatter plot with `plt.scatter(x , y)` where you pass in two series (one as x and the other as y), plotting histograms with the `series.hist()` method, or creating simple bar graphs as shown above.

Pass two series:
```python
plt.scatter(df.play_star_rating, df.star_rating)
#Here, two different column types from the csv file are being plotted. You can add any of those column types with a 'df.' in front of i`t
```
Then, once that data has been run, you can:
```python
df.play_star_rating.hist()
```

# Python Practice

This provides lots of reminders!!!!
```python
help(str)
```

```python
melissa = "melissa"
melissa.title()
melissa.capitalize()
melissa.upper()
```
num to string
```python
str()
```

Replace
```python
name = "Bart Simpson"
name = name.replace("Bart Simpson", "Bart Flanders", 1)

print(name)
```

## Practice 1:

given a string and a non-negative int n, return a larger string that is n copies of the origial string.
string_times('hi', 2) -> 'hihi'
```python
#the same answer!
def string_times(str, n):
 x = ''
 for i in range(n):
   x = x + string
 return x

def string_times(str, n):
  return str + n
```
## Dictionary Methods

There's plenty more that you can do with dictionaries, although worrying too much about specifics can be overwhelming early on. As a good starting point, recall that you can look up dictionary methods using tab completion, or the help method. Furthermore, if you wish to know how a specific method works, you can pull up the docstring.

```python
help(dict)

friends. #tab to show up

#Pulling up documentation for a specific method
friends.get?
```

calling dictionaries:
```python
creators = ['David Crane', 'Marta Kauffman']

friends['creators']
['David Crane', 'Marta Kauffman']
```
## creating a list of dictionaries:

A dictionary is an unordered collection of key-value pairs. We mark the start and end of a dictionary with curly braces, {}, and then follow the pattern of 'key':'value' for each of the associated attributes, with each attribute separated by a comma: dictionary = {'key_1':'value_1', 'key_2':'value_2'}.

```python
seinfeld = {'name': 'Seinfeld', 'creators': ['Larry David', 'Jerry Seinfeld'], 'genre': 'sitcom', 'no_of_seasons': 10, 'no_of_episodes': 180}

tv_shows = [friends, seinfeld]
tv_shows

#
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
  ### pulling information from a nested data structure

  Ok, now let's start working with this nested data structure. First let's select the second creator of Seinfeld and set it equal to the variable jerry. We'll retrieve this data in steps. First, we'll select the correct TV show.

  ```python
  tv_shows[1]
  #seinfeld. Now we have the first data group

  tv_shows[1]['creators']

  tv_shows[1]['creators'][1]

  jerry = tv_shows[1]['creators'][1]
jerry
  ```
## Loops
```python
iteration_count = 0
for whatever_we_want in zero_to_three:
    iteration_count += 1
    print("This is iteration:", iteration_count)
    print(whatever_we_want)
print("The for loop is finished now! I am not in the for loop block, which is why I only printed once!")
```

More on range:

```python
len(countries)

range(0, len(countries))

#conver to a list
list(range(0, len(countries)))

for index in list(range(0, len(countries))):
    print(cities[index]+",", countries[index])
```

NOte: Note: More conventionally, these contrived examples would employ the enumerate() method, but that is beyond the scope of the current lesson. At some point in the future, examine how this code snippet works:
```python
for idx, item in enumerate(['A', 'B', 'C']):
    print(idx, item)
```
## Loops and dictionaries

```python
first_name = ""
last_name = ""
for key, value in example_dictionary.items():
    if key == "last_name":
        last_name = value.title()
    if key == "first_name":
        first_name = value
print(first_name, last_name)
````

## FOR LOOP through Dictionary

```python
city_names = []
for city in cities:
  city_names.append(city['City'])


city_names
```

## Matplotlib

```python
# Import matplotlib
import matplotlib.pyplot as plt

# Set plot space as inline for inline plots and qt for external plots
%matplotlib inline
```
## Conditionals

```python
vacation_days = 1
if False:
    # if block starts    
    # code does not run since conditional argument is False
    vacation_days += 1
    print("vacation_days = ", vacation_days)
    print("we incremented vacation days")
# if block ends    
else:
    # else block starts
    print("vacation_days = ", vacation_days)
    print("we did NOT increment vacation days")
# else block ends

#vacation_days =  1
#we did NOT increment vacation days
```
Using elif:

```python
vacation_days = 1
if False:
    # code does not run since conditional argument is False
    vacation_days += 1
    print("vacation_days = ", vacation_days)
    print("we incremented vacation days")
elif True:
    print("We are now in our elif statement!")
    print("This means that we exceeded our goals this quarter")
    print("We will increase our vacation days by two")
    vacation_days += 2
    print("vacation_days = ", vacation_days)
else:
    print("vacation_days = ", vacation_days)
    print("we did NOT increment vacation days")

We are now in our elif statement!
This means that we exceeded our goals this quarter
We will increase our vacation days by two
vacation_days =  3
```

## Plotting Lab

 First, provide some labels for both axes by using plt.xlabel() and plt.ylabel(). You can also change the size of the plot with plt.figure(figsize=(a,b)), where a and b specify the width and height of the plot in inches.

```python
# Set the figure size in inches
plt.figure(figsize=(10,6))

plt.scatter(x, y, label = "y = sin(x)" )

# Set x and y axes labels
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.title('Scatter Plot in Matplotlib')
plt.legend()
plt.show()
```

# Day 2

## Nested Dictionary:

```python
test =  { 'subject': 'Corvettes',
       'data_given': '06-04-19',
       'concepts': ['size', 'horsepower', 'MPG'],
        'questions': {'A': {'question': 'How many people can fit in a Corvette?',
                          'response_choices': [1,2,3,4],
                            'answer': 2},
             'B': {'question': 'What is the MPG of a Corvette?',
                  'response_choices': [15,20, 25, 30],
                    'answer': 15},
             'C': {'question': 'How much horsepower does a Corvette have?',
                  'response_choices': [200,300, 400, 500],
                    'answer': 400}}}
```

## View Keys and Values

```python
print(test.keys())

print(test.values())

#retreive specific value
print(test['subject'])
```
## chaining
```python
test['concepts'][0]

#Return all the possible answers to question A in the questions dictionary?

print(test['questions']['A']['response_choices'])
```
## dict_items

```python
my_dict

#vs: keys only

my_dict.items()
```

List dict:
```python
list(my_dict)
```
More:
```python
for i in my_dict:
    print(i)
#output is in keys
brand
model
year

for i in my_dict.items():
    print(i)
#output is keys and values

for i in my_dict.items():
    print(i)

for i in my_dict.items():
    print(type(i))
#output is type of each item

for k, v in my_dict.items():
    newdict.update({k: v})
print(newdict)
#output passes in keys and values

newdict = {}
for i in my_dict.items():
    newdict[i[0]] = i[1]
print(newdict)
#adding to a new dict
```

Answers:
1. tuples...
2. dictionary
3. List

## Loops

```python
friends = ['Margot', 'Kathryn', 'Prisila']

for i in range(len(friends)):
#     print('i is now:', i)
    print(friends[i])

Margot
Kathryn
Prisila
```

### While loop

```python
number = 0
prompt = "What is the meaning of life, the universe, and everything? "

while number != "42":
    number =  input(prompt)

#needs to be anseswered:
What is the meaning of life, the universe, and everything? # answer
```
The flow of execution for a while statement works like this:

1. Evaluate the condition (BOOLEAN EXPRESSION), yielding False or True.
2. If the condition is false, exit the while statement and continue execution at the next statement.
3. If the condition is true, execute each of the STATEMENTS in the body and then go back to step 1.

**Generate random integer whileloop**
```python
x = np.random.randint(0,11,1)[0]


guess = input("Guess a number 0 throught 10 ")
tot_guesses = 0

#below evaluates both the guess ANd the number of guesses

while int(guess) != x and tot_guesses <= 5:
    print("Nope, that's not it!" )
#     print('Guess Count:',tot_guesses + 1)
    guess = input("Guess again: ")
    tot_guesses = tot_guesses + 1
if int(guess) == x:
    print('you got it right')
```

## Looping through dictionaries

```python
questions =  {'A': {'question': 'How many people can fit in a Corvette?',
                          'response_choices': [1,2,3,4],
                            'answer': 2},
             'B': {'question': 'What is the MPG of a Corvette?',
                  'response_choices': [15,20, 25, 30],
                    'answer': 15},
             'C': {'question': 'How much horsepower does a Corvette have?',
                  'response_choices': [200,300, 400, 500],
                    'answer': 400}}
```
For a list of questions from this dictionary:
```python
#just the Values associates with the question key:

print(questions.values())

```
To loop through all question values to get a list of all the questions:

```python

#create a container to hold my list of questions
list_of_questions = []

#create a loop that goes through the dictionary
for v in questions.values():
    #set variable question to the question in the dictionary
    print(v)
    question = v['question']
    # using just the above code you can call JUST the questions (if the following line of code is hashed out)
    list_of_questions.append(question)
    
    #here is a one line version of this
#     list_of_questions.append(v['question'])

print(list_of_questions)
```
Do the same thing for the answers!
```python
#create a container to hold my list of questions
list_of_answers = []

#create a loop that goes through the dictionary
for a in questions.values():
    list_of_answers.append(a['answer'])

print(list_of_answers)
```

## Dictionary Methods

 Finally, we'll look at a few dictionary methods:

.keys() is used to return a list-like dict_keys object with the name of each key in the dictionary
.values() is used to return a list-like dict_values object with the values in the dictionary
```python
dictionary = {'name-key': 'example-dict', 'key_2': 'value_2', 'num_keys': 3}
print(dictionary.keys())
print(dictionary.values())
```

## ALL COMPARISON OPERATORS!!!

What Are Comparison Operators?
Comparison operators (or Relational operators) take two elements and compare their values and then return a value that is either True or False. In Python, comparison operators are:

== # tests equality between two elements
!= # tests inequality between two elements
<, >, <=, >= # each tests the value between two elements
Perhaps the last line's operators are a little more familiar because we've seen these operators in math classes. But the first two might be a bit more confusing, so, let's dive into those first.

The double equals operator (==) is testing whether the value of the first element is equal to that of the second element (e.g. element_1 == element_2).
```python
False == True # returns False
False == False # returns True
10 == 20 # returns False
10 == 10 # returns True
"hi" == "HI" # returns False
"heLLo" == "heLLo" # returns True
```
The bang (exclamation point) equals operator (!=) is testing whether the value of the first element is NOT equal to that of the second element (e.g. element_1 != element_2).
```python
True != True # returns False
True != False # returns True
10 != 20 # returns True
10 != 10 # returns False
"hi" != "HI" # returns True
"heLLo" != "heLLo" # returns False
```
Now onto the third grouping of comparison operators. The greater than (>), less than (<), greater than or equal to (>=) and less than or equal (<=) to operators also only return True or False as the output.
```python
True > True # False
True >= True # True
10 <= 10 # True
7 < 7 # False
10 < 100 # True
100 > 101 # False
```
We can even compare strings to see which is alphabetically greater or less than. A string is greater than if it comes after another string alphabetically (or if its ascii value is greater). An important note is that capital letters have lower ascii values, which means that they come earlier in the alphabet than lowercase letters. For example the ascii alphabet would look something like: Aa Bb Cc Dd Ee Ff ... Xx Yy Zz with A having the lowest ascii value and z having the highest ascii value.
```python
"APPLE" < "apple" # True
"aaron" > "alexa" # False
"Terrance" > "Teresa" # True
"SAME" == "SAME" # True
```

# Day 3

Code challenge:

Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
```python
def threetimes(var1):
  if len(var1)<=3:
    return var1*3
  else:
    temp = var1[:3]
    return temp*3
```
## Nested Loops

So, if we wanted to take the above list of `programmers` and dynamically list out everyone's `favorite_languages` we would need to use two separate loops. 

```python
for programmer in programmers:
    for language in programmer['favorite_languages']:
        print(language)
```

iterate over the soccer_match list to create a new list with the name of the country for each team
```python
countries = []
for team in soccer_match:
    countries.append(team['country'])
    print(countries)
 ```
 In the cell below, iterate over the soccer_match list to create a new list with the colors for each team this should be only one list containing strings for each of the country's colors.
 ```python
  # iterate over the soccer_match list to create a new list with the colors for each team
# this should be only one list containing strings for each of the country's colors
colors = []
for team in soccer_match:
     colors.append(team['colors'])
     print(colors)

 ```   
 This time, iterate over the soccer_match list to create a new list with the players from each team. players should be a single list containing the dictionaries for each of the country's players.
 ```python
 players = []
for team in soccer_match:
    for player in team['players']:
        players.append(player)

print(players)
```
Iterate over the soccer_match list to create a new list with the captains from each team. This should be a single list containing the dictionaries for each of the country's captains.
```python
captains = []
for team in soccer_match:
    for player in team['players']:
        if player['captain'] == True:
            captains.append(player)
            
print(captains)
```

## descriptive statistic

mean:
```python
def calc_mean(data):
 return sum(data)/len(data)
```

median:
```python
def calc_median(data):
  data = data.sort
  return (data[len(data)//2 + data[(len(data2//2))-1])/2)

#Needs this one to evaluate both the even and odd situations:

def calc_median(data):
 data.sort
 n = len(data)
 if n % 2 == 0: 
  return data[n//2]
 else n % 2 == 1:
  return (data[n)//2 + data[(len(n//2))-1])/2)
```
## Review Covariance and Pearson Correlation Coefficient

## OOP Lecture

numpy
```python
n_p.a = np_array([])
#if you press tab it will dropdown, provide instructions.

np_a

import numpy as np
np.
```

## Interquartile Range:
Calculating IQR for a Given Data Set
You will now get a feel for how IQR is calculated using the collection of numbers from the image above. First, put the numbers in a list.

# List of numbers
x = [3, 5, 8, 12, 15, 18, 20, 22, 25, 30, 50, 80, 687]
Step 1: Sort the data in ascending order (these numbers are already sorted but don't skip this step when you do this on other data- it's important!).

# Sort in ascending order
x = sorted(x)
Step 2: Calculate the distance between the last element and the first element.

# Distance between last and first element
distance = len(x) - 1
Step 3: Multiply the distance by the desired percentiles, 25th and 75th, expressed as fractions. This will yield the indices of the elements that correspond to the 25th percentile and 75th percentile, respectively.

# Multiply distance by percentiles
​
# Index of 25th percentile
index_p25 = 0.25*distance
index_p25
3.0
# Index of 75th percentile
index_p75 = 0.75*distance
index_p75
9.0
Step 4: Using the indices calculated above, determine the 25th and 75th percentiles.

# 25th Percentile
p25 = x[int(index_p25)]
p25
12
# 75th Percentile
p75 = x[int(index_p75)]
p75
30
Step 5: Calculate the IQR by subtracting the 25th percentile from the 75th percentile.

# IQR
iqr = p75 - p25
iqr
18
In practice, you will probably never calculate the IQR by hand since numpy has a built-in method for calculating percentiles.

import numpy as np
​
np.percentile(x, 75) - np.percentile(x, 25)
18.0
You might have noticed that the indices calculated above happened to be whole numbers. Whole numbers are great to work with here since they can be used as indices directly. The calculation becomes a little more complicated when the indices are fractional numbers. In this case, numpy will use a technique called "linear interpolation" to take the fractional components into account. This is beyond the scope of what you need to know but if you are curious about how it works you can check out the documentation.