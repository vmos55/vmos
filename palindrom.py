queue = []
while True:
    print("\n=== Pemrosesan Teks Palindrom ===")
    print("1. Masukkan Teks")
    print("2. Riwayat teks")
    print("3. Keluar")

    menu = input("Pilih opsi (1/2/3): ")

    if menu == '1':
        kata = input("Masukkan teks: ")
        queue.append(kata)

        stack = []
        for huruf in kata:
            stack.append(huruf)
            
        reversed_text = '' #menyimpan hasil teks yang dibalik
        while stack:
            reversed_text += stack.pop()

        if kata == reversed_text:
            print(f"Teks '{kata}' adalah palindrom.")
        else:
            print(f"Teks '{kata}' bukan palindrom.")

    elif menu == '2':
        if queue:
            print("\nRiwayat teks yang diperiksa:")
            for idx, item in enumerate(queue, 1):
                print(f"{idx}. {item}")
        else:
            print("\nRiwayat kosong.")

    elif menu == '3':
        print("\nProgram selesai. Terima kasih!")
        break

    else:
        print("\nPilihan tidak valid. Coba lagi.")