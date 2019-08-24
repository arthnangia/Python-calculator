# Basic Calculator
# Accept 2 numbers from user - x and y -
# and an operator - op - and calculate the solution - z - according to the
# type of the given operator.


def calc(a, b, op):
    """
    function to return the calculated value
    accepts 2 numbers as input [x & y] and returns
    'X op Y = Z' as output where Z is operation done.
    """

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  # Wrapper function

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input('What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    print(calc(a, b, op))

if __name__ == '__main__':
    main()
