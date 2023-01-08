## 0x00. Python - Hello, World

#### Concepts
*For this project, we expect you to look at this concept:*
- [Python programming](https://alx-intranet.hbtn.io/concepts/550)
![Meme about Python and C](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)
### Author’s disclaimer
> Welcome to the Python world!
> 
> The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
> If you've already played with Python, don't worry, fun things will come.
> You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
> Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.
> 
> Enjoy!
> 
> - Guillaume
## Resources
**Read or watch:**

- [The Python tutorial](https://alx-intranet.hbtn.io/rltoken/JsFCs_NBzMAR7-XPAZ9BoA) *(only the first three chapters below)*
- [Whetting Your Appetite](https://alx-intranet.hbtn.io/rltoken/kifRlLG2iMX5AZiW8lrCMg)
- [Using the Python Interpreter](https://alx-intranet.hbtn.io/rltoken/RVpfAuagCo9SdfYeoHd6jg)
- [An Informal Introduction to Python](https://alx-intranet.hbtn.io/rltoken/bVps0ZPWq7qVZ7vc-eJGTw) *(Read up until “3.1.2. Strings” included)*
- [How To Use String Formatters in Python 3](https://alx-intranet.hbtn.io/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
- [Learn to Program](https://alx-intranet.hbtn.io/rltoken/szBsJ-Qyig_RrImN7RGlOg)
- [Pycodestyle – Style Guide for Python Code](https://alx-intranet.hbtn.io/rltoken/tgYt-0zVy1T4sDlE9ohxnA)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/TYWTMEj3W1HhTHqMKu8kWA), **without the help of Google:**

### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## More Info
### Zen
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Pycodestyle
`Pycodestyle` is now the [new standard of Python style code](https://alx-intranet.hbtn.io/rltoken/UQ25jC6sA5XqZl6ZZIdAaw)
![an image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg)

## Tasks

#### 0. Run Python file

- `0-run` - a Shell script that runs a Python script.

#### 1. Run inline

- `1-run_inline` - a Shell script that runs Python code.

#### 2. Hello, print

- `2-print.py` -  a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

#### 3. Print integer

- `3-print_number.py` - prints the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

#### 4. Print float

- `4-print_float.py` - prints the float stored in the variable `number` with a precision of 2 digits.

#### 5. Print string

- `5-print_string.py` - prints 3 times a string stored in the variable `str`, followed by its first 9 characters.

#### 6. Play with strings

- `6-concat.py` - prints `Welcome to Holberton School!`

#### 7. Copy - Cut - Paste

- `7-edges.py` - prints some letters of a string

#### 8. Create a new sentence

- `8-concat_edges.py` - prints `object-oriented programming with Python`, followed by a new line.

#### 9. Easter Egg

- `9-easter_egg.py` - a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

#### 10. Linked list cycle

- `10-check_cycle.c` - a function in C that checks if a singly linked list has a cycle in it.

#### 11. Hello, write

- `100-write.py` - a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

#### 12. Compile

- `101-compile` - a script that compiles a Python script file.

#### 13. ByteCode -> Python #1

- `102-magic_calculation.py` - the Python function `def magic_calculation(a, b):` (does exactly the same as a given disassembler).
