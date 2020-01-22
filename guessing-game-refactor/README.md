# Guessing game

## Story

Your friend Victor has done some kind of game in Python, but he did it in a
somewhat ugly way (no offense, Victor only started coding a couple of weeks ago).

But you know how important clean code is, so it's your chance to help him make his code more readable and maintainable!

## What are you going to learn?
You will learn and practice how to do the following things in Python:
- code comprehension (understand written code),
- clean code refactoring (making code more easy to read and maintain without changing any feature).

## Tasks


1. Read the code and try to understand it without running. Use comments to write down what you understood, next to the code line. Commit and push your work. Remove the comments after pushing.
**Disclamier**: *You shouldn't comment your program this way* in real life. For a professional programmer a `starting_number = 5` is something pretty obvious. This task is just to check if it's obvious to you as well.

    - Every line of the program has comments next to it describing what's going on in it. E.g.:
    ```python
    starting_number = 5 # assign 5 to the `starting_number` variable
    numbers = [1, 2, 3] # initialize list with values
    for number in numbers: # loop through list elements (assign each value to a `number` variable)
    ```
    - Comments should use proper technical language, be short and specific enough to understand what's going on
    - One-sentence comment at the top of the file should describe what this program does
    - Modifications should be committed with a message "add code comprehension comments" and pushed into the remote repository afterwards

2. Make the program easier to understand and modify (maintain). Do it step by step and commit after each modification. Push your changes afterwards.

    - Program should behave the same before and after refactoring.
    - Variable names used in the program are meaningful nouns and are not abbreviated
    - Function names used in the program are meaningful verbs and are not abbreviated
    - There's no unnecessary (dead) code or comments in the program
    - There are no duplicating code parts or code parts doing the same thing differently in the program
    - There are no functions doing more than one thing in the program (single responsibility principle - a function should only do what it's meant to do, nothing more)
    - Changes are committed after each modification
    - Commit messages are meaningful
    - Program is runnable and results are the same than at the beginning
    

## General requirements

None

## Hints
- Always keep the features of the original code (don't even change a dot or a newline).
- Always keep the code in a runnable state.
- Commit early, commit often.
- Pay attention to create not only readable, but maintainable code as well.

## Starting repository

Click here to clone your own Git repository for this assignment:
https://classroom.github.com/a/689-Yuec


## Background materials
- :exclamation: [Basics of clean code](https://learn.code.cool/codecool-graph/#/../pages/general/clean-code)
- :exclamation: [Refactoring in action](https://learn.code.cool/codecool-graph/#/../pages/general/refactoring-in-action)
- :exclamation: About [nice commit messages](https://chris.beams.io/posts/git-commit/)
