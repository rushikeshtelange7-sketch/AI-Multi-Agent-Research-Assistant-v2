from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

topic = "Artificial Intelligence"

print("Planner\n")
plan = planner_agent(topic)
print(plan)

print("\nResearch\n")
research = researcher_agent(topic)
print(research)

print("\nAnalysis\n")
analysis = analyst_agent(topic, research)
print(analysis)

print("\nReport\n")
report = writer_agent(topic, analysis)
print(report)