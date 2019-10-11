# Dictionary Practice

```python
def get_mode(data):

    # Create and populate frequency distribution
    frequency_dict = {}
    
    # For all elements in the list:
    for item in data:
        if item not in frequency_dict:
            frequency_dict[item] = 1
    # If an element is not in the dictionary, add it with value 1
        else:
            frequency_dict[item] = frequency_dict[item] + 1
            
    
    # If an element is already in the dictionary, +1 the value
    
    print(frequency_dict)
    
   
    # Create a list for mode values
    modes = []
    max_value = max(frequency_dict.values())
    for key, value in frequency_dict.items():
        if value == max_value:
            modes.append(key)
        
        
    #from the dictionary, add element(s) to the modes list with max frequency

    # Return the mode list 
    return modes

test1 = [1, 2, 3, 5, 5, 4]
test2 = [1, 1, 1, 2, 3, 4, 5, 5, 5]

print(get_mode(test1)) # [5]
#print(get_mode(test2)) # [1, 5]
```