from FactoryES import FactoryES
from MakerFactory import MakerFactory
from FactoryEN import FactoryEN

def main():

    cont = True
    while cont:
        lenguage = input('Ingrese un idioma (ES-EN) : ')
        makerf = MakerFactory()
        if lenguage == 'ES' or lenguage == 'EN':
            if lenguage == 'ES':
                factory = makerf.create_f(FactoryES())
            if lenguage == 'EN':
                factory = makerf.create_f(FactoryEN())
            print(f'IDIOMA {lenguage.upper()} CARGADO')

            op = int(input('\nSALUDOS(1) | PREGUNTAS(2)  Elige un opcion: '))

            if op == 1 or op == 2:
                if op == 1:
                    print(f'\nSALUDOS EN "{lenguage}": ')
                    print(factory.saludar().buenosDias())
                    print(factory.saludar().buenasTardes())
                    print('\n')
                if op == 2:
                    print(f'\nPREGUNTAS EN "{lenguage}": ')
                    print(factory.preguntar().preguntaHora())
                    print(factory.preguntar().preguntaTiempo())
                    print('\n')
                resp = input('Desear continuar? (S/N) : ')
                if resp.upper() == 'N' or resp.upper() == 'S':
                    if resp.upper() == 'N':
                        cont = False
                    else:
                        cont = True
                else:
                    print('Parece que fue compleja la pregunta.. bye bye')
                    cont = False
            else:
                print('Bue se ve que es complejo esto.. es colocar 1 0 2 nomas')


        else:
            print(f'{lenguage.upper()} no es un idioma soportado..')
    else:
        print('bye bye :) ')



main()