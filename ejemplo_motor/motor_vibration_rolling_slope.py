import random
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) Simulación: vibración de motor (60 días)
# -----------------------------
days = list(range(1, 61))
vibration = []
base = 45

for day in days:
    trend = base + day * 0.2        # desgaste lento
    noise = random.randint(-3, 3)   # ruido
    vibration.append(trend + noise)

df = pd.DataFrame({"Day": days, "Vibration": vibration})

# -----------------------------
# 2) Pendiente móvil (rolling slope)
#    Calculamos la pendiente en ventanas de N días:
#    slope_window = (v_last - v_first) / (N-1)
# -----------------------------
window = 20  # últimos 10 días
df["RollingSlope"] = (
    df["Vibration"].rolling(window=window)
    .apply(lambda s: (s.iloc[-1] - s.iloc[0]) / (window - 1), raw=False)
)

# -----------------------------
# 3) Alerta por pendiente móvil
# -----------------------------
threshold_slope = 0.22  # ajustable
df["AboveThresh"] = df["RollingSlope"] > threshold_slope

print("Últimas filas (para ver pendiente móvil y alertas):")
print(df.tail(15))

# "Debounce": alerta si supera el umbral 3 días seguidos
consecutive_days = 3
df["TrendAlert"] = df["AboveThresh"].rolling(consecutive_days).sum() >= consecutive_days

# ¿En qué días saltó alerta?
alert_days = df[df["TrendAlert"]]["Day"].tolist()
print("\nDías con ALERTA CONFIRMADA (3 días seguidos):", alert_days)

# -----------------------------
# 4) Gráficos
# -----------------------------
plt.plot(df["Day"], df["Vibration"], label="Vibration")
plt.xlabel("Day")
plt.ylabel("Vibration")
plt.title("Motor Vibration Over Time")
plt.legend()
plt.show()

plt.plot(df["Day"], df["RollingSlope"], label=f"Rolling Slope ({window} days)")
plt.axhline(threshold_slope, linestyle="--", label="Slope Threshold")
plt.xlabel("Day")
plt.ylabel("Slope (units/day)")
plt.title("Rolling Trend Detection")
plt.legend()
plt.show()