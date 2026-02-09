import customtkinter as ctk
from mat import Mat

app = ctk.CTk()
app.title("Calculadora")

class Botoes:
    #botão C
    btnC = ctk.CTkButton(app, height=50, width=50, fg_color="#525252", text="C", corner_radius=15)
    btnC.grid(column = 1, row= 1)
    #botão CE
    btnCE = ctk.CTkButton(app, width=50, height=50, fg_color="#525252", text="CE", corner_radius=15)
    btnCE.grid(column=2, row=1)
    #botão DEL
    btnDEL = ctk.CTkButton(app, width= 50, height=50, fg_color="#525252", text="DEL", corner_radius=15)
    btnDEL.grid(column=3, row=1)
    #botão +
    btnDivisao = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text="/", corner_radius=15)
    btnDivisao.grid(column = 4, row = 1)
    #botão 7
    btn7 = ctk.CTkButton(app, height=50, width=50, fg_color="#525252", text="7", corner_radius=15)
    btn7.grid(column = 1, row= 2)
    #botão 8
    btn8 = ctk.CTkButton(app, width=50, height=50, fg_color="#525252", text="8", corner_radius=15)
    btn8.grid(column=2, row=2)
    #botão 9
    btn9 = ctk.CTkButton(app, width= 50, height=50, fg_color="#525252", text="9", corner_radius=15)
    btn9.grid(column=3, row=2)
    #botão *
    btnVezes = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text="x", corner_radius=15)
    btnVezes.grid(column = 4, row = 2)
    #botão 4
    btn4 = ctk.CTkButton(app, height=50, width=50, fg_color="#525252", text="4", corner_radius=15)
    btn4.grid(column = 1, row= 3)
    #botão 5
    btn5 = ctk.CTkButton(app, width=50, height=50, fg_color="#525252", text="5", corner_radius=15)
    btn5.grid(column=2, row=3)
    #botão 6
    btn6 = ctk.CTkButton(app, width= 50, height=50, fg_color="#525252", text="6", corner_radius=15)
    btn6.grid(column=3, row=3)
    #botão -
    btnSubtracao = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text="-", corner_radius=15)
    btnSubtracao.grid(column = 4, row = 3)
    #botão 1
    btn1 = ctk.CTkButton(app, height=50, width=50, fg_color="#525252", text="1", corner_radius=15)
    btn1.grid(column = 1, row= 4)
    #botão 2
    btn2 = ctk.CTkButton(app, width=50, height=50, fg_color="#525252", text="2", corner_radius=15)
    btn2.grid(column=2, row=4)
    #botão 3
    btn3 = ctk.CTkButton(app, width= 50, height=50, fg_color="#525252", text="3", corner_radius=15)
    btn3.grid(column=3, row=4)
    #botão +
    btnSoma = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text="+", corner_radius=15)
    btnSoma.grid(column = 4, row = 4)
    #botão +/-
    btnSinal = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text="+/-", corner_radius=15)
    btnSinal.grid(column = 1, row = 5)
    #botão 0
    btn0 = ctk.CTkButton(app, width=50, height=50, fg_color="#525252", text="0", corner_radius=15)
    btn0.grid(column = 2, row = 5)
    #botão ,
    btnVirgula = ctk.CTkButton(app, width=50, height=50, fg_color="#343434", text=",", corner_radius=15)
    btnVirgula.grid(column = 3, row = 5)
    #botão =
    btnResultado = ctk.CTkButton(app, width=50, height=50, corner_radius=15, fg_color="orange", text="=")
    btnResultado.grid(column= 4, row= 5)


app.mainloop()