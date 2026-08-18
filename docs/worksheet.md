I used several Linux CLI commands to set up the python lab project. i used the following;
mkdir: to create the python_lab directory and its subdirectories.
cd: change directory as i required.
touch: i used it to create the empty python files like main.py
echo & >: to write inside README.md while using the CLI.
tree: used it to display the complete directory structure.
ls -a: lists all files even the hidden ones.
cat: displays content of a file in the terminal.
git init: initializes a new Git repo in current project directory.
git add . : stages all egilible files in the current project for the next commit.
git status: shows current state of the git repo.
git commit -m "...": creates a commit containing everything and a message.
git log: displays the commit history of the git repo.




#why the folders are separated?
this is because each folder has specific purpose and separating them is a good practice in any project and keeps everything organised and easy to understand.
src: contains the main python source code.
test: is used for testing the code.
docs: contains project documentation.


— .gitignore

The .gitignore file tells Git which files and folders should not be tracked or included in commits. In this project, __pycache__/ ignores Python cache folders, *.pyc ignores compiled Python files and .env ignores environment files. These patterns are important because cache and compiled files are generated automatically and do not need to be stored in the repository while .env files may contain private configuration or sensitive information.

— Commit history

The Git commit history shows how a project develops over time by recording commits made to the repository. It can reveal the commit message, author, date, and commit ID, allowing developers to see when changes were made and what each change was intended to accomplish. This makes it easier to track progress and understand the project's development history.

#utils.py#
def square(n) :
    return n ** 2
    return n

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
    

#main.py#
from utils import square, is_even, celsius_to_fahrenheit
number = float(input("Enter a number: "))

square_result = square(number)
even_result = is_even(number)
fahrenheit_result = celsius_to_fahrenheit(number)

print("square:", square_result)
if even_result:
    print("The number is even.")
else:
    print("The number is odd.")

print("Fahrenheit:", fahrenheit_result)

#how the import system connects maint to utils;
py import system allows main.py to use functions defined in utils.py. thus main.py doesnt have to write codes of those functions again.

