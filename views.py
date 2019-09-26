from route_helper import simple_route

GAME_HEADER = """
<h1>Welcome to Pet Quest!</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""

@simple_route('/')
def hello(world: dict) -> str:
    """
    Welcome screen

    :param world: Current world
    :return: HTML for the page
    """
    return GAME_HEADER + """Hello and welcome to the GAME? <br>
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
        """
    elif where == "town":
        return GAME_HEADER + """This is the town. It's pretty empty right now.
        """

@simple_route('/ask/<pet>/')
def 


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
