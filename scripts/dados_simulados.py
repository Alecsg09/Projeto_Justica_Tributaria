import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Configuração inicial
fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

# Configurar os tipos de tributos e motivos da ação
tipos_tributos = ["ICMS", "ISS", "IPI", "IRPJ", "PIS/Cofins", "CSLL"]
motivos_acao = [
    "Revisão de débito tributário",
    "Imunidade tributária",
    "Isenção tributária",
    "Compensação tributária",
    "Restituição de tributo pago",
    "Nulidade de lançamento"
]
status_list = ["Arquivado", "Sentença Proferida", "Finalizado", "Em Andamento"]
sentencas_decisoes = ["Improcedente", "Parcialmente Procedente", "Sem Decisão", "Procedente"]

# Gera dados fictícios
def gerar_dados_simulados(num_registros):
    dados = []
    hoje = datetime.now()
    
    for _ in range(num_registros):
        numero_processo = fake.random_int(min=100000000000, max=999999999999)
        nome_cliente = fake.name()
        tipo_tributo = random.choice(tipos_tributos)
        motivo_acao = random.choice(motivos_acao)
        
        data_distribuicao = hoje - timedelta(days=random.randint(0, 730))  # Últimos 2 anos
        prazo_audiencia = data_distribuicao + timedelta(days=random.randint(30, 180))
        
        status = random.choice(status_list)
        valor_envolvido = round(random.uniform(1000, 1000000), 2)
        sentenca_decisao = random.choice(sentencas_decisoes)
        numero_juizo = fake.random_int(min=1, max=50)
        vara = f"{random.randint(1, 30)}ª Vara Tributária"
        responsavel = fake.name()

        dados.append([
            numero_processo,
            nome_cliente,
            tipo_tributo,
            motivo_acao,
            data_distribuicao.strftime("%d/%m/%Y"),
            prazo_audiencia.strftime("%d/%m/%Y"),
            status,
            valor_envolvido,
            sentenca_decisao,
            numero_juizo,
            vara,
            responsavel
        ])

    return dados

# Número de registros simulados
num_registros = 1000

# Colunas da planilha
colunas = [
    "Número do Processo",
    "Nome do Cliente",
    "Tipo de Tributo",
    "Motivo da Ação",
    "Data da Distribuição",
    "Prazo de Audiência",
    "Status",
    "Valor Envolvido",
    "Sentença/Decisão/Acórdão",
    "Número do Juízo",
    "Vara",
    "Responsável pelo Caso"
]

# Gerar os dados e criar o DataFrame
dados_simulados = gerar_dados_simulados(num_registros)
df = pd.DataFrame(dados_simulados, columns=colunas)

# Salvar em Excel
nome_arquivo = "simulacao_justica_tributaria.xlsx"
df.to_excel(nome_arquivo, index=False)

print(f"Planilha '{nome_arquivo}' gerada com sucesso!")
