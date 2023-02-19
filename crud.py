#Berikut adalah code untuk CRUD Data Pasien Rumah Sakit
#sudah ada 2 data dummy
dataPasien = [{'NIP' : '1', 'Nama' : 'Benaya', 'Gender' : 'Pria', 'Kontak' : '081234' , 'Domisili' : 'BSD'},
{'NIP' : '2', 'Nama' : 'Beng', 'Gender' : 'Pria', 'Kontak' : '0812345' , 'Domisili' : 'GadingSerpong'}]

#function menampilkan data
def tampil():
    menuTampil = True
    while menuTampil != '3':
        print('\n-----Menu Tampilkan Data Pasien-----\n1. Tampilkan Seluruh Data\n2. Tampilkan Data tertentu\n3. Kembali ke Menu')                                                                    
        menuTampil = input('Silahkan pilih opsi menu Tampil: ')
        if menuTampil == '1':
            if len(dataPasien) != 0 :                                                                      
                print('Daftar Pasien :')                                                    
                for j, i in enumerate(dataPasien):
                    print(f"{j+1}. NIP : {i['NIP']}, Nama : {i['Nama']}, Gender : {i['Gender']}, Kontak : {i['Kontak']}, Domisili : {i['Domisili']}")
            else:                                                                                   
                print('\nTidak ada Data Pasien')   
            continue                                            
        elif menuTampil == '2':
            if len(dataPasien) != 0 :                                                                      
                std = input('Masukkan NIP : ').upper() 
                print(f'Data pasien dengan NIP : {std}')                                                 
                for j, i in enumerate(dataPasien):                                                                       
                    if i['NIP'] == std:
                        print(f"{j+1}. NIP : {i['NIP']}, Nama : {i['Nama']}, Gender : {i['Gender']}, Kontak : {i['Kontak']}, Domisili : {i['Domisili']}")  
                        break
                else:
                    print('\nTidak ada Data Pasien')                                                       
            else:                                                                                   
                print('\nTidak ada Data Pasien')  
            continue
        elif menuTampil == '3':
            menu()
        else:
            print('\nMenu yang anda masukkan salah\nMasukkan angka sesuai pilihan')

#function menambah data
def tambah():
    menuTambah = True
    while menuTambah != '2':
        print('\n-----Menu Tambah Data Pasien-----\n1. Tambah data pasien\n2. Kembali ke Menu')
        menuTambah = input('Silahkan pilih opsi menu Tambah: ')
        if menuTambah == '1':
            while True:
                nip = input('Masukkan NIP Pasien: ')
                if nip.isdigit():
                    break
                else:
                    print('Input harus berupa angka')
            for i in dataPasien:
                if i['NIP'] == nip:
                    print("Anda memasukkan data yang sudah ada")
                    break
            else:
                nama = input("Masukkan Nama Pasien: ")
                while True:
                    gender = input("Masukkan Jenis Kelamin Pasien: ").capitalize()             
                    if gender == 'Pria' or gender == 'Wanita':
                        break
                    else:
                        print('Gender hanya bisa Pria atau Wanita')                
                while True:
                    kontak = input("Masukkan Nomor Kontak Pasien: ")               
                    if kontak.isdigit() and len(kontak) >= 6:
                        kontak = int(kontak)
                        break
                    else:
                        print('Input harus berupa angka dan lebih dari 6 digit')
                domisili = input("Masukkan Domisili Pasien: ")
                save = True
                while save:
                    simpan = input("Apakah data sudah benar?(Y/N): ").upper()
                    if simpan == 'Y':
                            data = {"NIP": nip, "Nama": nama, "Gender": gender, "Kontak": kontak, "Domisili": domisili}
                            dataPasien.append(data)
                            print("\nData Pasien Berhasil Ditambahkan!")
                            save = False
                            break
                    elif simpan == 'N':
                        print("Data tidak jadi disimpan")
                        save = False
                        break
        elif menuTambah == '2':
            menu()
        else:
            print('\nMenu yang anda masukkan salah\nMasukkan angka sesuai pilihan')
    
#function mengubah data
def ubah():
    menuUbah = True
    while menuUbah != '2':
        print('\n-----Menu Ubah Data Pasien-----\n1. Ubah data pasien\n2. Kembali ke Menu')
        menuUbah = input('Silahkan pilih opsi menu Ubah: ')
        if menuUbah == '1':
            nip = input("Masukkan NIP Pasien yang Ingin Diubah: ")
            for i in dataPasien:
                if i['NIP'] == nip:
                    print(f"NIP : {i['NIP']}, Nama : {i['Nama']}, Gender : {i['Gender']}, Kontak : {i['Kontak']}, Domisili : {i['Domisili']}")
                    setuju = True
                    while setuju:
                        agree = input("Apakah yakin ingin mengubah data?(Y/N) : ").upper()
                        if agree == 'Y':
                            variabel = input("Masukkan variabel yang ingin diubah : ").capitalize()
                            dataBaru = input(f"Masukkan {variabel} Baru : ")
                            setuju = False
                            simpan = True
                            while simpan:
                                simpan = input("Apakah Data akan diUpdate? (Y/N) : ").upper()
                                if simpan == 'Y':
                                    i[variabel] = dataBaru
                                    print('Data sudah berubah')
                                    simpan = False
                                    break
                                elif simpan == 'N':
                                    print("Data tidak jadi diubah")
                                    simpan = False
                                    break
                            break
                        elif agree == 'N':
                            print("Data tidak jadi diubah")
                            setuju = False
                        else:
                            continue
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")
                continue

        elif menuUbah == '2':
            menu()
        else:
            print('\nMenu yang anda masukkan salah\nMasukkan angka sesuai pilihan')

#function hapus data
def hapus():
    menuHapus = True
    while menuHapus != '2':
        print('\n-----Menu Hapus Data Pasien-----\n1. Hapus data pasien\n2. Kembali ke Menu')
        menuHapus = input('Silahkan pilih opsi menu Hapus: ')
        if menuHapus == '1':
            nip = input('Masukkan NIP yang ingin dihapus: ')
            for i in dataPasien:
                if i['NIP'] == nip:
                    Delete = True
                    while Delete:
                        Delete = input("Apakah yakin ingin menghapus data?(Y/N) :").upper()
                        if Delete == 'Y':
                            x = dataPasien.index(i)
                            dataPasien.pop(x)
                            print('Data sudah dihapus')
                            Delete = False
                            break
                        elif Delete == 'N':
                            print("Data tidak jadi dihapus")
                            Delete = False
                            break
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")
                continue
        elif menuHapus == '2':
            menu()
        else:
            print('\nMenu yang anda masukkan salah\nMasukkan angka sesuai pilihan')

#function menu
def menu():

    inputMenu = 5
    while (inputMenu != '5'):
        print('\n-----Menu Data Pasien Rumah Sakit-----\n\n1. Tampilkan Data Pasien\n2. Menambahkan Data Pasien Baru\n3. Mengubah Data Pasien\n4. Menghapus Data Pasien\n5. Exit\n')
        inputMenu = input('Silahkan pilih Menu: ')
        if (inputMenu == '1'):
            tampil()
        elif (inputMenu == '2'):
            tambah()
        elif (inputMenu == '3'):
            ubah()
        elif (inputMenu == '4'):
            hapus()
        elif (inputMenu == '5'):
            print('\nTerimakasih sudah memakai aplikasi ini\n')
            quit()
        else:
            print('\nMenu yang anda masukkan salah!\nMasukkan Menu dari angka 1-5')
            
menu()