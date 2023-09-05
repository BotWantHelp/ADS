jar = (30, 30, 40)

def calculate_total(jar):
    sum = 0
    for amount in jar:
        sum += amount
    return sum

resultado = calculate_total(jar)
print(resultado)
