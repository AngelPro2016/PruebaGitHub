def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2

try:
    B = float(input("Ingrese la longitud de la base mayor: "))
    b = float(input("Ingrese la longitud de la base menor: "))
    h = float(input("Ingrese la altura: "))

    area = area_trapecio(B, b, h)
    print(f"El área del trapecio es: {area:.2f}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
