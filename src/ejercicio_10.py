def calcular_puntajes(scores):
    total_scores = {}
    
    for cook, jueces in scores.items():
        total = sum(jueces.values())
        total_scores[cook] = total
        
    return total_scores

def actualizar_estadisticas(stats, puntajes_ronda, winner, round_number):
    for cook, points in puntajes_ronda.items():
        stats[cook]["total"] += points
        if stats[cook]["best"] < puntajes_ronda[cook]:
            stats[cook]["best"] = points
        stats[cook]["average"] = round((stats[cook]["total"] / round_number),1)
    stats[winner]["wins"]  += 1

def imprimir_tabla_ronda(stats):
    print("Tabla parcial de resultados!")
    print(f"{'Nombre':14} {'Puntos totales':17} {'Rondas ganadas':17} {'Mejor puntuacion':17} {'Promedio':17}")
    for name, values in stats.items():
            print(f"{name:10} {values["total"]:15} {values["wins"]:15} {values["best"]:15} {values["average"]:15}")
    
        
def imprimir_tabla_final(stats):
    ordenada = sorted(stats.items(), key= lambda x: x[1]["total"], reverse = True)
    print("*" * 30 +  "TABLA FINAL" + "*" * 30)
    print("-" * 76)
    print(f"{'Nombre':14} {'Puntos totales':17} {'Rondas ganadas':17} {'Mejor puntuacion':17} {'Promedio':17}")
    print()
    for key, value in ordenada:
        print(f"{key:10} {value['total']:15} {value['wins']:15} {value['best']:15} {value['average']:15}")
        
    print("-" * 76)
    winner_of_competition = ordenada[0][0]
    
    print("La ganadora de este torneo es: ")
    print(winner_of_competition)
    
def concurso(rounds):
    
    stats = {
        "Valentina" : {"total" : 0, "wins" : 0, "best" : 0, "average" : 0},
        "Mateo" : {"total" : 0, "wins" : 0, "best" : 0, "average" : 0},
        "Camila" : {"total" : 0, "wins" : 0, "best" : 0, "average" : 0},
        "Santiago" : {"total" : 0, "wins" : 0, "best" : 0, "average" : 0},
        "Lucía" : {"total" : 0, "wins" : 0, "best" : 0, "average" : 0}
    }
    
    round_number = 1
    
    for round in rounds:
        print(f"Ronda {round_number} - '{round["theme"]}'")
        puntajes_ronda = calcular_puntajes(round['scores'])
        winner = max(puntajes_ronda, key=puntajes_ronda.get)
        actualizar_estadisticas(stats, puntajes_ronda, winner, round_number)
        round_number += 1
        print(f"Ganador de la ronda {winner} ({puntajes_ronda[winner]} pts)")
        imprimir_tabla_ronda(stats)
        print()
        
    print()   
    imprimir_tabla_final(stats)
            
        
        
if __name__ == "__main__":
    concurso(rounds)
    

        
        