# Python Practices
This repository was created with the purpose of learning by practicing through different exercises outlined in each of the scripts. 
If you're interested in learning Python from scratch, 
I recommend you check out my courses (Spanish lang):
- [Web Development with Python and Django](https://www.udemy.com/course/desarrollo-de-sitios-web-con-python-3-con-django/?referralCode=A491B0944C634BFAA48C) [[Demo](https://www.youtube.com/playlist?list=PLp7PPjAxisAICL8_g0lmC3thJvHW5Hbe3)]
- [Python from Scratch](https://www.youtube.com/playlist?list=PLp7PPjAxisALk2zFlMx3DzT1MytOEGUmF)

I also have a podcast where I talk about development, especially in Python. 
It's called "En Código," and you can find it on [Spotify](https://podcasters.spotify.com/pod/show/maxi-burgos9).

## Getting Started
Create and activate the virtual environment:

> python -m venv venv

> .\venv\Scripts\activate

Install dependencies:

> pip install -r requirements.txt

## Flake8
Flake8 has been implemented in the project, which can be run using this command:
> flake8 --exclude=venv

The virtual environment is excluded to focus only on the current project.
Possible warnings reported by Flake8:
> .\level_beginner\filtrar_palabras.py:2:40: W291 trailing whitespace

> .\level_advance\regex\is_phone_number.py:35:80: E501 line too long (86 > 79 characters)

> .\level_advance\regex\detect_start_end_str.py:28:44: W292 no newline at end of file

At the moment, all warnings have been resolved, but if new ones are detected, please open an issue. If you want to know more about it, I leave you an [article](https://dev.to/maxwellnewage/diario-de-python-17-un-paseo-por-flake8-33do) where I talk about this linter.

## Exercises
- [Beginner Level](level_beginner/README.md): Programming fundamentals such as data structures, flow control, logical and arithmetic operators, file manipulation, among others.
- [Intermediate Level](level_intermediate/README.md): Applied principles of object-oriented programming.
- [Advanced Level](level_advance/README.md): Exercises related to design patterns, testing, interoperability, among others.
- [HackerRank](hackerrank/README.md): Selected challenges from [HackerRank](https://www.hackerrank.com/).

## Projects
### Console Apps
- [Censored Word Detector](projects/bad_word_detector.py): Reads a sentence from the console and censors it.
- [Term Deposit](projects/plazo_fijo.py): Defines how much can be earned monthly with a certain Annual Nominal Rate (TNA) and an amount.
- [Anime Finder](projects/anime_finder.py): Anime searcher that connects to the Jikan API.
- [Tip Calculator App](projects/tip_calculator_app.py): Tip calculator.
- [Random Password Generator](projects/random_password_generator.py): Password generator.
- [Python File Explorer](projects/file_manager.py): File explorer.
- [Random Wikipedia Article](projects/rand_wiki_article.py): Returns a random Wikipedia article.
- [Instagram Photo Downloader - Deprecated](projects/ig_photo_downloader_deprecated.py): Downloads images posted on Instagram. (Deprecated)
- [Instagram Info Downloader](projects/ig_info_downloader.py): Downloads information posted on Instagram.
- [Excel Cleaner](projects/excel_cleaner/main.py): Modifies an xlsx file without corrupting the style.
- [Calculator](projects/calculadora): Calculator that progressively advances in its versions as Python fundamentals are learned.
- [Email Sender](projects/email_sender): Sends emails from Gmail using token authentication.
- [Love Calculator](projects/love_calculator.py): Calculates ideal love based on people's names.
- [AWS S3 CRUD](projects/aws_s3_crud/main.py): Methods to create and delete buckets, as well as upload and download files.
- [Caesar Cipher](projects/caesar_cipher.py): Caesar cipher with custom encode, decode, and shift.
- [Weather](projects/weather/main.py): Pandas & CSV Lib implementation reading a weather dataset.
- [Nato Alphabet](projects/nato/main.py): Nato Alphabet.
- [OpenWeather App](projects/open_weather.py): OpenWeather App.
- [Stock Price Movement Manager](projects/stock_price_movement_manager.py): Stock Price Movement Manager.
- [Speed Calculator Decorator](projects/speed_calc_decorator.py): Speed Calculator Decorator.
- [Nexo Earn Calculator](projects/nexo_earn_calculator/main.py): Nexo Earn Calculator.
- [Pillow Image Converter](projects/image_converter): Convert any image to jpg with Pillow lib.
- [Chat](projects/chat): Chat implemented with sockets.
- [Complex Hello World](projects/complex_hello_world): Hello World, but in hell.

### Graphical User Interface (GUI)
- [Speed Typing Test](projects/speed_typing_test.py): Detects how fast you type.
- [YouTube Video Downloader](projects/yt_video_downloader.py): Downloads videos from YouTube.
- [Desktop Notifier App](projects/desktop_notifier_app/main.py): Application that generates notifications on the operating system.
- [Music Player](projects/music_player/main.py): Music player.
- [Mile to Km Converter](projects/mile_km_converter.py): Mile to Km Converter.
- [Pomodoro](projects/pomodoro/main.py): Pomodoro App.
- [Name the states](projects/name_the_states/main.py): Game to guess the states of the USA based on a dataset.
- [Etch a Sketch](projects/etch_a_sketch.py): Etch a Sketch.
- [Random Walk](projects/random_walk.py): Turtle random walk.
- [Dot Paint Generator](projects/dot_paint_generator/main.py): Dot Paint Generator on Turtle.
- [Flashy](projects/flashy/main.py): Famous exercise to learn languages with cards.
- [ISS Position App](projects/iss_position/main.py): ISS Position App.

### Video Games
- [Pong](projects/pong/main.py): Pong game on Turtle.
- [Turtle Race](projects/turtle_race/main.py): Turtle Race.
- [Blackjack](projects/blackjack.py): Blackjack card game.
- [Hangman](projects/hangman.py): Hangman game.
- [Rock, Paper, Scissors v2](https://replit.com/@maxwellnewage/python-rock-paper-scissors-game): Nicer version of the previous project.
- [Battle Rol Game System](projects/battle_rol_game_system/main.py): Role-playing game where we can create a player and fight against a random enemy.
- [Snake Game](projects/snake_game/main.py): Snake game.
- [Dice Rolling Simulator](projects/dice_rolling_simulator.py): Dice rolling simulator.
- [Number Guessing](projects/number_guessing.py): Guess the number I'm thinking of.

### APIs
- [Pizza Delivery API](https://github.com/maxwellnewage/fastapi-pizza-delivery-api): API developed in FastAPI based on a pizzeria management system.

### Websites
- [Employee Manager](https://github.com/maxwellnewage/udemy-django-employee-manager): ABM-style Employee System (developed in Django).
- [Hero Game](https://github.com/maxwellnewage/udemy-django-hero-game): CRUD for a role-playing game with Players, Enemies, Shop, and Weapons (developed in Django and Django-Rest-API).
- [YCombinator News Scrapper](projects/scrapper_ycombinator.py): YCombinator News Scrapper.
- [Wikipedia Finder](/projects/wikipedia_finder.py): Searches for a Wikipedia article using Selenium.
- [LinkedIn Tracker](/projects/linkedin_tracker/main.py): Profile information tracking based on search.
- [Age & Gender Guess by Name](projects/age_gender_guess/main.py): Guesses age and gender by name.

## Inspiration
Some exercises and projects are inspired (only in their brief, the solution is authored by me) by the following sources:
- [pythondiario](https://pythondiario.com/ejercicios-de-programacion-python)
- [Python Tutorial for Beginners](https://youtu.be/B9nFMZIYQl0)
- [learnpython](https://www.learnpython.org/)
- [upgrad](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)
- [Udemy Course: 100 days of code](https://www.udemy.com/course/100-days-of-code/)
