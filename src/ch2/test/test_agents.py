from src.ch2.agents import SimpleReflexAgent
from src.ch2.agent.vacuum_agents import sra_vacuum_interpret_input, sra_vacuum_actions, vacuum_world_2d_evaluation
from src.ch2.environments import FullyObservableGridEnvironment2D, PartiallyObservableGridEnvironment2D

fully_observed_vacuum_environment = FullyObservableGridEnvironment2D(squares=[['dirty', 'dirty', 'clean'], ['clean', 'dirty', 'clean'], ['clean', 'dirty', 'dirty']])
partially_observed_vacuum_environment = PartiallyObservableGridEnvironment2D(squares=[['dirty', 'dirty', 'dirty'], ['dirty', 'dirty', 'dirty'], ['clean', 'dirty', 'dirty']])


'''
Simple reflex agent in fully and partially observed environment
'''
sra_vacuum_agent = SimpleReflexAgent(sra_vacuum_actions, sra_vacuum_interpret_input)

########### Fully Observable
print("Running simple reflex agent in fully observed environment")
for step in range(25):
    action, percept = fully_observed_vacuum_environment.step(sra_vacuum_agent)
    print(f"Step {step}: Agent did {action}, percept = {percept}")

score = vacuum_world_2d_evaluation(fully_observed_vacuum_environment)
print("Score for simple reflex agent in fully observed environment")
print(f"Squares cleaned: {score}")




########### Partially Observable
print("\nRunning simple reflex agent in partially observed environment")
for step in range(25):
    action, percept = partially_observed_vacuum_environment.step(sra_vacuum_agent)
    print(f"Step {step}: Agent did {action}, percept = {percept}")

score = vacuum_world_2d_evaluation(partially_observed_vacuum_environment)
print("Score for simple reflex agent in partially observed environment")
print(f"Squares cleaned: {score}")


