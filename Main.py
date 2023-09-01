from Classes import *

funcionario = Programador("Carlos")
equipamento = Computador("Avell", "Intel Core I5")
aparelho = Celular("Samsung", "S22 Ultra")

funcionario.setFerramenta(equipamento)
print(funcionario.ferramenta_trabalho.marca)
print("######################################")
print(funcionario.getFerramenta().marca)
print("######################################")
print(funcionario.getFerramenta().getMarca())