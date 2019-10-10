from route_helper import simple_route
from flask import render_template

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
    return render_template('index.html')
           + """Hello and welcome to the GAME? <br>
    This game is (instructions here). <br>
    
    <a href="goto/petfacility/">Go to the pet area.</a><br>
    <a href="goto/town">Go to the town.</a><br>
    """

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
        return GAME_HEADER + """Welcome to the Pet Facility.<br>
        Choose your new pet to take care of.<br>
        <link rel = "stylesheet" href = "/static/imagefix.css" >
        <a href="/ask/eagle/">
            <img src="/static/eagle.jpg" alt="Picture of eagle">
        </a>
        <a href="/ask/jellyfish/">
            <img src="/static/jellyfish.jpg" alt="Picture of jellyfish">
        </a>
        <a href="/ask/leopard/">
            <img src="/static/leopard.jpg" alt="Picture of leopard">
        </a>
        <a href="/ask/elephant/">
            <img src="/static/elephant.jpg" alt="Picture of elephant">
        </a>
        """
    elif where == "town":
        return GAME_HEADER + """This is the town. It's pretty empty right now.
        """

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
        world['image'] = '<img src="/static/elephant.jpg" alt="Picture of elephant"/>'
    elif pet == 'leopard':
        world['image'] = '<img src="/static/leopard.jpg" alt="Picture of leopard"/>'
    elif pet == 'jellyfish':
        world['image'] = '<img src="/static/jellyfish.jpg" alt="Picture of jellyfish"/>'
    elif pet == 'eagle':
        world['image'] = '<img src="/static/eagle.jpg" alt="Picture of eagle"/>'
    return GAME_HEADER + CHOOSE_PET.format(pet)

@simple_route('/pet/naming/')
def name(world: dict) -> str:
    """
    Place to name your pet

    :param world: The current world
    :return: HTML that shows the page
    """
    return GAME_HEADER+'<link rel = "stylesheet" href = "/static/image.css" >' + "You have chosen the " + world['pet'] +  " as a pet.<br>" + world['image'] + """<br>
    What would you like to name your new pet?<br>
    """

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
