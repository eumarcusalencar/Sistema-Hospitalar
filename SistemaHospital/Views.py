from tkinter import *
from tkinter import messagebox
from app import *
from estilo import *
from config import *

class Views():
	def __init__(self, tela):
		self.janela = tela
		self.janela["bg"] = BG_DARK
		self.widget1 = Frame(tela)
		self.widget1.pack()
		self.carregarTela(TELA_MENU)
		self.widgetInfo = None

	def renderizarListaConsultas(self):
		title = Label(self.widget1, text="HospMed Vida - Consultas")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()

		listaContainer = Frame(self.widget1)
		listaContainer.pack()

		consultas = getConsultas()

		barraRolagem = Scrollbar(listaContainer, orient=VERTICAL)
		consultasLista = Listbox(listaContainer, yscrollcommand=barraRolagem.set)
		consultasLista["width"] = 100
		consultasLista["height"] = 25
		
		barraRolagem.pack(side=RIGHT, fill=Y)

		consultasLista.pack()
		consultasLista.insert(END, "ID | NOME | Data | Hora")
		for consulta in consultas:
			dadosLinha = str(consulta.getID())+" | "+consulta.getPaciente().getNome()+" | "+ consulta.getData()+" | "+consulta.getHorario()
			consultasLista.insert(END, dadosLinha)

		voltarBtn = Button(self.widget1, borderwidth=0)
		voltarBtn['text'] = "Voltar"
		voltarBtn['fg'] = TEXT_DARK
		voltarBtn['bg'] = TEXT_WHITE
		voltarBtn['font'] = FONT_BOLD
		voltarBtn['borderwidth'] = 1
		voltarBtn['highlightbackground'] = BG_DARK
		voltarBtn['command'] = lambda: self.carregarTela(MENU_CONSULTA)
		voltarBtn.pack()

	def renderizarTelaPaciente(self):
		title = Label(self.widget1, text="HospMed Vida - Paciente")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()
  		
		consultaIdLbl = Label(self.widget1, text = "Digite o ID da consulta")
		consultaIdLbl['bg'] = BG_DARK
		consultaIdLbl['fg'] = TEXT_WHITE
		consultaIdLbl.pack()
  
		consultaIdinput = Entry(self.widget1)
		consultaIdinput.pack()
  
		botaoId = Button(self.widget1, text = "Pesquisa")
		botaoId['bg'] = BG_LIGHT
		botaoId['fg'] = TEXT_DARK
		botaoId['font'] = FONT_BOLD
		botaoId['command'] = lambda: self.carregarInfoPaciente(consultaIdinput.get())
		botaoId.pack()

		voltarBtn = Button(self.widget1, borderwidth=0)
		voltarBtn['text'] = " Voltar "
		voltarBtn['fg'] = TEXT_DARK
		voltarBtn['bg'] = TEXT_WHITE
		voltarBtn['font'] = FONT_BOLD
		voltarBtn['borderwidth'] = 1
		voltarBtn['highlightbackground'] = BG_DARK
		voltarBtn['command'] = lambda: self.carregarTela(TELA_MENU)
		voltarBtn.pack()

	def renderizarMenuConsulta(self):
		title = Label(self.widget1, text="HospMed Vida - Consulta")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()

		pesquisaBtn = Button(self.widget1, borderwidth=0)
		pesquisaBtn['text'] = " Pesquisar Consultas "
		pesquisaBtn['fg'] = TEXT_DARK
		pesquisaBtn['bg'] = TEXT_WHITE
		pesquisaBtn['font'] = FONT_BOLD
		pesquisaBtn['borderwidth'] = 1
		pesquisaBtn['highlightbackground'] = BG_DARK
		pesquisaBtn['command'] = lambda: self.carregarTela(TELA_CONSULTA)
		pesquisaBtn.pack()

		marcarConsultaBtn = Button(self.widget1, borderwidth=0)
		marcarConsultaBtn['text'] = " Marcar Consulta "
		marcarConsultaBtn['fg'] = TEXT_DARK
		marcarConsultaBtn['bg'] = TEXT_WHITE
		marcarConsultaBtn['font'] = FONT_BOLD
		marcarConsultaBtn['borderwidth'] = 1
		marcarConsultaBtn['command'] = lambda: self.carregarTela(TELA_FORMULARIO_CONSULTA)
		marcarConsultaBtn['highlightbackground'] = BG_DARK
		marcarConsultaBtn.pack()

		consultasBtn = Button(self.widget1, borderwidth=0)
		consultasBtn['text'] = " Consultas "
		consultasBtn['fg'] = TEXT_DARK
		consultasBtn['bg'] = TEXT_WHITE
		consultasBtn['font'] = FONT_BOLD
		consultasBtn['borderwidth'] = 1
		consultasBtn['highlightbackground'] = BG_DARK
		consultasBtn['command'] = lambda: self.carregarTela(LISTA_CONSULTAS)
		consultasBtn.pack()

		voltarBtn = Button(self.widget1, borderwidth=0)
		voltarBtn['text'] = " Voltar "
		voltarBtn['fg'] = TEXT_DARK
		voltarBtn['bg'] = TEXT_WHITE
		voltarBtn['font'] = FONT_BOLD
		voltarBtn['borderwidth'] = 1
		voltarBtn['highlightbackground'] = BG_DARK
		voltarBtn['command'] = lambda: self.carregarTela(TELA_MENU)
		voltarBtn.pack()

	def renderizarTelaMenu(self):
		title = Label(self.widget1, text="HospMed Vida")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()

		ConsultaBtn = Button(self.widget1, borderwidth=0)
		ConsultaBtn['text'] = "Consulta"
		ConsultaBtn['fg'] = TEXT_DARK
		ConsultaBtn['bg'] = TEXT_WHITE
		ConsultaBtn['font'] = FONT_BOLD
		ConsultaBtn['borderwidth'] = 1
		ConsultaBtn['highlightbackground'] = BG_DARK
		ConsultaBtn['command'] = lambda: self.carregarTela(MENU_CONSULTA)
		ConsultaBtn.pack()

		pacienteBtn = Button(self.widget1, borderwidth=0)
		pacienteBtn['text'] = "Paciente"
		pacienteBtn['fg'] = TEXT_DARK
		pacienteBtn['bg'] = TEXT_WHITE
		pacienteBtn["command"] = lambda : self.carregarTela(TELA_PACIENTE)
		pacienteBtn['font'] = FONT_BOLD
		pacienteBtn['borderwidth'] = 1
		pacienteBtn['highlightbackground'] = BG_DARK
		pacienteBtn['command'] = lambda: self.carregarTela(TELA_PACIENTE)
		pacienteBtn.pack()

		sairBtn = Button(self.widget1, borderwidth=0)
		sairBtn['text'] = "Sair"
		sairBtn['fg'] = TEXT_DARK
		sairBtn['bg'] = TEXT_WHITE
		sairBtn['font'] = FONT_BOLD
		sairBtn['borderwidth'] = 1
		sairBtn['highlightbackground'] = BG_DARK
		sairBtn['command'] = lambda: self.janela.destroy()
		sairBtn.pack()

	def renderizarTelaConsulta(self):
		title = Label(self.widget1, text="HospMed Vida - Consulta")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()

		linha1 = Frame(self.widget1)
		linha1['bg'] = BG_DARK
		linha1['pady'] = PADDING_3
		linha1.pack()

		pesquisaLbl = Label(linha1, text="ID:  ")
		pesquisaLbl['bg'] = BG_DARK
		pesquisaLbl['fg'] = TEXT_WHITE
		pesquisaLbl['font'] = FONT_BOLD
		pesquisaLbl.pack(side=LEFT)

		pesquisaInput = Entry(linha1)
		pesquisaInput.pack(side=LEFT)

		pesquisaBtn = Button(linha1, text="Pesquisar")
		pesquisaBtn['bg'] = BG_LIGHT
		pesquisaBtn['fg'] = TEXT_DARK
		pesquisaBtn['font'] = FONT_BOLD
		pesquisaBtn['command'] = lambda: self.carregarInfoConsulta(pesquisaInput.get())
		pesquisaBtn.pack(side=LEFT)
  
		voltarBtn = Button(self.widget1, borderwidth=0)
		voltarBtn['text'] = " Voltar "
		voltarBtn['fg'] = TEXT_DARK
		voltarBtn['bg'] = TEXT_WHITE
		voltarBtn['font'] = FONT_BOLD
		voltarBtn['borderwidth'] = 1
		voltarBtn['highlightbackground'] = BG_DARK
		voltarBtn['command'] = lambda: self.carregarTela(MENU_CONSULTA)
		voltarBtn.pack(side=BOTTOM)

	def renderizarConsultaForm(self):
		title = Label(self.widget1, text="HospMed Vida - Marcar Consulta")
		title['font'] = TITLE_FONT
		title['bg'] = BG_DARK
		title['fg'] = TEXT_WHITE
		title['pady'] = PADDING_3
		title['borderwidth'] = 0
		title.pack()

		linha1 = Frame(self.widget1)
		linha1['bg'] = BG_DARK
		linha1.pack()

		nomeLbl = Label(linha1, text="Nome: ")
		nomeLbl['font'] = FONT_NORMAL
		nomeLbl['bg'] = BG_DARK
		nomeLbl['fg'] = TEXT_WHITE
		nomeLbl['pady'] = PADDING_3
		nomeLbl['borderwidth'] = 0
		nomeLbl.pack(side=LEFT)

		nomeInput = Entry(linha1)
		nomeInput.pack(side=LEFT)

		nomeLbl = Label(linha1, text="   Nascimento: ")
		nomeLbl['font'] = FONT_NORMAL
		nomeLbl['bg'] = BG_DARK
		nomeLbl['fg'] = TEXT_WHITE
		nomeLbl['pady'] = PADDING_3
		nomeLbl['borderwidth'] = 0
		nomeLbl.pack(side=LEFT)
		nascimentoInput = Entry(linha1)
		nascimentoInput.pack(side=LEFT)

		linha2 = Frame(self.widget1)
		linha2['bg'] = BG_DARK
		linha2.pack()
		
		sexoLbl = Label(linha2, text="Sexo: ")
		sexoLbl['font'] = FONT_NORMAL
		sexoLbl['bg'] = BG_DARK
		sexoLbl['fg'] = TEXT_WHITE
		sexoLbl['pady'] = PADDING_3
		sexoLbl['borderwidth'] = 0
		sexoLbl.pack(side=LEFT)

		sexoSelecionado = StringVar(linha2)
		sexoSelecionado.set("Selecione o sexo")
		selecaoSexo = OptionMenu(linha2, sexoSelecionado, "Masculino", "Feminino")
		selecaoSexo['font'] = FONT_NORMAL
		selecaoSexo['bg'] = BG_DARK
		selecaoSexo['fg'] = TEXT_WHITE
		selecaoSexo.pack(side=LEFT)

		CPFLbl = Label(linha2, text="   CPF: ")
		CPFLbl['font'] = FONT_NORMAL
		CPFLbl['bg'] = BG_DARK
		CPFLbl['fg'] = TEXT_WHITE
		CPFLbl['pady'] = PADDING_3
		CPFLbl['borderwidth'] = 0
		CPFLbl.pack(side=LEFT)
		CPFInput = Entry(linha2)
		CPFInput.pack(side=LEFT)

		linha3 = Frame(self.widget1)
		linha3['bg'] = BG_DARK
		linha3.pack()


		Sanguelbl = Label(linha3, text="   Tipo Sanguíneo: ")
		Sanguelbl['font'] = FONT_NORMAL
		Sanguelbl['bg'] = BG_DARK
		Sanguelbl['fg'] = TEXT_WHITE
		Sanguelbl['pady'] = PADDING_3
		Sanguelbl['borderwidth'] = 0
		Sanguelbl.pack(side=LEFT)

		sangueSelecionado = StringVar(linha3)
		sangueSelecionado.set("Selecione o tipo")

		SangueInput = OptionMenu(linha3, sangueSelecionado, "A+", "A-", "B+", "B-","AB+","AB-", "O+", "O-")
		SangueInput['font'] = FONT_NORMAL
		SangueInput['bg'] = BG_DARK
		SangueInput['fg'] = TEXT_WHITE
		SangueInput.pack(side=LEFT)

		doencaLbl = Label(linha3, text="   Doença: ")
		doencaLbl['font'] = FONT_NORMAL
		doencaLbl['bg'] = BG_DARK
		doencaLbl['fg'] = TEXT_WHITE
		doencaLbl['pady'] = PADDING_3
		doencaLbl['borderwidth'] = 0
		doencaLbl.pack(side=LEFT)
		doencaInput = Entry(linha3)
		doencaInput.pack(side=LEFT)

		linha4 = Frame(self.widget1)
		linha4['bg'] = BG_DARK
		linha4.pack()

		medicoLbl = Label(linha4, text="Médico: ")
		medicoLbl['font'] = FONT_NORMAL
		medicoLbl['bg'] = BG_DARK
		medicoLbl['fg'] = TEXT_WHITE
		medicoLbl['pady'] = PADDING_3
		medicoLbl['borderwidth'] = 0
		medicoLbl.pack(side=LEFT)

		medicoSelecionado = StringVar(linha4)
		medicoSelecionado.set("Selecione um médico")

		medicoInput = OptionMenu(linha4, medicoSelecionado, *getMedicos())
		medicoInput['font'] = FONT_NORMAL
		medicoInput['bg'] = BG_DARK
		medicoInput['fg'] = TEXT_WHITE
		medicoInput.pack(side=LEFT)

		quartoSelecionado = StringVar(linha4)
		quartoSelecionado.set("Selecione um quarto")

		quartoLbl = Label(linha4, text="Quarto: ")
		quartoLbl['font'] = FONT_NORMAL
		quartoLbl['bg'] = BG_DARK
		quartoLbl['fg'] = TEXT_WHITE
		quartoLbl['pady'] = PADDING_3
		quartoLbl['borderwidth'] = 0
		quartoLbl.pack(side=LEFT)

		quartoInput = OptionMenu(linha4, quartoSelecionado, *getQuartosDisponiveis())
		quartoInput['font'] = FONT_NORMAL
		quartoInput['bg'] = BG_DARK
		quartoInput['fg'] = TEXT_WHITE
		quartoInput.pack(side=LEFT)

		linha5 = Frame(self.widget1)
		linha5['bg'] = BG_DARK
		linha5.pack()


		datalbl = Label(linha5, text="   Data: ")
		datalbl['font'] = FONT_NORMAL
		datalbl['bg'] = BG_DARK
		datalbl['fg'] = TEXT_WHITE
		datalbl['pady'] = PADDING_3
		datalbl['borderwidth'] = 0
		datalbl.pack(side=LEFT)

		dataInput = Entry(linha5)
		dataInput['font'] = FONT_NORMAL
		dataInput['bg'] = BG_LIGHT
		dataInput['fg'] = TEXT_DARK
		dataInput.pack(side=LEFT)

		horaLbl = Label(linha5, text="   Horário: ")
		horaLbl['font'] = FONT_NORMAL
		horaLbl['bg'] = BG_DARK
		horaLbl['fg'] = TEXT_WHITE
		horaLbl['pady'] = PADDING_3
		horaLbl['borderwidth'] = 0
		horaLbl.pack(side=LEFT)

		horaInput = Entry(linha5)
		horaInput.pack(side=LEFT)

		submitBtn = Button(self.widget1, borderwidth=0)
		submitBtn['text'] = " Marcar Consulta "
		submitBtn['fg'] = TEXT_DARK
		submitBtn['bg'] = TEXT_WHITE
		submitBtn['font'] = FONT_BOLD
		submitBtn['borderwidth'] = 1
		submitBtn['highlightbackground'] = BG_DARK
		submitBtn['command'] = lambda: [self.registrarConsulta(nomeInput.get(), nascimentoInput.get(), sexoSelecionado.get(), CPFInput.get(), sangueSelecionado.get(), doencaInput.get(), medicoSelecionado.get(), quartoSelecionado.get(), dataInput.get(), horaInput.get()),  self.carregarTela(LISTA_CONSULTAS)]
		submitBtn.pack()

		voltarBtn = Button(self.widget1, borderwidth=0)
		voltarBtn['text'] = " Voltar "
		voltarBtn['fg'] = TEXT_DARK
		voltarBtn['bg'] = TEXT_WHITE
		voltarBtn['font'] = FONT_BOLD
		voltarBtn['borderwidth'] = 1
		voltarBtn['highlightbackground'] = BG_DARK
		voltarBtn['command'] = lambda: self.carregarTela(MENU_CONSULTA)
		voltarBtn.pack()

	def renderizarInfoPaciente(self,paciente):
		if(self.widgetInfo):
			self.widgetInfo.destroy()

		self.widgetInfo = Frame(self.widget1)
		self.widgetInfo['bg'] = BG_DARK
		self.widgetInfo.pack()

		linha2 = Frame(self.widgetInfo)
		linha2['bg'] = BG_DARK
		linha2.pack()

		nomeLbl = Label(linha2, text="Paciente: " + paciente.getNome() )
		nomeLbl['bg'] = BG_DARK
		nomeLbl['fg'] = TEXT_WHITE
		nomeLbl['font'] = FONT_NORMAL
		nomeLbl.pack(side=LEFT)

		separadorLbl = Label(linha2, text=" | " )
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)

		nascimentoLbl = Label(linha2, text="Nascimento: " + paciente.getNascimento() )
		nascimentoLbl['bg'] = BG_DARK
		nascimentoLbl['fg'] = TEXT_WHITE
		nascimentoLbl['font'] = FONT_NORMAL
		nascimentoLbl.pack(side=LEFT)

		linha3 = Frame(self.widgetInfo)
		linha3['bg'] = BG_DARK
		linha3.pack()

		sexoLbl = Label(linha3, text="Sexo: " + paciente.getSexo() )
		sexoLbl['bg'] = BG_DARK
		sexoLbl['fg'] = TEXT_WHITE
		sexoLbl['font'] = FONT_NORMAL
		sexoLbl.pack(side=LEFT)

		separadorLbl = Label(linha3, text=" | ")
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)

		cpfLbl = Label(linha3, text="CPF: " + paciente.getCpf() ) 
		cpfLbl['bg'] = BG_DARK
		cpfLbl['fg'] = TEXT_WHITE
		cpfLbl['font'] = FONT_NORMAL
		cpfLbl.pack(side=LEFT)

		linha4 = Frame(self.widgetInfo)
		linha4['bg'] = BG_DARK
		linha4.pack()

		sangueLbl = Label(linha4, text="Tipo Sanguíneo: " + paciente.getTipoSanguineo() )
		sangueLbl['bg'] = BG_DARK
		sangueLbl['fg'] = TEXT_WHITE
		sangueLbl['font'] = FONT_NORMAL
		sangueLbl.pack(side=LEFT)

		separadorLbl = Label(linha4, text=" | ")
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)
              
		doencaLbl = Label(linha4, text="Doença: " + paciente.getDoenca() )
		doencaLbl['bg'] = BG_DARK
		doencaLbl['fg'] = TEXT_WHITE
		doencaLbl['font'] = FONT_NORMAL
		doencaLbl.pack(side=LEFT)


		linha4 = Frame(self.widgetInfo)
		linha4['bg'] = BG_DARK
		linha4.pack()	

	def renderizarInfoConsulta(self, consulta):
		if(self.widgetInfo):
			self.widgetInfo.destroy()

		self.widgetInfo = Frame(self.widget1)
		self.widgetInfo['bg'] = BG_DARK
		self.widgetInfo.pack()

		linha2 = Frame(self.widgetInfo)
		linha2['bg'] = BG_DARK
		linha2.pack()

		idConsultaLbl = Label(linha2, text="ID da Consulta: "+str(consulta.getID()) + " | ")
		idConsultaLbl['bg'] = BG_DARK
		idConsultaLbl['fg'] = TEXT_WHITE
		idConsultaLbl['font'] = FONT_NORMAL
		idConsultaLbl.pack(side=LEFT)

		nomeLbl = Label(linha2, text="Paciente: "+consulta.getPaciente().getNome())
		nomeLbl['bg'] = BG_DARK
		nomeLbl['fg'] = TEXT_WHITE
		nomeLbl['font'] = FONT_NORMAL
		nomeLbl.pack(side=LEFT)

		separadorLbl = Label(linha2, text=" | ")
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)

		nascimentoLbl = Label(linha2, text="Nascimento: "+consulta.getPaciente().getNascimento())
		nascimentoLbl['bg'] = BG_DARK
		nascimentoLbl['fg'] = TEXT_WHITE
		nascimentoLbl['font'] = FONT_NORMAL
		nascimentoLbl.pack(side=LEFT)

		linha3 = Frame(self.widgetInfo)
		linha3['bg'] = BG_DARK
		linha3.pack()

		sexoLbl = Label(linha3, text="Sexo: "+consulta.getPaciente().getSexo())
		sexoLbl['bg'] = BG_DARK
		sexoLbl['fg'] = TEXT_WHITE
		sexoLbl['font'] = FONT_NORMAL
		sexoLbl.pack(side=LEFT)

		separadorLbl = Label(linha3, text=" | ")
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)

		cpfLbl = Label(linha3, text="CPF: "+consulta.getPaciente().getCpf())
		cpfLbl['bg'] = BG_DARK
		cpfLbl['fg'] = TEXT_WHITE
		cpfLbl['font'] = FONT_NORMAL
		cpfLbl.pack(side=LEFT)

		linha4 = Frame(self.widgetInfo)
		linha4['bg'] = BG_DARK
		linha4.pack()

		sangueLbl = Label(linha4, text="Tipo Sanguíneo: "+consulta.getPaciente().getTipoSanguineo())
		sangueLbl['bg'] = BG_DARK
		sangueLbl['fg'] = TEXT_WHITE
		sangueLbl['font'] = FONT_NORMAL
		sangueLbl.pack(side=LEFT)

		separadorLbl = Label(linha4, text=" | ")
		separadorLbl['bg'] = BG_DARK
		separadorLbl['fg'] = TEXT_WHITE
		separadorLbl['font'] = FONT_BOLD
		separadorLbl.pack(side=LEFT)

		doencaLbl = Label(linha4, text="Doença: "+consulta.getPaciente().getDoenca())
		doencaLbl['bg'] = BG_DARK
		doencaLbl['fg'] = TEXT_WHITE
		doencaLbl['font'] = FONT_NORMAL
		doencaLbl.pack(side=LEFT)


		linha5 = Frame(self.widgetInfo)
		linha5['bg'] = BG_DARK
		linha5.pack()

		dataHoraLbl = Label(linha5, text="Data: "+consulta.getData() + " - " + consulta.getHorario())
		dataHoraLbl['bg'] = BG_DARK
		dataHoraLbl['fg'] = TEXT_WHITE
		dataHoraLbl['font'] = FONT_NORMAL
		dataHoraLbl.pack(side=LEFT)

		medicoLbl = Label(linha5, text=" | Médico: "+consulta.getMedico())
		medicoLbl['bg'] = BG_DARK
		medicoLbl['fg'] = TEXT_WHITE
		medicoLbl['font'] = FONT_NORMAL
		medicoLbl.pack(side=LEFT)

		linha5 = Frame(self.widgetInfo)
		linha5['bg'] = BG_DARK
		linha5.pack()

		quartoLbl = Label(linha5, text="Quarto: "+consulta.getQuarto())
		quartoLbl['bg'] = BG_DARK
		quartoLbl['fg'] = TEXT_WHITE
		quartoLbl['font'] = FONT_NORMAL
		quartoLbl.pack(side=LEFT)

		cancelarBtn = Button(self.widget1, borderwidth=0)
		cancelarBtn['text'] = "Cancelar Consulta "
		cancelarBtn['fg'] = TEXT_DARK
		cancelarBtn['bg'] = TEXT_WHITE
		cancelarBtn['font'] = FONT_BOLD
		cancelarBtn['borderwidth'] = 1
		cancelarBtn['highlightbackground'] = BG_DARK
		cancelarBtn['command'] = lambda: [cancelarConsulta(consulta.getID()), messagebox.showinfo("Sucesso!", "A consulta foi cancelada."),self.carregarTela(MENU_CONSULTA)]
		cancelarBtn.pack()

		concluirBtn = Button(self.widget1, borderwidth=0)
		concluirBtn['text'] = "Concluir Consulta"
		concluirBtn['fg'] = TEXT_DARK
		concluirBtn['bg'] = TEXT_WHITE
		concluirBtn['font'] = FONT_BOLD
		concluirBtn['borderwidth'] = 1
		concluirBtn['highlightbackground'] = BG_DARK
		concluirBtn['command'] = lambda: [cancelarConsulta(consulta.getID()), messagebox.showinfo("Sucesso!", "A consulta foi concluída."), self.carregarTela(MENU_CONSULTA)]
		concluirBtn.pack()
