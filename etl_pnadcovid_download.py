import os
import requests
import zipfile
import io
import pandas as pd

# Meses a baixar (formato: MMYYYY)
meses = ['052020', '062020', '072020']

# URL base correta com pasta "Microdados/Dados"
base_url = 'https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Dados'

# Pasta de destino local
dest_folder = 'dados_pnadcovid'
os.makedirs(dest_folder, exist_ok=True)

dfs = []

for mes in meses:
    print(f'\n📥 Baixando dados do mês: {mes}')
    url = f'{base_url}/PNAD_COVID_{mes}.zip'
    print(f'🔗 URL: {url}')

    response = requests.get(url)
    response.raise_for_status()  # Erro se não encontrar o arquivo

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        for nome in z.namelist():
            if nome.lower().endswith(('.txt', '.csv')):
                print(f'📄 Lendo: {nome}')
                with z.open(nome) as f:
                    df = pd.read_csv(f, sep=';', dtype=str, low_memory=False)
                df['mes'] = mes
                dfs.append(df)

# Concatena os dados em um único DataFrame
df_total = pd.concat(dfs, ignore_index=True)

# Salva como CSV
output = os.path.join(dest_folder, 'pnadcovid_052020_072020.csv')
df_total.to_csv(output, index=False)
print(f'\n✅ Arquivo salvo em: {output}')

# Exibe primeiras colunas
print('\n🧾 Colunas iniciais:')
print(df_total.columns.tolist()[:20])
