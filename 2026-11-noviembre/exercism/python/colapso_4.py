
def is_criticality_balanced(temperature, neutrons):
    #He aprendido a ver de otra forma los bools, de una funcion if else que tenia, el copilot ha mejorado de esta maneraa el codigo.
    return bool(temperature < 800 and neutrons > 500 and temperature * neutrons < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):

    percentual_value = (voltage * current / theoretical_max_power)*100

    if percentual_value >= 80:
        return "Green"
    elif percentual_value >= 60:
        return "Orange"
    elif percentual_value >= 30 :
        return "Red"
    return "Black"

def fail_safe(temperatura, neutrons_produced_per_second, threshold):
    state = temperatura * neutrons_produced_per_second
    if state < threshold*0.9:
        return "LOW"
    if threshold*0.9 <= state <= threshold* 1.1:
        return "NORMAL"
    return "DANGER"



print(is_criticality_balanced(700, 600))
print(reactor_efficiency(200,10,15000))
print(fail_safe(150, 30, 5000))