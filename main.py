# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Jogador:
    def __init__(self, nome, numeros):
        self.nome = nome
        self.numeros = numeros
        self.soma = 0

    def soma(self):
        return sum(self.numeros)

jogador1 = Jogador('Joao', (3, 5, 7) )
jogador2 = Jogador('Mario', (6, 9, 12) )

print(jogador1.soma())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
