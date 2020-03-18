from Pessoa import Pessoa
from random import randint

class Paciente(Pessoa):
    def __init__(self, doenca, nome, nascimento, sexo, cpf, tipoSangue):
        Pessoa.__init__(self, nome, nascimento, sexo, cpf, tipoSangue)
        self.__doenca = doenca
        self.__num_Quarto = 0
        self.__id = randint(1111,9999)

    def setDoenca(self,novaDoenca):
        self.__doenca = novaDoenca

    def getID(self):
        self.__id

    def setNumquarto(self,novoNum_Quarto):
        self.__num_Quarto = novoNum_Quarto

    def getDoenca(self):
        return self.__doenca

    def getNumQuarto(self):
        return self.__num_Quarto

    def setNum_Quarto(self, quarto):
        self.__num_Quarto = quarto

    def internar(self, quarto):
        setNum_Quarto(quarto)
    
