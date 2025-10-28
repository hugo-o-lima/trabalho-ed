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

@dataclass
class No:
    '''
    Representa um nó da lista encadeada contendo uma figurinha
    e uma referência para o próximo nó.
    '''
    figurinha: Figurinha
    proximo: No | None = None

class Colecao:
    '''
    Coleção de figurinhas implementada com lista encadeada com sentinela.
    A sentinela é um nó especial no início que facilita as operações.
    '''
    sentinela: No
    
    def __init__(self):
        '''
        Inicia uma coleção de figurinhas vazia usando lista encadeada com sentinela.
        A sentinela contém uma Figurinha(0) e aponta para None inicialmente.
        
        Exemplos:
        >>> x = Colecao()
        >>> x.sentinela.figurinha.numero
        0
        >>> x.sentinela.proximo is None
        True
        '''
        self.sentinela = No(Figurinha(0), None)
        self.ultimo_no_encontrado: No | None = None


    def busca_no(self, numero: int) -> No | None:
        '''
        Busca um nó que contenha a figurinha com o número especificado.
        Retorna o nó se encontrado, ou None caso contrário.

        Exemplos:
        >>> c = Colecao()
        >>> c.adiciona_figurinha(Figurinha(5))
        >>> no = c.busca_no(5)
        >>> no.figurinha.numero
        5
        >>> c.busca_no(10) is None
        True
        '''
        atual = self.sentinela.proximo
        
        while atual is not None:
            if atual.figurinha.numero == numero:
                return atual
            atual = atual.proximo
        
        return None

    def adiciona_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Adiciona uma figurinha na coleção. Se a figurinha já existe,
        incrementa sua quantidade. Caso contrário, adiciona um novo nó
        mantendo a ordem crescente dos números.
        
        Exemplos:
        >>> Album = Colecao()
        >>> neymar = Figurinha(4)
        >>> Album.adiciona_figurinha(neymar)
        >>> no = Album.busca_no(4)
        >>> no.figurinha.numero
        4
        >>> no.figurinha.quantidade
        1
        >>> Album.adiciona_figurinha(neymar)
        >>> no = Album.busca_no(4)
        >>> no.figurinha.quantidade
        2
        '''
        no_existente = self.busca_no(figurinha.numero)
        
        if no_existente is not None:
            no_existente.figurinha.quantidade = no_existente.figurinha.quantidade + 1
        else:
            anterior = self.sentinela
            atual = self.sentinela.proximo
            
            while atual is not None and atual.figurinha.numero < figurinha.numero:
                anterior = atual
                atual = atual.proximo
            
            novo_no = No(Figurinha(figurinha.numero, 1), atual)
            anterior.proximo = novo_no

    def remove_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Remove uma figurinha da coleção.
        Se a quantidade for > 1, apenas diminui a quantidade.
        Se a quantidade for 1, remove o nó da lista.
        Se a figurinha não estiver na coleção, não altera nada.
        
        Exemplos:
        >>> copa = Colecao()
        >>> fig1 = Figurinha(1)
        >>> copa.adiciona_figurinha(fig1)
        >>> copa.adiciona_figurinha(fig1)
        >>> no = copa.busca_no(1)
        >>> no.figurinha.quantidade
        2
        >>> copa.remove_figurinha(fig1)
        >>> no = copa.busca_no(1)
        >>> no.figurinha.quantidade
        1
        >>> copa.remove_figurinha(fig1)
        >>> copa.busca_no(1) is None
        True
        '''
        anterior = self.sentinela
        atual = self.sentinela.proximo
        
        while atual is not None:
            if atual.figurinha.numero == figurinha.numero:
                if atual.figurinha.quantidade > 1:
                    atual.figurinha.quantidade = atual.figurinha.quantidade - 1
                else:
                    anterior.proximo = atual.proximo
            anterior = atual
            atual = atual.proximo

    def gera_figurinhas_presentes(self) -> str:
        '''
        Retorna uma string com as figurinhas presentes na coleção.
        
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
        resultado_final = ""
        primeiro_item_encontrado = True
        
        atual = self.sentinela.proximo
        
        while atual is not None:
            numero_str = str(atual.figurinha.numero)
            
            if primeiro_item_encontrado:
                resultado_final = numero_str
                primeiro_item_encontrado = False
            else:
                resultado_final = resultado_final + ", " + numero_str
            
            atual = atual.proximo
        
        return resultado_final

    def gera_figurinhas_repetidas(self) -> str:
        '''
        Retorna uma string com as figurinhas repetidas da coleção.
        
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
        resultado_final = ""
        primeiro_item_encontrado = True
        atual = self.sentinela.proximo
        
        while atual is not None:
            if atual.figurinha.quantidade > 1:
                quant_repetida = atual.figurinha.quantidade - 1
                item_str = str(atual.figurinha.numero) + " (" + str(quant_repetida) + ")"
                
                if primeiro_item_encontrado:
                    resultado_final = item_str
                    primeiro_item_encontrado = False
                else:
                    resultado_final = resultado_final + ", " + item_str
            
            atual = atual.proximo
        
        return resultado_final

    def conta_figurinhas_trocaveis(self, colecao_destino: Colecao) -> int:
        """
        Conta quantas figurinhas repetidas esta coleção possui que a 
        coleção de destino ainda não tem. Uma figurinha é considerada trocável quando está presente nesta coleção 
        com quantidade maior que 1 (repetida) e não está presente na coleção de destino (numero = 0)

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
        quantidade_trocavel = 0
        atual = self.sentinela.proximo
        
        while atual is not None:
            if atual.figurinha.quantidade > 1:
                tem_em_destino = colecao_destino.busca_no(atual.figurinha.numero) is not None
                
                if not tem_em_destino:
                    quantidade_trocavel = quantidade_trocavel + 1
            
            atual = atual.proximo

        return quantidade_trocavel
    
    def encontra_proxima_figurinha_trocavel(self, colecao_destino: Colecao, no_inicial: No | None) -> Figurinha:
        """
        Encontra a próxima figurinha trocável a partir de um índice inicial. Percorre o nó de figurinhas 
        desta coleção começando pelo índice_inicial e retorna a primeira figurinha 
        que atende aos critérios de troca que são quantidade maior que 1 (repetida) e não presente na coleção de destino
        A busca é feita em ordem crescente de número, garantindo que as trocas ocorram respeitando essa ordem.
        Exemplos:
        >>> c1 = Colecao()
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c2 = Colecao()
        >>> c2.adiciona_figurinha(Figurinha(1))
        >>> fig = c1.encontra_proxima_figurinha_trocavel(c2, None)
        >>> fig.numero
        2
        >>> fig2 = c1.encontra_proxima_figurinha_trocavel(c2, c1.ultimo_no_encontrado)
        >>> fig2.numero
        5
        >>> fig3 = c1.encontra_proxima_figurinha_trocavel(c2, c1.ultimo_no_encontrado)
        >>> fig3.numero
        0
        """
        if no_inicial is None:
            atual = self.sentinela.proximo
        else:
            atual = no_inicial.proximo

        figurinha_encontrada = Figurinha(0)
        self.ultimo_no_encontrado = None

        while atual is not None:
            if atual.figurinha.quantidade > 1:
                tem_em_destino = colecao_destino.busca_no(atual.figurinha.numero) is not None

                if not tem_em_destino and figurinha_encontrada.numero == 0:
                    figurinha_encontrada = Figurinha(atual.figurinha.numero)
                    self.ultimo_no_encontrado = atual

            atual = atual.proximo

        return figurinha_encontrada
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
        quantidade_col1_pode_dar = self.conta_figurinhas_trocaveis(colecao2)
        quantidade_col2_pode_dar = colecao2.conta_figurinhas_trocaveis(self)
        
        numero_de_trocas = min(quantidade_col1_pode_dar, quantidade_col2_pode_dar)
        
        trocas_realizadas = 0
        no_col1 = None
        no_col2 = None
        
        while trocas_realizadas < numero_de_trocas:
            figurinha_para_col2 = self.encontra_proxima_figurinha_trocavel(colecao2, no_col1)
            no_col1 = self.ultimo_no_encontrado
            
            figurinha_para_col1 = colecao2.encontra_proxima_figurinha_trocavel(self, no_col2)
            no_col2 = colecao2.ultimo_no_encontrado
            
            if figurinha_para_col2.numero != 0 and figurinha_para_col1.numero != 0:
                self.remove_figurinha(figurinha_para_col2)
                colecao2.adiciona_figurinha(figurinha_para_col2)
                
                colecao2.remove_figurinha(figurinha_para_col1)
                self.adiciona_figurinha(figurinha_para_col1)
                
                trocas_realizadas = trocas_realizadas + 1