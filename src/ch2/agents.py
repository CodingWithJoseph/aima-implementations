# 1. Base Agent
class Agent:
    def perceive(self, percept):
        raise NotImplementedError

    def act(self):
        raise NotImplementedError

# 2. Specific Agent Types
class SimpleReflexAgent(Agent):
    def __init__(self, actions):
        super().__init__()
        self.current_state = None
        self.actions = actions

    def perceive(self, percept):
        self.current_state = self.interpret_input(percept)
        return self.act()

    def act(self):
        return self.actions.get(self.current_state, "NoOp")

    def interpret_input(self, percept):
        raise NotImplementedError

# Model-Based Reflex Agent
# - Has an internal model of the world.
# - Can handle partially observable environments.
# - Updates its model based on percepts before acting.
class ModelBasedReflexAgent(Agent):
    def __init__(self, actions):
        super().__init__()
        self.current_state = None
        self.actions = actions

    def perceive(self, percept):
        super().perceive(percept)
        return self.act()

    def act(self):
        return self.actions.get(self.percept, "NoOp")


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