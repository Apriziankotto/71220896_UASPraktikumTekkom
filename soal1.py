string= ''
bar= 1
x = 10
while bar <= x:
    kol= bar

    while kol > 0:
        string= string + "="
        kol=kol - 1
    string = string
    bar = bar + 1

print(string)
print("**********Justice League***********")
string= ''
bar= 1
x =10
while bar <= x:
    kol= bar

    while kol > 0:
        string= string + "="
        kol=kol - 1
    string = string
    bar = bar + 1
print(string)

t = str(input("Masukkan username anda:"))
if t == 'victorstone':
    print("=====WELCOME victorstone=====")
elif t == 'brucewyne':
    print("=====WELCOME brucewyne=====")
elif t == 'ciscoramon':
    print("=====WELCOME ciscoramon=====")
else:
    print("Access Deniel")
print("1.Tambah Angota Justice League")
print("2.Hapus Angota Justice League")
print("3.Tampilkan Angota Justice League")
print("4.Exit")
n = str(input("Masukkan pilihan anda:"))
if n == 1:
    m = str(input("Nama anggota baru:"))
    print("data", m, "berhasil ditambahkan")
elif n == 2:
    m = str(input("Anggota yang akan dihapus:"))
elif n == 3:
    m = str(input("Daftar Anggota Justice Leangue:"))
else:
    print("see u next time Mr. victorstone, GLHF")
