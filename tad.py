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
    figurinhas: array[Figurinha]
    figurinhas_repetidas: array[int]
    
    def __init__(self):
        '''
        Inicia uma coleção de figurinhas com 15 espaços, sendo que é inicializado com todas valendo 0,
        onde 0 significa vazio
        
        Exemplos:
        >>> x = Colecao()
        >>> len(x.figurinhas)
        15
        >>> len(x.figurinhas_repetidas)
        15
        '''
        self.figurinhas = array(15, Figurinha(0))
        self.figurinhas_repetidas = array(15, 0)
    
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
        if figurinha.numero >= len(self.figurinhas):
            tamanho_novo = figurinha.numero + 10
            novo_figurinhas = array(tamanho_novo, Figurinha(0))
            novo_repetidas = array(tamanho_novo, 0)
            for i in range(len(self.figurinhas)):
                novo_figurinhas[i] = self.figurinhas[i]
                novo_repetidas[i] = self.figurinhas_repetidas[i]
            self.figurinhas = novo_figurinhas
            self.figurinhas_repetidas = novo_repetidas
        
        if self.figurinhas[figurinha.numero].numero == 0:
            self.figurinhas[figurinha.numero] = figurinha
        else:
            self.figurinhas_repetidas[figurinha.numero] = self.figurinhas_repetidas[figurinha.numero] + 1
    
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
        >>> copa.figurinhas[1].numero
        0
        '''
        if figurinha.numero >= len(self.figurinhas):
            return
        
        if self.figurinhas[figurinha.numero].numero == 0:
            return
        
        if self.figurinhas_repetidas[figurinha.numero] > 0:
            self.figurinhas_repetidas[figurinha.numero] = self.figurinhas_repetidas[figurinha.numero] - 1
        else:
            self.figurinhas[figurinha.numero] = Figurinha(0)
    
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
        resultado = ''
        for i in range(len(self.figurinhas)):
            if self.figurinhas[i].numero != 0:
                if resultado != '':
                    resultado = resultado + ', '
                resultado = resultado + str(i)
        return resultado
    
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
        ''
        '''
        resultado = ''
        for i in range(len(self.figurinhas_repetidas)):
            if self.figurinhas_repetidas[i] > 0:
                if resultado != '':
                    resultado = resultado + ', '
                resultado = resultado + str(i) + '(' + str(self.figurinhas_repetidas[i]) + ')'
        return resultado

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
        >>> Colecao.troca_maxima(c1, c2)
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
        tamanho_max = len(colecao1.figurinhas)
        if len(colecao2.figurinhas) > tamanho_max:
            tamanho_max = len(colecao2.figurinhas)
        
        for i in range(tamanho_max):
            if i < len(colecao1.figurinhas):
                if colecao1.figurinhas_repetidas[i] > 0:
                    if i < len(colecao2.figurinhas) and colecao2.figurinhas[i].numero == 0:
                        fig = Figurinha(i)
                        colecao1.remove_figurinha(fig)
                        colecao2.adiciona_figurinha(fig)
            
            if i < len(colecao2.figurinhas):
                if colecao2.figurinhas_repetidas[i] > 0:
                    if i < len(colecao1.figurinhas) and colecao1.figurinhas[i].numero == 0:
                        fig = Figurinha(i)
                        colecao2.remove_figurinha(fig)
                        colecao1.adiciona_figurinha(fig)