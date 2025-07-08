# Análise PNAD COVID-19 - Dados 2020

Este repositório contém o código para o tratamento e análise dos microdados da Pesquisa PNAD COVID-19 referente ao ano de 2020.

---

## Sobre o projeto

A pesquisa PNAD COVID-19 é uma pesquisa nacional realizada pelo IBGE para acompanhar o impacto da pandemia no Brasil.  
Neste projeto, foram analisados dados de 3 meses de 2020 (setembro, outubro e novembro) com até 15 variáveis selecionadas para estudos descritivos e geração de insights.

---

## Conteúdo

- `tratamento_dados_pnad.py` - Script Python para carregar, limpar e consolidar os dados CSV dos 3 meses, selecionando 15 colunas relevantes.
- `pnadcovid_tratado_3meses.csv` - Arquivo CSV resultante do tratamento dos dados (gerado pelo script).
- `README.md` - Documentação do projeto.

---

## Como executar

1. Baixe os arquivos CSV da PNAD COVID-19 referentes aos meses de interesse (ex: setembro, outubro e novembro de 2020) do site do IBGE.  
2. Ajuste o caminho dos arquivos na variável `arquivos_csv` dentro do script `tratamento_dados_pnad.py`.  
3. Execute o script Python:

```bash
python tratamento_dados_pnad.py

4.O script irá gerar o arquivo pnadcovid_tratado_3meses.csv com os dados consolidados e exibirá análises descritivas no terminal.

Variáveis selecionadas
As 15 variáveis selecionadas para análise foram:

Ano

UF (Estado)

CAPITAL

V1012 (Sexo)

V1013 (Idade)

V1008 (Renda)

Estrato

UPA

V1022

V1030

B0011

C001

D0011

E001

F001

Obs: As descrições completas das variáveis podem ser consultadas no dicionário oficial da PNAD COVID-19 disponível no site do IBGE.

Requisitos
Python 3.x

Pandas

Instale as dependências com:

bash
Copiar
Editar
pip install pandas

Referências
Pesquisa PNAD COVID-19: https://www.ibge.gov.br/estatisticas/sociais/saude/27947-divulgacao-mensal-pnadcovid2.html

Dicionário de variáveis PNAD COVID-19: arquivo XLS disponível na mesma página.