import os
import pytz
import cfscrape
import urllib
import bs4
from datetime import datetime,timedelta

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from megasena.models import SorteioMegaSena

def check_new_megasena_draw():
    tz = pytz.timezone('America/Sao_Paulo')
    current_time = datetime.now(tz)
    if SorteioMegaSena.objects.count() == 0:
        return True
    last_draw = SorteioMegaSena.objects.all().order_by("date").last().date
    list = SorteioMegaSena.objects.all()
    for i in list:
        print(i.date)
    last_draw_weekday = last_draw.weekday()
    print(last_draw.tzinfo)
    print(last_draw)
    print(current_time)
    time_delta = current_time - last_draw
    print(time_delta)
    if time_delta < timedelta(days=3):
        return False
    if time_delta < timedelta(days=4):
        if last_draw_weekday == 5:
            return False
    return True

def update_last_draw():
    if check_new_megasena_draw():
        query = urllib.parse.quote_plus("caixa mega sena")
        url = "https://www.google.com/search?q=" + query

        scraper = cfscrape.create_scraper()
        response = scraper.get(url)

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        spans = soup.findAll('span', class_="zSMazd UHlKbe")

        mega_sena_hour = "20:00:00 GMT-0300"
        span_str = soup.find('span',class_="qLLird").get_text()
        date_str = span_str.split()[2][1:-1]+" "+mega_sena_hour

        date = datetime.strptime(date_str,'%d/%m/%y %H:%M:%S GMT%z')
        last_draw = SorteioMegaSena.objects.order_by("-date").last()
        if last_draw == date:
            return False
        else:
            dezenas = [span.get_text() for span in spans]
            data_instance = {f'dezena{str(i + 1)}': int(dezenas[i]) for i in range(len(dezenas))}
            print(data_instance)
            data_instance["date"] = date

            sorteio1 = SorteioMegaSena(**data_instance)
            sorteio1.save()
            return True

update_last_draw()