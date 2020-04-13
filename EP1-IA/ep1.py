"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP,
  DECLARO QUE SOU A UNICA PESSOA AUTORA E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E, PORTANTO, NAO CONSTITUEM ATO DE DESONESTIDADE ACADEMICA,
  FALTA DE ETICA OU PLAGIO.
  DECLARO TAMBEM QUE SOU A PESSOA RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : Daniela Gonzalez Favero
  NUSP : 10277443

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma referencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em:
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

import util

############################################################
# Part 1: Segmentation problem under a unigram model

class SegmentationProblem(util.Problem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def isState(self, state):
        """ Metodo que implementa verificacao de estado """
        index = state[0]
        cost = state[1]
        if not isinstance(index, int) or index > len(self.query):
            return False
        if not isinstance(cost, float):
            return False
        return True

    def initialState(self):
        """ Metodo que implementa retorno da posicao inicial """
        cost = self.unigramCost(self.query)
        return (0, cost)

    def actions(self, state):
        """ Metodo que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        index = state[0]
        actions_list = []
        for i in range(index + 1, len(self.query) + 1):
            actions_list.append(str(i))
        return actions_list

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        index = state[0]
        action = int(action)
        cost = self.unigramCost(self.query[index:action])
        return action, cost

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        index = state[0]
        return index >= len(self.query)


    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        return self.nextState(state, action)[1]


def segmentWords(query, unigramCost):

    if len(query) == 0:
        return ''
    
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)

    problem = SegmentationProblem(query, unigramCost)
    goalNode = util.uniformCostSearch(problem)
    valid, solution = util.getSolution(goalNode, problem)

    if valid:
        solution = solution.split(' ')
        answer = ""
        prev = 0
        for index in solution:
            cut = int(index)
            answer += query[prev:cut] + " "
            prev = cut
        return answer[:-1]

    return None

    # END_YOUR_CODE

############################################################
# Part 2: Vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.Problem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def isState(self, state):
        """ Metodo  que implementa verificacao de estado """
        if not isinstance(state[0], str):
            return False
        if not isinstance(state[1], int) or state[1] >= len(self.queryWords):
            return False
        if not isinstance(state[2], int):
            return False
        return True

    def initialState(self):
        """ Metodo  que implementa retorno da posicao inicial """
        return util.SENTENCE_BEGIN, 0, 0

    def actions(self, state):
        """ Metodo  que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        index = state[1] 
        word = self.queryWords[index]
        possible_fills = list(self.possibleFills(word))
        if possible_fills:
            return possible_fills
        return [word]

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        cost = self.bigramCost(state[0], action)
        return action, state[1] + 1, cost

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        index = state[1]
        return index >= len(self.queryWords)

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        return self.nextState(state, action)[2]



def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)

    if len(queryWords) == 0:
        return ''
   
    problem = VowelInsertionProblem(queryWords, bigramCost, possibleFills)
    goal = util.uniformCostSearch(problem)
    valid, solution = util.getSolution(goal, problem)

    if valid:
        return solution

    return None

    # END_YOUR_CODE

############################################################


def getRealCosts(corpus='corpus.txt'):

    """ Retorna as funcoes de custo unigrama, bigrama e possiveis fills obtidas a partir do corpus."""
    
    _realUnigramCost, _realBigramCost, _possibleFills = None, None, None
    if _realUnigramCost is None:
        print('Training language cost functions [corpus: '+ corpus+']... ')
        
        _realUnigramCost, _realBigramCost = util.makeLanguageModels(corpus)
        _possibleFills = util.makeInverseRemovalDictionary(corpus, 'aeiou')

        print('Done!')

    return _realUnigramCost, _realBigramCost, _possibleFills

def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    unigramCost, bigramCost, possibleFills  =  getRealCosts()
    
    resulSegment = segmentWords('believeinyourselfhavefaithinyourabilities', unigramCost)
    print(resulSegment)
    

    resultInsert = insertVowels('smtms ltr bcms nvr'.split(), bigramCost, possibleFills)
    print(resultInsert)

if __name__ == '__main__':
    main()
