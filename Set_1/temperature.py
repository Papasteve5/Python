def my_function1():
    celcius = float(input('Celcius: '))
    result = celcius + 273.15
    print('Kelvin = ', result)


def my_function2():
    celcius = float(input('Celcius: '))
    result = celcius * 1.8 + 32
    print('Fahrenheit = ', result)


def my_function3():
    kelvin = float(input('Kelvin: '))
    result = kelvin - 273.15
    print('Celcius = ', result)


def my_function4():
    kelvin = float(input('Kelvin: '))
    result = 1.8 * (kelvin - 273) + 32
    print('Fahrenheit = ', result)


def my_function5():
    fahrenheit = float(input('Fahrenheit: '))
    result = 5/9 * (fahrenheit - 32)
    print('Celcius = ', result)


def my_function6():
    fahrenheit = float(input('Fahrenheit: '))
    result = (fahrenheit - 32) * 5 / 9 + 273.15
    print('Kelvin = ', result)


duration = True

while duration:

    op1 = '(1) Umrechnung von Celsius nach Kelvin'
    op2 = '(2) Umrechnung von Celsius nach Fahrenheit'
    op3 = '(3) Umrechnung von Kelvin nach Celsius'
    op4 = '(4) Umrechnung von Kelvin nach Fahrenheit'
    op5 = '(5) Umrechnung von Fahrenheit nach Celsius'
    op6 = '(6) Umrechnung von Fahrenheit nach Kelvin'

    auswahl = [op1, op2, op3, op4, op5, op6]

    for word in auswahl:
        print(word)

    wahl = int(input('Ihre Wahl: '))

    if wahl == 1:
        my_function1()
    elif wahl == 2:
        my_function2()
    elif wahl == 3:
        my_function3()
    elif wahl ==4:
        my_function4()
    elif wahl == 5:
        my_function5()
    elif wahl == 6:
        my_function6()
    else:
        print('Geben Sie eine gültige Möglichkeit ein!')
        break
