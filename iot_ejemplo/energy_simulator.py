import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


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

X = df[["hour"]]
y = df["consumption_kwh"]

print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nPrimeras filas de X:")
print(X.head())

print("\nPrimeras filas de y:")
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train:", X_train.shape, "X_test:", X_test.shape)
print("y_train:", y_train.shape, "y_test:", y_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)

print("slope (a):", model.coef_[0])
print("intercept (b):", model.intercept_)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("MAE:", round(mae, 3))
print("RMSE:", round(rmse, 3))
print("R2:", round(r2, 3))

df.loc[df["day"] == 17, "consumption_kwh"] *= 2

daily_avg = df.groupby("day")["consumption_kwh"].mean()

mean_daily = daily_avg.mean()
std_daily = daily_avg.std()

print("Mean daily consumption:", round(mean_daily, 2))
print("Std daily consumption:", round(std_daily, 2))

anomalous_days = daily_avg[abs(daily_avg - mean_daily) > 2 * std_daily]

print("\nAnomalous days detected:")
print(anomalous_days)

hourly_avg = df.groupby("hour")["consumption_kwh"].mean()

peak_hour = hourly_avg.idxmax()
peak_value = hourly_avg.max()
print(f"\nPeak hour: {peak_hour} with {peak_value:.2f} kWh")



# plt.plot(daily_avg.index, daily_avg.values, marker="o")

# plt.scatter(
#     anomalous_days.index,
#     anomalous_days.values,
#     color="red",
#     s=100
# )

# plt.xlabel("Day")
# plt.ylabel("Average Consumption (kWh)")
# plt.title("Average Daily Energy Consumption")
# plt.show()

# plt.plot(hourly_avg.index, hourly_avg.values, marker="o")
# plt.xlabel("Hour of day")
# plt.ylabel("Average Consumption (kWh)")
# plt.title("Average Consumption Profile (by Hour)")
# plt.xticks(range(0, 24, 1))
# plt.grid(True, alpha=0.3)
# plt.show()