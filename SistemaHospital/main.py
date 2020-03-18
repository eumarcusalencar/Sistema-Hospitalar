# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from Views import Views
from estilo import *
from config import *
from app import *

class App(Views):
	def __init__(self, tela):
		Views.__init__(self, tela)

	def carregarTela(self, tela):
		self.widget1.destroy()
		self.widget1 = Frame(self.janela)
		self.widget1['bg'] = BG_DARK
		self.widget1.pack()
		if(tela == TELA_MENU):
			self.renderizarTelaMenu()

		elif(tela == MENU_CONSULTA):
			self.renderizarMenuConsulta()

		elif(tela == TELA_FORMULARIO_CONSULTA):
			self.renderizarConsultaForm()

		elif(tela == TELA_CONSULTA):
			self.renderizarTelaConsulta()

		elif(tela == LISTA_CONSULTAS):
			self.renderizarListaConsultas()
      
		elif (tela == TELA_PACIENTE):
			self.renderizarTelaPaciente()

	def carregarInfoConsulta(self, id):
		try:
			id = int(id)
			if(quantidadeConsultas() > 0):
				consulta = getConsulta(id)
				self.renderizarInfoConsulta(consulta)
			else:
				print("Não há consultas marcadas")
		except Exception as e:
			print("O ID da consulta deve ser um número inteiro!")
			print(e)

	def carregarInfoPaciente(self,ID):
		ID = int(ID)
		if(quantidadeConsultas()>0):
			paciente = getConsulta(ID).getPaciente()
	
			self.renderizarInfoPaciente(paciente)
		paciente =  getConsulta(ID).getPaciente()

	def registrarConsulta(self, nome, nascimento, sexo, cpf, sangue, doenca, medico, quarto, data, horario):
		consulta = marcarConsulta(nome, nascimento, sexo, cpf, sangue, doenca, medico, quarto, data, horario)
		messagebox.showinfo("Sucesso!","A consulta foi marcada! O ID da consulta é: " + str(consultas[-1].getID()))

tela = Tk()
w, h = tela.winfo_screenwidth(), tela.winfo_screenheight()
tela.geometry("%dx%d+0+0" %(w, h))
tela.attributes("-fullscreen", True)
App(tela)
tela.mainloop()