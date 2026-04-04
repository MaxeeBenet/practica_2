"""Valide una dirección de email ingresada por el usuario con los siguientes
criterios:
Contiene exactamente un @.
Tiene al menos un carácter antes del @.
Tiene al menos un punto (.) después del @.
No empieza ni termina con @ ni con ..
La parte después del último punto tiene al menos 2 caracteres (el dominio).
"""


def validar(email):
    if email.count("@") != 1:
        return False
    
    if email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        return False
    
    parts = email.split("@")
    domain = parts[1]
    name = parts[0]  
      
    if domain.count(".") < 1:
        return False
    
    if len(name) < 1:
        return False
    
    domain_parts = domain.split(".")
    
    if len(domain_parts[-1]) < 2:
        return False
    
    return True
    