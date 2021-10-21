# 20) Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
# de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.

quilo = float(input('Informe o peso em quilogramas: '))
libra = quilo / 0.45
print(f'{quilo} quilos são {libra} libras')