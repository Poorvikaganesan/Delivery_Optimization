import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed_dataset.csv")

data = data.dropna()

priority_map = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

data["Priority_Value"] = data["Priority"].map(priority_map)

data = data.sort_values(by=["Priority_Value", "Distance"])

data = data.drop("Priority_Value", axis=1)


agent_distance = {
    "Agent_A": 0,
    "Agent_B": 0,
    "Agent_C": 0
}

assigned_agents = []


for i in range(len(data)):

    selected_agent = min(agent_distance, key=agent_distance.get)

    assigned_agents.append(selected_agent)

    delivery_distance = data.iloc[i]["Distance"]

    agent_distance[selected_agent] += delivery_distance


data["Assigned_Agent"] = assigned_agents


data.to_csv("output/delivery_plan.csv", index=False)


print("\nDelivery Assignment Summary\n")

for agent in agent_distance:
    print(agent, "Total Distance:", round(agent_distance[agent], 2))

print("\nDeliveries handled by each agent:")
print(data["Assigned_Agent"].value_counts())

print("\nTotal deliveries processed:", len(data))


print("\nAverage distance per delivery:")

for agent in agent_distance:

    deliveries = len(data[data["Assigned_Agent"] == agent])

    if deliveries > 0:
        avg = agent_distance[agent] / deliveries
        print(agent, ":", round(avg, 2))

agents = list(agent_distance.keys())
distances = list(agent_distance.values())
plt.bar(agents, distances)
plt.title("Total Distance Handled by Each Agent")
plt.xlabel("Agents")
plt.ylabel("Total Distance")
plt.show()
print("\nDelivery plan saved in output/delivery_plan.csv")