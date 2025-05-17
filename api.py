import requests
from pprint import pprint

numero = input("Número do CNPJ (somente números): ")
url = f"https://publica.cnpj.ws/cnpj/{numero}"

requisicao = requests.get(url)
dados = requisicao.json()

#pprint(dados)

razao_social = dados.get("razao_social", "Razão social não disponível")
print("Razão Social:", razao_social, "\n")

atividade_principal = dados["estabelecimento"]["atividade_principal"]["descricao"]
print("Atividade principal:", atividade_principal,"\n")

ativ_sec = dados["estabelecimento"].get("atividades_secundarias", [])
print("\nAtividades secundárias:")
if ativ_sec:
    for i, atividade in enumerate(ativ_sec, start=1):
        print(f"  {i}. {atividade['descricao']}")
else:
    print("  Nenhuma atividade secundária cadastrada.\n")

print("\n")

