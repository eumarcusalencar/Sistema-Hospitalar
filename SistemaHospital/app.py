from Paciente import Paciente
from Consulta import Consulta
from Quarto import Quarto

appConfig = {"nome":"Medicare", "quantidadeQuartos": 10}

consultas = []

medicos = [
			"dr. Rancho Krutz", 
			"dr. Marcus",
			"dr. Matheus",
			"dr. Pedro"
		  ]

quartos = []

def getQuartosDisponiveis():
	#Compreensão de lista
	quartosDisponiveis = [quarto.getNumero() for quarto in quartos if not quarto.isOcupado()]
	return(quartosDisponiveis)

def getQuartos():
	return quartos

def novoQuarto():
	if(len(quartos) > 0):
		novoQuarto = Quarto(quartos[-1].getNumero()+1)
		quartos.append(novoQuarto)
	else:
		novoQuarto = Quarto(0)
		quartos.append(novoQuarto)


## Criação de quartos
for i in range(0, appConfig["quantidadeQuartos"]):
	novoQuarto()

def getQuartoIndex(numero):
	#Compreensão de lista
	indice = [i for i in range(0,len(quartos)) if quartos[i].getNumero() == int(numero)]
	return indice

def getMedicos():
	return medicos

#Localiza e apaga consulta da lista
def getConsultaPorPaciente(id):
	for i in range(0, len(consultas)):
		if(consultas[i].getPaciente.getID() == id):
			consultas.pop(i)
			break

def marcarConsulta(nome, nascimento, sexo, cpf, sangue, doenca, medico, quarto, data, horario):
	quartoIndice = getQuartoIndex(int(quarto))

	if(len(quartoIndice) > 0):
		quartoIndice = quartoIndice[0]
		paciente = Paciente(doenca, nome, nascimento, sexo, cpf,sangue)
		consultas.append(Consulta(medico, paciente, data, horario, quarto))

		quartos[quartoIndice].setOcupado()
		quartos[quartoIndice].setPaciente(nome)

		return consultas[-1]

	return False
	
def cancelarConsulta(id):
	for i in range(0, len(consultas)):
		if(consultas[i].getID() == int(id)):
			quartoIndice = getQuartoIndex(consultas[i].getQuarto())[0]
			quartos[quartoIndice].setOcupado()
			consultas.pop(i)
			break

def getConsulta(id):
	for i in range(0, len(consultas)):
		if(consultas[i].getID() == id):
			return consultas[i]
			break

def quantidadeConsultas():
	return len(consultas)

def getConsultas():
	return consultas