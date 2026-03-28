import pandas as pd

df = pd.read_csv("data/raw_dataset.csv")
df = df.dropna()
df["Delivery_person_Ratings"] = pd.to_numeric(
    df["Delivery_person_Ratings"], errors="coerce"
)
df = df.dropna(subset=["Delivery_person_Ratings"])
location_ids = []
for i in range(len(df)):
    location_ids.append("L" + str(i + 1))
df["Location_ID"] = location_ids
distance_values = []
for i in range(len(df)):
    lat1 = df.iloc[i]["Restaurant_latitude"]
    lon1 = df.iloc[i]["Restaurant_longitude"]
    lat2 = df.iloc[i]["Delivery_location_latitude"]
    lon2 = df.iloc[i]["Delivery_location_longitude"]
    distance = ((lat1 - lat2)**2 + (lon1 - lon2)**2) ** 0.5
    distance_values.append(round(distance, 2))
df["Distance"] = distance_values
priority_values = []
for rating in df["Delivery_person_Ratings"]:
    if rating >= 4.5:
        priority_values.append("High")
    elif rating >= 4.0:
        priority_values.append("Medium")
    else:
        priority_values.append("Low")
df["Priority"] = priority_values
final_data = df[["Location_ID", "Distance", "Priority"]]
final_data.to_csv("data/processed_dataset.csv", index=False)
print("Dataset preprocessing completed.")
print("Total deliveries:", len(final_data))