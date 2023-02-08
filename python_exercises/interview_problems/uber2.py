def min_cost(distance, fares, spend):
    iterable = 0
    result = "Nothing"
    price_miles = list(map(lambda x: x * distance, fares))
    posibles_services_cars = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    posibles_services_cars_with_prices = dict(zip(posibles_services_cars, price_miles))
    for key, value in posibles_services_cars_with_prices.items():
        if (value <= spend and iterable < spend):
            iterable = value
            result = key
    return result

distance = 30
fares = [0.3, 0.5, 0.7, 1, 1.5]
spend = 9
x= min_cost(distance, fares, spend)
print(x)