'''
Você sabe que chegar nesse resultado pode levar um tempo, mas você também sabe que é possível começar fazendo as
estruturas e operações básicas que serão necessárias para manter as coleções. Como as figurinhas são enumeradas (1,
2, 3, ...), o seu trabalho é manter uma coleção ordenada de números, com o detalhe de que cada número pode aparecer
mais que uma vez na coleção (figurinhas repetidas).
Para uma coleção você identificou as seguintes operações:
• Criação de uma coleção com a quantidade de figurinhas (número de figurinhas total do álbum)
• Inserção de uma figurinha
• Remoção de uma figurinha
• Geração de uma string com as figurinhas presentes sem considerar as repetições (ex “[4, 10, 25]”)
• Geração de uma string com as figurinhas repetidas (ex “[12 (1), 60 (2)]”, 1 repetida da 12 e 2 repetidas da 60)
• Troca máxima entre duas coleções (Suponha que o programa identificou duas pessoas para fazerem a troca de
figurinhas, a primeiro tem 6 figurinhas repetidas que a segunda não tem e a segunda tem 8 figurinhas repetidas
que a primeira não tem. Então, essa operação tem que transferir 6 figurinhas da primeira para a segunda pessoa
e 6 figurinhas da segunda para a primeira. As figurinhas que serão transferidas são escolhidas por ordem).
Agora você precisa trabalhar!
1) Faça a especificação de um TAD para representar coleções de figurinhas com as operações identificadas acima.
2) Faça uma implementação usando arranjo estático.
3) Faça uma implementação usando encadeamento.
Note que você não deve alocar todo o espaço para as figurinhas no construtor.
'''

from dataclasses import dataclass
from tad_ed import array
from __future__ import annotations

class Figurinha:
    '''
    >>> messi = Figurinha(1)
    >>> messi
    Figurinha(numero=1) 
    '''
    numero: int

class Colecao:
    figurinhas = array[Figurinha]
    figurinhas_repetidas = array[int]

    def __init__(self):
        '''
        Inicia uma coleção de figurinhas com 15 espaços, sendo que é inicializado com todas valendo 0,
        ou seja vazias
        >>> x = Colecao()
        '''

    def adiciona_figurinha(self, figurinha: Figurinha):
        '''
        Adiciona uma *figurinha* na colecao. Se o tamanho do album estiver pequeno,aloca mais espaço
        tanto para o album como para o bolo de repetidas como forma de prevenção 

        Exemplos:

        >>> Copa2014 = Colecao()
        >>> neymar = Figurinha(2)
        >>> Copa2014.adiciona(neymar)            
        '''

    def remove (self, figurinha:Figurinha):
        '''
        Remove uma *figurinha* da coleção se não houver nenhuma repetida.
        Havendo repetida,remove do bolo de respetidas.
        Se a figurinha nao estiver contida em *self* nao altera nada 
        '''

    def gera_figurinhas_presentes(self) -> str:
        '''
        Retorna uma string com as figurinhas presentes na colecao
        '''
        return ''

    def gera_figurinhas_repetidas(self) -> str:
        '''
        Retorna uma string com as figurinhas repetidas de uma colecao
        '''
        return ''
    
    def troca_maxima(colecao1: Colecao, colecao2: Colecao) -> None:
        """
        Realiza a troca máxima de figurinhas entre duas coleções.

        Para cada par de coleções:
        - A função identifica figurinhas repetidas que cada coleção tem
        e que a outra ainda não possui no álbum.
        - Em seguida, realiza a troca dessas figurinhas, respeitando o limite
        do número de figurinhas repetidas disponíveis e da quantidade de figurinhas
        que o outro ainda não tem.
        - O número de trocas é limitado ao mínimo entre a quantidade de figurinhas
        possíveis de enviar por uma e a quantidade possíveis de receber da outra.
        - A troca ocorre em ordem crescente do número da figurinha.

        Parâmetros:
        -----------
        colecao1 : Colecao
            Primeira coleção envolvida na troca.
        colecao2 : Colecao
            Segunda coleção envolvida na troca.

        Efeitos Colaterais:
        -------------------
        Modifica as duas coleções, adicionando e removendo figurinhas conforme a troca.

        Exemplo:
        --------
        Suponha:
        - colecao1 tem as figurinhas 1, 2, 3, 3, 4, 4, 5
        - colecao2 tem as figurinhas 4, 5, 6, 6, 7, 7, 8, 8

        Após a troca máxima:
        - colecao1 recebe 6, 7, 8
        - colecao2 recebe 3, 4, 5

        Observações:
        ------------
        - A troca só ocorre se houver interesse mútuo: cada um deve ter algo que o outro queira.
        - As figurinhas são transferidas na ordem crescente de número.
        - Apenas figurinhas **repetidas** podem ser trocadas.
        - Não é retornado nenhum valor; o efeito é direto nas coleções.
        """