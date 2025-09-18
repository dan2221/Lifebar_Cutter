import webbrowser
from tkinter import PhotoImage, Toplevel, Label, Button

# Crie o botão de coração e janela de agradecimento
def open_love_window():
    love_win = Toplevel(root)
    love_win.title("Agradecimentos 💖")
    love_win.geometry("340x140")
    love_win.resizable(False, False)
    Label(love_win, text="Feito com carinho por Chavyn.\n\nConfira também:", font=("Arial", 12)).pack(pady=5)
    
    # Link 1
    link1 = Label(love_win, text="GitHub do projeto", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link1.pack()
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/dan2221"))
    
    # Link 2 (adicione mais se quiser)
    link2 = Label(love_win, text="Meu canal no YouTube", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link2.pack()
    link2.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.youtube.com/@chavyn"))
    
    Label(love_win, text="\nObrigado por usar!", font=("Arial", 10)).pack()

# --- No final do seu código principal (antes do mainloop) ---

# Ícone de coração (pode usar um emoji ou imagem)
try:
    # Se quiser usar imagem, descomente e coloque arquivo "heart.png"
    # heart_img = PhotoImage(file="heart.png")
    # heart_btn = Button(root, image=heart_img, command=open_love_window, bd=0)
    # heart_btn.image = heart_img  # evita garbage collection
    # heart_btn.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)
    
    # Usando só emoji:
    heart_btn = Button(root, text="❤️", font=("Arial", 15), command=open_love_window, bd=0)
    heart_btn.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)
except Exception as e:
    print("Erro ao carregar ícone:", e)