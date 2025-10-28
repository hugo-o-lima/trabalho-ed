from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Figurinha:
    '''
    Uma figurinha tem um numero e uma quantidade.
    Por padrão, quando criamos uma figurinha nova, ela tem quantidade 1.
    
    Exemplos:
    >>> messi = Figurinha(1)
    >>> messi
    Figurinha(numero=1, quantidade=1)
    >>> neymar = Figurinha(10)
    >>> neymar.numero
    10
    >>> neymar.quantidade
    1
    '''
    numero: int
    quantidade: int = 1

class Colecao:
    '''
    Uma colecao de figurinhas.
    '''
    
    def __init__(self):
        '''
        Cria uma colecao vazia.
        
        Exemplos:
        >>> x = Colecao()
        '''

    def adiciona_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Adiciona uma figurinha na colecao. Se ja tiver essa figurinha,
        apenas aumenta a quantidade.
        
        Exemplos:
        >>> Album = Colecao()
        >>> neymar = Figurinha(4)
        >>> Album.adiciona_figurinha(neymar)
        >>> Album.adiciona_figurinha(neymar)
        >>> ronaldo = Figurinha(20)
        >>> Album.adiciona_figurinha(ronaldo)
        >>> copa.gera_figurinhas_presentes()
        '4, 20'
        '''

    def remove_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Remove uma figurinha da colecao. Se tiver mais de uma, so diminui
        a quantidade. Se tiver apenas uma, remove completamente.
        Se nao tiver a figurinha, nao faz nada.
        
        Exemplos:
        >>> copa = Colecao()
        >>> fig1 = Figurinha(1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.remove_figurinha(fig1)
        >>> copa.remove_figurinha(fig1)
        >>> copa.gera_figurinhas_presentes()
        ''
        '''

    def gera_figurinhas_presentes(self) -> str:
        '''
        Retorna uma string com os numeros das figurinhas que tem na colecao.
        
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
        Retorna uma string com as figurinhas repetidas, mostrando quantas
        a mais cada uma tem.
        
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
        '1 (2), 2 (1)'
        >>> vazia = Colecao()
        >>> vazia.gera_figurinhas_repetidas()
        ''
        '''
        return ''

    def conta_figurinhas_trocaveis(self, colecao_destino: Colecao) -> int:
        """
        Conta quantas figurinhas repetidas eu tenho que a outra pessoa nao tem.
        So da pra trocar se eu tiver repetida e o outro nao tiver nenhuma.
        
        Exemplos:
        >>> c1 = Colecao()
        >>> c1.adiciona_figurinha(Figurinha(1))
        >>> c1.adiciona_figurinha(Figurinha(1))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c2 = Colecao()
        >>> c2.adiciona_figurinha(Figurinha(1))
        >>> c2.adiciona_figurinha(Figurinha(3))
        >>> c1.conta_figurinhas_trocaveis(c2)
        1
        >>> c2.conta_figurinhas_trocaveis(c1)
        0
        """
        return 0

    def encontra_proxima_figurinha_trocavel(self, colecao_destino: Colecao, posicao_inicial) -> Figurinha:
        """
        Procura a proxima figurinha que da pra trocar, comecando de uma posicao.
        Retorna a primeira figurinha repetida que o outro nao tem.
        
        Exemplos:
        >>> c1 = Colecao()
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c2 = Colecao()
        >>> c2.adiciona_figurinha(Figurinha(1))
        >>> fig = c1.encontra_proxima_figurinha_trocavel(c2, inicio)
        >>> fig.numero
        2
        >>> fig2 = c1.encontra_proxima_figurinha_trocavel(c2, proxima)
        >>> fig2.numero
        5
        >>> fig3 = c1.encontra_proxima_figurinha_trocavel(c2, apos_todas)
        >>> fig3.numero
        0
        """
        return Figurinha(0)

    def troca_maxima(self, colecao2: Colecao) -> None:
        """
        Faz a troca de figurinhas entre duas colecoes. Cada um da figurinhas
        repetidas que tem e que o outro ainda nao tem. A troca so acontece
        se os dois tiverem algo pra trocar (interesse mutuo). As trocas sao
        feitas em ordem crescente de numero.
        
        Exemplos:
        >>> c = Colecao()
        >>> c.adiciona_figurinha(Figurinha(2))
        >>> c.adiciona_figurinha(Figurinha(2))
        >>> c.adiciona_figurinha(Figurinha(4))
        >>> c.adiciona_figurinha(Figurinha(4))
        >>> c.adiciona_figurinha(Figurinha(7))
        >>> c.adiciona_figurinha(Figurinha(7))
        >>> c.adiciona_figurinha(Figurinha(1))
        >>> c.adiciona_figurinha(Figurinha(1))
        >>> d = Colecao()
        >>> d.adiciona_figurinha(Figurinha(2))
        >>> d.adiciona_figurinha(Figurinha(6))
        >>> d.adiciona_figurinha(Figurinha(6))
        >>> d.adiciona_figurinha(Figurinha(8))
        >>> d.adiciona_figurinha(Figurinha(8))
        >>> d.adiciona_figurinha(Figurinha(10))
        >>> d.adiciona_figurinha(Figurinha(10))
        >>> c.troca_maxima(d)
        >>> c.gera_figurinhas_presentes()
        '1, 2, 4, 6, 7, 8, 10'
        >>> c.gera_figurinhas_repetidas()
        '2 (1)'
        >>> d.gera_figurinhas_presentes()
        '1, 2, 4, 6, 7, 8, 10'
        >>> d.gera_figurinhas_repetidas()
        ''
        """
