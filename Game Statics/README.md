Game statistics reports
The story
You are a happy programmer at a big game developer company, named "ID Software". Judy, your statistician colleague, asks help from you in a competitor evaluation project. She has a data file with a lot of statistical information about famous games of all time. Judy has some unanswered questions about the games. She needs you to write a program that can answer these questions.

Description
Your task is to write reports that answer Judy's questions. Every report needs to be implemented as a function so every function is related to a question. For every report function you need to write a printer function also. The printer function has to print the return value(s) of the report function.

The input file
You can find the input file in the repository. Its name is game_stat.txt. Every line in the file contains the following information about a game:

title
total copies sold (million)
release date
genre
publisher
These are the properties of a game. Properties are separated by a tab character and lines are separated by line break characters. You need to pay attention these special characters when you read the file. The first line:

Minecraft⟶23⟶2009⟶Survival game⟶Microsoft↲
General expectations of the report functions
Every report function:

has to be named properly (as you see in the Questions section)
must NOT contain printing to console
returns only the asked information
should run in any order
has only the parameters predefined in the questions
has to be prepared for any other data files (not just the game_stat.txt) within the same structure
do NOT import other modules
Expectation of the source code
You need to write your project into 3 source files:

reports.py: write only the report functions in it.
printing.py: for printing the output of the report functions in a user friendly way. You can use this to test your solutions.
export.py: for exporting the reports into a single export file. By running this program Judy will get a single text file with all the answers she needs (you should export only the answers line by line, Judy will know the questions).
Judy will run printing.py and export.py to get the answers she want's, ask her for input where needed (e.g. game title).

Remember to apply the advice about not using magic numbers.

Judy's questions
How many games are in the file?
Expected name of the function: count_games(file_name)
Expected output of the function: a number
Is there a game from a given year?
Expected name of the function: decide(file_name, year)
Expected output of the function: boolean value
Which was the latest game?
Expected name of the function: get_latest(file_name)
Expected output of the function: the title of the latest game as a string
Other expectation: if there is more than one, then return the first from the file
How many games do we have by genre?
Expected name of the function: count_by_genre(file_name, genre)
Expected output of the function: a number
What is the line number of the given game (by title)?
Expected name of the function: get_line_number_by_title(file_name, title)
Expected output of the function: a number (if there is no game found, then raises ValueError exception)
...and more bonus questions! (nice to have)
Judy knows that you are a very busy programmer, but she has more questions and she looks like a cute little dog with big eyes.

What is the alphabetical ordered list of the titles?
Expected name of the function: sort_abc(file_name)
Expected output of the function: a list of strings
Do not use the builtin sort() or sorted() functions, but implement an easy sort algorithm by your own!
What are the genres?
Expected name of the function: get_genres(file_name)
Expected output of the function: a list of the genres (without duplicates, in alphabetical order)
What is the release date of the top sold "First-person shooter" game?
Expected name of the function: when_was_top_sold_fps(file_name)
Expected output of the function: year of the release, as integer (if there is no game with genre "First-person shooter" then raises ValueError exception
