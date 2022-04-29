import json
import subprocess, sys, os
import datetime


# Envio de uma midia
# userMedia = input('▲ Media url? %s')
# subprocess.run('wp media import %s' % userMedia , shell=True)


# Envio de post
# usertitle = input("Title? ")
# userdesc = input("Desc? ")
# date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
# subprocess.run('wp post create --post_title="%s" --post_content"%s" --post_status=publish --post_date="%s"' % (usertitle, userdesc, date) , shell=True)


# Cria um post atraves de um arquivo json
# with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], i['descricao'], i['data']) , shell=True)



# Cria um post atraves de um arquivo json e envia uma midia
# with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], i['descricao'], i['data']) , shell = True)
#         id_post = (str(cmd)[24:27])
#         userMedia = input('▲ Media url? %s')
#         subprocess.run('wp media import %s --post_id=%s --featured_image --porcelain' % (userMedia, id_post), shell=True)


# Cria um post com midia na descrição do post
# usertitle = input("Title? ")
# Desc = input("Desc? ")
# userMedia = input('Media url? %s')
# date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
# cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % userMedia, shell=True)
# media = (str(cmd) [2:5])
# desc_and_midia = Desc + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % media)
# subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (usertitle, desc_and_midia, date), shell=True)


# Cria um post atraves de um arquivo json com midia na descrição do post
# with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in data:
#         userMedia = input('▲ Media url? ')
#         cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % userMedia, shell=True)
#         media = (str(cmd) [2:5])
#         desc_and_midia = i['descricao'] + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % media)
#         subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], desc_and_midia, i['data']), shell=True)