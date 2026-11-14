def matritsa_yigindisi(matritsa):
    return sum(sum(qator) for qator in matritsa)


matritsa = [
    [1, 2, 3], 
    [4, 5, 6]
]

print("Yig'indi:", matritsa_yigindisi(matritsa))