from Transferjob import *

menu_options = {
    1: 'Cria um post',
    2: 'Fazer upload de uma midia',
    3: 'Cria um post com midia na descrição do post',
    4: 'Cria um post atraves de um arquivo json',
    5: 'Cria um post atraves de um arquivo json e fazer upload de uma midia',
    6: 'Cria um post atraves de um arquivo json com midia na descrição do post',
    7: 'Fazer upload de varias midias de uma pasta',
    8: 'Cria um post via arquivios json',
    9: 'Cria um post e fazer upload de varias midias de uma pasta',
    10: 'Cria um post via json e fazer upload de varias midias de uma pasta',
    11: 'Cria varios post via aquivos json e upload de varias midias de uma pasta',
    12: 'Exit',
}

def print_menu():
    print("\n")
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    Title = input("Titulo: ")
    Desc = input("Descrição: ")
    Date = input("Insiri data e hora ( Exemplo 2020-12-01 14:00:00): ")
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreatePost(Title, Desc, Date, category, type)

def option2():
     Media = input('caminho da pasta do arquivo ou url: ')
     UploadMedia(Media)

def option3():
    Title = input("Titulo: ")
    Desc = input("Descrição: ")
    Date = input("Insiri data e hora ( Exemplo 2020-12-01 14:00:00): ")
    category = input("Categoria: ")
    type = input("Post_type: ")
    Media = input('caminho da pasta do arquivo ou url: ')
    PostMidia(Title, Desc, category, type , Date, Media)

def option4():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreatePostJson(jsonFile, category, type)

def option5():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreateUpload(jsonFile, category, type)

def option6():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreateUpload(jsonFile, category, type)

def option7():
    Media = input('caminho da pasta das midias para upload: ')
    UploadMediafiles(Media)

def option8():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreatePostJsons(jsonFile, category, type)

def option9():
    Title = input("Titulo: ")
    Desc = input("Descrição: ")
    Date = input("Insiri data e hora ( Exemplo 2020-12-01 14:00:00): ")
    category = input("Categoria: ")
    type = input("Post_type: ")
    Media = input('caminho da pasta do arquivo ou url: ')
    PostMidiafiles(Title, Desc, Date , category, type, Media)

def option10():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreateUploadfiles(jsonFile, category, type)

def option11():
    jsonFile = input('caminho da pasta do arquivo: ')
    category = input("Categoria: ")
    type = input("Post_type: ")
    CreateUploadfiles(jsonFile, category, type)
