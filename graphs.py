import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = 'Basededatos_SituacionProblemaE1.xlsx'
df = pd.read_excel(data, skiprows=[1])

print("Vista previa:")
print(df.head())

sns.set_theme(style="whitegrid") 

# Gráfico de dispersión: Precio vs Edad
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Age', y='Sale price', color='#1f77b4', alpha=0.8, edgecolor='w', s=80)
plt.title('Relación entre el Precio de Venta y la Edad del Vehículo', fontsize=14, pad=15)
plt.xlabel('Edad (Años)', fontsize=12)
plt.ylabel('Precio de Venta (Pesos)', fontsize=12)
plt.tight_layout()
plt.show()

# Gráfico de dispersión: Precio vs Kilometraje
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Mileage', y='Sale price', color='#d62728', alpha=0.8, edgecolor='w', s=80)
plt.title('Relación entre el Precio de Venta y el Kilometraje', fontsize=14, pad=15)
plt.xlabel('Kilometraje (Millas)', fontsize=12)
plt.ylabel('Precio de Venta (Pesos)', fontsize=12)
plt.tight_layout()
plt.show()