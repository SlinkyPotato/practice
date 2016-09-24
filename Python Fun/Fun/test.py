def mult_func(s):
    num_lst = s # Split the user input into a list by comma ( , )
    # enumerate generates an integer relevant to the number of iterations starting at 0
    # eg. 1st num, i = 0, 2nd num, i = 1, 3rd num, i = 2, etc
    for i, num in enumerate(num_lst):
        value = float(num)*(i+1)
        print('{0} x {1} = {2}'.format(float(num), (i+1), value))

if __name__ == '__main__':
    # The user entered numbers have to be separeted by commas ( , )
    # The user entered numbers have to be separeted by commas ( , )
    print input("s");
    mult_func(input('Enter a list of numbers: '))