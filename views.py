from route_helper import simple_route
from flask import render_template, request
from random import random, randint

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
    world['status'] = {}
    world['speedpill'] = 0
    world['sizepill'] = 0
    world['strengthpill'] = 0
    world['beautypill'] = 0
    world['contestlevel'] = 0
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
        return render_template('petfacility.html', balance=world['balance'])
    elif where == "town":
        return render_template('town.html', balance=world['balance'])
    elif where == "home":
        return render_template('home.html', pet=world['pet'], name=world['name'], balance=world['balance'])

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
        world['status'] = {
            "speed": 20,
            "size": 95,
            "strength": 80,
            "beauty": 25
        }
    elif pet == 'leopard':
        world['image'] = "/static/leopard.jpg"
        world['status'] = {
            "speed": 75,
            "size": 70,
            "strength": 75,
            "beauty": 65,
        }
    elif pet == 'jellyfish':
        world['image'] = "/static/jellyfish.jpg"
        world['status'] = {
            "speed": 10,
            "size": 10,
            "strength": 10,
            "beauty": 100,
        }
    elif pet == 'eagle':
        world['image'] = "/static/eagle.jpg"
        world['status'] = {
            "speed": 100,
            "size": 45,
            "strength": 40,
            "beauty": 70,
        }
    return render_template('askpet.html', pet=pet, balance=world['balance'])

@simple_route('/pet/naming/')
def name(world: dict) -> str:
    """
    Place to name your pet

    :param world: The current world
    :return: HTML that shows the page
    """
    return render_template('petnaming.html', pet=world['pet'], image=world['image'], balance=world['balance'])

@simple_route('/pet/naming/', methods=['POST'])
def name_post(world: dict, name: str) -> str:
    """
    Pet has been named

    :param other: I don't know what this is.
    :param world: The current world
    :return: HTML that shows page
    """
    world['name'] = name
    if name.lower() == "lemon":
        world['balance'] += 1200
    return render_template('nameconfirm.html', pet=world['pet'], image=world['image'], name=world['name'], balance=world['balance'])

@simple_route('/pet/status/')
def check_status(world: dict) -> str:
    '''

    :param world: The current world
    :return: HTML that shows page
    '''
    return render_template('petstatus.html', pet=world['pet'], image=world['image'], name=world['name'], status=world['status'], balance=world['balance'], speedpill=world['speedpill'], sizepill=world['sizepill'], strengthpill=world['strengthpill'], beautypill=world['beautypill'])

@simple_route('/purchase/<item>/')
def purchase_item(world:dict, item:str) -> str:
    '''

    :param item: The item you would like to purchase
    :param world: The current world
    :return: HTML that shows page
    '''
    world['current_item'] = item
    if world['balance'] >= 100:
        if world['current_item'] == "speed":
            world['speedpill'] += 1
            world['balance'] -= 100
            return render_template('purchase.html', current_item=world['current_item'], balance=world['balance'])
        elif world['current_item'] == "size":
            world['sizepill'] += 1
            world['balance'] -= 100
            return render_template('purchase.html', current_item=world['current_item'], balance=world['balance'])
        elif world['current_item'] == 'strength':
            world['strengthpill'] += 1
            world['balance'] -= 100
            return render_template('purchase.html', current_item=world['current_item'], balance=world['balance'])
        elif world['current_item'] == 'beauty':
            world['beautypill'] += 1
            world['balance'] -= 100
            return render_template('purchase.html', current_item=world['current_item'], balance=world['balance'])
    else:
        return render_template('poor.html', current_item=world['current_item'], balance=world['balance'])

@simple_route('/money/')
def make_money(world:dict) -> str:
    '''

    :param world: The current world
    :return: HTML that shows the page
    '''
    a = randint(0,20)
    b = randint(0,20)
    c = a+b
    return render_template('money.html', balance=world['balance'], a=a, b=b, c=c)

@simple_route('/money/', methods=['POST'])
def made_money(world:dict, answer:str, c:str) -> str:
    '''

    :param c: The answer to the math question
    :param answer: The user answer to the math question
    :param world: The current world
    :return: HTML that shows the page
    '''
    try:
        if int(c) == int(answer):
            amount = randint(50,150)
            world['balance'] += amount
            return render_template('moneymade.html', balance=world['balance'], amount=amount)
        else:
            return render_template('nomoney.html', balance=world['balance'], c=c, answer=answer)
    except ValueError:
        return render_template('nomoney.html', balance=world['balance'], c=c, answer=answer)

