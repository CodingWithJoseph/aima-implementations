from src.ch2.agents import SimpleReflexAgent
from src.ch2.agent.vacuum_agents import sra_vacuum_interpret_input, sra_vacuum_actions_2d, vacuum_world_2d_evaluation
from src.ch2.environments import FullyObservableVacuumEnvironment

fully_observed_vacuum_environment = FullyObservableVacuumEnvironment(squares=[['dirty', 'dirty', 'clean'], ['clean', 'dirty', 'clean'], ['clean', 'dirty', 'dirty']])
sra_vacuum_agent = SimpleReflexAgent(sra_vacuum_actions_2d, sra_vacuum_interpret_input)

print("Running fully simple reflex agent in fully observed environment")
for step in range(25):
    action, percept = fully_observed_vacuum_environment.step(sra_vacuum_agent)
    print(f"Step {step}: Agent did {action}, percept = {percept}")

score = vacuum_world_2d_evaluation(fully_observed_vacuum_environment)
print("Score for simple reflex agent in fully observed environment")
print(f"Squares cleaned: {score}")  