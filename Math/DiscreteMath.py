def closed_form(n):
    # 2^n = 2^(n+1) - 1
    partOne = (pow(2,(n+1))-1)
    print('2^n: ' + str(partOne))

    # (-1)^n = ...
    partTwo = (pow(-1, (n+1)) - 1)/(-2)
    print('-1n: ' + str(partTwo) + '\n')

    print(partOne + partTwo)

closed_form(1)
closed_form(2)
closed_form(3)