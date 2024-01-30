# Prácticas en Python
Este repositorio fue creado con el propósito de aprender practicando mediante distintos ejercicios planteados en cada uno de los scripts.
Si estás interesado/a en aprender Python de cero, te recomiendo que entres a mis cursos:
- [Desarrollo web con Python y Django](https://www.udemy.com/course/desarrollo-de-sitios-web-con-python-3-con-django/?referralCode=A491B0944C634BFAA48C)
- [Demo del curso anterior](https://www.youtube.com/playlist?list=PLp7PPjAxisAICL8_g0lmC3thJvHW5Hbe3)

También tengo un podcast donde hablo de desarrollo, especialmente en Python. Se llama En Código, y lo puedes encontrar en [Spotify](https://podcasters.spotify.com/pod/show/maxi-burgos9).

## Puesta en marcha (PyCharm)
Esto es un proyecto en [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/), un IDE gratuito y sencillo de usar. Simplemente puedes clonar este repositorio y abrirlo en el editor. Luego debes entrar a algun script que quieras correr, y darle al botón Run.

## Puesta en marcha (VSC)
Ahora también se preparó para [Visual Studio Code](https://code.visualstudio.com/). Para instalarlo debes seguir los siguientes pasos:

Clonar el Proyecto; y una vez dentro, crear y activar el entorno virtual:

> python -m venv venv

> .\venv\Scripts\activate

Instalar las dependencias

> pip install -r requirements.txt

## Flake8
Se implementó Flake8 en el proyecto, el cual se puede correr mediante este comando:
> flake8 --exclude=venv

Se excluye el entorno virtual para enfocarnos sólo en el proyecto actual.
Posibles warnings que reporta Flake8:
> .\level_beginner\filtrar_palabras.py:2:40: W291 trailing whitespace

> .\level_advance\regex\is_phone_number.py:35:80: E501 line too long (86 > 79 characters)

> .\level_advance\regex\detect_start_end_str.py:28:44: W292 no newline at end of file

De momento todas las advertencias fueron resueltas, pero en el caso de detectar nuevas, por favor abrir un issue. Si querés saber más al respecto, te dejo un [artículo](https://dev.to/maxwellnewage/diario-de-python-17-un-paseo-por-flake8-33do) donde hablo de este linter.

## Ejercicios
- [Nivel Principiante](level_beginner/README.md): Fundamentos de la programación tales como estructuras de datos, control de flujo, operadores lógicos y aritméticos, manipulación de archivos, entre otros.
- [Nivel Intermedio](level_intermediate/README.md): Principios aplicados de la programación orientada a objetos.
- [Nivel Avanzado](level_advance/README.md): Ejercicios relacionados con patrones de diseño, testing, interoperabilidad, entre otros.
- [HackerRank](hackerrank/README.md): Challenges seleccionados de [HackerRank](https://www.hackerrank.com/).

## Proyectos
### Apps de Consola
- [Detector de palabras censuradas](projects/bad_word_detector.py): Lee una frase de la consola y la censura.
- [Plazo Fijo](projects/plazo_fijo.py): Define cuanto se puede ganar mensualmente con una determinada TNA (tasa nominal anual) y un monto.
- [Anime Finder](projects/anime_finder.py): Buscador de anime que se conecta con la API Jikan.
- [Tip Calculator App](projects/tip_calculator_app.py): Calculadora de propinas.
- [Random Password Generator](projects/random_password_generator.py): Generador de contraseñas.
- [Python File Explorer](projects/file_manager.py): Explorador de archivos.
- [Random Wikipedia Article](projects/rand_wiki_article.py): Devuelve un artículo aleatorio de Wikipedia.
- [Instagram Photo Downloader - Deprecado](projects/ig_photo_downloader_deprecated.py): Descarga imágenes publicadas en Instagram. (Deprecado)
- [Instagram Info Downloader](projects/ig_info_downloader.py): Descarga información publicada en Instagram.
- [Excel Cleaner](projects/excel_cleaner/main.py): Modifica un archivo xlsx sin corromper el estilo.
- [Calculadora](projects/calculadora): Calculadora que avanza progresivamente en sus versiones a medida que se aprenden los fundamentos en Python.
- [Email Sender](projects/email_sender): Envía emails de gmail mediante autenticación por token.
- [Love Calculator](projects/love_calculator.py): Calcula el amor ideal según el nombre de las personas.
- [AWS S3 CRUD](projects/aws_s3_crud/main.py): Métodos para crear y eliminar buckets, así como también subir y bajar archivos.
- [Caesar Cipher](projects/caesar_cipher.py): Cifrado de Caesar con encode, decode y shift personalizado.
- [Weather](projects/weather/main.py): Pandas & CSV Lib implementation reading a weather dataset.
- [Nato Alphabet](projects/nato/main.py): Nato Alphabet.
- [OpenWeather App](projects/open_weather.py): OpenWeather App.
- [Stock Price Movement Manager](projects/stock_price_movement_manager.py): Stock Price Movement Manager.
- [Speed Calculator Decorator](projects/speed_calc_decorator.py): Speed Calculator Decorator.


### Interfaz Gráfica (GUI)
- [Speed Typing Test](projects/speed_typing_test.py): Detecta que tan rápido escribes.
- [YouTube Video Downloader](projects/yt_video_downloader.py): Descarga videos desde YouTube.
- [Desktop Notifier App](projects/desktop_notifier_app/main.py): Aplicación que genera notificaciones en el sistema operativo.
- [Music Player](projects/music_player/main.py): Reproductor de música.
- [Mile to Km Converter](projects/mile_km_converter.py): Mile to Km Converter.
- [Pomodoro](projects/pomodoro/main.py): Pomodoro App.
- [Name the states](projects/name_the_states/main.py): Juego para adivinar los estados de USA basado en un dataset.
- [Etch a Sketch](projects/etch_a_sketch.py): Etch a Sketch.
- [Random Walk](projects/random_walk.py): Turtle random walk.
- [Dot Paint Generator](projects/dot_paint_generator/main.py): Dot Paint Generator on Turtle.
- [Flashy](projects/flashy/main.py): Famoso ejercicio para aprender idiomas con cards.
- [ISS Position App](projects/iss_position/main.py): ISS Position App.

### Videojuegos
- [Pong](projects/pong/main.py): Pong game on Turtle.
- [Turtle Race](projects/turtle_race/main.py): Turtle Race.
- [Blackjack](projects/blackjack.py): Juego de cartas Blackjack.
- [Hangman](projects/hangman.py): Juego del ahorcado.
- [Rock, Paper, Scissors v2](https://replit.com/@maxwellnewage/python-rock-paper-scissors-game): Versión más bonita del anterior proyecto.
- [Battle Rol Game System](projects/battle_rol_game_system/main.py): Juego de rol donde podemos crear un player y luchar contra un enemigo al azar.
- [Snake Game](projects/snake_game/main.py): Juego de la serpiente.
- [Dice Rolling Simulator](projects/dice_rolling_simulator.py): Simulador de tirada de dados.
- [Number Guessing](projects/number_guessing.py): Adivina el número que estoy pensando.
- [Rock, Paper, Scissors](projects/rock_paper_scissors.py): El famoso juego "Piedra, Papel o Tijeras".

### APIs
- [Pizza Delivery API](https://github.com/maxwellnewage/fastapi-pizza-delivery-api): API desarrollada en FastAPI basada en un sistema de gestión de una pizzería.

### Sitios Web
- [Employee Manager](https://github.com/maxwellnewage/udemy-django-employee-manager): Sistema de Empleados estilo ABM (desarrollado en Django)
- [Hero Game](https://github.com/maxwellnewage/udemy-django-hero-game): CRUD de un juego de rol con Players, Enemies, Shop y Weapons (desarrollado en Django y Django-Rest-API)
- [YCombinator News Scrapper](projects/scrapper_ycombinator.py): YCombinator News Scrapper.
- [Wikipedia Finder](/projects/wikipedia_finder.py): Busca un artículo de Wikipedia con Selenium.
- [LinkedIn Tracker](/projects/linkedin_tracker/main.py): Track de información sobre perfiles según búsqueda.

## Inspiración
Algunos ejercicios y proyectos están inspirados (solo en su consigna, la solución es de mi autoría) en las siguientes fuentes:
- [pythondiario](https://pythondiario.com/ejercicios-de-programacion-python)
- [Python Tutorial for Beginners](https://youtu.be/B9nFMZIYQl0)
- [learnpython](https://www.learnpython.org/)
- [upgrad](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)
- [Udemy Course: 100 days of code](https://www.udemy.com/course/100-days-of-code/)