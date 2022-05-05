import json
import os
import subprocess

# Mundando para a pasta raiz do wordpress
def RaizWordpress(RaizWord):
    os.chdir(RaizWord)
    print("Pasta do Wordpress: " + os.getcwd() + "\n")

# Envio de uma midia
def UploadMedia(Media):
    subprocess.run('wp media import %s' % Media, shell=True)


# Envio de post
def CreatePost(Title, Desc, Date, category, type):
    subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_Date="%s" --post_category="%s" --post_type="%s"' % (Title, Desc, Date, category, type), shell=True)

# Cria um post atraves de um arquivo json
def CreatePostJson(jsonFile, category, type):
    with open(jsonFile, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], i['descricao'], i['data'], category, type), shell=True)

# Cria um post atraves de um arquivo json e fazer upload de uma midia
def CreateUpload(jsonFile, category, type):
    with open(jsonFile, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], i['descricao'], i['data'], category, type), shell = True)
            ConvertStr = str(Cmd)
            IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
            Media = input('Media url? ')
            subprocess.run('wp media import %s --post_id=%s' % (Media, IdPost[3]), shell=True)

# Cria um post com midia na descrição do post
def PostMidia(Title, Desc, category, type , Date,Media):
    Title = input("Titulo? ")
    Desc = input("Descrição? ")
    Media = input('Midia url? ')
    Date = input("Insiri data e hora ( exemplo 2020-12-01 14:00:00): ")
    Cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % Media, shell=True)
    ConvertStr = str(Cmd) 
    IdMedia = ConvertStr.replace("'", "").replace("b","")
    DescMidia = Desc + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % IdMedia)
    subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (Title, DescMidia, Date, category, type), shell=True)

# Cria um post atraves de um arquivo json com midia na descrição do post
def MidiaDesc(jsonFile, category, type):
    with open(jsonFile, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Media = input('caminho da pasta do arquivo ou url: ')
            Cmd = subprocess.check_output('wp media import %s --featured_image --porcelain' % Media, shell=True)
            ConvertStr = str(Cmd)
            IdMedia = ConvertStr.replace("'", "").replace("b","")
            DescMidia = i['descricao'] + ("[gallery ids='$(wp media import %s --porcelain)' size='full']" % IdMedia)
            subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], DescMidia, i['data'], category, type), shell=True)

# Upload de varias midias de uma pasta
def UploadMediafiles(Media) :
    for folder, subfolder, files in os.walk(Media):
        for file in files:
            MediaUrl = os.path.join(os.path.realpath(folder), file)
            subprocess.run('wp media import %s' % MediaUrl , shell=True)

# Cria um post e upload de varias midias de uma pasta
def PostMidiafiles(Title, Desc, Date , category, type, Media):
    Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (Title, Desc, Date, category, type), shell = True)
    ConvertStr = str(Cmd)
    IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
    for folder, subfolder, files in os.walk(Media):
        for file in files:
            MediaUrl = os.path.join(os.path.realpath(folder), file)
            subprocess.run('wp media import %s --post_id=%s' % (MediaUrl, IdPost[3]), shell=True)

# Cria um post via json e upload de varias midias de uma pasta
def CreateUploadfiles(jsonFile, category, type):
    with open( jsonFile, 'r', encoding='utf-8') as File:
        Data = json.load(File)
        for i in Data:
            Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], i['descricao'], i['data'], category, type), shell = True)
            ConvertStr = str(Cmd)
            IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
            Media = input('caminho da pasta do arquivo ou url: ')
            for folder, subfolder, files in os.walk(Media):
                for file in files:
                    MediaUrl = os.path.join(os.path.realpath(folder), file)
                    subprocess.run('wp media import %s --post_id=%s' % (MediaUrl, IdPost[3]), shell=True)

# Cria varios post via aquivos json e upload de varias midias de uma pasta
def CreateUploadsfiles(jsonFile, category, type):
    for folder, subfolder, files in os.walk(jsonFile):
        for file in files:
            jsonFiles = os.path.join(os.path.realpath(folder), file)
            with open( jsonFiles, 'r', encoding='utf-8') as Filej:
                Data = json.load(Filej)
                for i in Data:
                    Cmd = subprocess.check_output('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], i['descricao'], i['data'], category, type) , shell = True)
                    ConvertStr = str(Cmd)
                    IdPost = ConvertStr.replace("'", "").replace("b","").replace(".","").split()
                    Media = input('caminho da pasta do arquivo ou url: ')
                    for folder, subfolder, files in os.walk(Media):
                        for file in files:
                            MediaUrl = os.path.join(os.path.realpath(folder), file)
                            subprocess.run('wp media import %s --post_id=%s' % (MediaUrl, IdPost[3]), shell=True)

# Cria um post via arquivos json
def CreatePostJsons(jsonFile, category, type):
    for folder, subfolder, files in os.walk(jsonFile):
        for file in files:
            jsonFiles = os.path.join(os.path.realpath(folder), file)
            with open(jsonFiles, 'r', encoding='utf-8') as File:
                Data = json.load(File)
                for i in Data:
                    subprocess.run('wp post create --post_title="%s" --post_content="%s" --post_status=publish --post_date="%s" --post_category="%s" --post_type="%s"' % (i['nome'], i['descricao'], i['data'], category, type), shell=True)
