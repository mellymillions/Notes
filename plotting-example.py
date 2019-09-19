# pip install plotly
# pip install pandas

# pip is a python tool to install libraries (bundles of code) from the internet via your terminal
# because we're doing this in a web browser, we'll install it in this made up way below:

# Just because you installed it on your computer doesn't mean your code knows about it. You have to import a library into your code to use it

# import plotly

# If we were on a computer and using Excel, we'd need this code to read in a spreadsheet of users
# import pandas
# file_name = './users.xlsx'
# users_df = pandas.read_excel(file_name)
# users = users_df.to_dict('records')

# instead we'll just pretend they came from a spreadsheet but define them here:
users = [
  {
    'id': 1,
    'email': 'devilchick182@hotmail.com',
    'address': {
      'street': 'Park Place',
      'number': 123
    },
    'age': 10
  },
  {
    'id': 3,
    'email': 'sporkler@biz.co',
    'address': {
      'street': 'Nowhere',
      'number': 100000000
    },
    'age': 99,
  },
  {
    'id': 2,
    'email': 'surfingbear10@chillers.bro',
    'address': {
      'street': 'The north pole',
      'number': 55
    },
    'age': 3
  },
]


# we want to plot users id and age
# write a function get_ids that takes in the list of users, and returns a list of their ids 
# get_ids(users) == [1, 3, 2]

def get_ids(list_of_users):
  ids = []
  for person in list_of_users:
    ids.append(person['id'])
  return ids

list_of_ids = get_ids(users)
print(list_of_ids)

# now do the same for ages
def get_ages(list_of_users):
  ages_list = []
  for person in list_of_users:
    ages_list.append(person['age'])
  return ages_list

list_of_ages = get_ages(users)
print (list_of_ages)


# rembmer how we imported plotly above? lets use it now. This code initializes a plotly notebook in offline mode since you don't have an account with them. (Look it up if you want to know more)

# plotly.offline.init_notebook_mode(connected=True)

# Then we want to plot a graph with ids in the x axis, and ages in the y axis. lets make it a bar graph for funsies
# the iplot function takes a list of dictionaries, each of which contain everything we need to make a graph (x values, y values, type, label, etc)

# plotly.offline.iplot([{'type': 'bar', 'x': list_of_ids, 'y': list_of_ages}])


# so why does iplot take a list of dictionaries instead of a single one? cause we can graph two things over each other. Let's, for no real reason, plot the street numbers as a line graph over the bar graph of ages. Let's also give the x axis more readable labels, so it's not just id numbers

# first pull out the numbers
def get_number(list_of_users):
  numbers_list = []
  for person in list_of_users:
    numbers_list.append(person['address']['number'])
  return numbers_list

list_of_numbers = get_number(users)

# Then collect the emails for the labels
def get_emails(list_of_users):
  emails_list = []
  for person in list_of_users:
    emails_list.append(person['email'])
  return emails_list

emails = get_emails(users)

# now lets remake that bar graph dictionary, but this time with lables, and saved to a variable for readability

age_graph = {
  'type': 'bar',
  'x': list_of_ids,
  'y': list_of_ages,
  'text': emails
}
street_number_graph = {
  # 'type': 'line'?? just guessing, not sure, maybe 'line' is the default and we don't need it
  'x': list_of_ids, # x axis matches up
  'y': list_of_numbers,
  # 'text': emails? I assume we don't need this cause the other already has it, but not sure
}

# plotly.offline.iplot([age_graph, street_number_graph])


def get_streets(list_of_users):
  streets_list = []
  for person in list_of_users:
    streets_list.append(person['address']['street'])
  return streets_list

print(get_streets(users))
```
