if __name__ == "__main__":
    while True:
        try:
            array = input("Masukkan angka : ").split(", ")
            print("Yang lebih besar adalah : ", max(array))
        except KeyboardInterrupt:
            print("stopping")
            exit()