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

### Day 012 Number Guessing Game
Built a CLI number guessing game.
https://github.com/pbrazeale/100-Days-of-Code/blob/main/Day_012_Number_Guessing_Game/task1.py
Watched the first video, and built the game in ~30 minutes. ~10 minutes for working prototype and ~20 testing edge cases and refactoring.

### Day 013 Debugging
Fixed buggy code. Super simple.

### Day 014 Higher or Lower Game
Built a CLI game comparing Instagram followers.

Built the prototype using a dictionary, for real world use, I'd import a dictionary fil with more data. I used the key as their followers, and the value as a string description of the person. Ran into a bug where I created an infinite while loop despite making a play bool function which I switched to False upon completion; refactored into if logic chain. If I had the data, I'd change my selection to use random len(list), and then pair my follower value to == `data[x]["follower_count"]` to grab my int.

### Day 015 Coffee Machine
Built CLI coffee machine logic.

Managed to build everything but the "off" function without watching the solution. When she went over that requirement, I `import sys` and added a `sys.exit()` call for an "off" request. This was far more engaging than the fist chunk of problems, and I'm finally excited to keep going.

### Day 016 OOP Coffee Machine
Built a CLI coffee machine using OOP.

This was far more fun than the previous version. I learned a lot from the lecture and was able to make a working version by reading the documentation. Overall this felt more akin to what I've seen professional software developers demonstrate as their daily duties. (*Though be it, quite simplified. It's easy to solve a completely known problem space.*)

1. Had to switch my if statements to check for resources first, instead of payment first.
2. Deleted my else print statements because the objects handle those themselves.
3. Refactored code to make it cleaner.

### Day 017 Quiz Game
Built a CLI Quiz Game.

Using OOP I created 5 modules. Main, 2 classes: Question, QuizBrain, data, and data2. Using: https://opentdb.com/api_config.php API, I manually downloaded a JSON data structure, cleaned it up and plugged into into the program to update the question_bank.

Overall this was an enjoyable project, and I feel it solidified the OOP concepts covered in the previous lesson.

### Day 018 Turtle GUI
Created a popup that painted a Hirst style dot painting.

Watched the lecture up to the point that Dr. Yu introduced the Colorgram module and then I ran with it, reading the documentation and figuring out how to convert Colorgram object into a needed tuple for Turtle. Created a painting function and extrapolated out the row function from the columns. All-in-all it was a fun project with only minor bugs to fix. Maybe took ~45 minutes to read and code up?

### Day 019 Turtle Race
Fun lesson.

My new strategy is to see the objective in the lesson, and them attempt to solve it entirely on my own. Then when I hit a dead end I can watch the lecture further or use ChatGPT; which I found a way to make it a tutor instead of an answer generator.

I wrote two journals:
https://pbrazeale.github.io/ChatGPT-Technical-Tutor/

https://github.com/pbrazeale/100-Days-of-Code/blob/main/Day_019_turtle_race/turtle_race/ChatGPT.md

### Day 020 & 021 Snake Game
A true classic that was fun to build.

Adjusted the food class. Named my method `plop()` and when selecting randint, I chose `(-28, 28) * 10` to make the food align better with the snake.

Built snake method `grow()` on my own ahead of the lecture. By day 021 I understood the assignment and with the introduction of Super Classes I was off an running.

Built class Scoreboard on my own, and then refactored according to the lesson to use CONSTANTS, and separated my score() to extrapolate out the update_scoreboard() method and keep the logic seperated. *Still need to read Clean Code*

Followed the instructions to change my `grow()` method.

### Day 022 Pong
A fun project, but for some reason my turtle module is glitched, and no matter what I've done I can't get the ball to bounce from the top. It double bounces and continues out of bounds.
1. Adjusted upper boundary point
2. Doublechecked code to match lesson
3. Changed Ball shape

Gave up on the bug issue after searching for 30 minutes with no answer.

Otherwise, I achieved the project, but not going to really count this one, as I have no clue what's causing the bug, that actually bricks the game.

