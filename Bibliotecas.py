#Biblioteca time
#Trabalhando com tempo, no caso ele utiliza o for para contar até 5, começando do 0 até o 4, em um time de 1 segundo
#Basicamente ele conta 0 até 4 esperando 1 segundo
import time

for i in range(5):
    print(i)

    time.sleep(1)

#Biblioteca tkinter
#Fazendo um botão básico que ao clicar ele fecha a tela, nome do botão é OK
from tkinter import *
box = Button(text="Ok", command='exit')
box.pack()
box.mainloop()
