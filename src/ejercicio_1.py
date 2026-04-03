
def estadisticas(text):
    lines = text.split(".")

    total_lines = len(lines)
    
    total = sum(len(line.split()) for line in lines)
    
    average = round((total / total_lines),2)
    
    print(f"El total de lineas es {total_lines}")
    print()
    print(f"El total de palabras es: {total} ")
    print()
    print(f"Lineas por encima del promedio {average}: ")
    print()
    for line in lines:
        words = line.split()
        if len(words) > average:
            print(f'- "{line.replace("\n", " ").strip()}" ({len(words)} palabras)')
    
    
    
    
    
