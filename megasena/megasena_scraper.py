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

class MegaSenaDraw:
    tz = pytz.timezone('America/Sao_Paulo')
    def __init__(self):
        self.__current_time = datetime.now(MegaSenaDraw.tz)
        self.__count_draws = SorteioMegaSena.objects.count()
        self.__last_draw = SorteioMegaSena.objects.order_by("date").last().date
        self.runScraper = self.check_new_megasena_draw()
        self.update_last_draw()

    def update_last_draw(self):
        if self.runScraper:
            web_scraper = WebScraper()
            date = web_scraper.date
            if self.__last_draw != date:
                dezenas = web_scraper.dezenas
                data_instance = {f'dezena{str(i + 1)}': int(dezenas[i]) for i in range(len(dezenas))}
                data_instance["date"] = date
                sorteio1 = SorteioMegaSena(**data_instance)
                sorteio1.save()

    def check_new_megasena_draw(self):
        if self.__count_draws == 0:
            return True
        last_draw_weekday = self.__last_draw.weekday()
        time_delta = self.__current_time - self.__last_draw
        if time_delta < timedelta(days=3):
            return False
        if time_delta < timedelta(days=4):
            if last_draw_weekday == 5:
                return False
        return True

class WebScraper:
    query = urllib.parse.quote_plus("caixa mega sena")
    url = "https://www.google.com/search?q=" + query
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    def __init__(self):
        self.__soup = bs4.BeautifulSoup(WebScraper.response.text, "html.parser")

    @property
    def date(self):
        mega_sena_hour = "20:00:00 GMT-0300"
        span_str = self.__soup.find('span', class_="qLLird").get_text()
        date_str = span_str.split()[2][1:-1] + " " + mega_sena_hour
        return datetime.strptime(date_str, '%d/%m/%y %H:%M:%S GMT%z')

    @property
    def dezenas(self):
        spans = self.__soup.findAll('span', class_="zSMazd UHlKbe")
        return [span.get_text() for span in spans]
