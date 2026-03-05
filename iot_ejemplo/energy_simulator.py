import random
import pandas as pd
import matplotlib.pyplot as plt

data = []

for day in range(1, 31):

    for hour in range(24):

        if hour < 6:
            consumption = random.uniform(0.2, 0.4)

        elif hour < 12:
            consumption = random.uniform(0.4, 0.8)

        elif hour < 18:
            consumption = random.uniform(0.8, 1.5)

        else:
            consumption = random.uniform(1.2, 2.5)

        data.append({
            "day": day,
            "hour": hour,
            "consumption_kwh": round(consumption, 2)
        })

df = pd.DataFrame(data)

# Inyectar una anomalía (pico raro) en una hora específica
anomaly_hour = 14
df.loc[df["hour"] == anomaly_hour, "consumption_kwh"] = 3.5

mean_consumption = df["consumption_kwh"].mean()
std_consumption = df["consumption_kwh"].std()

print("Average consumption:", round(mean_consumption, 2))
print("Standard deviation:", round(std_consumption, 2))

anomalies = df[abs(df["consumption_kwh"] - mean_consumption) > 2 * std_consumption]

for _, row in anomalies.iterrows():
    print(f"⚠ anomalous consumption detected at hour {int(row['hour'])}: {row['consumption_kwh']} kWh")

plt.plot(df["hour"], df["consumption_kwh"], marker="o")

if not anomalies.empty:
    plt.scatter(anomalies["hour"], anomalies["consumption_kwh"], marker="x", s=100)

plt.xlabel("Hour of day")
plt.ylabel("Consumption (kWh)")
plt.title("Daily Energy Consumption (with anomalies)")
plt.show()