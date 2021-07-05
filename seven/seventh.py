

def getMaxValue(carrotTypes, capacity):
    sorted_carrots = sorted(carrotTypes, key=lambda carrot_type: carrot_type['price'], reverse=True)
    max_value = 0

    for carrot_type in sorted_carrots:
        quantity_to_fill = capacity // carrot_type['kg']
        if quantity_to_fill > 0:
            capacity -= (carrot_type['kg'] * quantity_to_fill)
            max_value += (carrot_type['price'] * quantity_to_fill)

    return max_value
