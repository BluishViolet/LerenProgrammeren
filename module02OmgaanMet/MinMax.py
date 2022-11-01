a = 10
b = 5

if a > b:
    Max = a
    Min = b
    minste = 'b'
    maximum = 'a'
    print(f"a is het grootste getal:{Max}")
elif a < b:
    Min = b
    Max = a
    minste = 'a'
    maximum = 'b'
    print(f"b is het kleinste getal:, {Min}")
else:
    print("a en b zijn even groot")


print(f"Het minimum is: {minste} gevolgd door de waarde van {Min}")
print(f"Het maximum is: {maximum} gevolgd door de waarde van {Max}")