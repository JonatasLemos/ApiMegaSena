import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()
from django.forms import model_to_dict
from megasena.models import SorteioMegaSena, NovoJogo
from django.contrib.auth.models import User


class Jogo:
    min = 1
    max = 60
    range_values = range(min, max + 1)
    dezenas_mega_sena = [f'dezena{i}' for i in range(1,7)]
    ultimo_sorteio = SorteioMegaSena.objects.order_by("-date").values_list(*dezenas_mega_sena)[0]

    # Pelo menos 6 dezenas
    def __init__(self, dezenas):
        self.dezenas = dezenas
        self.sorteio_usuario = random.sample(Jogo.range_values, dezenas)
        self.acertos = self.compare_game_megasena()
        self.insert_novo_jogo()

    def compare_game_megasena(self):
        sorteio_usuario = set(self.sorteio_usuario)
        ultimo_sorteio = set(Jogo.ultimo_sorteio)
        dezenas_certas = ultimo_sorteio.intersection(sorteio_usuario)
        # ultimo_sorteio = list(ultimo_sorteio)
        # sorteio_usuario = list(sorteio_usuario)
        # ultimo_sorteio.sort()
        # sorteio_usuario.sort()
        # print(list(ultimo_sorteio))
        # print(list(sorteio_usuario))
        # print(len(dezenas_certas))
        return len(dezenas_certas)

    def insert_novo_jogo(self):
        novo_jogo = {f'dezena{str(i + 1)}': self.sorteio_usuario[i] for i in range(self.dezenas)}
        novo_jogo["dezenas"] = self.dezenas
        novo_jogo["acertos"] = self.acertos
        novo_jogo["user"] = User.objects.first()
        jogo = NovoJogo(**novo_jogo)
        jogo.save()

