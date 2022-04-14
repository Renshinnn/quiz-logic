from numpy import append

if __name__ == "__main__":

    arrHasil = []
    array = []
    while True:
        try:
            N = int(input("Masukkan angka N : "))
            
            for i in range(N):
                array.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
            for i in range(N):
                if array[i] % 2 == 0:
                    arrHasil.append("Genap")
                else:
                    arrHasil.append("Ganjil")
            print(arrHasil)
            arrHasil = []
            array = []
        except KeyboardInterrupt:
            print("stopping")
            exit()