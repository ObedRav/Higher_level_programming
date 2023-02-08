def solucion(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    result = []
    cost_per_minute_mine = list(map(lambda x: x * ride_time, cost_per_minute))
    cost_per_mile_mine = list(map(lambda x: x * ride_distance, cost_per_mile))
    minimus = min(len(cost_per_minute), len(cost_per_mile))
    for i in range(minimus):
        result.append(round(cost_per_minute_mine[i] + cost_per_mile_mine[i], 1))
    return result

ride_time = 30
ride_distance = 7
cost_per_minute = [0.2 , 0.35, 0.4, 0.45]
cost_per_mile = [1.1, 1.8, 2.3, 3.5]

result = solucion(ride_time, ride_distance, cost_per_minute, cost_per_mile)
print(result) 
