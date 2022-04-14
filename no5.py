if __name__ == "__main__":
    arr = []
    while True:
        try:
            N = int(input("Masukkan angka N : "))
            for i in range(N):
                arr.append(int(input("Masukkan angka ke-{} : ".format(i+1))))
            print("Nilai maksimum adalah : ", max(arr) , "\n")
            arr = []
        except KeyboardInterrupt:
            print("stopping")
            exit()