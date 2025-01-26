import tkinter as tk
from tkinter import ttk, messagebox
from functions import carregar_arquivo, processar_dados  # Importa as funções do outro arquivo

# Configuração da janela principal
root = tk.Tk()
root.title("Análise de Dados do Excel com Pandas")
root.geometry("400x300")

# Variáveis globais
resultado_var = tk.StringVar()  # Para exibir o resultado na interface

# Elementos da interface
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Botão para carregar o arquivo
coluna_cb = ttk.Combobox(frame, state="readonly")  # Combobox para coluna
funcao_cb = ttk.Combobox(frame, state="readonly", values=["Média", "Primeiro Quartil", "Mediana", "Terceiro Quartil"])  # Funções disponíveis

tk.Button(frame, text="Carregar Arquivo Excel", command=lambda: carregar_arquivo(coluna_cb, resultado_var)).pack(pady=5)

# Dropdown para selecionar a coluna
tk.Label(frame, text="Selecione a Coluna:").pack(pady=5)
coluna_cb.pack(pady=5)

# Dropdown para selecionar a função
tk.Label(frame, text="Selecione a Função:").pack(pady=5)
funcao_cb.pack(pady=5)

# Botão para processar os dados
tk.Button(
    frame,
    text="Processar Dados",
    command=lambda: processar_dados(coluna_cb, funcao_cb, resultado_var)
).pack(pady=10)

# Campo para exibir o resultado
tk.Label(frame, textvariable=resultado_var, font=("Arial", 12), fg="green").pack(pady=10)


# Executar a aplicação
root.mainloop()
