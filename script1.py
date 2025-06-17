import customtkinter
import customtkinter as ctk
import requests

# Dicionário com nomes e símbolos
moedas = {
    "BRL": ("Real Brasileiro", "R$"),
    "USD": ("Dólar Americano", "$"),
    "EUR": ("Euro", "€"),
    "JPY": ("Iene Japonês", "¥"),
    "GBP": ("Libra Esterlina", "£"),
    "ARS": ("Peso Argentino", "$"),
    "CAD": ("Dólar Canadense", "C$")
}

def converter():
    valor = entry_valor.get().replace(",", ".")
    moeda_origem = combo_origem.get()
    moeda_destino = combo_destino.get()

    if not valor:
        label_resultado.configure(text="⚠️ Digite um valor.")
        return

    if moeda_origem == moeda_destino:
        label_resultado.configure(text="⚠️ Escolha moedas diferentes.")
        return

    try:
        valor_float = float(valor)
        url = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
        resposta = requests.get(url).json()
        chave = moeda_origem + moeda_destino
        taxa = float(resposta[chave]["bid"])
        convertido = valor_float * taxa

        nome_destino, simbolo_destino = moedas[moeda_destino]
        nome_origem, simbolo_origem = moedas[moeda_origem]

        label_resultado.configure(
            text=f"{simbolo_origem}{valor_float:.2f} ({nome_origem})\n= {simbolo_destino}{convertido:.2f} ({nome_destino})"
        )
    except Exception:
        label_resultado.configure(text="❌ Erro na conversão.")

def limpar():
    entry_valor.delete(0, "end")
    combo_origem.set("BRL")
    combo_destino.set("USD")
    label_resultado.configure(text="")

# Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Conversor de Moedas")
app.geometry("460x430")
app.resizable(False, False)

# Título
titulo = ctk.CTkLabel(app, text="💱 Conversor de Moedas", font=("Arial", 22, "bold"))
titulo.pack(pady=20)

# Entrada de valor
entry_valor = ctk.CTkEntry(app, placeholder_text="Digite o valor", width=200)
entry_valor.pack(pady=10)

# Seleção de moedas
combo_origem = ctk.CTkComboBox(app, values=list(moedas.keys()), width=120)
combo_origem.set("BRL")
combo_origem.pack(pady=5)

combo_destino = ctk.CTkComboBox(app, values=list(moedas.keys()), width=120)
combo_destino.set("USD")
combo_destino.pack(pady=5)

# Botões
frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack(pady=20)

botao_converter = ctk.CTkButton(frame_botoes, text="Converter", command=converter, width=100)
botao_converter.pack(side="left", padx=10)

botao_limpar = ctk.CTkButton(frame_botoes, text="Limpar", command=limpar, width=100)
botao_limpar.pack(side="left", padx=10)

# Resultado
label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 16))
label_resultado.pack(pady=10)

app.mainloop()
