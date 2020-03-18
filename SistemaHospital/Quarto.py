from random import randint


class Quarto:
	def __init__(self, numero):
		try:
			self.__numero = int(numero)
		except Exception as e:
			self.__numero = randint(1111, 9999)
			print("ERRO! "+e)
			print("Aleatorizando quarto!")
		finally:
			self.__paciente = None
			self.__ocupado = False

	def getNumero(self):
		return self.__numero

	def getPaciente(self):
		return self.__paciente
	def setPaciente(self, paciente):
		self.__paciente = paciente

	def isOcupado(self):
		return self.__ocupado
	def setOcupado(self):
		self.__ocupado = not self.__ocupado