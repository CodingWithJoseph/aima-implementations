import random

from src.ch2.agents import ModelBasedReflexAgent


def vacuum_world_2d_evaluation(env):
    return sum(row.count('clean') for row in env.squares)

def vacuum_interpret_input(percept):
    return percept['location'], percept['status']

def vacuum_interpret_input_partial(percept):
    return percept['status']

def  sra_vacuum_actions_full(state):
    location, status = state
    x, y = location
    if isinstance(status, str) and status == 'dirty':
        return 'suck'
    if isinstance(status, list) and isinstance(status[0], list) and status[x][y] == 'dirty':
        return 'suck'
    else:
        return random.choice(['up', 'down', 'left', 'right'])

def sra_vacuum_actions_partial(state):
    status = state
    if isinstance(status, str) and status == 'dirty':
        return 'suck'
    else:
        return random.choice(['up', 'down', 'left', 'right'])


class ModelBasedVacuumAgent(ModelBasedReflexAgent):
    def __init__(self, agent_location, rules, sensor_model, transition_model, interpret_input):
        super().__init__(
            internal_state=self._initialize_internal_state(agent_location),
            rules=rules,
            sensor_model=sensor_model,
            transition_model=transition_model,
            interpret_input=interpret_input
        )

    def _initialize_internal_state(self, agent_location):
        return {'agent_location': agent_location, 'internal_state': {agent_location: 'unknown'}, 'movement_history': []}


def sensor_model_vacuum(predicted_state, percept, interpret_input):
    agent_location = predicted_state['agent_location']
    internal_state = predicted_state['internal_state']
    movement_history = predicted_state['movement_history']

    status = interpret_input(percept)
    internal_state[agent_location] = status

    return {
        'agent_location': agent_location,
        'internal_state': internal_state,
        'movement_history': movement_history
    }


def transition_model_vacuum(state, action):
    location = state['agent_location']
    internal_state = dict(state['internal_state'])
    movement_history = state['movement_history']
    if action == 'suck':
        internal_state[location] = 'clean'
        return {'agent_location': location, 'internal_state': internal_state, 'movement_history': movement_history}
    elif action == 'up':
        return {'agent_location': (location[0] - 1, location[1]), 'internal_state': internal_state, 'movement_history': movement_history}
    elif action == 'down':
        return {'agent_location': (location[0] + 1, location[1]), 'internal_state': internal_state, 'movement_history': movement_history}
    elif action == 'left':
        return {'agent_location': (location[0], location[1] - 1), 'internal_state': internal_state, 'movement_history': movement_history}
    elif action == 'right':
        return {'agent_location': (location[0], location[1] + 1), 'internal_state': internal_state, 'movement_history': movement_history}
    return state

def rule_clean(state):
    location = state['agent_location']
    internal_state = state['internal_state']
    if internal_state[location] == 'dirty':
        return 'suck'
    return None

def rule_movement(state):
    location = state['agent_location']
    internal_state = state['internal_state']
    movement_history = state['movement_history']
    loc_actions = [
        ((location[0] - 1, location[1]), 'up'),
        ((location[0] + 1, location[1]), 'down'),
        ((location[0], location[1] - 1), 'left'),
        ((location[0], location[1] + 1), 'right')
    ]

    while loc_actions:
        neighbor_loc, action = random.choice(loc_actions)
        loc_actions.remove((neighbor_loc, action))

        if (neighbor_loc in internal_state and internal_state[
            neighbor_loc] == 'dirty') or neighbor_loc not in internal_state:
            movement_history.append(action)
            return action
    return None

def rule_backtrack(state):
    mov_action = state['movement_history'].pop()
    if mov_action == 'up':
        print(f'backtrack: down')
        return 'down'
    elif mov_action == 'down':
        print(f'backtrack: up')
        return 'up'
    elif mov_action == 'left':
        print(f'backtrack: right')
        return 'right'
    elif mov_action == 'right':
        print(f'backtrack: left')
        return 'left'
    return None