# 6) Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
# e C A temperatura em Celsius

tempC = float(input('Informe a temperatura em celsius: '))
tempF = tempC * (9.0 / 5.0) + 32.0

print (f'{tempC} graus celsius equivale a {tempF} graus fahrenheit' )