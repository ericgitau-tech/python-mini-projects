# 🐍 Python Programming Reference Guide

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Learning](https://img.shields.io/badge/Learning-In%20Progress-orange?style=for-the-badge)

**A comprehensive guide to Python fundamentals and best practices**

[Features](#-features) • [Getting Started](#-getting-started) • [Core Concepts](#-core-concepts) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Core Concepts](#-core-concepts)
  - [Variables & Data Types](#-variables--data-types)
  - [Control Flow](#-control-flow)
  - [Loops](#-loops)
  - [Collections](#-collections)
  - [Functions](#-functions)
  - [Object-Oriented Programming](#-object-oriented-programming)

---

## 🎯 Overview

This repository serves as a **complete reference guide** for Python programming fundamentals. Whether you're a beginner or brushing up on concepts, you'll find clear explanations, practical examples, and best practices.

## ✨ Features

- ✅ **Clear Definitions** - Easy-to-understand explanations of Python concepts
- 💡 **Practical Examples** - Real-world code snippets for each topic
- 🎨 **Clean Formatting** - Well-organized and visually appealing documentation
- 🚀 **Beginner Friendly** - Perfect for those starting their Python journey
- 📚 **Comprehensive Coverage** - From basics to OOP concepts

---

## 🔑 Core Concepts

### 📦 Variables & Data Types

#### 🔹 Variable

A **variable** is a named container used to store data in memory. The value can be of different data types such as strings, integers, floats, or booleans.

```python
age = 20
name = "Emmanuel"
is_student = True
height = 5.9
```

**Key Points:**
- Variables are dynamically typed in Python
- Once assigned, variables behave like the value they contain
- Naming convention: Use `snake_case` for variable names

---

#### 🔹 Type Casting

**Type casting** converts a value from one data type to another using built-in functions.

| Function | Description | Example |
|----------|-------------|---------|
| `str()` | Converts to string | `str(25)` → `"25"` |
| `int()` | Converts to integer | `int("25")` → `25` |
| `float()` | Converts to float | `float("25.5")` → `25.5` |
| `bool()` | Converts to boolean | `bool(1)` → `True` |

```python
# Converting string input to integer
age = "18"
age = int(age)  # Now age is 18 (integer)

# Converting for calculations
price = "99.99"
total = float(price) * 2  # 199.98
```

---

#### 🔹 Input Function

The `input()` function prompts users to enter data during program execution.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Type casting for numerical operations

print(f"Hello {name}, you are {age} years old!")
```

⚠️ **Important:** `input()` always returns a **string**. Use type casting for numerical operations.

---

### 🎛️ Control Flow

#### 🔹 If Statement

The `if` statement enables **decision-making** in programs by executing code based on conditions.

```python
marks = 75

if marks >= 70:
    print("Grade: A")
elif marks >= 50:
    print("Grade: B")
else:
    print("Grade: C")
```

**Comparison Operators:**
```python
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

📝 **Note:** Proper indentation is **mandatory** in Python!

---

#### 🔹 Logical Operators

Logical operators evaluate **multiple conditions** in a single statement.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | All conditions must be `True` | `age >= 18 and has_id` |
| `or` | At least one condition must be `True` | `is_weekend or is_holiday` |
| `not` | Inverts the condition | `not is_raining` |

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("✅ Access granted")
else:
    print("❌ Access denied")
```

---

#### 🔹 Conditional Expression (Ternary Operator)

A **one-line shortcut** for the `if-else` statement.

**Syntax:**
```python
value_if_true if condition else value_if_false
```

**Example:**
```python
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Minor

# Inline with print
print("Eligible" if age >= 18 else "Not Eligible")
```

---

#### 🔹 Match-Case Statement (Switch)

A cleaner alternative to multiple `elif` statements (Python 3.10+).

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4 | 5:  # Multiple cases
        print("Thursday or Friday")
    case _:  # Default case
        print("Weekend or Invalid")
```

**Benefits:**
- ✅ More readable than multiple `elif`
- ✅ Easier to maintain
- ✅ Supports pattern matching

---

### 🔄 Loops

#### 🔹 While Loop

Executes code repeatedly **as long as** a condition remains `True`.

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

# Output: Count: 1, 2, 3, 4, 5
```

**Use Cases:**
- Unknown number of iterations
- Input validation
- Game loops

---

#### 🔹 For Loop

Executes code a **fixed number of times** by iterating over sequences.

```python
# Using range
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# With enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

---

#### 🔹 Nested Loop

A **loop inside another loop**. The inner loop completes all iterations for each iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(f"Outer: {i}, Inner: {j}")

# Output:
# Outer: 1, Inner: 1
# Outer: 1, Inner: 2
# Outer: 2, Inner: 1
# Outer: 2, Inner: 2
# Outer: 3, Inner: 1
# Outer: 3, Inner: 2
```

**Common Use Cases:**
- Creating multiplication tables
- Working with 2D arrays/matrices
- Pattern printing

---

### 📚 Collections

A **collection** stores multiple values in a single variable.

#### 🔹 List `[]`

**Ordered**, **mutable**, allows **duplicates**.

```python
fruits = ["apple", "banana", "apple"]
fruits.append("orange")
fruits.remove("apple")
print(fruits[0])  # Access by index
```

**Common Methods:**
```python
fruits.append("mango")      # Add item
fruits.insert(0, "grape")   # Insert at index
fruits.pop()                # Remove last item
fruits.sort()               # Sort list
```

---

#### 🔹 Set `{}`

**Unordered**, **mutable**, **no duplicates**.

```python
numbers = {1, 2, 3, 3}  # Duplicate 3 is ignored
numbers.add(4)
numbers.remove(1)
```

**Use Cases:**
- Removing duplicates from a list: `unique = list(set(my_list))`
- Mathematical set operations (union, intersection)

---

#### 🔹 Tuple `()`

**Ordered**, **immutable**, allows **duplicates**, **faster** than lists.

```python
coordinates = (10, 20, 10)
x, y, z = coordinates  # Tuple unpacking
```

**When to Use:**
- Data that shouldn't change (constants)
- Function return values
- Dictionary keys (lists can't be keys)

---

#### 🔹 Dictionary `{}`

Stores **key-value pairs**. Keys must be **unique**.

```python
student = {
    "name": "Emmanuel",
    "age": 20,
    "course": "Engineering"
}

# Accessing values
print(student["name"])
print(student.get("age"))

# Adding/updating
student["gpa"] = 3.8

# Iterating
for key, value in student.items():
    print(f"{key}: {value}")
```

---

### 🧰 Functions

#### 🔹 Function Definition

A **reusable block of code** that performs a specific task.

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet("Emmanuel")
```

**Best Practices:**
- Use descriptive function names
- Add docstrings to explain purpose
- Keep functions focused on one task

---

#### 🔹 Return Statement

**Sends a result back** to the caller and **ends function execution**.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
```

---

#### 🔹 Default Arguments

Parameters with **predefined values** used when no argument is provided.

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Emmanuel")              # Hello, Emmanuel!
greet("Emmanuel", "Welcome")   # Welcome, Emmanuel!
```

**Argument Order:**
1. Positional arguments
2. Default arguments
3. Keyword arguments
4. Arbitrary arguments (`*args`, `**kwargs`)

---

#### 🔹 Keyword Arguments

Arguments preceded by parameter names for **better readability** and **flexible ordering**.

```python
def student_info(name, age, course):
    print(f"{name} is {age} years old, studying {course}")

# Arguments in any order
student_info(course="Engineering", name="Emmanuel", age=20)
```

---

#### 🔹 *args and **kwargs

Accept a **variable number of arguments**.

**`*args`** - Positional arguments (stored as tuple):
```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))  # 10
```

**`**kwargs`** - Keyword arguments (stored as dictionary):
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Emmanuel", age=20, country="Kenya")
```

**Unpacking Operator `*`:**
```python
numbers = [1, 2, 3]
print(*numbers)  # 1 2 3
```

---

### 🎨 Advanced Concepts

#### 🔹 Iterables

Any object that can return elements **one at a time**.

```python
# All iterables
for char in "Python":        # String
    print(char)

for num in [1, 2, 3]:        # List
    print(num)

for key in {"a": 1, "b": 2}: # Dictionary
    print(key)
```

---

#### 🔹 Membership Operators

Test if a value **exists in a sequence**.

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True

# Works with strings
print("Py" in "Python")       # True
```

---

#### 🔹 List Comprehension

A **concise way** to create lists.

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Examples:**
```python
# Square numbers
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Filter even squares
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
# [4, 16]

# Convert to uppercase
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
# ["HELLO", "WORLD"]
```

---

#### 🔹 Format Specifiers

Control how values are **displayed in strings**.

**Syntax:** `{value:flags}`

```python
price = 1234.5678

# 2 decimal places
print(f"Price: ${price:.2f}")        # $1234.57

# Thousands separator
print(f"Price: ${price:,.2f}")       # $1,234.57

# Alignment
name = "Python"
print(f"{name:>10}")   # Right align:      Python
print(f"{name:<10}")   # Left align:  Python
print(f"{name:^10}")   # Center:       Python
```

---

#### 🔹 Modules

A **file containing Python code** that can be imported and reused.

```python
# Built-in modules
import math
print(math.sqrt(16))  # 4.0

import random
print(random.randint(1, 10))

# Import specific functions
from datetime import datetime
print(datetime.now())

# Alias imports
import pandas as pd
```

**Benefits:**
- ✅ Code organization
- ✅ Reusability
- ✅ Easier maintenance

---

### 🏗️ Object-Oriented Programming

#### 🔹 Object

A bundle of related **attributes** (variables) and **methods** (functions).

**Real-world examples:**
- 📱 Phone → Attributes: brand, model | Methods: call(), text()
- 📖 Book → Attributes: title, author | Methods: open(), close()

---

#### 🔹 Class

A **blueprint** for creating objects.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

# Creating objects
student1 = Student("Emmanuel", 20)
student1.introduce()
```

**`__init__` method:**
- Constructor that initializes object attributes
- Called automatically when object is created

---

#### 🔹 Class Variable

A variable **shared among all instances** of a class.

```python
class Student:
    school = "Kenyatta University"  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable

student1 = Student("Emmanuel")
student2 = Student("John")

print(student1.school)  # Kenyatta University
print(student2.school)  # Kenyatta University
```

**Class vs Instance Variables:**
- **Class variable:** Shared by all objects
- **Instance variable:** Unique to each object

---

#### 🔹 Inheritance

Allows a class to **inherit attributes and methods** from another class.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is speaking")

class Student(Person):  # Student inherits from Person
    def __init__(self, name, student_id):
        super().__init__(name)  # Call parent constructor
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying")

student = Student("Emmanuel", "S12345")
student.speak()   # Inherited method
student.study()   # Own method
```

**Benefits:**
- ✅ Code reusability
- ✅ Logical hierarchy
- ✅ Easy to extend functionality

---

## 🚀 Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/python-reference-guide.git
   ```

2. **Navigate to the directory**
   ```bash
   cd python-reference-guide
   ```

3. **Start learning!** Browse through the concepts and run the examples.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add more concepts or improve existing ones:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-concept`)
3. Commit your changes (`git commit -m 'Add new concept'`)
4. Push to the branch (`git push origin feature/new-concept`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Eric Gitau** - [@yourhandle](https://twitter.com/yourhandle)

Project Link: [https://github.com/yourusername/python-reference-guide](https://github.com/ericgitau-tech/python-mini-projects.git)

---

<div align="center">

**⭐ If you found this helpful, please give it a star! ⭐**

Made with ❤️ by Emmanuel

</div>
