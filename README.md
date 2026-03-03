# AP1 - Trabalho de Mineração de Dados (PNS 2019)

Este repositório contém códigos e análises referentes à **Atividade Prática 1 (AP1)** do curso de Mineração de Dados, usando microdados da Pesquisa Nacional de Saúde (PNS) 2019.

Os scripts calculam indicadores sobre **idosos, doenças crônicas e depressão**, servindo como análise inicial da base.

---

## Indicadores Calculados

| Indicador | Valor Absoluto | Percentual* |
|-----------|----------------|------------|
| Total de idosos (>60 anos) | 40.676 | 100% |
| Total de idosos (>60 anos) sem nenhuma doença crônica | 20.612 | 50,7% |
| Total de pessoas (>=19 anos) com depressão | 8.204 | — |
| Total de idosos (>60 anos) com depressão | 2.212 | 5,4% |

\*Percentual calculado sobre o total de idosos (>60 anos), exceto o indicador de adultos com depressão.

---

## Sobre a base de dados

A base de dados **PNS 2019** não está incluída no repositório devido ao tamanho do arquivo (**~900 MB**).  

Para obter a base:

- Acesse o site oficial do IBGE: [Microdados PNS 2019](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html)  
- Salve o arquivo no mesmo diretório do script com o nome: `pns2019.csv`.

---

## Como usar

1. Clone o repositório:  
   ```bash
   git clone <URL_DO_REPOSITORIO>
