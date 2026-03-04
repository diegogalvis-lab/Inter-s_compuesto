# para programar determina el incremento con interes compuesto de una capital c

# 1. Pedimos el capital inicial
c = int(input("Ingrese el capital: "))

# 2. El capital actual empieza siendo igual al inicial
capital = c

# 3. Contador de meses
meses = 0

# 4. Mientras no se haya duplicado
while capital < 2 * c:
    capital = capital + capital * 0.05
    meses = meses + 1

# 5. Mostramos el resultado
print("El capital se duplica en", meses, "meses")