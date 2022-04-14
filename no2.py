if __name__ == "__main__":
    while True:
        try:
            angka = int(input("Masukkan angka : "))
            if angka % 2 == 0:
                print("Genap")
            else:
                print("Ganjil")
        except KeyboardInterrupt:
            print("stopping")
            exit()