from tkinter import *
from turtle import left

janela = Tk()

def center(win):
    win.update_idletasks()  # Update "requested size" from geometry manager
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def calculafolha():
    vsalario = float(e_salario.get())
    padiantamento = float(e_adiant.get())
    # calculo do adiantamento
    vadiantamento = vsalario * float(padiantamento)/100

    vhe = int(e_he.get())
    valor_he = vsalario / 220 * vhe * 1.5

    vfalta = float(e_faltas.get()) * vsalario / 20

    # subtrair salario bruto do adiantamento
    vsalario = vsalario - vadiantamento
    vsf = float(e_dep.get()) * 52
 
    vprovento = vsalario + vadiantamento + valor_he + vsf
    Label(frame_baixo,text=f'{vsalario:.2f}', font='Courier 10', width=8, 
          bg='#C4C4C4', bd=1, relief='solid', justify=RIGHT).place(x=175,y=254)
    Label(frame_baixo,text=f'{vadiantamento:.2f}', font='Courier 10', width=8,
          bg='#C4C4C4', bd=1, relief='solid', justify=RIGHT).place(x=175,y=279)
    Label(frame_baixo,text=f'{valor_he:.2f}', font='Courier 10', width=8,
          bg='#C4C4C4', bd=1, relief='solid', justify=RIGHT).place(x=175,y=301)
    Label(frame_baixo,text=f'{vsf:.2f}', font='Courier 10', width=8,
          bg='#C4C4C4', bd=1, relief='solid', justify=RIGHT).place(x=175,y=323)
    Label(frame_baixo,text=f'{vprovento:.2f}', font='Courier 10', width=8,
          bg='#C4C4C4', bd=1, relief='solid', justify=RIGHT).place(x=175,y=350)

    Label(frame_baixo,text=f'{vfalta:.2f}', font='Courier 10', width=8,
          bg='#A6D2DF', bd=1, relief='solid', justify=RIGHT).place(x=409,y=255)


janela.title("Folha de Pagamento")
janela.geometry("500x500")
center(janela)

frame_cima = Frame(janela, width=500, height=70, bg="#01C3C3")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=500, height=430, bg="white")
frame_baixo.grid(row=1, column=0)

app_nome= Label(frame_cima, text="Cálculo e Contra Cheque", width=35, height=2,
          bg="#01C3C3", fg='yellow', font='Ivy 16 bold')
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, width=500, bg='green')
app_linha.place(x=0, y=60)

l_salario = Label(frame_baixo, text="Salário", height=1, 
               font="Ivy 10 bold", bg='white')
l_salario.place(x=20, y=30)
e_salario = Entry(frame_baixo, width=8, bg="#FFFE97")
e_salario.place(x=130, y=30)

l_adiant = Label(frame_baixo, text="Adiantamento", height=1, 
               font="Ivy 10 bold", bg='white')
l_adiant.place(x=230, y=30)
e_adiant = Entry(frame_baixo, width=8, bg="#FFFE97")
e_adiant.place(x=340, y=30)

l_he = Label(frame_baixo, text="Hora Extra", height=1, 
               font="Ivy 10 bold", bg='white')
l_he.place(x=20, y=60)
e_he = Entry(frame_baixo, width=8, bg="#FFFE97")
e_he.place(x=130, y=60)

l_faltas = Label(frame_baixo, text="N. Faltas", height=1, 
               font="Ivy 10 bold", bg='white')
l_faltas.place(x=230, y=60)
e_faltas = Entry(frame_baixo, width=8, bg="#FFFE97")
e_faltas.place(x=340, y=60)

l_dep = Label(frame_baixo, text="N.Dependentes", height=1, 
               font="Ivy 10 bold", bg='white')
l_dep.place(x=20, y=90)
e_dep = Entry(frame_baixo, width=8, bg="#FFFE97")
e_dep.place(x=130, y=90)

l_pensao = Label(frame_baixo, text="Pensão (s/n)", height=1, 
               font="Ivy 10 bold", bg='white')
l_pensao.place(x=230, y=90)
e_pensao = Entry(frame_baixo, width=8, bg="#FFFE97")
e_pensao.place(x=340, y=90)

l_frase = Label(frame_baixo, text='Proventos', width=24, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_frase.place(x=20, y=230)

l_frase2 = Label(frame_baixo, text='Descontos', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_frase2.place(x=243, y=230)
l_faltas = Label(frame_baixo, text='Faltas                 ', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_faltas.place(x=243, y=254)
l_ir = Label(frame_baixo, text='IRRF                   ', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_ir.place(x=243, y=277)

l_pensao = Label(frame_baixo, text='Pensão                 ', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_pensao.place(x=243, y=300)
l_inss = Label(frame_baixo, text='INSS                   ', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_inss.place(x=243, y=323)
l_inss = Label(frame_baixo, text='Total                  ', width=23, height=1, 
         font='Courier 12', bg='#A6D2DF', bd=1, relief='solid')
l_inss.place(x=243, y=350)


l_exsalario = Label(frame_baixo, text='Salario              ', width=22, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_exsalario.place(x=20, y=254)

l_exadiant = Label(frame_baixo, text='Adiantamento         ', width=22, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_exadiant.place(x=20, y=277)

l_exhe = Label(frame_baixo, text='Hora Extra           ', width=22, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_exhe.place(x=20, y=300)
l_sf = Label(frame_baixo, text='S.Família             ', width=22, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_sf.place(x=20, y=323)

l_sf = Label(frame_baixo, text='Total                ', width=22, height=1, 
         font='Courier 12', bg='#C4C4C4', bd=1, relief='solid')
l_sf.place(x=20, y=350)

l_inss = Label(frame_baixo, text='Líquido                ', width=23, height=1, 
         font='Courier 12', bg='#E6E683', bd=1, relief='solid')
l_inss.place(x=243, y=377)


b_calcular = Button(frame_baixo, text='Calcular', width=45, height=1,
    font='Ivy 12 bold',  bg='blue', fg='white', command=calculafolha)
b_calcular.place(x=20, y=200)



janela.mainloop()
