import random
from django.contrib.auth.models import User
from megasena.models import SorteioMegaSena, NovoJogo

class Jogo:
    """Criar um jogo randomico com input de dezenas"""
    min = 1
    max = 60
    range_values = range(min, max + 1)
    dezenas_mega_sena = [f'dezena{i}' for i in range(1,7)]
    ultimo_sorteio = SorteioMegaSena.objects.order_by("-date").values_list(*dezenas_mega_sena)[0]

    def __init__(self, dezenas,usuario):
        self.dezenas = dezenas
        self.usuario = usuario
        self.sorteio_usuario = random.sample(Jogo.range_values, dezenas)
        self.acertos = self.compare_game_megasena()
        self.insert_novo_jogo()

    def compare_game_megasena(self):
        """Comparar jogo randomico com ultimo sorteio da Megasena"""
        sorteio_usuario = set(self.sorteio_usuario)
        ultimo_sorteio = set(Jogo.ultimo_sorteio)
        dezenas_certas = ultimo_sorteio.intersection(sorteio_usuario)
        return len(dezenas_certas)

    def insert_novo_jogo(self):
        """Criar model instance NovoJogo com jogo randomico"""
        novo_jogo = {f'dezena{str(i + 1)}': self.sorteio_usuario[i] for i in range(self.dezenas)}
        novo_jogo["dezenas"] = self.dezenas
        novo_jogo["acertos"] = self.acertos
        novo_jogo["user"] = self.usuario
        jogo = NovoJogo(**novo_jogo)
        jogo.save()
