import random

def vacuum_world_2d_evaluation(env):
    return sum(row.count('clean') for row in env.squares)

def vacuum_world_evaluation(env):
    return env.squares.count('clean')

def sra_vacuum_interpret_input(percept):
    return percept['location'], percept['status']

def  sra_vacuum_actions_2squares_1d(state):
    location, status = state
    x, y = location
    if status[x][y] == 'dirty' or status == 'dirty':
        return 'suck'
    elif location == 0:
        return 'right'
    else:
        return 'left'

def  sra_vacuum_actions_2d(state):
    location, status = state
    x, y = location
    if status[x][y] == 'dirty' or status == 'dirty':
        return 'suck'
    else:
        return random.choice(['up', 'down', 'left', 'right'])