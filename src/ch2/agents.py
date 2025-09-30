from abc import ABC, abstractmethod

# 1. Base Agent
class Agent(ABC):
    @abstractmethod
    def step(self, percept):
        pass

# 2. Specific Agent Types
class SimpleReflexAgent(Agent):
    def __init__(self, actions, interpret_input):
        super().__init__()
        self.actions = actions
        self.interpret_input = interpret_input

    def step(self, percept):
        state = self.interpret_input(percept)
        return self.actions(state)


# Model-Based Reflex Agent
class ModelBasedReflexAgent(Agent):
    def __init__(self, internal_state, rules, sensor_model, transition_model):
        super().__init__()
        self.internal_state = internal_state
        self.rules = rules
        self.action = 'NoOp'
        self.sensor_model = sensor_model
        self.transition_model = transition_model

    def update_state(self, percept):
        predicted_state = self.transition_model(self.internal_state, self.action)
        self.internal_state = self.sensor_model(predicted_state, percept)

    def rule_match(self):
        for condition in self.rules:
            action = condition(self.internal_state)
            if action is not None:
                return action
        return 'NoOp'

    def step(self, percept):
        self.update_state(percept)
        self.action = self.rule_match()
        return self.action

# Goal-Based Agent
class GoalBasedAgent(Agent):
    def step(self, percept):
        pass

# Utility-Based Agent
class UtilityBasedAgent(Agent):
    def step(self, percept):
        pass

# Learning Agent
class LearningBasedAgent(Agent):
    def step(self, percept):
        pass