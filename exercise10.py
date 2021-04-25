#Christina Andrea Putri - Universitas Kristen Duta Wacana

#Andi ingin menginput data pribadinya dan teman-temannya untuk keperluan pendataan liburan mereka. 
# Yang perlu diinput adalah nama, umur, dan destinasi pilihan masing-masing. 
# Namun, Andi salah menginput salah satu data dan salah satu temannya batal ikut juga. Bagaimana penyelesaiannya?

#Input : nama, umur, destinasi pilihan setiap orang
#Proses : memasukkan setiap datanya ke dalam dict() dan keys berbeda, edit data, hapus data
#Output : dict() akhir

try:
    emp = dict()
    while True:
        inp=int(input("Menu : \n 1. Tambah data \n 2. Ubah data \n 3. Hapus data \n 4. Keluar \n Pilihan Anda: "))

        if inp==1:
            sumadd = int(input("Jumlah data: "))

            for i in range(sumadd):
                r = i+1
                print(r)
                name = input("Nama: ")
                age = int(input("Umur : "))
                dest = input("Destinasi : ")

                emp[r] = {'nama':name,'umur':age,'destinasi':dest}
                print(emp)
        elif inp==2:
            inp_edit = int(input("No. yang ingin diubah: "))
            inp_bag = input("Bagian yang ingin diubah: ")
            inpcontent = input("Masukkan data yang ingin diubah: ")

            emp[inp_edit][inp_bag] = inpcontent
            
        elif inp == 3 : 
            inpdel = int(input("No. yang ingin dihapus: "))
            del emp[inpdel]
            print("Berhasil dihapus!")
            print(emp)
        elif inp==4:
            for i in emp.items():
                print(i)
            print("Terimakasih sudah menggunakan layanan kami.")
            break
            
except:
    print("Invalid input. Try again.")