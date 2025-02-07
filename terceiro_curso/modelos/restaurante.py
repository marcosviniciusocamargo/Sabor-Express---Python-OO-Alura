from .cardapio.item_cardapio import ItemCardapio
from terceiro_curso.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome:'.ljust(25)} | {'Categoria:'.ljust(25)} | {'Avaliacao:'.ljust(25)} | {'Ativo:'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'

        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas,1)
        return media

    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print (f'Cardapio do Restaurante: {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}')
            else:
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}')

