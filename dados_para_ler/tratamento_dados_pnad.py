import pandas as pd
import os

# Lista dos arquivos que você quer analisar (ajuste o caminho e nomes)
arquivos_csv = [
    'dados_para_ler/PNAD_COVID_092020.csv',
    'dados_para_ler/PNAD_COVID_102020.csv',
    'dados_para_ler/PNAD_COVID_112020.csv'
]

# Suas 15 colunas selecionadas para análise
colunas_selecionadas = [
    'Ano', 'UF', 'CAPITAL', 'V1012', 'V1013', 'V1008', 'Estrato', 'UPA',
    'V1022', 'V1030', 'B0011', 'C001', 'D0011', 'E001', 'F001'
]

# Verificar quais colunas existem de fato em TODOS os arquivos para evitar erro
colunas_arquivos = []
for arquivo in arquivos_csv:
    df_temp = pd.read_csv(arquivo, nrows=1, encoding='latin1')
    colunas_arquivos.append(set(df_temp.columns))

colunas_comuns = set.intersection(*colunas_arquivos)
print(f'Colunas comuns em todos os arquivos: {sorted(colunas_comuns)}')

# Ajustar colunas finais só para as que existem em todos os arquivos
colunas_final = [c for c in colunas_selecionadas if c in colunas_comuns]
print(f'Colunas selecionadas que serão usadas: {colunas_final}')

# Carregar os dados só com as colunas_final e adicionar coluna mes_ano
dfs = []
for arquivo in arquivos_csv:
    print(f'Carregando arquivo {arquivo}...')
    df = pd.read_csv(arquivo, usecols=colunas_final, dtype=str, encoding='latin1')
    mes = arquivo[-10:-4]  # pega "092020", "102020", etc (ajuste caso necessário)
    df['mes_ano'] = mes
    dfs.append(df)

# Concatenar todos os meses
df_total = pd.concat(dfs, ignore_index=True)
print(f'Tamanho total do dataframe concatenado: {df_total.shape}')
print(df_total.head())

# Exemplo simples de análise descritiva
# Converter idade para numérico
if 'V1013' in df_total.columns:
    df_total['V1013'] = pd.to_numeric(df_total['V1013'], errors='coerce')
    print('Média de idade geral:', df_total['V1013'].mean())

# Distribuição de sexo (V1012)
if 'V1012' in df_total.columns:
    print('Distribuição de sexo:')
    print(df_total['V1012'].value_counts(dropna=False))

# Contagem por estado (UF)
if 'UF' in df_total.columns:
    print('Número de registros por estado:')
    print(df_total['UF'].value_counts())

# Exemplo: quantos responderam uma das questões V1022
if 'V1022' in df_total.columns:
    print('Distribuição da questão V1022:')
    print(df_total['V1022'].value_counts(dropna=False))

# Salvar CSV tratado para uso posterior
output_dir = 'dados_output'
os.makedirs(output_dir, exist_ok=True)
df_total.to_csv(os.path.join(output_dir, 'pnadcovid_tratado_3meses.csv'), index=False)
