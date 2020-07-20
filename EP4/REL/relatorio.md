# Exercício-Programa 4: Previsão de Estágio da Infecção por COVID-19
Autores: Bento Pereira, Daniela Favero


## 1. Resumo
Último trabalho da disciplina MAC0425 que gira em torno dos dados de exames realizados por diversos hospitais de São Paulo relacionados à atual epidêmia do SARS-CoV-2.


## 2. Introdução

### Motivação
Atualmente o mundo se encontra numa situação ímpar para as gerações atuais. A atual pandêmia do SARS-CoV-2 colocou imposições das mais diversas no modo de vida da contemporaneidade, desde de deslocamento até de estudos e trabalho. Um dos fatores que mais preocupam nesta conjuntura é a rápida capacidade de disseminação do vírus, que faz medidas como o 'contact tracing' serem extremamente úteis e importantes. Temos então que é essencial a tarefa de determinar se um indívudo apresenta ou não o vírus no seu sistema de forma rápida e confiante, e é visando este ideal que idealizamos uma rede neural que utiliza entradas dos mais diversos exames para atingir estes resultados.

### Objetivos 
Organização dos dados laboratoriais de diversos hospitais de São Paulo com o objetivo de treinar uma rede neural que utilizará diversos resultados de exames diversos determinar se um indivíduo já teve SARS-CoV-2 ou se apresenta o vírus e em qual estágio de infecção.

### Estrutura do relatório
1. Resumo
2. Introdução
    - Motivação
    - Objetivos
    - Estrutura do relatório
3. Metodologia
    - Pré-processamento dos dados
    - Arquitetura da rede neural
    - Experimentos
4. Resultados
5. Discussão
6. Bibliografia


## 3. Metodologia

### Pré-processamento dos dados
A primeira coisa que fizemos foi descobrir quais eram as possíveis formas de se preencher a coluna `de_exame` e `de_analito`. Para isso, fizemos a função `filter_inputs()` em `data.py` para gerar os arquivos `exames.txt` e `analitos.txt`. Depois verificamos (na mão) os exames que faziam sentido para a análise de pacientes com Covid-19 - gerando `exames_selecionados.txt` e `analitos_selecionados.txt`. Alguns dos exames que apresentam relação com a doença observada são: PCR, IgG, IgM, produção de anticorpos em geral, Alfa-1 Glicoproteína Ácida (que detecta processos inflamatórios), ferro/ferritina/gasometria venosa (que detectam quão eficiente o pulmão está sendo em oxigenar o corpo), Hematócrito, Dímero D, Tempo de Protrombina, Fibrinogênio e Contagem de Plaquetas.¹  

Depois disso, unimos as colunas `de_exame` e `de_analito` em apenas uma coluna `exames` para facilitar a forma como lidaríamos com os dados. Então, criamos um nodo *dataframe*: o seu formato possui um par paciente-data em cada linha, e seus respectivos resultados de exames. Desta forma, para passar pela rede neural, só seria necessário inserir um par paciente-data e as colunas do PCR, IgG e IgM para prever o resultado. Tal tabela se encontra em `final_data.csv`.

**Para fazer:** Restou mapear os resultados dos exames para variáveis booleanas (a função de mapeamento analisaria o valor de referência e informaria se aquele parâmetro está em valores esperados de um indivíduo saudável ou não).
(1. Fontes: <https://newslab.com.br/alteracoes-laboratoriais-mais-frequentes-em-pacientes-com-covid-19>,
<https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(20)30217-9/fulltext>)

### Arquitetura da rede neural
Utilizamos a rede neural feita em aula pelo professor, no exercício dado.

### Experimentos
Não foi possível realizar experimentos, pois não finalizamos o pré-processamento dos dados.


## 4. Resultados


## 5. Discussão
Nossa discussão girou em torno de como melhor tratar os dados. Não sendo estudantes de áreas das ciências biológicas utilizamos como heurística para determinar a relevância de um certo exame como ela se relacionaria com uma das formas de manifestação da infecção por SARS-CoV-2, seja afetando o sistema circulatório ou respiratório. Infelizmente não chegamos a conseguir testar os resultados do tratamento, contudo apresentávamos confiança de que nossas decisões de projeto produziriam bons resultados.


## 6. Bibliografia
Fontes: <https://newslab.com.br/alteracoes-laboratoriais-mais-frequentes-em-pacientes-com-covid-19>,
<https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(20)30217-9/fulltext>