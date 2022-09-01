# pythonanywhere2019
This code was created before 2020 on pythonanywhere and is on github for archiving purposes.

## How to run
This code was developed and tested on python 2.7 so it is incompatable with any python 3 and if a syntax error (e.g. `Syntax Error: Missing parentheses in call to 'print'...`) is raised then it is most likely that you are running it through a python3 interpretor.

Additionally, this code was designed to run through python2's `execfile` and so a function may need to be called after running a command.

For example, to run `mono.py`:

```
root@example:~/pythonanywhere2019$ python2
Python 2.7.18 (default, Jan  1 1970, 00:00:00) 
[GCC 9.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> execfile("mono.py")
>>> movement_money()
Please type Player 1's name in here. -> ...
```

Furthermore, many confirmation prompts and other prompts that may require you to input a number have no validation and will throw an error, usually either a `SyntaxError` or a `NameError` if your input is not a number or even more unusual behaviour if your input matches the name of a defined variable as it evaluates the user's input. I am now aware that this is a terrible idea but as these files are for archiving processes, not use or development, I have not modified it.

## Further Notes
A significant proportion of this code was written earlier than the name of the repository or the age of the file suggests as it was moved from an earlier location to over hear. Some of it, such as `mono.py`, is as old as 2016 or even older. 

Additionally, much of this code remains unfinished and abandoned so there are no guarantees that any given file will be complete or even work.
