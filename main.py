from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def root():
    return HTMLResponse('<h2>Marvellous Mavericks Make Methodical Mad-Libs</h2>')

with open('dino_rhyme.html', 'r') as fd:
    dino_rhyme_html = fd.read()
with open('mystery_museum.html', 'r') as fd:
    mystery_museum_html = fd.read()
with open('furry_scaly_pets.html', 'r') as fd:
    furry_scaly_pets_html = fd.read()

madlibsDB = list()
# 3 mad-libs
dino_rhyme = dict()
mystery_museum = dict()
furry_scaly_pets = dict()
# mad-lib: Dino Rhymes
dino_rhyme['name'] = "dino_rhyme"
dino_rhyme['title'] = "Dinosaur Rhymes"
dino_rhyme['HTML'] = dino_rhyme_html
dino_rhyme['adjectives'] = ['long', 'exciting', 'amazing', 'sharp', 'golden', 'silly', 'difficult', 'warm', 'ridiculous', 'delightful', 'tired', 'weepy']
dino_rhyme['nouns'] = ['basketball', 'butterfly', 'corn', 'firetruck', 'globe', 'newspaper', 'orange slice', 'owl', 'palm-tree', 'rhino', 'superhero', 'train']
dino_rhyme['verbs'] = ['dig', 'zip', 'slurp', 'scratch', 'clap', 'sail', 'dance', 'gallop', 'blink', 'tango', 'chew', 'pedal']
dino_rhyme['miscellanies'] = ['banana', 'bread', 'celery', 'cookies', 'deer', 'dice', 'eagle', 'hat', 'moon', 'plant', 'surfer', 'trumpet']
madlibsDB.append(dino_rhyme)
# mad-lib: Mystery Museum
mystery_museum['name'] = 'mystery_museum'
mystery_museum['title'] = "Museum Mystery"
mystery_museum['HTML'] = mystery_museum_html
mystery_museum['adjectives'] = ['sticky', 'bumpy', 'slimy', 'charming', 'bouncy', 'tall', 'happy', 'wiggly', 'stylish', 'ripe', 'weird', 'wrinkly']
mystery_museum['nouns'] = ['canoe', 'castle', 'clown', 'elephant', 'fish', 'flowers', 'knight', 'parrot', 'pirate', 'soccerball', 'tortoise', 'unicorn', ]
mystery_museum['verbs'] = ['skipped', 'burped', 'jogged', 'yelled', 'scrambled', 'rolled', 'walked', 'rode', 'dribbled', 'wobbled', 'jumped', 'sang']
mystery_museum['miscellanies'] = ['bat', 'beaker', 'caterpillar', 'dinosaur', 'dolphin', 'frog', 'kid', 'Little Red Riding Hood', 'eel', 'piano', 'present', 'rocks']
madlibsDB.append(mystery_museum)
# mad-lib: Furry Scaly Pets
furry_scaly_pets['name'] = 'furry_scaly_pets'
furry_scaly_pets['title'] = "Quiz: Furry or Scaly Pets"
furry_scaly_pets['HTML'] = furry_scaly_pets_html
furry_scaly_pets['adjectives'] = ['crunchy', 'dry', 'prickly', 'cuddly', 'sweaty', 'slow', 'quiet', 'hot', 'fresh', 'friendly']
furry_scaly_pets['nouns'] = ['apple', 'cat', 'Dragon', 'flamingo', 'football', 'Lion', 'Pinnoccio', 'Snorkler', 'tree', 'UFO']
furry_scaly_pets['verbs'] = ['smell', 'fetch', 'love', 'call', 'type', 'drip', 'catch', 'yawn', 'whistle', 'cry']
furry_scaly_pets['miscellanies'] = ['astronaut', 'cake', 'car', 'dragon', 'grapes', 'guitar', 'potion', 'robot', 'teapot']
madlibsDB.append(furry_scaly_pets)

@app.get('/madlibs/{name}')
async def getMadLib(name: str):
    payload = dict()
    selection = [mad_lib for mad_lib in madlibsDB if mad_lib.get('name', None) == name]
    if selection:
        payload = selection[0]
    return payload

@app.get('/madlibsgame/{name}')
async def getMadLibGame(request: Request, name: str):
    my_mad_lib = dict()
    selection = [mad_lib for mad_lib in madlibsDB if mad_lib.get('name', None) == name]
    if selection:
        my_mad_lib = selection[0]
        return templates.TemplateResponse('madlib.html', {
            'request': request,
            'name': my_mad_lib.get('name'),
            'title': my_mad_lib.get('title'),
            'my_mad_lib': my_mad_lib.get('HTML'),
            'adjectives': my_mad_lib.get('adjectives'),
            'nouns': my_mad_lib.get('nouns'),
            'verbs': my_mad_lib.get('verbs'),
            'miscellanies': my_mad_lib.get('miscellanies')
        })