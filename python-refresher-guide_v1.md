# Python Refresher Guide

A quick-reference memory aid designed for rapid recall. Find a topic, review it in 30–90 seconds, and immediately remember how to use it.

---

## Quick Navigation

### [1. Python Foundations](#1-python-foundations)
- [Variables](#variables)
- [Data Types (Numbers, Strings, Booleans)](#data-types)
- [Operators & Comparisons](#operators--comparisons)
- [Conditional Statements (if, elif, else)](#conditional-statements)
- [Loops (for, while, break, continue, pass)](#loops)

### [2. Collections](#2-collections)
- [Indexing & Slicing](#indexing--slicing)
- [Lists & List Methods](#lists--list-methods)
- [Tuples](#tuples)
- [Sets](#sets)
- [Dictionaries & Dictionary Methods](#dictionaries--dictionary-methods)
- [String Methods](#string-methods)

### [3. Functions & Scope](#3-functions--scope)
- [Functions (Parameters vs Arguments)](#functions)
- [Return vs Print](#return-vs-print)
- [Default Parameters](#default-parameters)
- [Scope (Local vs Global)](#scope)
- [*args and **kwargs](#args-and-kwargs)
- [Lambda Functions](#lambda-functions)
- [List Comprehensions](#list-comprehensions)

### [4. Errors & Modules](#4-errors--modules)
- [Error Handling (try, except, finally, raise)](#error-handling)
- [Modules & Imports](#modules--imports)

### [5. Classes & Object-Oriented Programming](#5-classes--object-oriented-programming)
- [Classes & Objects](#classes--objects)
- [__init__ Method](#init--method)
- [self Keyword](#self-keyword)
- [Instance vs Class Attributes](#instance-vs-class-attributes)
- [Inheritance & Method Overriding](#inheritance--method-overriding)
- [Mutable vs Immutable Objects](#mutable-vs-immutable-objects)

---

## 1. Python Foundations

<a id="variables"></a>
#### Variables

##### What it is
A named container that holds a reference to a value stored in memory.

##### Why it exists
Allows you to store, reuse, and update data dynamically throughout your code.

##### Syntax
```python
variable_name = value
```

##### Simple Example
```python
price = 19.99
quantity = 3
total_cost = price * quantity
print(total_cost)  # 59.97
```

##### What to Remember
- Variable names should be descriptive and use `snake_case`.
- You do not specify data types explicitly; Python infers them automatically.
- Reassigning a variable points it to a new value in memory.

##### Common Mistake
**Wrong:**
```python
1st_user = "Alice"
```
**Correct:**
```python
user_1 = "Alice"
```
Variable names cannot start with numbers or contain spaces/hyphens.

---

<a id="data-types"></a>
#### Data Types

##### What it is
The category of data stored in a variable, determining what operations can be performed on it.

##### Why it exists
Ensures Python processes numbers, text, and logical decisions correctly.

##### Syntax
```python
# Numbers (int, float)
age = 25
gpa = 3.8

# Strings (str)
name = "Jordan"

# Booleans (bool)
is_active = True
```

##### Simple Example
```python
item_name = "Coffee"   # str
price = 4.50          # float
count = 2             # int
is_available = True   # bool

print(type(price))    # <class 'float'>
```

##### What to Remember
- `int` represents whole numbers; `float` represents decimals.
- `str` values are enclosed in single (`'`) or double (`"`) quotes.
- `bool` values are strictly capitalized: `True` or `False`.

---

<a id="operators--comparisons"></a>
#### Operators & Comparisons

##### What it is
Symbols that perform calculations, compare values, or combine logical expressions.

##### Why it exists
Enables arithmetic computations and decision-making logic in programs.

##### Syntax
```python
# Arithmetic: +, -, *, /, //, %, **
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
```

##### Simple Example
```python
cart_total = 45.00
shipping_threshold = 50.00
is_member = True

free_shipping = (cart_total >= shipping_threshold) or is_member
print(free_shipping)  # True
```

##### What to Remember
- Use `==` to test equality; `=` is strictly for assignment.
- `/` always returns a float; `//` performs floor (integer) division.
- `%` (modulo) yields the remainder of a division.

##### Common Mistake
**Wrong:**
```python
if status = "active":
    print("Welcome")
```
**Correct:**
```python
if status == "active":
    print("Welcome")
```
Single `=` attempts to assign a variable inside an `if` statement, causing a syntax error.

---

<a id="conditional-statements"></a>
#### Conditional Statements

##### What it is
Control flow structures that execute specific blocks of code based on boolean conditions.

##### Why it exists
Allows code to branch and react dynamically to different inputs or states.

##### Syntax
```python
if condition1:
    # execute if condition1 is True
elif condition2:
    # execute if condition2 is True
else:
    # execute if all above are False
```

##### Simple Example
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)  # B
```

##### What to Remember
- Conditions are evaluated top-to-bottom; execution stops after the first `True` branch.
- Indentation (4 spaces) defines the code block inside each branch.
- `elif` and `else` are optional.

---

<a id="loops"></a>
#### Loops

##### What it is
Structures that repeat a block of code multiple times or iterate over a sequence.

##### Why it exists
Eliminates repetitive code when processing items in a collection or running tasks until a condition is met.

##### Syntax
```python
# for loop
for item in sequence:
    # repeat code

# while loop
while condition:
    # repeat code
```

##### Simple Example
```python
# for loop example
temperatures = [68, 72, 75]
for temp in temperatures:
    if temp > 70:
        print(f"Warm day: {temp}°F")

# break & continue control
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # skip rest of iteration
    if count == 5:
        break     # exit loop completely
    print(count)
```

##### What to Remember
- `for` loops iterate over a known sequence; `while` loops run until a condition turns `False`.
- `break` exits the loop immediately.
- `continue` skips the remainder of the current iteration and jumps to the next.
- `pass` acts as a placeholder doing nothing.

##### Common Mistake
**Wrong:**
```python
i = 0
while i < 3:
    print(i)
```
**Correct:**
```python
i = 0
while i < 3:
    print(i)
    i += 1
```
Forgetting to update the loop variable in a `while` loop creates an infinite loop.

---

## 2. Collections

<a id="indexing--slicing"></a>
#### Indexing & Slicing

##### What it is
A syntax mechanism to access individual items or sub-ranges from ordered sequences like lists, tuples, and strings.

##### Why it exists
Allows rapid extraction, inspection, or manipulation of elements in ordered data structures.

##### Syntax
```python
sequence[index]               # Single element
sequence[start:stop:step]      # Slice (stop is exclusive)
```

##### Simple Example
```python
colors = ["red", "green", "blue", "yellow", "purple"]

print(colors[0])       # "red" (first)
print(colors[-1])      # "purple" (last)
print(colors[1:4])     # ['green', 'blue', 'yellow']
```

##### What to Remember
- Python indexing is 0-based.
- Negative indices count backward from the end (`-1` is the last item).
- Slicing `[start:stop]` includes `start` but excludes `stop`.

---

<a id="lists--list-methods"></a>
#### Lists & List Methods

##### What it is
An ordered, mutable sequence of items enclosed in square brackets `[]`.

##### Why it exists
Stores collected items in order where addition, removal, or modification is needed.

##### Syntax
```python
my_list = [item1, item2, item3]
```

##### Simple Example
```python
orders = ["order_101", "order_102"]

orders.append("order_103")      # Add to end
orders.insert(0, "priority_0")  # Insert at index
orders.remove("order_102")      # Remove by value
last_order = orders.pop()       # Remove & return last

print(orders)      # ['priority_0', 'order_101']
print(last_order)  # 'order_103'
```

##### What to Remember
- Lists retain insertion order.
- Lists are mutable (can be changed in-place).
- Common methods: `.append()`, `.extend()`, `.pop()`, `.remove()`, `.sort()`.

##### Common Mistake
**Wrong:**
```python
numbers = [3, 1, 2]
sorted_numbers = numbers.sort()
print(sorted_numbers)  # None!
```
**Correct:**
```python
numbers = [3, 1, 2]
numbers.sort()  # Modifies list in place
# OR: sorted_numbers = sorted(numbers)
```
In-place list methods like `.sort()` and `.append()` return `None`, not the modified list.

---

<a id="tuples"></a>
#### Tuples

##### What it is
An ordered, immutable sequence of items enclosed in parentheses `()`.

##### Why it exists
Stores fixed data that should not be accidentally modified or corrupted during execution.

##### Syntax
```python
my_tuple = (item1, item2)
```

##### Simple Example
```python
screen_res = (1920, 1080)
width, height = screen_res  # Unpacking

print(f"Width: {width}, Height: {height}")
```

##### What to Remember
- Tuples cannot be modified after creation (no appending or reassigning elements).
- Faster and more memory-efficient than lists.
- A single-element tuple requires a trailing comma: `single = (5,)`.

---

<a id="sets"></a>
#### Sets

##### What it is
An unordered collection of unique elements enclosed in curly braces `{}`.

##### Why it exists
Eliminates duplicate values and enables high-performance mathematical set operations (intersections, unions).

##### Syntax
```python
my_set = {item1, item2}
```

##### Simple Example
```python
raw_tags = ["python", "code", "python", "data"]
unique_tags = set(raw_tags)

unique_tags.add("ai")
print(unique_tags)  # {'python', 'code', 'data', 'ai'}
print("code" in unique_tags)  # True (O(1) lookup)
```

##### What to Remember
- Sets do NOT maintain order and do NOT allow indexing or slicing.
- Duplicates are silently discarded automatically.
- Item membership tests (`item in set`) are extremely fast.

---

<a id="dictionaries--dictionary-methods"></a>
#### Dictionaries & Dictionary Methods

##### What it is
A collection of key-value pairs enclosed in curly braces `{}` with `key: value` syntax.

##### Why it exists
Allows quick lookups of values associated with unique keys, similar to a real-world dictionary or database record.

##### Syntax
```python
my_dict = {"key1": value1, "key2": value2}
```

##### Simple Example
```python
employee = {
    "name": "Sarah",
    "role": "Developer",
    "salary": 85000
}

employee["department"] = "Engineering"  # Add key-value
role = employee.get("role", "N/A")      # Safe lookup

print(employee.keys())    # dict_keys(['name', 'role', 'salary', 'department'])
print(employee.values())  # dict_values(['Sarah', 'Developer', 85000, 'Engineering'])
```

##### What to Remember
- Keys must be unique and immutable (strings, numbers, tuples).
- Accessing a non-existent key with `dict[key]` raises `KeyError`; use `dict.get(key)` to avoid crashes.
- Iterate over keys and values using `for key, val in dict.items():`.

---

<a id="string-methods"></a>
#### String Methods

##### What it is
Built-in functions designed to transform, inspect, or format string data.

##### Why it exists
Simplifies text processing, cleaning, and formatting without writing manual parsing logic.

##### Syntax
```python
formatted_string = original_string.method_name()
```

##### Simple Example
```python
raw_email = "  USER@Example.com \n"
clean_email = raw_email.strip().lower()

words = "apple,banana,cherry".split(",")
joined = "-".join(words)

print(clean_email)  # "user@example.com"
print(joined)       # "apple-banana-cherry"
```

##### What to Remember
- Strings are immutable; string methods return *new* strings rather than altering the original string.
- Key methods: `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, `.join()`.

---

## 3. Functions & Scope

<a id="functions"></a>
#### Functions

##### What it is
A reusable block of organized code defined using the `def` keyword that executes when called.

##### Why it exists
Prevents code duplication, improves readability, and organizes complex logic into manageable modular units.

##### Syntax
```python
def function_name(parameter1, parameter2):
    # code logic
    return result
```

##### Simple Example
```python
def calculate_tax(amount, tax_rate):
    return amount * tax_rate

bill_tax = calculate_tax(100.0, 0.08)  # 100.0 & 0.08 are arguments
print(bill_tax)  # 8.0
```

##### Mental Model
- **Parameters vs Arguments:**
  - **Parameters:** The placeholder variables defined in the function header (the *slots*).
  - **Arguments:** The actual values passed into the function when calling it (the *data plugged in*).

##### What to Remember
- Functions define scope for inner variables.
- If a function lacks an explicit `return` statement, it returns `None` by default.

---

<a id="return-vs-print"></a>
#### Return vs Print

##### What it is
`print()` outputs text to the screen console; `return` sends a value back from a function to the caller.

##### Why it exists
Distinguishes between presenting info to a human user (`print`) versus handing data back to the program for further processing (`return`).

##### Syntax
```python
# print displays info
print(value)

# return passes data back
def func():
    return value
```

##### Simple Example
```python
def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

res1 = add_with_print(3, 4)   # Displays 7, but res1 is None
res2 = add_with_return(3, 4)  # Nothing printed, but res2 is 7
total = res2 * 10             # Works! total = 70
```

##### Mental Model
- **`print()`** is like writing a number on a whiteboard for people to read.
- **`return`** is like handing a envelope containing money to someone so they can spend it in the next step.

##### What to Remember
- You cannot perform further calculations on the output of `print()`.
- `return` immediately halts execution of the function and exits.

##### Common Mistake
**Wrong:**
```python
def get_user_name():
    print("Alice")

name = get_user_name()
print("Hello " + name)  # TypeError: can only concatenate str (not "NoneType") to str
```
**Correct:**
```python
def get_user_name():
    return "Alice"

name = get_user_name()
print("Hello " + name)  # Works
```

---

<a id="default-parameters"></a>
#### Default Parameters

##### What it is
Fallback values assigned to parameters in function definitions, used if no argument is provided during invocation.

##### Why it exists
Makes function calls flexible by allowing optional parameters with sensible standard values.

##### Syntax
```python
def function_name(param1, param2=default_value):
    # code logic
```

##### Simple Example
```python
def create_account(username, account_type="standard"):
    return f"User {username} created with {account_type} account."

print(create_account("alex"))                  # Uses default "standard"
print(create_account("jordan", "premium"))    # Overrides default
```

##### What to Remember
- Parameters with default values must follow non-default parameters in the function definition.
- Avoid using mutable objects (like empty lists `[]`) as default parameter values.

---

<a id="scope"></a>
#### Scope

##### What it is
The region of a program where a specific variable is recognized and accessible.

##### Why it exists
Prevents variable naming conflicts and isolates function logic from global state.

##### Syntax
```python
global_var = "Global"

def my_func():
    local_var = "Local"
    print(global_var)  # Accessible
```

##### Simple Example
```python
balance = 500  # Global scope

def deposit(amount):
    global balance
    fee = 2.50  # Local scope
    balance += (amount - fee)

deposit(100)
print(balance)  # 597.5
# print(fee)    # NameError: name 'fee' is not defined
```

##### Mental Model
- **Local vs Global:**
  - **Local scope** is inside a house's room—only visible inside that room.
  - **Global scope** is out on the street—visible to every house on the block.

##### What to Remember
- Variables created inside a function are local to that function.
- To modify a global variable inside a function, use the `global` keyword.

---

<a id="args-and-kwargs"></a>
#### *args and **kwargs

##### What it is
Special parameter syntaxes that allow functions to accept an arbitrary number of positional (`*args`) or keyword (`**kwargs`) arguments.

##### Why it exists
Enables flexible function definitions when the exact count of incoming inputs is unknown beforehand.

##### Syntax
```python
def function_name(*args, **kwargs):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
```

##### Simple Example
```python
def summarize_order(customer, *items, **details):
    print(f"Customer: {customer}")
    print(f"Items: {items}")          # Tuple of items
    print(f"Details: {details}")      # Dict of extra metadata

summarize_order("Sam", "Laptop", "Mouse", payment="Card", express=True)
```

##### Mental Model
- **`*args`** collects extra unassigned items into a single **backpack (tuple)**.
- **`**kwargs`** collects extra labeled packages into a single **filing cabinet (dictionary)**.

##### What to Remember
- `*args` packs positional arguments into a `tuple`.
- `**kwargs` packs keyword arguments into a `dict`.
- The names `args` and `kwargs` are conventions; the asterisks (`*` and `**`) perform the actual packing.

---

<a id="lambda-functions"></a>
#### Lambda Functions

##### What it is
Small, inline, anonymous functions evaluated as a single expression.

##### Why it exists
Allows quick inline definitions for short tasks (such as sorting or filtering) without declaring a full `def` function block.

##### Syntax
```python
lambda argument1, argument2: expression
```

##### Simple Example
```python
products = [("Shirt", 25), ("Pants", 40), ("Socks", 10)]

# Sort products by price (second element in tuple)
products.sort(key=lambda item: item[1])

print(products)  # [('Socks', 10), ('Shirt', 25), ('Pants', 40)]
```

##### What to Remember
- Lambda functions are restricted to a single expression.
- They automatically return the result of that single expression.

---

<a id="list-comprehensions"></a>
#### List Comprehensions

##### What it is
A concise, elegant syntax for constructing a new list from an existing iterable in a single line.

##### Why it exists
Replaces multi-line `for` loop blocks with clean, readable code when transforming or filtering lists.

##### Syntax
```python
[expression for item in iterable if condition]
```

##### Simple Example
```python
prices = [10, 25, 50, 80, 100]

# Double prices over 30
discounted = [p * 0.9 for p in prices if p > 30]

print(discounted)  # [45.0, 72.0, 90.0]
```

##### Mental Model
Read list comprehensions inside-out:
1. `for item in iterable`: Start with the loop source.
2. `if condition`: Filter down items.
3. `expression`: Apply transformation to remaining items.

##### What to Remember
- Always enclosed in square brackets `[]`.
- Keep them simple; if logic gets complex, revert to a standard `for` loop for readability.

---

## 4. Errors & Modules

<a id="error-handling"></a>
#### Error Handling

##### What it is
A construct (`try`, `except`, `finally`, `raise`) that catches and handles runtime exceptions gracefully without crashing the program.

##### Why it exists
Prevents unexpected failure when working with volatile inputs, network calls, or missing files.

##### Syntax
```python
try:
    # Code that might fail
except SpecificError as e:
    # Code to execute if error occurs
finally:
    # Code that ALWAYS runs regardless
```

##### Simple Example
```python
def divide_payment(total, num_people):
    try:
        return total / num_people
    except ZeroDivisionError:
        print("Cannot divide among zero people.")
        return 0.0
    finally:
        print("Transaction processing attempt completed.")

print(divide_payment(100, 0))
```

##### What to Remember
- Always specify concrete exception types (e.g., `ValueError`, `KeyError`) instead of catching bare `Exception`.
- `finally` executes unconditionally, making it ideal for cleanup tasks (closing files/connections).
- Use `raise ValueError("custom message")` to manually throw an error.

---

<a id="modules--imports"></a>
#### Modules & Imports

##### What it is
Python files (`.py`) containing reusable code definitions that can be loaded into other scripts using `import`.

##### Why it exists
Promotes code reuse across multiple files and enables access to Python's extensive Standard Library and external packages.

##### Syntax
```python
import module_name
from module_name import specific_function
import module_name as alias
```

##### Simple Example
```python
import math
from datetime import date

radius = 5
area = math.pi * (radius ** 2)
today = date.today()

print(f"Area: {area:.2f}, Date: {today}")
```

##### What to Remember
- Place imports at the top of the script file.
- Aliases (`import pandas as pd`) keep code concise when referencing heavily used modules.

---

## 5. Classes & Object-Oriented Programming

<a id="classes--objects"></a>
#### Classes & Objects

##### What it is
A **class** is a blueprint/template; an **object** is an individual instance constructed from that blueprint.

##### Why it exists
Groups related state (data/attributes) and behavior (functions/methods) into self-contained real-world entities.

##### Syntax
```python
class ClassName:
    # blueprint definitions

object_instance = ClassName()
```

##### Simple Example
```python
class Car:
    pass

car1 = Car()
car2 = Car()

print(car1)  # <__main__.Car object at 0x...>
```

##### What to Remember
- Class names use `PascalCase` convention.
- An object is created by calling the class name as if it were a function.

---

<a id="init--method"></a>
#### \_\_init\_\_ Method

##### What it is
The special initialization method (constructor) automatically called when a new instance of a class is created.

##### Why it exists
Sets up the initial attributes and state of a newly created object.

##### Syntax
```python
class ClassName:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```

##### Simple Example
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Alice", 150.0)
print(acc1.owner, acc1.balance)  # Alice 150.0
```

##### Mental Model
`__init__` is the **factory setup line**. When you order a new car or open a bank account, `__init__` runs automatically to stamp the custom name and starting values onto the fresh account card.

##### What to Remember
- Starts and ends with double underscores (dunder).
- Always takes `self` as its first parameter.
- Executes automatically during instantiation—you never call `acc1.__init__()` manually.

---

<a id="self-keyword"></a>
#### self Keyword

##### What it is
A reference variable representing the **specific instance** of the class currently executing the method.

##### Why it exists
Allows methods to read and modify attributes belonging to *that specific instance*, distinguishing it from all other instances of the same class.

##### Syntax
```python
class ClassName:
    def method_name(self):
        print(self.attribute_name)
```

##### Detailed Simple Example
```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # self.brand attaches 'brand' to THIS instance

    def describe(self):
        print(f"Car brand: {self.brand}")

car1 = Car("Toyota")
car2 = Car("Honda")

car1.describe()  # Prints: Car brand: Toyota
car2.describe()  # Prints: Car brand: Honda
```

##### Breakdown of `self.brand` vs `car1.brand`
When you execute `car1 = Car("Toyota")`:
- Inside `__init__`, `self` points directly to the newly allocated object `car1`.
- `self.brand = "Toyota"` creates an attribute named `brand` on `car1`.
- Outside the class, you access it as `car1.brand`.
- Inside class methods, you access it via `self.brand`.
- When you call `car1.describe()`, Python automatically passes `car1` as the `self` argument behind the scenes!

##### Mental Model
`self` is the pronoun **"my"** or **"myself"**.
When `car1` says `self.brand`, it means *"my brand"*. When `car2` says `self.brand`, it means *"my brand"*. It ensures each object accesses its own stored data.

##### What to Remember
- Always list `self` as the first parameter of any instance method.
- You do NOT pass `self` manually when invoking the method (`car1.describe()`).
- Without `self.`, variables inside methods are treated as temporary local variables that disappear when the method finishes.

##### Common Mistake
**Wrong:**
```python
class Employee:
    def __init__(self, name):
        name = name  # Forgot self.!

    def greet(self):
        print("Hello " + self.name)
```
**Correct:**
```python
class Employee:
    def __init__(self, name):
        self.name = name  # Attached to object

    def greet(self):
        print("Hello " + self.name)
```

---

<a id="instance-vs-class-attributes"></a>
#### Instance vs Class Attributes

##### What it is
- **Instance attributes:** Variables unique to each instance created inside `__init__`.
- **Class attributes:** Variables shared equally across *all* instances defined directly in the class body.

##### Why it exists
Differentiates between data unique to an individual object versus constants or state shared across the entire class population.

##### Syntax
```python
class ClassName:
    class_attr = value  # Shared by all

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr  # Unique to each
```

##### Simple Example
```python
class Student:
    school_name = "Tech Academy"  # Class attribute

    def __init__(self, name):
        self.name = name          # Instance attribute

s1 = Student("Leo")
s2 = Student("Maya")

print(s1.school_name, s1.name)  # Tech Academy Leo
print(s2.school_name, s2.name)  # Tech Academy Maya
```

##### Mental Model
- **Instance Attribute:** Your personal driver's license number (unique to you).
- **Class Attribute:** The speed limit on the highway (applies to every driver in the class).

##### What to Remember
- Modifying a class attribute via `ClassName.class_attr` updates it for all instances simultaneously.
- Modifying `s1.school_name` creates an instance attribute that overrides the class attribute for `s1` only.

---

<a id="inheritance--method-overriding"></a>
#### Inheritance & Method Overriding

##### What it is
- **Inheritance:** A mechanism where a child class inherits attributes and methods from a parent class.
- **Method Overriding:** Redefining a inherited method in the child class to customize its behavior.

##### Why it exists
Promotes code reuse, reduces duplication, and allows specialized classes to build upon general base classes.

##### Syntax
```python
class BaseClass:
    # Parent logic

class DerivedClass(BaseClass):
    # Child inherits BaseClass and can override methods
```

##### Simple Example
```python
class User:
    def __init__(self, username):
        self.username = username

    def get_permissions(self):
        return "Basic member access"

class AdminUser(User):  # Inherits from User
    def get_permissions(self):  # Method Overriding
        return "Full administrative access"

u = User("guest1")
a = AdminUser("superadmin")

print(u.get_permissions())  # Basic member access
print(a.get_permissions())  # Full administrative access
```

##### Mental Model
- **Inheritance** is like inheriting your parents' house.
- **Method Overriding** is repainting the living room after moving in—it's still a house, but customized for your specific needs.

##### What to Remember
- Use `super().__init__(...)` inside a child class `__init__` to run parent initialization logic.
- A child class inherits everything from the parent unless explicitly overridden.

---

<a id="mutable-vs-immutable-objects"></a>
#### Mutable vs Immutable Objects

##### What it is
- **Mutable:** Objects whose state/content can be modified in-place after creation (Lists, Dicts, Sets).
- **Immutable:** Objects whose state cannot be changed in-place after creation (Ints, Floats, Strings, Tuples, Booleans).

##### Why it exists
Determines how Python handles memory allocation, assignment, function arguments, and dictionary keys.

##### Simple Example
```python
# Immutable (String)
s = "hello"
# s[0] = "H"  # TypeError: 'str' object does not support item assignment
s = s.upper() # Creates a BRAND NEW string in memory

# Mutable (List)
lst = [1, 2, 3]
lst.append(4) # Modifies existing object in place
print(lst)    # [1, 2, 3, 4]
```

##### Mental Model
- **Immutable:** A printed wooden plaque. You can't rewrite letters on it; if you want a change, you must make a new plaque.
- **Mutable:** A whiteboard. You can erase and rewrite parts of it anytime without replacing the board.

##### What to Remember
- Passing mutable objects (lists/dicts) into functions allows the function to modify the original object.
- Only immutable objects can be used as dictionary keys or set elements.
