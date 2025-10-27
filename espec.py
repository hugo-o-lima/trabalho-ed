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
from __future__ import annotations
from dataclasses import dataclass
from ed import array


@dataclass
class Figurinha:
    '''
    Representa uma figurinha com um número identificador.
    
    Exemplos:
    >>> messi = Figurinha(1)
    >>> messi
    Figurinha(numero=1)
    >>> neymar = Figurinha(10)
    >>> neymar.numero
    10
    '''
    numero: int


class Colecao:
    
    def __init__(self):
        '''
        Inicia uma coleção de figurinhas com 15 espaços, sendo que é inicializado com todas valendo 0,
        ou seja vazias
        
        Exemplos:
        >>> x = Colecao()
        >>> len(x.figurinhas)
        15
        >>> len(x.figurinhas_repetidas)
        15
        '''
    
    def adiciona_figurinha(self, figurinha: Figurinha):
        '''
        Adiciona uma *figurinha* na colecao. Se o tamanho do album estiver pequeno, aloca mais espaço
        tanto para o album como para o bolo de repetidas como forma de prevenção
        
        Exemplos:
        >>> Copa2014 = Colecao()
        >>> neymar = Figurinha(2)
        >>> Copa2014.adiciona_figurinha(neymar)
        >>> Copa2014.figurinhas[2].numero
        2
        >>> Copa2014.adiciona_figurinha(neymar)
        >>> Copa2014.figurinhas_repetidas[2]
        1
        '''

    def remove_figurinha(self, figurinha: Figurinha):
        '''
        Remove uma *figurinha* da coleção se não houver nenhuma repetida.
        Havendo repetida, remove do bolo de repetidas.
        Se a figurinha nao estiver contida em *self* nao altera nada
        
        Exemplos:
        >>> copa = Colecao()
        >>> fig1 = Figurinha(1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.figurinhas_repetidas[1]
        1
        >>> copa.remove_figurinha(fig1)
        >>> copa.figurinhas_repetidas[1]
        0
        >>> copa.remove_figurinha(fig1)
        >>> copa.figurinhas[1]
        0
        '''

    def gera_figurinhas_presentes(self) -> str:
        '''
        Retorna uma string com as figurinhas presentes na colecao
        
        Exemplos:
        >>> copa = Colecao()
        >>> copa.adiciona_figurinha(Figurinha(1))
        >>> copa.adiciona_figurinha(Figurinha(3))
        >>> copa.adiciona_figurinha(Figurinha(5))
        >>> copa.gera_figurinhas_presentes()
        '1, 3, 5'
        >>> vazia = Colecao()
        >>> vazia.gera_figurinhas_presentes()
        ''
        '''
        return ''
    def gera_figurinhas_repetidas(self) -> str:
        '''
        Retorna uma string com as figurinhas repetidas de uma colecao
        
        Exemplos:
        >>> copa = Colecao()
        >>> fig1 = Figurinha(1)
        >>> fig2 = Figurinha(2)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig2)
        >>> copa.adiciona_figurinha(fig2)
        >>> copa.gera_figurinhas_repetidas()
        '1(2), 2(1)'
        >>> vazia = Colecao()
        >>> vazia.gera_figurinhas_repetidas()
        '''
        return ''

    def troca_maxima(colecao1: Colecao, colecao2: Colecao):
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
        
        Exemplos:
        --------
        >>> c1 = Colecao()
        >>> c2 = Colecao()
        >>> c1.adiciona_figurinha(Figurinha(1))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(3))
        >>> c1.adiciona_figurinha(Figurinha(3))
        >>> c2.adiciona_figurinha(Figurinha(4))
        >>> c2.adiciona_figurinha(Figurinha(5))
        >>> c2.adiciona_figurinha(Figurinha(5))
        >>> c2.adiciona_figurinha(Figurinha(6))
        >>> c2.adiciona_figurinha(Figurinha(6))
        >>> troca_maxima(c1, c2)
        >>> c1.gera_figurinhas_presentes()
        '1, 2, 3, 5, 6'
        >>> c2.gera_figurinhas_presentes()
        '2, 3, 4, 5, 6'
        
        Observações:
        ------------
        - A troca só ocorre se houver interesse mútuo: cada um deve ter algo que o outro queira.
        - As figurinhas são transferidas na ordem crescente de número.
        - Apenas figurinhas **repetidas** podem ser trocadas.
        - Não é retornado nenhum valor; o efeito é direto nas coleções.
        """