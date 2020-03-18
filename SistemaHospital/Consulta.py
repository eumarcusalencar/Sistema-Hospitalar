from random import randint

class Consulta:
	def __init__(self, medico, paciente, data, horario, quarto):
		self.__medico = medico
		self.__paciente = paciente
		self.__data = data
		self.__horario = horario
		self.__id = randint(1111,9999)
		self.__quarto = quarto

	def getQuarto(self):
		return self.__quarto

	def getID(self):
		return self.__id

	def getMedico(self):
		return self.__medico

	def setMedico(self, medico):
		self.__medico = medico

	def getPaciente(self):
		return self.__paciente

	def getData(self):
		return self.__data
	def setData(self, data):
		self.__data = data

	def getHorario(self):
		return self.__horario
	def setHorario(self, horario):
		self.__horario = horario