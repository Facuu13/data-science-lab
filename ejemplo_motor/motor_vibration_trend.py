import random
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) Simulación: vibración de motor (60 días)
#    - tendencia creciente lenta
#    - ruido pequeño
# -----------------------------
days = list(range(1, 61))  # 60 días

vibration = []
base = 45

for day in days:
    trend = base + day * 0.2          # aumento lento y progresivo
    noise = random.randint(-3, 3)     # ruido pequeño
    vibration.append(trend + noise)

df = pd.DataFrame({
    "Day": days,
    "Vibration": vibration
})

# -----------------------------
# 2) Mostrar una muestra
# -----------------------------
print("Primeras filas:")
print(df.head())

print("\nÚltimas filas:")
print(df.tail())

# -----------------------------
# 3) Medir tendencia (pendiente promedio simple)
# -----------------------------
slope = (df["Vibration"].iloc[-1] - df["Vibration"].iloc[0]) / (len(df) - 1)

print("\nVibración inicial:", df["Vibration"].iloc[0])
print("Vibración final:", df["Vibration"].iloc[-1])
print("Pendiente promedio por día:", slope)

# Umbral simple de alerta (ajustable)
threshold_slope = 0.15
if slope > threshold_slope:
    print("⚠️ ALERTA: Tendencia creciente detectada (posible desgaste).")
else:
    print("✅ OK: No se detecta tendencia preocupante.")

# -----------------------------
# 4) Gráfico
# -----------------------------
plt.plot(df["Day"], df["Vibration"], label="Vibration")
plt.xlabel("Day")
plt.ylabel("Vibration")
plt.title("Motor Vibration Over Time")
plt.legend()
plt.show()