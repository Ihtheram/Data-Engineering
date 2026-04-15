# Python
Documentation on Python Programming Language

**[⇐ Foundational Tools](../README.md)**


### `print()` Statement Formatting
* `format()` Method
    - "String.. {} String.. {} ... ".format(value(s) sequentially) or
    - "String.. {value1} String.. {value2} ... ".format(value1 = value, value2 = value...)
* f-String Method
    - f"String.. {value1} String.. {value2} ... "

### Enumerate
```py
A = ['a', 'b', 'c']
print(enumerate(A))
```
Output:
```CLI
[(0,'a'), (1, 'b'), (2, 'c')]
```

### Zip

**Example 1:**
```py
r1 = ['x1', 'x2', 'x3']
r2 = ['y1', 'y2', 'y3']
r3 = ['z1', 'z2', 'z3']

print(list(zip(r1, r2, r3)))
```
Output:
```CLI
[('x1', 'y1', 'z1'), ('x2', 'y2', 'z2'), ('x3', 'y3', 'z3')]
```

Example 2:
```py
for i, j, k in zip(r1, r2, r3):
    print(i, j, k)
```
Output:
```CLI
x1 y1 z1
x2 y2 z2
x3 y3 z3
```

### Range
* range(terminal)
* range(initial, terminal)
* range(initial, terminal, increment)

### * Data Structures *
* * Dictionary *
* * List *

### Random Number Generator
```py
from  random import randint

randint(initial, terminal) # Generates a random number between two int
```
```py
from random import shuffle

listX = [1, 3, 2, 4, 0]
shuffle(listX) # Shuffles items in listX 
```
### Lambda
```py
lambda parameter: return_operation
```

### Map & Filter
A map calls a funtion for each item of an iterable
```py
map(function, iterable)
```
A filter filters out false values from iterables
```py
filter(function, iterable)
```

## List Comprehension
Examples:
```py
list_a = [i for i in "String"]
list_b = [i**2 for i in range(0, 100) if i%2 == 0]
list_c = [i**2 if i%2 == 0 else "skipped Odd number" for i in range(0, 100)]
list_d = [i*j for i in [1, 2, 3] for j in [1, 10, 100]]
```


## Object-Oriented Programming with Python

### Class in Python
```py
class NameOfClass():

    class_attribute_1 = "value"
    class_attribute_2 = 0

    def __init__(self, param1, param2):
    # Constructor
        self.param1 = param1
        self.param2 = param2
        self.param3 = 2 * param2
    
    def example_method(self):
        # action(s)

Instance1 = NameOfClass(param1 = "value1", param2 = "value2") # Creates an instance object
```

### Inheritance with Python

```py

class ParentClassName():

    # class attribute(s)

    def __init__(self, param1, param2):
        self.param1 = value1
        self.param2 = value2

class InheritorClassName(ParentClassName):
    def __init__(self):
        ParentClassName.__init__(self, param...)

```

### Polymorphism with Python

example_method() in Inheritor1 and Inheritor2 behaves in different ways although it is inherited from the same ParentClass.

```py
class ParentClass():

    def __init__(self, params..):
        self.param1 = value1
        ...

    def example_method(self):
        print("Parent")


class Inheritor1(ParentClass):
    def example_method(self):
        print("First")

class Inheritor2(ParentClass):
    def example_method(self):
        print("2nd")

```

## Magic/Dunder Methods
Functions like `__init__()`, `__str__()`, `__len__()`, `__del__()` etc. are implicitly generated for every class in python, but also can be modified by defining explicitly in the class.


## Error
```py
try:
    # statements that may cause error
except error_name: # Leave only 'except:' for all kind of errors
    # statements that execute only when the try block causes an error
finally:
    # statements that will execute irrespective of occurance of an error
```

## Pandas

## PySpark

## Environment

1. Install `pyenv`
2. Install `python` with pyenv
3. Create `venv`
4. Install packages like `Pandas` in venv

Creating a Python virtual environment is straightforward, and it’s the recommended way to manage project dependencies. Here’s a step-by-step guide:

---

### 🛠 Steps to Create a Python Virtual Environment

#### 1. **Check Python Installation**
Make sure Python is installed:
```bash
python --version
```
or
```bash
python3 --version
```

#### 2. **Create a Virtual Environment**
Use the built-in `venv` module:
```bash
python -m venv myenv
```
- `myenv` is the name of your environment folder. You can call it anything (e.g., `env`, `venv`, `project_env`).

#### 3. **Activate the Environment**
- **Windows (Command Prompt):**
  ```bash
  myenv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```bash
  .\myenv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source myenv/bin/activate
  ```

Once activated, you’ll see the environment name (e.g., `(myenv)`) at the start of your terminal prompt.

#### 4. **Install Packages Inside the Environment**
Now you can install Pandas or any other library without affecting your global Python setup:
```bash
pip install pandas
```
Check the installation/version
```bash
pip show pandas
```
or
```bash
python -c "import pandas as pd; print(pd.__version__)"
```

#### 5. **Deactivate the Environment**
When you’re done:
```bash
deactivate
```

---

### ⚡ Pro Tips
- Use `requirements.txt` to save dependencies:
  ```bash
  pip freeze > requirements.txt
  ```
- Recreate the environment elsewhere:
  ```bash
  pip install -r requirements.txt
  ```
- If you work with multiple projects, each should have its own environment.

---


