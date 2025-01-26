from tkinter import filedialog, messagebox
import pandas as pd

# Variável global para armazenar o DataFrame
df = None

def carregar_arquivo(coluna_cb, resultado_var):
    filepath = filedialog.askopenfilename(
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    if filepath:
        try:
            global df
            df = pd.read_excel(filepath)
            
            # Filtrar apenas colunas com valores numéricos
            colunas_numericas = [
                col for col in df.columns 
                if pd.api.types.is_numeric_dtype(df[col])  # Verifica se a coluna é de tipo numérico
            ]
            
            if not colunas_numericas:
                messagebox.showwarning("Atenção", "O arquivo selecionado não possui colunas numéricas.")
                return
            
            coluna_cb['values'] = colunas_numericas
            coluna_cb.set('')  # Limpa a seleção anterior
            resultado_var.set("Arquivo carregado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

def processar_dados(coluna_cb, funcao_cb, resultado_var):
    global df  # Certifique-se de que a variável df está acessível
    if df is None or df.empty:
        messagebox.showwarning("Atenção", "Nenhum arquivo foi carregado. Por favor, carregue um arquivo primeiro.")
        return
    
    coluna = coluna_cb.get()
    funcao = funcao_cb.get()
    
    if not coluna or not funcao:
        messagebox.showwarning("Atenção", "Selecione uma coluna e uma função.")
        return
    
    try:
        if funcao == "Média":
            resultado = df[coluna].mean()
        elif funcao == "Mediana":
            resultado = df[coluna].median()
        elif funcao == "Primeiro Quartil":
            resultado = df[coluna].quantile(0.25)
        elif funcao == "Terceiro Quartil":
            resultado = df[coluna].quantile(0.75)
        else:
            resultado = "Função não implementada."
        
        resultado_var.set(f"Resultado ({funcao}): {resultado:.2f}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar os dados: {e}")
