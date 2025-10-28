from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Figurinha:
    '''
    Representa uma figurinha com um número identificador e sua quantidade.
    
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

    def __init__(self) -> None:
        '''
        Inicializa uma nova coleção de figurinhas, inicialmente vazia.
        '''
        pass

    def adiciona_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Adiciona uma figurinha à coleção.
        
        Se a figurinha (identificada pelo numero) já existir na coleção, 
        sua quantidade deve ser incrementada em 1.
        Se a figurinha não existir, ela deve ser adicionada à coleção
        com quantidade 1, mantendo a ordem numérica crescente.
        '''

    def remove_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Remove uma unidade da figurinha (identificada pelo numero) da coleção.
        Se a figurinha existir e sua quantidade for > 1, sua quantidade
        diminui em 1.
        Se a figurinha existir e sua quantidade for 1, a figurinha é removida.
        Se a figurinha não existir na coleção, não acontece nada
        '''

    def gera_figurinhas_presentes(self) -> str:
        '''
        Retorna uma string com os números de todas as figurinhas presentes
        na coleção, ou seja, com quantidade >= 1.
        Os números devem estar em ordem crescente.
        Os números devem ser separados por ", " (vírgula e espaço).
        Se a coleção estiver vazia, retorna uma string vazia "".
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
        Retorna uma string com as figurinhas que estão repetidas na coleção, ou seja,
        com quantidade > 1.
        O formato para cada figurinha repetida é: "NUMERO (REPETIDAS)",
        onde REPETIDAS é a quantidade - 1.
        As figurinhas devem ser listadas em ordem crescente de NÚMERO.
        Os itens devem ser separados por ", " (vírgula e espaço).
        Se não houver figurinhas repetidas, retorna uma string vazia "".
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
        '''
        Conta quantas figurinhas repetidas esta coleção possui que a 
        coleção de destino ainda não tem. Uma figurinha é considerada trocável quando está presente nesta coleção 
        com quantidade maior que 1 (repetida) e não está presente na coleção de destino.        
        Retorna o número total de figurinhas (tipos únicos) que atendem a esses critérios.
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
        '''
        return 0
    
    def encontra_proxima_figurinha_trocavel(self, colecao_destino: Colecao, indice_inicial: int) -> Figurinha:
        """
        Encontra a próxima figurinha trocável a partir de um índice inicial. Percorre as figurinhas 
        desta coleção começando pelo índice_inicial e retorna a primeira figurinha 
        que atende aos critérios de troca que são quantidade maior que 1 (repetida) e não presente na coleção de destino
        A busca é feita em ordem crescente de número, garantindo que as trocas ocorram respeitando essa ordem.
        """
        return Figurinha(0)

    def troca_maxima(self, colecao2: Colecao) -> None:
        """
        Realiza a troca máxima de figurinhas entre duas coleções.
        Para cada par de coleções:
        A função identifica figurinhas repetidas que cada coleção tem
        e que a outra ainda não possui no álbum.
        Em seguida, realiza a troca dessas figurinhas, respeitando o limite
        do número de figurinhas repetidas disponíveis e da quantidade de figurinhas
        que o outro ainda não tem.
        O número de trocas é limitado ao mínimo entre a quantidade de figurinhas
        possíveis de enviar por uma e a quantidade possíveis de receber da outra.
        A troca ocorre em ordem crescente do número da figurinha.
        - A troca só ocorre se houver interesse mútuo: cada um deve ter algo que o outro queira.
        - As figurinhas são transferidas na ordem crescente de número.
        - Apenas figurinhas **repetidas** podem ser trocadas.
        - Não é retornado nenhum valor; o efeito é direto nas coleções.
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