from libs import welcome_message, exit_program
from games import cuypy
from tools import Tebak_kata

def menu(): 
    user_option = int(input(f"silahkan pilih menu programnya:\n1. Games CUYPY\n2. Tebak Kata\n3. Exit\n\nsilahkan pilih: "))
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        Tebak_kata.start()
    elif user_option == 3:
        exit_program()
    else:
        print("hanya boleh pilih yang tersedia")
   
def main():
    welcome_message()
    menu()

if __name__=='__main__':    #untuk proteksi agar modul diluar tidak ter run
    main()