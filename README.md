This repository contains the 100 projects as found in '100 Days of Code: The Complete Python Pro Bootcamp' Created by Dr. Angela Yu.

[https://www.udemy.com/course/100-days-of-code/](https://www.udemy.com/course/100-days-of-code/)


## Tech Stack
Python 3.12.8


## Journal
### Day 001 Band Name Generator
A CLI that concatenates your birth city and pet's name to print your band name.

This was a simple introduction to `print`, `input`, and variables. I learned I could nest inputs directly into a desired print function which was neat, and I look forward to expanding upon my CS50P course.

### Day 002 Tip Calculator
A CLI that takes in the bill total, desired tip percent, and party members to divide amongst, and prints the individual bill amount.

When Subscripting you can use negative numbers to index a string backwards.

### Day 003 Treasure Island
A CLI game that mimics the '80s RPGs.

Easy enough. Looking forward to days 16+ after the downloaded material *which I skipped*. Not a fan of forced IDE and interface downloads.

### Day 004 Rock, Paper, Scissors
A CLI game for RPS.

Super easy. Coded it up with zero errors. Learned about `random.choice` which will indeed come in handy in the future.

### Day 005 Password Generator
A CLI for generating passwords.

I took the lesson and expanded upon it. My generator now requires a band of 12 to 20 characters, and then randomly generates the characters using a mix of letters, numbers, and symbols.  

### Day 006 Maze
Solved this problem, [reeborg.ca](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) using basic python functions to navigate maze using the follow right path method.

Easy, but I didn't consider the edge case of the square void starting position;
however the solution was easy enough [GitHub code](https://github.com/pbrazeale/100-Days-of-Code/blob/main/Day_006_Maze/maze.py)

### Day 007 Hangman
Knew I needed a holding list, tried turning the display into a list, but that approach failed. The solution to use a holding list of guessed letters, seems so obvious after the fact. Didn't download the starter software, so no word list file, and no hangman ascii art, but otherwise I think I demonstrated the core concepts well.

### Day 008 Caesar Cipher
Easy enough, though my approach was not nearly as elegant. I ended up creating a second list, which obviously wasted memory space, and would fail if I were trying to shift a much larger data list. Regardless, I am pleased to have thought through a solution on my own and solved it.

### Day 009 Secret Auction
Nothing to it. Simple use of nested list within a dictionary and increment the key by 1 each time. Similar to a SQL table with a UNIQUE PRIMARY KEY. Crate an infinite while loop and only break when auction is complete. Took 10 minutes or less, and zero need for the final video.

### Day 010 Calculator
Built a simplistic CLI calculator.

My solution used an if logic chain instead of creating a dictionary of operations. (task1) The dictionary solution version offers the ability to expand the calculator's functionality in the future, and thus is a far more elegant solution that my own. I too chose recursion as the simplest solution to maintain the first calculation moving forward until the user choses to clear and start over.

### Day 011 Blackjack
Built CLI blackjack game.

Watched the first video "intro", and built the game. Not sure if it's optimal, but I used `random` to shuffle my deck list and then delt by indexing into the deck. It's a total of 101 lines of code, which seems suboptimal, but I was able to build it in about an hour, so that was fun. Ran into the odd syntax error, and had to add in conditional check for dealer having 21 before entering the "hit()" phase of the game for the player, but otherwise everything worked as planned.

#### Day 012
Built a CLI number guessing game.
https://github.com/pbrazeale/100-Days-of-Code/blob/main/Day_012_Number_Guessing_Game/task1.py

Watched the first video, and built the game in ~30 minutes. ~5 minutes for working prototype and 25 testing edge cases and refactoring.
