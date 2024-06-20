import math

def Calculate(numbers):
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], numbers[4], numbers[5]],
        [numbers[6], numbers[7], numbers[8]]
    ]

    def mean(data):
        return sum(data) / len(data)

    def Variance(data):
        n = len(data)
        if n == 0:
            raise ValueError("Insufficient data")

        m = mean(data)
        var = sum((x - m) ** 2 for x in data) / n
        return var

    def SD(data):
        return math.sqrt(Variance(data))

    row_means = [mean(row) for row in matrix]
    col_means = [mean([row[i] for row in matrix]) for i in range(3)]
    flat_mean = mean(numbers)

    row_vars = [Variance(row) for row in matrix]
    col_vars = [Variance([row[i] for row in matrix]) for i in range(3)]
    flat_var = Variance(numbers)

    row_stds = [SD(row) for row in matrix]
    col_stds = [SD([row[i] for row in matrix]) for i in range(3)]
    flat_std = SD(numbers)

    row_maxs = [max(row) for row in matrix]
    col_maxs = [max([row[i] for row in matrix]) for i in range(3)]
    flat_max = max(numbers)

    row_mins = [min(row) for row in matrix]
    col_mins = [min([row[i] for row in matrix]) for i in range(3)]
    flat_min = min(numbers)

    row_sums = [sum(row) for row in matrix]
    col_sums = [sum([row[i] for row in matrix]) for i in range(3)]
    flat_sum = sum(numbers)

    results = {
        'mean': [row_means, col_means, flat_mean],
        'variance': [row_vars, col_vars, flat_var],
        'standard deviation': [row_stds, col_stds, flat_std],
        'max': [row_maxs, col_maxs, flat_max],
        'min': [row_mins, col_mins, flat_min],
        'sum': [row_sums, col_sums, flat_sum]
    }

    return results

result = Calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
