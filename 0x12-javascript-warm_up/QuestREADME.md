INSTRUCTIONS FOR 0x12. JavaScript - Warm up PROJECT

Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

Scripting (same as we did with Python)
Web front-end
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

Resources
Read or watch:

Writing JavaScript Code: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
Variables: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables
Data Types: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures
Operators: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
Operator Precedence:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
Controlling Program Flow: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling
Functions: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions
Objects and Arrays: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects
Intrinsic Objects: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects
Module patterns: https://darrenderidder.github.io/talks/ModulePatterns/#/
var, let and const: https://www.youtube.com/watch?v=sjyJBL5fkp8
JavaScript Tutorial: https://www.youtube.com/watch?v=vZBCTc9zHtI
Modern JS:https://github.com/mbeaudru/modern-js-cheatsheet

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JavaScript programming is amazing
How to run a JavaScript script
How to create variables and constants
What are differences between var, const and let
What are all the data types available in JavaScript
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use while and for loops
How to use break and continue statements
What is a function and how do you use functions
What does a function that does not use any return statement return
Scope of variables
What are the arithmetic operators and how to use them
How to manipulate dictionary
How to import a file
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
More Info
Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global

Tasks
0. First constant, first print
mandatory
Score: 65.0% (Checks completed: 100.0%)
Write a script that prints “JavaScript is amazing”:

You must create a constant variable called myVar with the value “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
File: 0-javascript_is_amazing.js

1. 3 languages
mandatory
Score: 54.17% (Checks completed: 83.33%)
Write a script that prints 3 lines:

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
File: 1-multi_languages.js

2. Arguments
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that prints a message depending of the number of arguments passed:

If no arguments are passed to the script, print “No argument”
If only one argument is passed to the script, print “Argument found”
Otherwise, print “Arguments found”
You must use console.log(...) to print all output
You are not allowed to use var
Reference: process.argv: https://nodejs.org/api/process.html#process_process_argv
File: 2-arguments.js

3. Value of my argument
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that prints the first argument passed to it:

If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length
File: 3-value_argument.js

4. Create a sentence
mandatory
Score: 65.0% (Checks completed: 100.0%)
Write a script that prints two arguments passed to it, in the following format: “ is ”

You must use console.log(...) to print all output
You are not allowed to use var
File: 4-concat.js

5. An Integer
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch
File: 5-to_integer.js

6. Loop to languages
mandatory
Score: 59.09% (Checks completed: 90.91%)
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use any if/else statement
You can use only one console.log
You must use a loop (while, for, etc.)
File: 6-multi_languages_loop.js

7. I love C
mandatory
Score: 65.0% (Checks completed: 100.0%)
Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)
File: 7-multi_c.js

8. Square
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
File: 8-square.js

9. Add
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var
File: 9-add.js

10. Factorial
mandatory
Score: 56.88% (Checks completed: 87.5%)
Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
File: 10-factorial.js

11. Second biggest!
mandatory
Score: 59.09% (Checks completed: 90.91%)
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
File: 11-second_biggest.js

12. Object
mandatory
Score: 55.71% (Checks completed: 85.71%)
Update this script to replace the value 12 with 89:

You are not allowed to use var
File: 12-object.js

13. Add file
mandatory
Score: 65.0% (Checks completed: 100.0%)
Write a function that returns the addition of 2 integers.

The function must be visible from outside
The name of the function must be add
You are not allowed to use var
Tip: https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html
File: 13-add.js

14. Const or not const
#advanced
Score: 65.0% (Checks completed: 100.0%)
Write a file that modifies the value of myVar to 333
Do you get it? Tweet! Post! Talk about it!

Hint: Scope

This exercise doesn’t pass semistandard so don’t worry about it.
File: 100-let_me_const.js

15. Call me Moby
#advanced
Score: 65.0% (Checks completed: 100.0%)
Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
File: 101-call_me_moby.js

16. Add me maybe
#advanced
Score: 65.0% (Checks completed: 100.0%)
Write a function that increments and calls a function.

The function must be visible from outside
Prototype: function (number, theFunction)
You are not allowed to use var
File: 102-add_me_maybe.js

17. Increment object
#advanced
Score: 55.71% (Checks completed: 85.71%)
Update this script by adding a new function incr that increments the integer value.

You are not allowed to use var
File: 103-object_fct.js

