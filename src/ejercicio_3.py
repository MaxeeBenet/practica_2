

def filtrado(text):
    
    text = text.split()

    print("Ingrese las palabras spoiler separadas por comas: ")
    spoilers = input().split(",")
    
    spoilers = [spoiler.strip().lower() for spoiler in spoilers]
  
    for words in range(len(text)):
        if text[words].lower() in spoilers:
            text[words] = len(text[words]) * "*"
    resultado = " ".join(text)
    
    resultado = resultado.replace(".", ".\n")
    
    print(resultado)
    
if __name__ == "__main__":
    review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""
    filtrado(review)
