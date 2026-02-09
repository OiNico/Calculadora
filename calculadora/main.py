import customtkinter as ctk
from mat import Mat

app = ctk.CTk()
app.title("Calculadora")

#botão 0
btn0 = ctk.CTkButton(app, width=50, height=50, fg_color="gray", text="0")
btn0.grid(column = 4, row = 4)
#botão ,
btnVirgula = ctk.CTkButton(app, width=50, height=50, fg_color="gray", text=",")
btnVirgula.grid(column = 5, row = 4)
#botão =
btnResultado = ctk.CTkButton(app, width=50, height=50, corner_radius=5, fg_color="orange", text="=")
btnResultado.grid(column= 6, row= 4)


app.mainloop()