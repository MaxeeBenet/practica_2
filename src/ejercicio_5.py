def calcular_costo_envio():
    peso = float(input("Ingrese el peso del paquete (kg): "))
    zona = input("Ingrese la zona de destino (local/regional/nacional):")
    
    if zona == "local":
        if peso <= 1:
            costo = 500
        elif peso <= 5:
            costo = 1000
        else:
            costo = 2000
    elif zona == "regional":
        if peso <= 1:
            costo = 1000
        elif peso <= 5:
            costo = 2500
        else:
            costo = 5000
    elif zona == "nacional":
        if peso <= 1:
            costo = 2000
        elif peso <= 5:
            costo = 4500
        else:
            costo = 8000
    else:
        print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
        return
    
    print(f"Costo de envío: ${costo}")

if __name__ == "__main__":    
    calcular_costo_envio()