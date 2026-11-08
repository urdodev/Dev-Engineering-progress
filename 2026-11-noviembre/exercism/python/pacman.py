
def eat_ghost(power_pill, touching_ghost):
    return power_pill and touching_ghost

"""
He aprendido a que los boleanos usan ya las funciones booleanas, por lo que no hace falta un if/else, por eso he podido mejorar mucho el codigo.
"""

def score (power_pill, touching_point):
    return power_pill or touching_point


def lose (power_pill, touching_ghost):
    return not power_pill and touching_ghost

def win(all_point, power_pill, touching_ghost):
    return all_point and not (not power_pill and touching_ghost)
#No he sabido la logica detra y me he quedado pillado, le he pedido ayuda a claude.
print(win(False, False, False))