### Day 023 Turtle Crossing
Built a capstone Turtle game.

A simplistic frogger clone, but an excellent learning tool to solidify the concepts around OOP and separation of methods.

### Day 024 Mail Merge
Excellent project. I can already see how using this to rename filenames throughout a dir would be helpful.

### Day 025 U.S. States Game
Built a quiz game using turtle and pandas.

Learned the *basics* of pandas, and can already see the advantages over an excel sheet that I'm accustomed to. 

### Day 026 NATO Alphabet
Built a CLI "word" to NATO phonetic alphabet converter.

Learned more built in functionality for pandas, List comprehension, and Dictionary comprehension. A pandas DataFrame functions similarly to a dictionary. 

### Day 027 Tkinter
Built GUI Miles to Km converter.

Built a working final project without watching the video. Grid system makes placement easy! Updated km formula from 1.6 to 1.609.

### Day 028 Pomodoro Timer
Built a pomodoro timer with Tkinter.

This was fun and far easier than I thought it would be at first glance. Was able to solve each section ahead of the instructional videos.

### Day 029 & 030 Password Generator
Built a password generator with Tkinter, random, and pyperclip.
#### Git Restore Deleted File
Accidentally deleted `day_029_password_manager/main.py` thankfully stack overflow saved me: https://stackoverflow.com/questions/953481/how-do-i-find-and-restore-a-deleted-file-in-a-git-repository

>`git log --diff-filter=D --summary` log, difference filtered by D (delete), summary for short.

>`git checkout e4e6d4d5e5c59c69f3bd7be2~1 path/to/file.ext` ~1 step back one hash from where the file was deleted and pull the file path. 

### Day 031 Flash Card App
Built a flash card language app.

Used this lesson to build my own Flash Card App to learn CompTIA Security+ Acronyms. 
https://github.com/pbrazeale/security_plus_acronym_flash_cards

### Day 032 Automate Birthday Emails
Built a app that automatically sends emails. 
- Used smtplib to send emails
- Setup app codes on gmail
- Used pandas to convert csv into data table

### Day 033 ISS Overhead Notifier
Built an app that uses two APIs to track sunset and ISS location, and then sends an email notification via smtplib.

Built functions:
- iss_call()
- sun_call()
- is_dark()
- iss_overhead()
- send_email()
- check_10_min()
- main()

This was an excellent project, and I already see how using APIs and cronjobs to build an automated pipeline would save me hours of work, and more importantly create automatic notifications so that I can stop checking dashboards manually throughout the day. Already thinking through project ideas...

### Day 034 Quiz App
Built a GUI version of the quiz game from day 17.

Learned about type suggestions.

### Day 035 Weather App
Skipped. Couldn't get OpenWeather's student API.

### Day 036 Stock Alert
Built an app that uses API calls to check stock prices compared across two days, and then "sends" a text with the top three recent news articles about that stock to your phone.

*Had to skip the Twilio texting part, and instead prints to console.*

### Day 037 Habit Tracker
Built a habit tracker heatmap (similar to github's tracker) for page reads.

However, I got this message when trying to build it out, *'Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter.'* and was unable to get the put-pixel API to work at all. It never acknowledged my requests.

Overall though, it was a great API to play with, and helped solidify my API knowledge. 

### Day 038 Workout Tracker
Built a CLI interface to track workouts.

Nutritionix API processes the data and returns a JSON object, which is processed and passed into Sheety API and finally posted to the Google Sheet for tracking. Saving at least 2 minutes every time I log an exercise.

Solved 99% on my own, missed the final API needed lowercase titles for the column fields. `-_-`

### Day 039 Flight Deal Finder
Built a backend application that used Amadaus API to track flight prices, and Sheety API to log new lowest price options on google sheets acting as the database.

Structured the application to use separation of logic:
- main.py
- datamanager.py
- flight_data.py
- flight_serach.py

Skipped the notification portion because the SMS API is not longer free for students.

### Day 040 HTML
Basic review of HTML.
