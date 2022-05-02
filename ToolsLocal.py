import json
import os
import subprocess

# Mundando para a pasta raiz do wordpress
def RaizWordpress(RaizWord):
    os.chdir(RaizWord)
    # print(os.getcwd())
# print("teste")
# raiz = r'C:\xampp\htdocs\testes'
# RaizWordpress(raiz)
# Envio de uma midia
def UploadMedia() :
    Media = input('Midia url? ')
    subprocess.run('wp media import %s' % Media , shell=True)

# Envio de post
def CreatePost():
    Title = input("Titulo? ")
    Desc = input("Descrição? ")
    Date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
    subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_Date="%s"' % (Title, Desc, Date) , shell=True)

# Cria um post atraves de um arquivo json
def CreatePostJson():
    with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], i['descricao'], i['data']) , shell=True)

# Cria um post atraves de um arquivo json e envia uma midia
def CreateUpload():
    with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], i['descricao'], i['data']) , shell = True)
            ConvertStr = str(Cmd)
            IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
            Media = input('Media url? ')
            subprocess.run('wp media import %s --post_id=%s' % (Media, IdPost[3]), shell=True)

# Cria um post com midia na descrição do post
def PostMidia():
    Title = input("Titulo? ")
    Desc = input("Descrição? ")
    Media = input('Midia url? ')
    Date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
    Cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % Media, shell=True)
    ConvertStr = str(Cmd) 
    IdMedia = ConvertStr.replace("'", "").replace("b","")
    DescMidia = Desc + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % IdMedia)
    subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (Title, DescMidia, Date), shell=True)

# Cria um post atraves de um arquivo json com midia na descrição do post
def MidiaDesc():
    with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Media = input('Midia url? ')
            Cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % Media, shell=True)
            ConvertStr = str(Cmd)
            IdMedia = ConvertStr.replace("'", "").replace("b","")
            DescMidia = i['descricao'] + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % IdMedia)
            subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], DescMidia, i['data']), shell=True)

# Upload de varias midias de uma pasta
def UploadMediafiles() :
    Media = input('Midia url? ')
    for folder, subfolder, files in os.walk(Media):
        for file in files:
            MediaUrl = os.path.join(os.path.realpath(folder), file)
            subprocess.run('wp media import %s' % MediaUrl , shell=True)

# Cria um post e upload de varias midias de uma pasta
def PostMidiafiles():
    Title = input("Titulo? ")
    Desc = input("Descrição? ")
    Media = input('Midia url? ')
    Date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
    Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (Title, Desc, Date) , shell = True)
    ConvertStr = str(Cmd)
    IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
    for folder, subfolder, files in os.walk(Media):
        for file in files:
            MediaUrl = os.path.join(os.path.realpath(folder), file)
            subprocess.run('wp media import %s --post_id=%s' % (MediaUrl, IdPost[3]), shell=True)

# Cria um post via json e upload de varias midias de uma pasta
def CreateUploadfiles():
    with open('C:/Users/BrasoDev/Downloads/teste/teste.json', 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s"' % (i['nome'], i['descricao'], i['data']) , shell = True)
            ConvertStr = str(Cmd)
            IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
            Media = input('Media url? ')
            for folder, subfolder, files in os.walk(Media):
                for file in files:
                    MediaUrl = os.path.join(os.path.realpath(folder), file)
                    subprocess.run('wp media import %s --post_id=%s' % (MediaUrl, IdPost[3]), shell=True)


