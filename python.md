# Python
This is how you capitalize first letters
```python
string = "art vandelay" # 'Art Vandelay'
(string.title())
```
This is how you make it all uppercase
```python
string = "Ceo" # 'CEO'
(string.upper())
```
This is how you validate if a string ends correctly
```python
string = "art.vandelay@vandelay.co" # False
(string.endswith('.com'))
```
This is how you validate if a string starts correctly
```python
'vandelay.com' # 'www.vandelay.com'
(string.startswith('www.'))
```
String Slicing: Isolate the area code
```python
string = "7285553334" # 728
"7285553334"[:3]
```
String Slicing: Isolate the phone number
```python
string = "7285553334" # 728
"7285553334"[4:10]
```
