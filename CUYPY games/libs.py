import socket
from time import sleep  #sleep berfungsi untuk delay

PC_name = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_name) + 6)
    print(style)
    print(f"** {PC_name} **")
    print(style)
    

def exit_program():
    print("program akan dihentikan")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("program berhasil dihentikan")
    exit()
    

if __name__ == '__main__':
    welcome_message()
    exit_program()