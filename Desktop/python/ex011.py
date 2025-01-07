# Parede
largura = float(input("largura da parede: "))
altura = float(input("altura da parede: "))
area = largura*altura
litros = area*0.5

print("Sua parede tem a dimmensão de {}x{} e sua área é de {}m² \n Para pintar essa parede, você precisará de {}L de tinta".format(largura, altura, area, litros))