import random
import main
def start():
    
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4   #GOA HARUS KOSONG
        goa = goa_kosong.copy()     #TEMPAT BARU UNTUK CUYPY

        cuypy_position = random.randint(1, 4)
        goa[cuypy_position - 1] = "|>_<|"
        # print(goa)
        # print(f"posisi: {cuypy_position}")

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)


        print(f"Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n")  

        # while True:
                
        pilihan_user = int(input("Menurut kamu dimana CUYPY berada? [1 / 2 / 3 / 4]: "))
        # while pilihan_user ==  :
            #     pilihan_user = input("Menurut kamu dimana CUYPY berada? [1 / 2 / 3 / 4]: ")
            # jawaban_pasti = input("Apakah anda sudah yakin dengan jawaban?[y / n]: ")
            # if jawaban_pasti == "y":
            #     break
            # elif jawaban_pasti == "n":
            #     print("Coba lagi!")
            # else:
                # print("Jawaban tidak valid coba ketik dengan benar!")
            
            
        if pilihan_user == cuypy_position:
            print(f"jawaban benarr! cuypy ada di goa nomor {cuypy_position}\n {goa}")
        else:
            print(f"Kamu salah, cuypy bukan disitu, cuypy ada di goa nomor {cuypy_position}\n {goa}")
        
        lanjut_main = input("\n\n Mau lanjut? [y/n]: ")
        if lanjut_main == "n":
            main.menu()
        elif lanjut_main == "y":
            continue
        else:
            print("Input Invalid")


if __name__=='__main__':
    start()