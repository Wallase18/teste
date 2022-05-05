from ToolsMenu import *

cred = '''
----------------------------------------------------------------------
                          TRANSFERJOB 
                                     V1.0
                                     By : Wallase Alan (@Wallase18)
----------------------------------------------------------------------
'''
print (cred + '\n')

if __name__=='__main__':
    print("caminho da pasta do wordpress: (Exemplo C:/Users/MeuPc/Downloads/teste) ")
    folder = input()
    RaizWordpress(folder)
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()  
        elif option == 7:
            option7() 
        elif option == 8:
            option9() 
        elif option == 9:
            option9()
        elif option == 10:
            option10()
        elif option == 11:
            option11()
        elif option == 12:
            print('Thanks message before exiting \n')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 12.')