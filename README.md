# Code Institute Christmas Challenge

_Team name: **UnitedGing**_

_Members:_
* Anthony O' Brien & Shane Muirhead

_Challenge Details:_
[Link to Challenge](https://drive.google.com/file/d/1NkaNnGjKdxp1fvp6m9aCT2D-Rc3XKdD-/view)

Originally we set out referencing the image in an list format with each pixel of the image converted into an integer. Then using loops we would loop over the list objects and the objects indexes to check for specific integers and then create the associated character value to print to the console. 
This scenario worked and it produced the desired result and was creative enough as an inception to the challenge solution.
```python
  # Christmas Tree
xmas_tree = [
  [4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,4,4,4,4,1,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,4,4,1,3,4,4,4,3,2,4,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,1,3,4,4,4,4,4,4,4,3,2,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,1,3,4,4,4,4,4,4,4,4,4,4,4,3,2,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4,4],
  [4,4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,4],
  [4,4,4,4,4,1,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,2,4,4,4,4,4],
  [4,4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4],
  [4,4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4],
  [4,4,4,1,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,2,4,4,4],
  [4,4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4,4],
  [4,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4,4],
  [4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,4],
  [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
  [4,4,4,4,4,4,4,4,4,4,4,2,3,3,3,3,3,1,4,4,4,4,4,4,4,4,4,4,4]
]

for picrow in xmas_tree:
  for px in picrow:
    if (px == 4):
      print(" ", end='')
    elif (px == 0):
      print("|", end='')
    elif (px == 1):
      print("/", end='')
    elif (px == 2):
      print("\\", end='')
    else:
      print("_", end='')
  print("")

print("Merry Christmas Code Institute")
```

After some thought on how to refactor the code we eventually settled on a much more condensed version of the above through referencing the `tree.txt` file directory using the `open()` built in Python function and looping through the lines of that file to create the desired output, this time checking for the special characters directly in a ternary operator and printing same to the terminal. 

```python
f = open("tree.txt", "r")
lines = f.readlines()


def xmas_tree():
    """
    Function to create a Christmas Tree
    as per Code Institute challenge
    """
    for line in lines:
        for px in line:
            print(" " if px == " " else
                  "|" if px == "|" else
                  "/" if px == "/" else
                  "\\" if px == "\\"
                  else "" if px == "\n"
                  else "_", end='')
        print("")
    print("Merry Christmas Code Institute")


xmas_tree()
```

[Final Code Attempt](https://github.com/auxfuse/christmas-challenge/blob/master/app.py)

To run the code, fork/clone the repo, open it up in your preferred IDE and run the app.py file to see the Tree generate with a little seasons greeting to accompany same in your terminal.

It was a pleasure to work alongside [Shane Muirhead](https://github.com/ShaneMuir) from Slack, a fellow Alumni Student and friend, and for welcoming the Team name to be `UnitedGing` <3 

Merry Christmas CI from Anthony & Shane. 

