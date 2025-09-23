def vacuum_world_evaluation(env):
    return env.squares.count('clean')

def sra_vacuum_interpret_input(percept):
    return percept['location'], percept['status']

def sra_vacuum_actions(state):
    location, status = state
    if status[location] == 'dirty' or status == 'dirty':
        return 'suck'
    elif location == 0:
        return 'right'
    else:
        return 'left'