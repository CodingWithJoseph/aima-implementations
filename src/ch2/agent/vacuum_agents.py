import random

def vacuum_world_2d_evaluation(env):
    return sum(row.count('clean') for row in env.squares)

def sra_vacuum_interpret_input(percept):
    return percept['location'], percept['status']

def  sra_vacuum_actions(state):
    location, status = state
    x, y = location
    if isinstance(status, str) and status == 'dirty':
        return 'suck'
    if isinstance(status, list) and isinstance(status[0], list) and status[x][y] == 'dirty':
        return 'suck'
    else:
        return random.choice(['up', 'down', 'left', 'right'])


def transition_model_fully_observable(state, action):
    pass