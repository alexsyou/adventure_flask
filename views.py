from route_helper import simple_route
from flask import render_template, request

CHOOSE_PET = """
Are you sure you want to choose a {}?<br>

<a href="/goto/petfacility/">No, I'm still deciding.</a><br>
<a href="/pet/naming/">Yes, I've decided.</a><br>
"""




@simple_route('/')
def hello(world: dict) -> str:
    """
    Welcome screen

    :param world: Current world
    :return: HTML for the page
    """
    world['balance'] = 0
    return render_template('index.html', balance=world['balance'])

@simple_route('/goto/<where>/')
def place(world: dict, where: str) -> str:
    """
    Decide where the player is and show the options
    :param world: Current world
    :param where: Where the player is
    :return: HTML to show player
    """

    world["location"] = where
    if where == "petfacility":
        return render_template('petfacility.html')
    elif where == "town":
        return render_template('town.html')
    elif where == "home"
        return render_template('home.html', pet=world['pet'], name=world['name'])

@simple_route('/ask/<pet>/')
def question(world: dict, pet: str) -> str:
    """
    This asks if you really want to pick the pet

    :param: world: The current world
    :param pet: The pet that you are considering
    :return: HTML of the page
    """
    world['pet'] = pet
    if pet == 'elephant':
        world['image'] = "/static/elephant.jpg"
    elif pet == 'leopard':
        world['image'] = "/static/leopard.jpg"
    elif pet == 'jellyfish':
        world['image'] = "/static/jellyfish.jpg"
    elif pet == 'eagle':
        world['image'] = "/static/eagle.jpg"
    return render_template('askpet.html', pet=pet)

@simple_route('/pet/naming/')
def name(world: dict) -> str:
    """
    Place to name your pet

    :param world: The current world
    :return: HTML that shows the page
    """
    return render_template('petnaming.html', pet=world['pet'], image=world['image'])

@simple_route('/pet/naming/', methods=['POST'])
def name_post(world: dict, other) -> str:
    """
    Pet has been named

    :param other: I don't know what this is.
    :param world: The current world
    :return: HTML that shows page
    """
    world['name'] = request.form['name']
    return render_template('nameconfirm.html', pet=world['pet'], image=world['image'], name=world['name'])

'''@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return GAME_HEADER+"""You are in the Town of Dogs.<br>
    
    <a href="goto/lair">Go further into the Town.</a><br>
    <a href="goto/entrance">Retreat.</a>"""


ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
"""


@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    return GAME_HEADER+ENCOUNTER_MONSTER.format(where)


@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name

    return GAME_HEADER+"""You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])'''
