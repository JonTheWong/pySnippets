# Python3 Snippet Repo
Building this repo as part of my journey into python3 development.

I've been working on code in the background and quickly realized that most of it
is reusable.

I'm creating a directory with snippets that i can use to build simple to more advanced projects.

I recently graduated from the SkillShare Python for Beginners in early 2020. The program was great.

I decided on python due to the implication it would compliment my experience as a Linux System Administrator.


### License
- free to use snippets and build your code
- project attribution/credit/linkback

### Goals
- Move existing code
- comment everything for learning
- allow import of code folder
- structure this repo so that it can be used as a boilerplate / framework? i guess django and flask already do this? right...? lol wtv

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