@simple_route('/pet/feed/')
def feed_pet(world:dict) -> str:
    '''

    :param world: The current world
    :return: HTML that shows the page
    '''
    return render_template('pickfeed.html', balance=world['balance'], speedpill=world['speedpill'], sizepill=world['sizepill'], strengthpill=world['strengthpill'], beautypill=world['beautypill'], name=world['name'])

@simple_route('/pet/feed/<food>/')
def true_feed_pet(world:dict, food:str) -> str:
    '''

    :param world: The current world
    :param food: The pill that user feeds to the pet
    :return: HTML that shows the page
    '''
    if food == "speed":
        world['speedpill'] -= 1
        world['status']['speed'] += 10
        return render_template('feed.html', balance=world['balance'], stat=food, name=world['name'])
    elif food == "size":
        world['sizepill'] -= 1
        world['status']['size'] += 10
        return render_template('feed.html', balance=world['balance'], stat=food, name=world['name'])
    elif food == "strength":
        world['strengthpill'] -= 1
        world['status']['strength'] += 10
        return render_template('feed.html', balance=world['balance'], stat=food, name=world['name'])
    elif food == "beauty":
        world['beautypill'] -= 1
        world['status']['beauty'] += 10
        return render_template('feed.html', balance=world['balance'], stat=food, name=world['name'])
    else:
        return render_template('pickfeed.html', balance=world['balance'], speedpill=world['speedpill'], sizepill=world['sizepill'], strengthpill=world['strengthpill'], beautypill=world['beautypill'], name=world['name'])

@simple_route('/contest/')
def contest(world:dict) -> str:
    '''

    :param world: The current world
    :return: HTML that shows the current page
    '''
    if world['contestlevel'] == 0:
        return render_template('contest_one.html', balance=world['balance'], status=world['status'], name=world['name'])
    if world['contestlevel'] == 1:
        return render_template('contest_two.html', balance=world['balance'], status=world['status'], name=world['name'])
    if world['contestlevel'] == 2:
        return render_template('contest_three.html', balance=world['balance'], status=world['status'], name=world['name'])

@simple_route('/contest/<which>/')
def contest_attempt(world:dict, which:str) -> str:
    '''

    :param which: The current contest attempt
    :param world: The current world
    :return: HTML that shows page
    '''
    if which == "speed1":
        if world['status']['speed'] > 50:
            world['contestlevel'] = 1
            return render_template('contest_win_one.html', balance=world['balance'], status=world['status'], name=world['name'], win="Speed")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "size1":
        if world['status']['size'] > 60:
            world['contestlevel'] = 1
            return render_template('contest_win_one.html', balance=world['balance'], status=world['status'], name=world['name'], win="Size")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "strength1":
        if world['status']['strength'] > 40:
            world['contestlevel'] = 1
            return render_template('contest_win_one.html', balance=world['balance'], status=world['status'], name=world['name'], win="Strength")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "beauty1":
        if world['status']['beauty'] > 75:
            world['contestlevel'] = 1
            return render_template('contest_win_one.html', balance=world['balance'], status=world['status'], name=world['name'], win="Beauty")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "speed2":
        if world['status']['speed'] > 75:
            world['contestlevel'] = 2
            return render_template('contest_win_two.html', balance=world['balance'], status=world['status'], name=world['name'], win="Speed")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "size2":
        if world['status']['size'] > 100:
            world['contestlevel'] = 2
            return render_template('contest_win_two.html', balance=world['balance'], status=world['status'], name=world['name'], win="Size")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "strength2":
        if world['status']['strength'] > 80:
            world['contestlevel'] = 2
            return render_template('contest_win_two.html', balance=world['balance'], status=world['status'], name=world['name'], win="Strength")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "beauty2":
        if world['status']['beauty'] > 125:
            world['contestlevel'] = 2
            return render_template('contest_win_two.html', balance=world['balance'], status=world['status'], name=world['name'], win="Beauty")
        else:
            world['contestlevel'] = 0
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])
    if which == "final":
        total = 0
        for k in world['status']:
            total += world['status'][k]
        if total > 350:
            return render_template('contestwin.html', balance=world['balance'], status=world['status'], name=world['name'], win='total')
        elif world['status']['beauty'] > 200:
            return render_template('contestwin.html', balance=world['balance'], status=world['status'], name=world['name'], win='beauty')
        else:
            return render_template('contestfail.html', balance=world['balance'], status=world['status'], name=world['name'])

@simple_route("/finish/")
def finish(world:dict) -> str:
    '''

    :param world: The current world
    :return: HTML to be shown
    '''
    return render_template('end.html', balance=world['balance'], status=world['status'], name=world['name'], image=world['image'])
