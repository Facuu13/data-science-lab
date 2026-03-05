import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1️⃣ Generar datos ficticios
# -----------------------------

days = list(range(1, 31))

minutes = []
base = 40

for day in days:
    trend = base + day * 0.8  # leve tendencia creciente
    noise = random.randint(-10, 10)  # pequeño ruido
    minutes.append(int(trend + noise))

# Inyectamos un día anómalo
minutes[14] = 5  # día 15 extremadamente bajo

intensity = [random.randint(5, 8) for _ in days]
energy = [random.randint(6, 9) for _ in days]

# Crear DataFrame
df = pd.DataFrame({
    "Day": days,
    "Minutes": minutes,
    "Intensity": intensity,
    "Energy": energy
})

df["Moving_Avg"] = df["Minutes"].rolling(window=5).mean()

# -----------------------------
# 2️⃣ Mostrar primeros datos
# -----------------------------
print("Primeras filas:")
print(df.head())

# -----------------------------
# 3️⃣ Estadísticas básicas
# -----------------------------
print("\nPromedio de minutos:", df["Minutes"].mean())
print("Día más intenso:", df.loc[df["Intensity"].idxmax()])

mean_minutes = df["Minutes"].mean()
std_minutes = df["Minutes"].std()

print("\nDesviación estándar:", std_minutes)

# Detectar anomalías
threshold = 2 * std_minutes

anomalies = df[abs(df["Minutes"] - mean_minutes) > threshold]

print("\nDías anómalos detectados:")
print(anomalies)

# -----------------------------
# 4️⃣ Graficar evolución
# -----------------------------
plt.plot(df["Day"], df["Minutes"], label="Minutes")
plt.plot(df["Day"], df["Moving_Avg"], label="Moving Average (5 days)")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.title("Training Minutes Over Time")
plt.legend()
plt.show()