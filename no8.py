if __name__ == "__main__":
    arrBuah = []
    arrJumlah = []
    while True:
        try:
            rawInput = input("Masukkan nama buah dan jumlah penjualan (pisahkan koma) : ").split(", ")
            for i in range(len(rawInput)):
                if i % 2 == 0:
                    arrBuah.append(rawInput[i])
                else:
                    arrJumlah.append(int(rawInput[i]))
            print("Buah yang paling laris adalah {}".format(arrBuah[arrJumlah.index(max(arrJumlah))]))
        except KeyboardInterrupt:
            print("stopping")
            exit()