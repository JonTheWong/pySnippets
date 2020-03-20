# Python3 Snippet Repo
Building this repo as part of my journey into python3 development.

I've been working on code in the background and quickly realized that most of it
is reusable.

I'm creating a directory with snippets that i can use to build simple to more advanced projects.

I completed my certificate from [SkillShare on the Python for Beginners program](https://jonthewong.com/wp-content/uploads/sites/5/2020/02/StackSkills-Python-for-Beginners.jpg) in early 2020. The program was great. Opened my mind to all the connections i was missing as a Linux System Administrator.

I decided on python due to the implication it would compliment my experience as a Linux System Administrator.


### License
- free to use snippets and build your code
- project attribution/credit/linkback

### Goals
- Move existing code
- comment everything for learning
- allow import of code folder
- structure this repo so that it can be used as a boilerplate / framework? i guess django and flask already do this? right...? lol wtv
- include unittest https://docs.python.org/3.7/library/unittest.html
- include CI/CD ?

## Installation
I'm on macOS, and will eventually include a tutorial. But essentially macOS comes with python 2.7.16 as of March 2020

It includes the following warning.

>WARNING: Python 2.7 is not recommended.
This version is included in macOS for compatibility with legacy software.
Future versions of macOS will not include Python 2.7.
Instead, it is recommended that you transition to using 'python3' from within Terminal.
- macOS Catalina v10.15.3
### Building environment
Clone this repository - ```git clone https://github.com/....```
- The repo should have an .ignore file excluding env from any pulls.

Create the environment using ```/usr/bin/python3 -m venv env```, this will create an env folder containing the essential files for python

Now enable the environment using ```source env/bin/activate``` it should resemble the following;

```
(env) jonthewong@GenX pySnippets %
```

It seems recommended; not sure if i read it; but pip complains about being an older version; so lets get that out of the way by doing; ```pip install pip --upgrade```

You can then install the requirements i use to get all the parts of the project
going.```pip install -r requirements.txt```

That should be it.

## Learning Log
March 20, 2020
So, i knew i could import modules and custom functions but i've never really did it. Did it. Hopefully the "best way" for now..
Decided to follow docstring as much as possible; https://www.python.org/dev/peps/pep-0257/, they recommend """ triple double quotes; but i prefer triple single; no one seems to care..
https://docs.python.org/release/1.5.1p1/tut/strings.html says its the same since the begining.. maybe "work" might care since PEP257 says just use double.. hmm
