from os import system


print()
print('$ App: Universal Temperature Converter')
print()
print('[1] Celsius Converter')
print('[2] Fahrenheit Converter')
print('[3] Kelvin Converter')
print('[4] Réaumur Converter')
print('[5] Rankine Converter')
print('[6] Delisle Converter')
print('[7] Newton Converter')
print('[8] Rømer Converter')
print()

option = input('# Option: ')

if option == '1':
    system('cls')
    print()
    input_celsius = int(input('Degrees in Celsius: '))

    value_fahrenheit = input_celsius * 1.8 + 32
    value_kelvin = input_celsius + 273.15
    value_reaumur = input_celsius * 0.8
    value_rankine = input_celsius * 1.8 + 491.67
    value_delisle = (100 - input_celsius) * 0.2 + 32
    value_newton = input_celsius * 0.33
    value_romer = input_celsius * 1.25

    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '2':
    system('cls')
    print()
    input_fahrenheit = int(input('Degrees in Fahrenheit: '))

    value_celsius = (input_fahrenheit - 32) * (5.0/9.0)
    value_kelvin = 273.5 + ((input_fahrenheit - 32.0) * (5.0/9.0))
    value_reaumur = (input_fahrenheit - 32) * (4.0/9.0)
    value_rankine = input_fahrenheit + 459.67
    value_delisle = (212 - input_fahrenheit) * (5.0/6.0)
    value_newton = (input_fahrenheit - 32) * (0.556)
    value_romer = (input_fahrenheit - 32) * (7.0/24.0)

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '3':
    system('cls')
    print()
    input_kelvin = int(input('Degrees in Kelvin: '))

    value_celsius = input_kelvin - 273.15
    value_fahrenheit = (input_kelvin - 273.15) * 1.8 + 32
    value_reaumur = input_kelvin * 0.8
    value_rankine = input_kelvin * 1.8 + 491.67
    value_delisle = (100 - input_kelvin) * 0.2 + 32
    value_newton = input_kelvin * 0.33
    value_romer = input_kelvin * 1.25

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '4':
    system('cls')
    print()
    input_reaumur = int(input('Degrees in Réaumur: '))

    value_celsius = input_reaumur * 1.25
    value_fahrenheit = input_reaumur * 1.25 + 32
    value_kelvin = input_reaumur + 273.15
    value_rankine = input_reaumur * 1.25 + 491.67
    value_delisle = (100 - input_reaumur) * 0.2 + 32
    value_newton = input_reaumur * 0.33
    value_romer = input_reaumur * 1.25

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '5':
    system('cls')
    print()
    input_rankine = int(input('Degrees in Rankine: '))

    value_celsius = (input_rankine - 491.67) * (5.0/9.0)
    value_fahrenheit = input_rankine - 459.67
    value_kelvin = (input_rankine - 491.67) * (5.0/9.0) + 273.15
    value_reaumur = (input_rankine - 491.67) * (4.0/9.0)
    value_delisle = (212 - input_rankine) * (5.0/6.0)
    value_newton = (input_rankine - 491.67) * (0.556)
    value_romer = (input_rankine - 491.67) * (7.0/24.0)

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '6':
    system('cls')
    print()
    input_delisle = int(input('Degrees in Delisle: '))

    value_celsius = (100 - input_delisle) * 0.2 + 32
    value_fahrenheit = (212 - input_delisle) * 0.2 + 32
    value_kelvin = (100 - input_delisle) * 0.2 + 273.15
    value_reaumur = (100 - input_delisle) * 0.2
    value_rankine = (212 - input_delisle) * 0.2 + 491.67
    value_newton = (100 - input_delisle) * 0.2 + 32
    value_romer = (100 - input_delisle) * 0.2 + 32

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Newton: {value_newton}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '7':
    system('cls')
    print()
    input_newton = int(input('Degrees in Newton: '))

    value_celsius = input_newton * 0.33
    value_fahrenheit = input_newton * 0.33 + 32
    value_kelvin = input_newton * 0.33 + 273.15
    value_reaumur = input_newton * 0.33
    value_rankine = input_newton * 0.33 + 491.67
    value_delisle = (100 - input_newton) * 0.2 + 32
    value_romer = input_newton * 0.33 + 32

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Rømer: {value_romer}')

    print()
    exit = input('To exit the program, press enter or type something: ')


if option == '8':
    system('cls')
    print()
    input_romer = int(input('Degrees in Rømer: '))

    value_celsius = input_romer * 1.25
    value_fahrenheit = input_romer * 1.25 + 32
    value_kelvin = input_romer + 273.15
    value_reaumur = input_romer * 1.25
    value_rankine = input_romer * 1.25 + 491.67
    value_delisle = (100 - input_romer) * 0.2 + 32
    value_newton = input_romer * 0.33

    print(f'Degrees in Celsius: {value_celsius}')
    print(f'Degrees in Fahrenheit: {value_fahrenheit}')
    print(f'Degrees in Kelvin: {value_kelvin}')
    print(f'Degrees in Réaumur: {value_reaumur}')
    print(f'Degrees in Rankine: {value_rankine}')
    print(f'Degrees in Delisle: {value_delisle}')
    print(f'Degrees in Newton: {value_newton}')

    print()
    exit = input('To exit the program, press enter or type something: ')
