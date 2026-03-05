import random
import pandas as pd
import matplotlib.pyplot as plt

data = []

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
        "hour": hour,
        "consumption_kwh": round(consumption, 2)
    })

df = pd.DataFrame(data)

mean_consumption = df["consumption_kwh"].mean()
std_consumption = df["consumption_kwh"].std()

print("Average consumption:", round(mean_consumption, 2))
print("Standard deviation:", round(std_consumption, 2))

plt.plot(df["hour"], df["consumption_kwh"])
plt.xlabel("Hour of day")
plt.ylabel("Consumption (kWh)")
plt.title("Daily Energy Consumption")
plt.show()