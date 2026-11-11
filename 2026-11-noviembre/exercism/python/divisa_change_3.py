

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_bills):
    return int(denomination * number_bills)

def get_number_of_bills(amount, denomination):
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    real_state = exchange_rate * (1 + spread/100)
    exchange_amount = budget / real_state
    number_bills = get_number_of_bills(exchange_amount, denomination)

    return get_value_of_bills(denomination, number_bills)

print(exchangeable_value(127.5, 1.20, 10, 100))