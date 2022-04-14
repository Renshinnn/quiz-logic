if __name__ == "__main__":
    a = 0
    while True:
        try:
            N = int(input("Masukkan angka : "))
            for i in range(N+1):
                a += i
            print("Total penjumlahan dari 1 sampai {} adalah {}".format(N, a))
            a=0
        except KeyboardInterrupt:
            print("stopping...")
            exit()