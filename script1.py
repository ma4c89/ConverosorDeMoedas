import customtkinter
import requests

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Conversor de Moedas")
janela.geometry("500x550")
janela.resizable(False, False)

simbolos = {
    "USD": "$",
    "BRL": "R$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "CNY": "¥",
    "BTC": "₿",
    "ETH": "Ξ",
    "CAD": "C$",
    "AUD": "A$",
    "ARS": "$",
    "CHF": "Fr.",
    "MXN": "$",
    "ZAR": "R",
    "INR": "₹"
}

def converter_moeda():
    origem = campo_moeda_origem.get()
    destino = campo_moeda_destino.get()
    valor = campo_valor.get()

    print(f"\n=== Conversão Solicitada ===")
    print(f"Moeda de origem: {origem}")
    print(f"Moeda de destino: {destino}")
    print(f"Valor digitado: {valor}")

    try:
        valor_float = float(valor)
        if origem == destino:
            resultado_label.configure(text="Por favor, selecione moedas diferentes.")
            print("Erro: moedas iguais selecionadas.")
            return

        par_moeda = f"{origem}-{destino}"
        url = f"https://economia.awesomeapi.com.br/last/{par_moeda}"
        resposta = requests.get(url).json()

        chave = origem + destino
        if chave in resposta:
            cotacao = float(resposta[chave]["bid"])
            resultado = cotacao * valor_float
            simbolo_origem = simbolos.get(origem, "")
            simbolo_destino = simbolos.get(destino, "")
            texto_resultado = f"{simbolo_origem}{valor_float:.2f} {origem} = {simbolo_destino}{resultado:.2f} {destino}"
            resultado_label.configure(text=texto_resultado)
            print(f"Resultado: {texto_resultado}")
            campo_valor.delete(0, "end")
        else:
            resultado_label.configure(text="Conversão não disponível para essas moedas.")
            print("Erro: conversão não disponível.")
    except ValueError:
        resultado_label.configure(text="Digite um valor numérico válido.")
        print("Erro: valor digitado não é numérico.")
    except Exception as e:
        resultado_label.configure(text=f"Erro: {e}")
        print(f"Erro inesperado: {e}")

titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial", 24, "bold"))
titulo.pack(pady=(20, 10))

texto_moeda_origem = customtkinter.CTkLabel(janela, text="Moeda de origem:")
texto_moeda_origem.pack(pady=(10, 0))

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(simbolos.keys()))
campo_moeda_origem.pack(pady=(0, 10), padx=20, fill="x")
campo_moeda_origem.set("USD")

texto_moeda_destino = customtkinter.CTkLabel(janela, text="Moeda de destino:")
texto_moeda_destino.pack(pady=(10, 0))

campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=list(simbolos.keys()))
campo_moeda_destino.pack(pady=(0, 10), padx=20, fill="x")
campo_moeda_destino.set("BRL")

texto_valor = customtkinter.CTkLabel(janela, text="Valor para converter:")
texto_valor.pack(pady=(10, 0))

campo_valor = customtkinter.CTkEntry(janela, placeholder_text="Ex: 100")
campo_valor.pack(pady=(0, 10), padx=20, fill="x")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, cursor="hand2")
botao_converter.pack(pady=10)

resultado_label = customtkinter.CTkLabel(janela, text="", font=("Arial", 16))
resultado_label.pack(pady=(0, 10))

lista_moeda = customtkinter.CTkScrollableFrame(janela, height=200)
lista_moeda.pack(padx=20, pady=(10, 20), fill="both", expand=True)

moedas_disponiveis = [
    "USD : Dólar americano",
    "BRL : Real brasileiro",
    "EUR : Euro",
    "GBP : Libra esterlina",
    "JPY : Iene japonês",
    "CNY : Yuan chinês",
    "BTC : Bitcoin",
    "ETH : Ethereum",
    "CAD : Dólar canadense",
    "AUD : Dólar australiano",
    "ARS : Peso argentino",
    "CHF : Franco suíço",
    "MXN : Peso mexicano",
    "ZAR : Rand sul-africano",
    "INR : Rúpia indiana"
]

for moeda in moedas_disponiveis:
    label_moeda = customtkinter.CTkLabel(lista_moeda, text=moeda)
    label_moeda.pack(anchor="w", pady=2, padx=10)

janela.mainloop()
