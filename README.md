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
