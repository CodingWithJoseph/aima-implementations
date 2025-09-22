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
    def __init__(self, rules, sensor_model, transition_model):
        super().__init__()
        self.state = None
        self.rules = rules
        self.action = 'NoOp'
        self.sensor_model = sensor_model
        self.transition_model = transition_model

    def update_state(self, percept):
        predicted_state = self.transition_model(self.state, self.action)
        self.state = self.sensor_model(predicted_state, percept)

    def rule_match(self):
        for condition in self.rules:
            action = condition(self.state)
            if action is not None:
                return action
        return 'NoOp'

    def step(self, percept):
        self.update_state(percept)
        self.action = self.rule_match()
        return self.action

# Goal-Based Agent
# - Has explicit goals.
# - Chooses actions by reasoning about future states.
# - Can plan sequences of actions to reach the goal.

# Utility-Based Agent
# - Uses a utility function to evaluate states.
# - Chooses the action that maximizes expected utility.
# - Can handle trade-offs between conflicting objectives.

# Learning Agent
# - Improves over time by learning from experience.
# - Components to implement conceptually:
#     - Performance element → selects actions.
#     - Learning element → updates knowledge/strategy.
#     - Critic → evaluates actions or outcomes.
#     - Problem generator → suggests exploratory actions.