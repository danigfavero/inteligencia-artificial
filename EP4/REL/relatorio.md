# Exercício-Programa 4: Previsão de Estágio da Infecção por COVID-19
Autores: Bento Pereira, Daniela Favero

## 1. Resumo
bláblá isso é um resumo


## 2. Introdução

### Motivação
motivação do trabalho - 1 ou 2 parágrafos 

### Objetivos 
objetivos do trabalho - 1 parágrafo

### Estrutura do relatório
1 parágrafo


## 3. Metodologia

### Pré-processamento dos dados
A primeira coisa que fizemos foi descobrir quais eram as possíveis formas de se preencher a coluna `de_exame` e `de_analito`. Para isso, fizemos a função `filter_inputs()` em `data.py` para gerar os arquivos `exames.txt` e `analitos.txt`. Depois verificamos (na mão) os exames que faziam sentido para a análise de pacientes com Covid-19 - gerando `exames_selecionados.txt` e `analitos_selecionados.txt`. Alguns dos exames que apresentam relação com a doença observada são: PCR, IgG, IgM, produção de anticorpos em geral, Alfa-1 Glicoproteína Ácida (que detecta processos inflamatórios), ferro/ferritina/gasometria venosa (que detectam quão eficiente o pulmão está sendo em oxigenar o corpo), Hematócrito, Dímero D, Tempo de Protrombina, Fibrinogênio e Contagem de Plaquetas.¹  
(1. Fontes: <https://newslab.com.br/alteracoes-laboratoriais-mais-frequentes-em-pacientes-com-covid-19>,
<https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(20)30217-9/fulltext>)

### Arquitetura da rede neural
lorem ipsum

### Experimentos
descrição dos experimentos feitos


## 4. Resultados
valores obtidos nos experimentos, apresentando gráficos e tabelas


## 5. Discussão
a viabilidade e utilidade deusar arquitetura neural proposta como uma previsor da fase da infecção


## 6. Bibliografia
todas as fontes utilizadas na realização desse trabalho
(as fontes devem estar citadas em alguma parte anterior do trabalho)