def area_trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio."""
    return ((base_mayor + base_menor) * altura) / 2

def perimetro_trapecio(base_mayor, base_menor, lado1, lado2):
    """Calcula el perímetro de un trapecio."""
    return base_mayor + base_menor + lado1 + lado2

print("=== Cálculo de Trapecio ===")
print("1. Calcular Área")
print("2. Calcular Perímetro")

opcion = input("Seleccione una opción (1 o 2): ")

try:
    if opcion == '1':
        B = float(input("Ingrese la longitud de la base mayor: "))
        b = float(input("Ingrese la longitud de la base menor: "))
        h = float(input("Ingrese la altura: "))
        
        area = area_trapecio(B, b, h)
        print(f"El área del trapecio es: {area:.2f}")

    elif opcion == '2':
        B = float(input("Ingrese la longitud de la base mayor: "))
        b = float(input("Ingrese la longitud de la base menor: "))
        L1 = float(input("Ingrese la longitud del lado no paralelo 1: "))
        L2 = float(input("Ingrese la longitud del lado no paralelo 2: "))
        
        perimetro = perimetro_trapecio(B, b, L1, L2)
        print(f"El perímetro del trapecio es: {perimetro:.2f}")

    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

except ValueError:
    print("Error: Ingrese valores numéricos válidos.")

