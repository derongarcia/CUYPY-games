import main 
import random

def start():
    while True:
        
        kata = [
            'rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks'
            ]
        
        kata_kata = random.choice(kata)
        tebakan = ''
        giliran = 12
        
        while giliran > 0:
            kesalahan = 0
            
            for char in kata_kata:
                if char in tebakan:
                    print(char, end=' ')
                else:
                    print("_", end=' ')
                    kesalahan += 1
            
            print()
            
            if kesalahan == 0:
                print("Kamu menang")
                print("Katanya adalah: ", kata_kata)
                break
            
            tebakan_pemain = input("Silahkan tuliskan satu huruf: ").lower()
            
            if tebakan_pemain in tebakan:
                print(f"kamu sudah menebak huruf {tebakan_pemain}")
                continue
            if tebakan_pemain not in kata_kata:
                giliran -= 1
                # if len(tebakan_pemain) > 1 or len(tebakan_pemain) <= 5:
                #     giliran = giliran - len(tebakan_pemain)
                # if len(tebakan_pemain) > 6:
                #     print("Kata terlalu panjang")
                print(f"tersisa {giliran} tebakan")
            
            
            if len(tebakan_pemain) != 1:
                print("coba tebak hanya 1 huruf!")
                continue
            
            tebakan += tebakan_pemain
            
            if giliran == 0:
                print(f"Kamu kalah, kata yang benar adalah {kata_kata}")
                break
                
        lanjut_main = input("Apakah ingin lanjut bermain? [y/n]: ")
        if lanjut_main == "n":
            main.menu()
        elif lanjut_main == "y":
            continue
        else:
            print("Input invalid")
                
if __name__ == '__main__':
    start() 