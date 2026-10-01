def organizar_eventos(eventos, expresion=False):
    if expresion:
        return sorted(eventos, reverse=True)
    else:
        return sorted(eventos)

lista_eventos = ["Kermes", "Concurso de comida", "Reunion del consejo municipal"]
print(organizar_eventos(lista_eventos))
print(organizar_eventos(lista_eventos, True))