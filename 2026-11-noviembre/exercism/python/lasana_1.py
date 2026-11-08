
def EXPECTED_BAKE_TIME():
    """
    Takes 0 parameters, but returns expected_time as 40 (INT).
    """
    return 40

def bake_time_remaining(time_remaining):
    """
    Takes as parameter the time used at that moment to cook, and return the diference between the expected time and the parameter.
    """
    return 40 - time_remaining

def preparation_time_in_minutes(number_of_layers):
    """
    Gives an estimation time taking as parameter the number of layers, every layer are 2 mins. Returns a product of 2 with the number of layers.
    """
    return 2 * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Sum both times and returns and INT.
    """
    return elapsed_bake_time + number_of_layers * 2

print(elapsed_time_in_minutes(4, 20))