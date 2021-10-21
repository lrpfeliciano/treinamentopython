# 16) Leia um valor de comprimento em polegadas e apresente-o convertido em centímetoros.
# A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
# comprimento em polegadas.

polegada = float(input('Informe o comprimento em polegadas: '))
centimetro = polegada * 2.54
print(f'{polegada} polegadas são {centimetro} centímetros')