from modules import *
import os

arquivo = open('cidades.txt', 'r')
cidades = arquivo.read().splitlines()
arquivo.close()
arquivo_html = montar_html(cidades)
os.system(arquivo_html)
