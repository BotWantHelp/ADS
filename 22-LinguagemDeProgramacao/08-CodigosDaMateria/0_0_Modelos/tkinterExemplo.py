import tkinter as tk

def button1_click():
    label.config(text="Eu também te amo ♥!")

def button2_click():
    label.config(text="Não mente clica em sim logo!")

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo com 2 Botões")

# Criar um rótulo
label = tk.Label(root, text="Me ama?.")
label.pack()

# Criar o primeiro botão
button1 = tk.Button(root, text="Sim", command=button1_click)
button1.pack()

# Criar o segundo botão
button2 = tk.Button(root, text="Não", command=button2_click)
button2.pack()

# Iniciar o loop de eventos principal
root.mainloop()

