from django.contrib import admin
from megasena.models import SorteioMegaSena,NovoJogo

class MegaSenaList(admin.ModelAdmin):
    list_display = ('id', 'dezena1', 'date')
    # list_display_links = ('id','artist','album')
    # search_fields = ('artist','album')
    list_filter = ('id',)
    list_per_page = 10

admin.site.register(SorteioMegaSena,MegaSenaList)

class NovoJogoList(admin.ModelAdmin):
    list_display = ('id','user','acertos','dezenas')
    list_filter = ('id',)
    list_per_page = 10

admin.site.register(NovoJogo,NovoJogoList)