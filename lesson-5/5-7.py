from json import dumps
results = [{}, {}]

with open('text7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        name, type_of_ownership, revenue, costs = line.split()
        results[0][name] = int(revenue) - int(costs)
    results[1]['average_profit'] = sum(profit for name, profit in results[0].items() if profit > 0) / len(results[0])

with open('profit.json', "w", encoding='utf-8') as fj:
    fj.write(dumps(results))
