celsius = float(input('Digite uma temperatura em Celsius: '))
fahrenheit = (9 * celsius + 160) / 5
kelvin = (273 + celsius)
print('A temperatura equivale a {:.2f} farheneit'.format(fahrenheit))
print('A temperatura equivale a {:.2f} Kelvin'.format(kelvin))