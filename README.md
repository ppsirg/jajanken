# jajanken

rock paper scissors django-flavored, check https://ppsirg.pythonanywhere.com/ for live demo.

## setup

environment requirements are in [requirements.txt](jajanken/requirements.txt)

## run project

being in `jajanken/` folder, run

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:9000
```

then, open in a modern web browser (firefox, Chrome) the url
`http://localhost:9000/`

## api

api explorer can be accessed on `http://localhost:9000/api/`, also you
can find postman collection of requests in [jajanken.postman_collection](jajanken.postman_collection.json).

resources are:

- players: id, name and won_matches of a player
- match: a jajanken match between two players
- match_round: a set of events in the game that can lead to a winner
- match_event: event register of a player choosing scissors, paper or rock liked to match_round

two additional urls were implemented for accessing some model calculations, such a match winner and round winner.

## design keynotes


it was designed having 2 bases:

- player: the ones that plays the game
- game: all related to game backend

backend implements basic game rules and validations and exposes as
resources players and match abstractions such as match, match_round
and match_event for frontend to implement game mechanics.


frontend was designed as a mix of classic django view (list view used for scores list) and a web application with vue for game itself.
