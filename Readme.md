# Python Mini Project

## Definitions of terms in python

**Variable**
A container for a value (string, float, intergerr, booleen)
A variable behave as if it was the value it contains

**Typecasting**
The process of converting a varible from one data type to another
`str()`, `int()`, `float()`, `bool()`

**input()**
A function that prompts the user to enter data
Return the entered data as a string

**if**
Do some code only If some condition is true
Else do somthing else

**logical operators**
Evaluate multiple condition (or, and , not)
or = at least one condition must be True
and = both condition must be True
not - invert the condition (not False, not True)

**conditional expression**
A one-line shortcut for the if-else statement (ternary operator)
print or assign one of two value based on acondition
X if condition else Y


**format specifiers**
{:flags} format a value based on what flags are inserted

**while loop**
Excute some code WHILE some condition remains true

**for loop**
Excute a block of code a fixed number of times
You can iterate over a range, string, sequence, etc

**nested loop** 
A loop within another loop(outer, inner)
outer loop:
   inner loop:

**collection**
single "variable" used to store multiple value

List = [] ordered and changeble. Duplicate OK
Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
Tuple = () ordered and unchangeable. Duplicate OK .Faster

**dictionary**
a collection of {key:value} pairs
ordered and changeable. No duplicates

**function**
A block of reusable code
place () after the function name to invoke it

**return**
Statement used to end a function and a result back to the caller

**default argument**
A default value for certain parameters
default is used when that argument is omitted
make your fuction mor flexible, reduce # of arguments
1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

**keyword arguments**
an arguement precced by an identifier
help with readability
order of arguments doesn't matter
1.positional 2. default 3.KEYWORD 4. arbitary


**args** 
allows you to pass multiple non-key arguments
**kwargs**
allows you to pass multiple keyword-argument
*unpacking operator
1. positional 2. default 3. keyword 4. ARBITARY


**Iterables**
An object/collection that can return its elements one at a time
allowing it to be iterated over in a loop

**Member operators**
Used to test whether a value or variable is found in a sequence
(string, list, tuple, set or dictionary)
1. in
2. not in

**List comprehension**
A consise to create lists in python
Compact and easier to read than traditional loops
[expression for value in iterable if condition]

**Match-case statement (switch)**
An alternative to using many 'elif' statement excute some code if a value matches a 'case' 
Benefits: cleaner and sysntax is more readable

**module**
A file containing code you want to include in your program
use 'import' to include a module (built-in or your own)
usefull to break up a large program reusable separate files.

**object**
A "bundle" of related attributes (variable) and methods (functions)
  ex. phone, cup, book
  You need a "class" to create many objects
**class** (blueprint) used to design the structure and layout of an object

**class variable** 
  Shared among all instance of a class
  Defined outside the constructor
  Allow you to share data among all objects created from that class

**Inheritance**
Allow a class to inherit attributes and methods from another class
Help with code reusability and extensibility
class child(parent)