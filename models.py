import pandas as pd
import statsmodels.formula.api as smf

data = 'Basededatos_SituacionProblemaE1.xlsx'
df = pd.read_excel(data, skiprows=[1])

# Reemplazar los espacios por guiones bajos en los nombres de las columnas
df.columns = df.columns.str.replace(' ', '_')

print("REGRESIÓN LINEAL SIMPLE")

# Modelo 1: Precio vs Edad
modelo_1 = smf.ols('Sale_price ~ Age', data=df).fit()
print("\nMODELO 1")
print(modelo_1.summary())

# Modelo 2: Precio vs Kilometraje
modelo_2 = smf.ols('Sale_price ~ Mileage', data=df).fit()
print("\nMODELO 2")
print(modelo_2.summary())


print("\n\nPARTE 3: REGRESIÓN MÚLTIPLE")

# Modelo 3: Edad y Kilometraje
modelo_3 = smf.ols('Sale_price ~ Age + Mileage', data=df).fit()

# Modelo 4: Edad, Kilometraje y Condición
modelo_4 = smf.ols('Sale_price ~ Age + Mileage + Condition + Excellent', data=df).fit()

# Modelo 5: Edad, Kilometraje, Condición y Único Dueño
modelo_5 = smf.ols('Sale_price ~ Age + Mileage + Condition + Excellent + One_owner', data=df).fit()

print("\nMODELO 5")
print(modelo_5.summary())

# PREDICCIÓN FINAL Y CÁLCULO DEL RESIDUO
auto_nuevo = pd.DataFrame({
    'Age': [5],
    'Mileage': [85], 
    'Condition': [0],
    'Excellent': [1],
    'One_owner': [1]
})

# Suponiendo que determinas que el Modelo 5 es el mejor (puedes cambiarlo al 3 o 4)
precio_predicho = modelo_5.predict(auto_nuevo)[0]
precio_real = 155000
residuo = precio_real - precio_predicho

print("\n--- PREDICCIÓN Y RESIDUO ---")
print(f"Precio Predicho: ${precio_predicho:,.2f}")
print(f"Precio Real: ${precio_real:,.2f}")
print(f"Residuo (Real - Predicho): ${residuo:,.2f}")