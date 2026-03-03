# Trabalho de Mineração de Dados (PNS 2019)

Este repositório contém códigos e análises usando dados da Pesquisa Nacional de Saúde (PNS) 2019.  

Os scripts calculam indicadores sobre **idosos, doenças crônicas e depressão**, servindo como análise inicial da base (corresponde à AP1 do trabalho).

---

## AP1: Definição do problema

**Tema:** Idosos com depressão  
**Faixa etária:** Acima de 60 anos  

---

## Indicadores Calculados

| Indicador | Valor Absoluto |
|-----------|----------------|
| Total de idosos (>60 anos) | 40.676 |
| Total de idosos (>60 anos) com depressão | 2.212 |
| Total de idosos (>60 anos) sem nenhuma doença crônica | 20.612 |
| Total de pessoas (>=19 anos) com depressão | 8.204 |

---

## Sobre a base de dados

A base de dados **PNS 2019** não está incluída no repositório devido ao tamanho do arquivo (**~900 MB**).  
Para obter a base, acesse o site oficial do IBGE: [Microdados PNS 2019](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html).

---

## Códigos para gerar os resultados

- **Total de idosos (>60 anos):** [totalidosos.py](https://github.com/MariaVManhaes/Trabalho-Mineracao-de-dados-pns/blob/main/totalidosos.py)  
- **Total de idosos (>60 anos) com depressão:** [idososcomdepressao.py](https://github.com/MariaVManhaes/Trabalho-Mineracao-de-dados-pns/blob/main/idososcomdepressao.py)  
- **Total de idosos (>60 anos) sem nenhuma doença crônica:** [idosossaudaveis.py](https://github.com/MariaVManhaes/Trabalho-Mineracao-de-dados-pns/blob/main/idosossaudaveis.py)  
- **Total de pessoas (>=19 anos) com depressão:** [totaldepessoascomdepressao+19.py](https://github.com/MariaVManhaes/Trabalho-Mineracao-de-dados-pns/blob/main/totaldepessoascomdepressao%2B19.py)  
