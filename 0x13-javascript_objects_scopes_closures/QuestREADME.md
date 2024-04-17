INSTRUCTIONS FOR 0x13. JavaScript - Objects, Scopes and Closures PROJECT
Resources
Read or watch:

JavaScript object basics: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics
Object-oriented JavaScript (read all examples!): https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
Class - ES6: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
super - ES6: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super
extends - ES6: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends
Object prototypes: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes
Inheritance in JavaScript: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
Closures: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
this/self: https://alistapart.com/article/getoutbindingsituations/
Modern JS: https://github.com/mbeaudru/modern-js-cheatsheet

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JavaScript programming is amazing
How to create an object in JavaScript
What this means
What undefined means
Why the variable type and scope is important
What is a closure
What is a prototype
How to inherit an object from another

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
You are not allowed to use var
More Info
Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global

Tasks
0. Rectangle #0
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an empty class Rectangle that defines a rectangle:

You must use the class notation for defining your class
File: 0-rectangle.js

1. Rectangle #1
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
File: 1-rectangle.js

2. Rectangle #2
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
File: 2-rectangle.js

3. Rectangle #3
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
File: 3-rectangle.js

4. Rectangle #4
mandatory
Score: 90.91% (Checks completed: 90.91%)
Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2
File: 4-rectangle.js

5. Square #0
mandatory
Score: 90.91% (Checks completed: 90.91%)
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

You must use the class notation for defining your class and extends
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())
File: 5-square.js

6. Square #1
mandatory
Score: 90.91% (Checks completed: 90.91%)
Write a class Square that defines a square and inherits from Square of 5-square.js:

You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
File: 6-square.js

7. Occurrences
mandatory
Score: 92.31% (Checks completed: 92.31%)
Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
File: 7-occurrences.js

8. Esrever
mandatory
Score: 90.0% (Checks completed: 90.0%)
Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
File: 8-esrever.js

9. Log me
mandatory
Score: 90.0% (Checks completed: 90.0%)
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>
File: 9-logme.js

10. Number conversion
mandatory
Score: 90.0% (Checks completed: 90.0%)
Write a function that converts a number from base 10 to another base passed as argument:

Prototype: exports.converter = function (base)
You are not allowed to import any file
You are not allowed to declare any new variable (var, let, etc..)
File: 10-converter.js

11. Factor index
#advanced
Score: 100.0% (Checks completed: 100.0%)
Write a script that imports an array and computes a new array.

Your script must import list from the file 100-data.js
You must use a map. Tips
A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
Print both the initial list and the new list
File: 100-map.js

12. Sorted occurences
#advanced
Score: 90.91% (Checks completed: 90.91%)
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

Your script must import dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Print the new dictionary at the end
File: 101-sorted.js

13. Concat files
#advanced
Score: 88.89% (Checks completed: 88.89%)
Write a script that concats 2 files.

The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
File: 102-concat.js

