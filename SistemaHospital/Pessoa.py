from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, nascimento, sexo, cpf, tipoSangue):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__cpf = cpf
        self.__tipoSanguineo = tipoSangue

    def setNome(self,novoNome):
        self.__nome = novoNome

    def setNascimento(self,novoNascimento):
        self.__nascimento = novoNascimento

    def setIdade(self,novaIdade):
        self.__idade = novaIdade

    def setSexo(self,novoSexo):
        self.__sexo = novoSexo

    def setCpf(self,NovoCpf):
        self.__cpf = NovoCpf

    def getTipoSanguineo(self):
        return self.__tipoSanguineo

    def setTipoSanguineo(self,NovoTipoSanguineo):
        self.__tipoSanguineo = NovoTipoSanguineo

    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

    def getNascimento(self):
        return self.__nascimento

    def getIdade(self):
        return self.__idade

    def getSexo(self):
        return self.__sexo