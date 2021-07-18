import random
from datetime import datetime,timedelta
import pytz
tz = pytz.timezone('America/Sao_Paulo')
min = 0
max = 60
range_values = range(min, max + 1)
sorteio = random.sample(range_values, 6)
random_dates = [datetime.now(tz) - random.random() * timedelta(days=7) for i in range(3)]
instances = []
for i in range(3):
    instance = {f'dezena{str(j + 1)}': sorteio[j] for j in range(6)}
    instance["date"] = random_dates[i]
    instances.append(instance)
# NovoJogo model additional values
additional_values = {
    "dezenas":8,
    "acertos":4,
    "dezena7":9,
    "dezena8":12
}