from __future__ import annotations
from dataclasses import dataclass
from ed import array

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
    figurinhas: array[Figurinha]
    
    def __init__(self):
        '''
        Cria uma coleção começando com 15 espaços vazios (todos com numero 0).
        
        Exemplos:
        >>> x = Colecao()
        >>> len(x.figurinhas)
        15
        '''
        self.figurinhas = array(15, Figurinha(0))

    def redimensiona(self, tamanho_necessario: int) -> None:
        '''
        Aumenta o tamanho do array quando precisamos adicionar uma figurinha
        com numero maior do que o tamanho atual.
        '''
        tamanho_atual = len(self.figurinhas)

        if tamanho_necessario > tamanho_atual:
            novo_tamanho = tamanho_atual

            if novo_tamanho == 0:
                novo_tamanho = 15

            while tamanho_necessario > novo_tamanho:
                novo_tamanho = novo_tamanho * 2

            novas_figurinhas = array(novo_tamanho, Figurinha(0))

            for i in range(tamanho_atual):
                novas_figurinhas[i] = self.figurinhas[i]

            self.figurinhas = novas_figurinhas

    def adiciona_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Adiciona uma figurinha na colecao. Se ja tiver essa figurinha,
        apenas aumenta a quantidade. Se o album estiver pequeno, aumenta o tamanho.
        
        Exemplos:
        Exemplos:
        >>> Album = Colecao()
        >>> neymar = Figurinha(4)
        >>> Album.adiciona_figurinha(neymar)
        >>> Album.adiciona_figurinha(neymar)
        >>> ronaldo = Figurinha(20)
        >>> Album.adiciona_figurinha(ronaldo)
        >>> Album.gera_figurinhas_presentes()
        '4, 20'
        '''
        num = figurinha.numero
        tamanho_necessario = num + 1
        
        if tamanho_necessario > len(self.figurinhas):
            self.redimensiona(tamanho_necessario)

        if self.figurinhas[num].numero == 0:
            self.figurinhas[num] = Figurinha(num, 1)
        else:
            self.figurinhas[num].quantidade = self.figurinhas[num].quantidade + 1

    def remove_figurinha(self, figurinha: Figurinha) -> None:
        '''
        Remove uma figurinha da colecao. Se tiver mais de uma, só diminui
        a quantidade. Se tiver apenas uma, remove completamente (vira Figurinha(0)).
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
        if figurinha.numero < len(self.figurinhas):
            item_album = self.figurinhas[figurinha.numero]

            if item_album.numero != 0:
                if item_album.quantidade > 1:
                    item_album.quantidade = item_album.quantidade - 1
                else:
                    self.figurinhas[figurinha.numero] = Figurinha(0)
                return
        
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
            resultado_final = ""
            primeiro_item_encontrado = True
            
            for i in range(len(self.figurinhas)):
                item_album = self.figurinhas[i]
                
                if item_album.numero != 0:
                    numero_str = str(item_album.numero)
                    
                    if primeiro_item_encontrado:
                        resultado_final = numero_str
                        primeiro_item_encontrado = False
                    else:
                        resultado_final = resultado_final + ", " + numero_str
                    
            return resultado_final

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
        resultado_final = ""
        primeiro_item_encontrado = True

        for i in range(len(self.figurinhas)):
            item_album = self.figurinhas[i]
            
            if item_album.numero != 0 and item_album.quantidade > 1:
                
                quant_repetida = item_album.quantidade - 1
                
                item_str = str(item_album.numero) + " (" + str(quant_repetida) + ")"

                if primeiro_item_encontrado:
                    resultado_final = item_str
                    primeiro_item_encontrado = False
                else:
                    resultado_final = resultado_final + ", " + item_str
        
        return resultado_final

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
        quantidade_trocavel = 0
        
        for i in range(len(self.figurinhas)):
            figurinha_origem = self.figurinhas[i]
            
            if figurinha_origem.numero != 0 and figurinha_origem.quantidade > 1:
                tem_em_destino = False
                if figurinha_origem.numero < len(colecao_destino.figurinhas):
                    if colecao_destino.figurinhas[figurinha_origem.numero].numero != 0:
                        tem_em_destino = True
                
                if not tem_em_destino:
                    quantidade_trocavel = quantidade_trocavel + 1
        
        return quantidade_trocavel

    def encontra_proxima_figurinha_trocavel(self, colecao_destino: Colecao, indice_inicial: int) -> Figurinha:
        """
        Procura a proxima figurinha que da pra trocar, comecando de um indice.
        Retorna a primeira figurinha repetida que o outro nao tem.
        
        Exemplos:
        >>> c1 = Colecao()
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(2))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c1.adiciona_figurinha(Figurinha(5))
        >>> c2 = Colecao()
        >>> c2.adiciona_figurinha(Figurinha(1))
        >>> fig = c1.encontra_proxima_figurinha_trocavel(c2, 0)
        >>> fig.numero
        2
        >>> fig2 = c1.encontra_proxima_figurinha_trocavel(c2, 3)
        >>> fig2.numero
        5
        >>> fig3 = c1.encontra_proxima_figurinha_trocavel(c2, 6)
        >>> fig3.numero
        0
        """
        indice_atual = indice_inicial
        figurinha_encontrada = Figurinha(0)
        
        while indice_atual < len(self.figurinhas) and figurinha_encontrada.numero == 0:
            fig = self.figurinhas[indice_atual]
            
            if fig.numero != 0 and fig.quantidade > 1:
                tem_em_destino = False
                if fig.numero < len(colecao_destino.figurinhas):
                    if colecao_destino.figurinhas[fig.numero].numero != 0:
                        tem_em_destino = True
                
                if not tem_em_destino:
                    figurinha_encontrada = Figurinha(fig.numero)
            
            indice_atual = indice_atual + 1
        
        return figurinha_encontrada

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
        quantidade_col1_pode_dar = self.conta_figurinhas_trocaveis(colecao2)
        quantidade_col2_pode_dar = colecao2.conta_figurinhas_trocaveis(self)
        numero_de_trocas = min(quantidade_col1_pode_dar, quantidade_col2_pode_dar)
        
        trocas_realizadas = 0
        indice_col1 = 0
        indice_col2 = 0
        continuar = True
        
        while trocas_realizadas < numero_de_trocas and continuar:
            figurinha_para_col2 = self.encontra_proxima_figurinha_trocavel(colecao2, indice_col1)
            figurinha_para_col1 = colecao2.encontra_proxima_figurinha_trocavel(self, indice_col2)
            
            if figurinha_para_col2.numero != 0 and figurinha_para_col1.numero != 0:
                self.remove_figurinha(figurinha_para_col2)
                colecao2.adiciona_figurinha(figurinha_para_col2)
                
                colecao2.remove_figurinha(figurinha_para_col1)
                self.adiciona_figurinha(figurinha_para_col1)
                
                trocas_realizadas += 1
                indice_col1 = figurinha_para_col2.numero + 1
                indice_col2 = figurinha_para_col1.numero + 1
            else:
                continuar = False