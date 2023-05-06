from math import *
from random import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Canvas

# TODO: Fungsi Input
def validasiintInput():
    jawab = entry1.get()
    try:
        int(jawab)
    except ValueError:
        return "   Masukkan hanya angka!"
    return "jawaban kamu adalah " + jawab 

# TODO: Fungsi Perkalian
def generateKali(range1, range2):
    angka_1 = randint(range1, range2)
    angka_2 = randint(range1, range2)
    jawaban = angka_1 * angka_2

    return angka_1, angka_2, jawaban

# TODO: Fungsi Pembagian 
def generateBagi(range1, range2):
    angka_1 = randint(range1, range2)
    angka_2 = randint(range1, range2)
    jawaban = angka_1 / angka_2

    if (jawaban.is_integer()):
        return angka_1, angka_2, int(jawaban)
    else:
        return generateBagi(range1, range2)

# TODO: Fungsi Luas
def generateluas(range1, range2, jenisbangun):
    if jenisbangun == "segitiga":
        alas = randint(range1, range2)
        tinggi = randint(range1, range2)
        jawaban = alas*tinggi/2

        if jawaban.is_integer():
            return alas, tinggi, jawaban
        else:
            return generateluas(range1, range2, jenisbangun)
    
    elif jenisbangun == "persegi":
        sisi = randint(range1,range2)
        jawaban = sisi**2

        return sisi, jawaban

    elif jenisbangun == "persegi panjang":
        panjang = randint(range1,range2)
        lebar = randint(range1, range2)
        jawaban = panjang*lebar

        return panjang, lebar, jawaban
    
    elif jenisbangun == "lingkaran":
        jari = randint(range1,range2)
        jawaban = (22/7)*jari*jari

        if jawaban.is_integer():
            return jari, jawaban
        else:
            return generateluas(range1, range2, jenisbangun)

    elif jenisbangun == "layang layang":
        diagonalx = randint(range1,range2)
        diagonaly = randint(range1, range2)
        jawaban = diagonalx*diagonaly/2

        if jawaban.is_integer():
            return diagonalx, diagonaly, jawaban
        else:
            return generateluas(range1, range2, jenisbangun)

    elif jenisbangun == "belah ketupat":
        diagonal = randint(range1,range2)
        jawaban = (diagonal**2)/2

        if jawaban.is_integer():
            return diagonal, jawaban
        else:
            return generateluas(range1, range2, jenisbangun)

# TODO: Fungsi Keliling
def generatekeliling(range1, range2, jenisbangun):
    if jenisbangun == "segitiga":
        alas = randint(range1, range2)
        tinggi = randint(range1, range2)
        smiring = sqrt(alas**2+tinggi**2)
        jawaban = smiring+alas+tinggi

        if jawaban.is_integer():
            return alas, tinggi, jawaban
        else:
            return generatekeliling(range1, range2, jenisbangun)

    elif jenisbangun == "persegi":
        sisi = randint(range1,range2)
        jawaban = sisi*4

        return sisi, jawaban

    elif jenisbangun == "persegi panjang":
        panjang = randint(range1,range2)
        lebar = randint(range1, range2)
        jawaban = (panjang+lebar)*2

        return panjang, lebar, jawaban
    
    elif jenisbangun == "lingkaran":
        jari = randint(range1,range2)
        jawaban = (44/7)*jari

        if jawaban.is_integer():
            return jari, jawaban
        else:
            return generatekeliling(range1, range2, jenisbangun)

    elif jenisbangun == "belah ketupat":
        diagonal = randint(range1,range2)
        x = (diagonal**2)/2
        smiring2 = sqrt(x)
        jawaban = 4*smiring2

        if jawaban.is_integer():
            return diagonal, jawaban
        else:
            return generatekeliling(range1, range2, jenisbangun)

# TODO: Fungsi GLBB
def generateGLBB(range1, range2, jenissoal):
    if jenissoal == 1:
        Vo = randint(range1, range2)
        a = randint(range1, range2//6)
        t = randint(range1, range2 - 10)
        Vt = Vo + a*t

        return Vt, a, t, Vo
    elif jenissoal == 2:
        Vo = randint(range1, range2)
        a = randint(range1, range2//6)
        t = randint(range1, range2 - 10)
        jawaban_benar = Vo + (a*t)

        return Vo, a, t, jawaban_benar
    elif jenissoal == 3:
        Vo = randint(range1, range2)
        a = randint(range1, range2//6)
        km = round(Vo * 3.6, 2)
        jawaban_benar = Vo/a

        if (jawaban_benar.is_integer()):
            return km, a, jawaban_benar
        else:
            return generateGLBB(range1, range2, jenissoal)

# TODO: Fungsi Momentum
def generateMomentum(range1, range2, jenissoal):
    if jenissoal == 1:
        m1 = randint(range1, range2//6)
        v1 = randint(range1, range2//5)
        m2 = randint(range1, range2//6)
        v = (m1*v1)/(m1+m2)

        if (v.is_integer()):
            return m1, v1, m2, v
        else:
            return generateMomentum(range1, range2, jenissoal)

    elif jenissoal == 2:
        m1 = randint(range1, range2//3)
        v1 = randint(range1, range2//5)

        m2 = randint(range1, range2//3)
        v2 = randint(range1, range2//5)

        v1s = randint(range1, range2//5)

        v2s = ((m1*v1) - (m2*v2) + (m1*v1s)) / m2

        if m2 > m1:
            return generateMomentum(range1, range2, jenissoal)
        elif v2 > v1:
            return generateMomentum(range1, range2, jenissoal)

        if v1 == v1s:
            return generateMomentum(range1, range2, jenissoal)
        else:
            return m1, v1, m2, v2, v1s, v2s

# TODO: Fungsi Listrik
def generateListrik(range1, range2, jenissoal):
    if jenissoal == 1: 
        V = randint(range1, range2//6)
        R1 = randint(range1, range2//3)
        R2 = randint(range1, range2//3)
        R3 = randint(range1, range2//3)

        R1R2 = lcm(R1, R2)
        Rk = lcm(R1R2, R3)

        Rt = Rk / ((Rk // R1) + (Rk // R2) + (Rk // R3))
        I = V / Rt

        if (I.is_integer()):
            return V, R1, R2, R3, I
        else:
            return generateListrik(range1, range2, jenissoal)
    elif jenissoal == 2:
        I = randint(range1, range2//3)
        V = randint(range1, range2)
        R1 = randint(range1, range2//6)
        R2 = randint(range1, range2//6)

        R3 = (V - (I*R1) - (I*R2)) / I

        if R3 < 1: 
            return generateListrik(range1, range2, jenissoal)

        if (R3.is_integer()):
            return I, V, R1, R2, R3
        else:
            return generateListrik(range1, range2, jenissoal) 

# TODO: Fungsi Energi
def generateEnergi(range1, range2, jenissoal):
    if jenissoal == 1:
        m = randint(range1, range2//3)
        g = 10
        v = randint(range1, range2)
        h =  (v*v)/(2*g)

        if (h.is_integer()):
            return m, g, v, h
        else:
            return generateEnergi(range1, range2, jenissoal)
    elif jenissoal == 2:
        m = randint(range1, range2//3)
        g = 10
        h = randint(range1, range2)
        Ek = m*g*h

        return m, g, h, Ek

# TODO: Fungsi Gelombang
def generateGelombang(range1, range2):
    n = randint(range1, range2)
    L = randint(range1, range2)
    v = randint(range1, range2//3)
    f = v/(L/n)

    if (f.is_integer()):
        return n, L, v, f
    else:
        return generateGelombang(range1, range2)

# TODO: Fungsi untuk mengakhiri Challenge
def akhir_game():
    root.destroy()

# TODO: Mengambil inputan user
def validasi_value():
    global jawaban_user, jawaban
    jawaban = validasiintInput()
    validasi_jawaban['text'] = jawaban
    
    if validasi_jawaban != "   Masukkan hanya angka!":
        jawaban_user = int(entry1.get())
        check1(jawaban_benar, jawaban_user, t)


# TODO: Fungsi cek jawaban user
def check1(jawaban_benar, jawaban_user, t):
    global life
    if jawaban_user != jawaban_benar and life > 0:
        validasi_jawaban.config(text=(f"Yahh! Jawaban kamu salah!\n\nKesempatan kamu tersisa {life}"))
        life -=1
        background1.config(image=imgheart1)
    else:
        check(jawaban_benar, jawaban_user, t)

def check(jawaban_benar, jawaban_user, t):
    global benarsalah
    challengewindow.destroy()
    resultwindow = Toplevel(root)
    resultwindow.title("Hasil Challenge")
    resultwindow.geometry("800x600")
    resultwindow.resizable(width=False,height=False)

    if t == 0 and jawaban_user == 123456789:
        cek = outoftime
        benarsalah = False
    elif jawaban_user == jawaban_benar:
        cek = wining
        benarsalah = True
    elif jawaban_user != jawaban_benar:
        cek = losing
        benarsalah = False

    hasilnya = Label(resultwindow,image=cek)
    hasilnya.place(x=0,  y=0)

    root.after(1500,akhir_game)

# TODO: Fungsi Display
def display_timer():
    global t
    if t>0:
        t -=1
        timer['text']= ('%.2d' %t)
        timer.after(1000,display_timer)
    if t==0:
        jawaban_user = 123456789
        check(jawaban_benar, jawaban_user, t)

def print_timer():
    global challengewindow, timer, t

    timer = Label(challengewindow,text="", font=('Consolas 16'), background='White', foreground='Black')
    timer.place(relx=0.484365, rely=0.025)
    display_timer()

def print_window():
    global challengewindow, entry1, validasi_jawaban, enter, printprintan, background1
    challengewindow = Toplevel(root)
    challengewindow.title("[ CHALLENGE ! ]")
    challengewindow.geometry('800x600')
    # challengewindow.resizable(width=False,height=False)



    background1 = Label(challengewindow, image=imgheart2)
    background1.pack( fill='both', expand='yes')
    background1.place(x=0, y=0)

    labelsoal = Label(challengewindow, text=printprintan,font=('Consolas 10'),background='#563d2d',foreground='White', width=113, height=10, anchor=CENTER)
    labelsoal.pack()
    labelsoal.place(relx=0.0025, rely=0.353)

    validasi_jawaban = Label(challengewindow,text='')
    validasi_jawaban.place(relx=1,rely=1)
    
    entry1 = Entry(challengewindow,font=('Consolas 12'), width=5,background='#84694d',foreground='White', justify=CENTER)
    entry1.place(relx=0.465, rely=0.7)

    enter= Button(challengewindow, image=imgenter, bg='#84694d', relief=FLAT, command= validasi_value,pady=4,padx=10)
    enter.place(relx=0.4408, rely=0.82)
    print_timer()

# TODO: List soal Matematika
def soal_operasi():
    global jawaban_benar, t, printprintan
    # Membuat variabel untuk ditampilan pada soal
    angka_1 = randint(50, 200)
    angka_2 = randint(50, 200)
    operasi = randint(1, 4)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        operasi = "+"
        jawaban_benar = (angka_1 + angka_2)
        t = 15
    elif operasi == 2:
        operasi = "-"
        jawaban_benar = (angka_1 - angka_2)
        t = 15
    elif operasi == 3:
        operasi = "x"
        angka_1, angka_2, jawaban_benar = generateKali(10, 50)
        t = 30
    elif operasi == 4:
        operasi = ":"
        angka_1, angka_2, jawaban_benar = generateBagi(25, 250)
        t = 15
    # TODO: Ngeprint soal-soal
    printprintan = (f"Hitung hasil dari {angka_1} {operasi} {angka_2} !")
    print_window()


def soal_matriks_pejumlahan():
    global jawaban_benar,t, printprintan
    list1 = [[0 for i in range(2)]for j in range (2)]
    list2 = [[0 for i in range(2)]for j in range (2)]
    listhasil = [[0 for i in range(2)]for j in range (2)]
    listjawaban = [[0 for i in range(2)]for j in range (2)]
    baris11 =""
    baris12 =""
    baris21 =""
    baris22 =""
    t = 30
    
    for i in range(2):
        for j in range(2):
            list1[i][j] = randint(1,9)
            list2[i][j] = randint(1,9)   
    baris11 += str(list1[0][0]) + "   " + str(list1[0][1]) 
    baris12 += str(list2[0][0]) + "   " + str(list2[0][1])
    baris21 += str(list1[1][0]) + "   " + str(list1[1][1])
    baris22 += str(list2[1][0]) + "   " + str(list2[1][1])

    for i in range(2):
        for j in range(2):
            listhasil[i][j]=list1[i][j]+list2[i][j]

    jawaban_benar = (listhasil[0][0]*listhasil[1][1]) - (listhasil[0][1]*listhasil[1][0])
    x = "+"

    printprintan = (f"\
Hitung determinan matriks dari penjumlahan Matriks berikut!\n\
\n\
{baris11.ljust(10) + baris12.rjust(10)}\n\
{x.center(21)}\n\
{baris21.ljust(10) + baris22.rjust(10)}")
    print_window()

def soal_Luas_Keliling_Bangun():
    global jawaban_benar,t, printprintan

    # TODO: Gacha soal
    jenis_soal = ["Luas", "Keliling"]
    jenis = choice(jenis_soal)
    jenis_bangun = ["segitiga", "persegi", "persegi panjang",
                    "lingkaran", "layang layang", "belah ketupat"]
    jenis_bangun1 = choice(jenis_bangun)
    if jenis == "Luas":
        if jenis_bangun1 == "segitiga":
            alas, tinggi, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun segitiga memiliki panjang alas {alas} m dan tinggi {tinggi} m.\nTentukan luas bangun segitiga tersebut!")
            t=20
        elif jenis_bangun1 == "persegi":
            sisi, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun persegi memiliki panjang sisi {sisi} m.\nTentukan luas bangun persegi tersebut!")
            t=20
        elif jenis_bangun1 == "persegi panjang":
            panjang, lebar, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun persegi panjang memiliki panjang {panjang} m dan lebar {lebar} m.\nTentukan luas bangun persegi panjang tersebut!")
            t=20
        elif jenis_bangun1 == "lingkaran":
            jari, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun lingkaran memiliki jari-jari {jari} m.\nTentukan luas bangun lingkaran tersebut!")
            t=30
        elif jenis_bangun1 == "layang layang":
            diagonalx, diagonaly, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun layang-layang memiliki diagonal mendatar {diagonalx} m dan diagonal tegak {diagonaly} m.\nTentukan luas bangun layang-layang tersebut!")
            t=30
        elif jenis_bangun1 == "belah ketupat":
            diagonal, jawaban_benar = generateluas(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun belah ketupat memiliki diagonal {diagonal} m.\nTentukan luas bangun belah ketupat tersebut!")
            t=30
    elif jenis == "Keliling":
        if jenis_bangun1 == "segitiga":
            alas, tinggi, jawaban_benar = generatekeliling(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun segitiga siku siku memiliki panjang alas {alas} m dan tinggi {tinggi} m.\nTentukan keliling bangun segitiga tersebut!")
            t=40
        elif jenis_bangun1 == "persegi":
            sisi, jawaban_benar = generatekeliling(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun persegi memiliki panjang sisi {sisi} m.\nTentukan keliling bangun persegi tersebut!")
            t=20
        elif jenis_bangun1 == "persegi panjang":
            panjang, lebar, jawaban_benar = generatekeliling(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun persegi panjang memiliki panjang {panjang} m dan lebar {lebar} m.\nTentukan keliling bangun persegi panjang tersebut!")
            t=20
        elif jenis_bangun1 == "lingkaran":
            jari, jawaban_benar = generatekeliling(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun lingkaran memiliki jari-jari {jari} m.\nTentukan keliling bangun lingkaran tersebut!")
            t=30
        elif jenis_bangun1 == "belah ketupat":
            diagonal, jawaban_benar = generatekeliling(1,30,jenis_bangun1)
            soal = (f"Sebuah bangun belah ketupat memiliki diagonal {diagonal} m.\nTentukan keliling bangun belah ketupat tersebut!")
            t=60

    # TODO: Print soal
    printprintan = (soal)
    print_window()

# TODO: List soal Fisika
def soalGLBB():
    global jawaban_benar,t, printprintan
    # Menentukan jenis soal 
    operasi = randint(1,3)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        Vt, a, t, jawaban_benar = generateGLBB(1, 30, operasi)
        soal = (f"Sebuah benda mempunyai kecepatan sebesar {Vt} m/s\nsetelah bergerak dengan percepatan {a} m/s^2 selama {t} sekon dari kecepatan awal.\nTentukan kecepatan awal benda !")
        t = 30
    elif operasi == 2:
        Vo, a, t, jawaban_benar = generateGLBB(1, 30, operasi)
        soal = (f"Sebuah bola bergerak lurus horizontal terhadap bidang datar licin.\nJika kecepatan awal benda adalah {Vo} m/s dan percepatan yang dialami benda adalah {a} m/s^2,\ntentukan kecepatan benda setelah bergerak selama {t} sekon !")
        t = 30
    elif operasi == 3:
        Vo, a, jawaban_benar = generateGLBB(1, 30, operasi)
        soal = (f"Sebuah kereta bergerak dengan kecepatan awal {Vo} km/jam.\nJika kereta melakukan pengereman dengan perlambatan sebesar {a} m/s^2,\ntentukan berapa lama kereta melakukan pengereman hingga berhenti (dalam s) !")
        t = 30   
    
    # TODO: Ngeprint soal-soal
    x = ("".center(100,"="))
    y = ("".center(100,"="))
    printprintan = (soal)
    print_window()

def soalMomentum():
    global jawaban_benar,t, printprintan
    # Menentukan jenis soal 
    operasi = randint(1,2)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        m1, v1, m2, jawaban_benar = generateMomentum(1, 30, operasi)
        soal = (f"Sebuah balok A bermassa {m1} kg dengan kecepatan {v1} m/s menumbuk balok B bermassa {m2} kg yang diam.\nSetelah tumbukan, kedua balok bergabung dan bergerak bersama-sama ke arah horizontal.\nTentukan kecepatan kedua balok setelah tumbukan (dalam m/s)!")
        t = 30
    elif operasi == 2:
        m1, v1, m2, v2, v1s, jawaban_benar = generateMomentum(1, 30, operasi)
        soal = (f"Balok B bermassa {m2} kg bergerak dengan kecepatan {v2} m/s ke arah sumbu x negatif menumbuk lenting sempurna\nbalok A bermassa {m1} kg yang bergerak dengan kecepatan {v1} m/s ke arah sumbu x positif.\nSetelah tumbukan, balok A bergerak dengan kecepatan {v1s} m/s ke arah sumbu x negatif dan balok B\nbergerak ke arah sumbu x positif. Tentukan kecepatan balok B setelah tumbukan !")
        t = 30

    # TODO: Ngeprint soal-soal
    x = ("".center(100,"="))
    y = ("".center(100,"="))
    printprintan = (soal)
    print_window()

def soalListrik():
    global jawaban_benar,t, printprintan
    # Menentukan jenis soal 
    operasi = randint(1,2)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        V, R1, R2, R3, jawaban_benar = generateListrik(1, 30, operasi)
        soal = (f"Tiga buah hambatan dirangkai secara paralel pada sebuah rangkaian listrik bertegangan {V} Volt.\nJika hambatan-1 sebesar {R1} Ohm, hambatan-2 sebesar {R2} Ohm, dan hambatan-3 sebesar {R3} Ohm,\nberapakah arus yang mengalir dalam rangkaian tersebut (dalam Ampere)?")
        t = 30
    elif operasi == 2:
        I, V, R1, R2, jawaban_benar = generateListrik(1, 30, operasi)
        soal = (f"Sebuah rangkaian listrik bertegangan {V} volt mempunyai tiga buah hambatan yang dirangkai secara seri.\nJika arus sebesar {I} Ampere mengalir pada hambatan-1 ({R1} Ohm), hambatan-2 ({R2} Ohm), dan hambatan-3.\nBerapakah besar hambatan-3 (dalam Ohm)?")
        t = 30

    # TODO: Ngeprint soal-soal
    x = ("".center(100,"="))
    y = ("".center(100,"="))
    
    printprintan = (soal)
    print_window()

def soalEnergi():
    global jawaban_benar,t, printprintan
    # Menentukan jenis soal 
    operasi = randint(1,2)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        m, g, v, jawaban_benar = generateEnergi(1, 30, operasi)
        soal = (f"Sebuah balok diam bermassa {m} kg berada di atas sebuah bidang miring licin setinggi h meter.\nLalu, balok didorong menuruni bidang miring licin tersebut dengan gravitasi {g} m/s^2 sehingga\nmemiliki kecepatan {v} m/s ketika mencapai dasar bidang miring.\nBerapakah ketinggian bidang miring tersebut (dalam m)?")
        t = 30

    elif operasi == 2:
        m, g, h, jawaban_benar = generateEnergi(1, 30, operasi)
        soal = (f"Sebuah bola jatuh bebas dari ketinggian {h} meter dari tanah.\nMassa bola adalah {m} kg dan gravitasi sebesar {g} m/s^2.\nTentukan energi kinetik benda ketika mencapai tanah (dalam Joule)!")
        t = 30

    # TODO: Ngeprint soal-soal
    x = ("".center(100,"="))
    y = ("".center(100,"="))
    
    printprintan = (soal)
    print_window()

def soalGelombang():
    global jawaban_benar,t, printprintan
    # Menentukan jenis soal 
    operasi = randint(1,2)

    # TODO: Gacha untuk jenis soal

    if operasi == 1:
        jenis = randint(1,2)

        if jenis == 1:
            tipe = "longitudinal"
            a1 = "regangan" ; a2 = "rapatan"
        elif jenis == 2:
            tipe = "tranversal"
            a1 = "bukit" ; a2 = "lembah"

        n, L, v, jawaban_benar = generateGelombang(1, 30)
        soal = (f"Sebuah gelombang {tipe} sepanjang {L} meter memiliki {n} {a1} dan {n} {a2}.\nGelombang tersebut bergerak dengan cepat rambat {v} m/s.\nTentukan berapa frekuensi gelombang tersebut (dalam Hz)!")
        t = 30

    elif operasi == 2:
        jenis = randint(1,2)

        if jenis == 1:
            tipe = "longitudinal"
            a1 = "regangan" ; a2 = "rapatan"
        else:
            tipe = "tranversal"
            a1 = "bukit" ; a2 = "lembah"

        n, jawaban_benar, v, f = generateGelombang(1, 30)
        soal = (f"Sebuah gelombang {tipe} yang bergerak dengan cepat rambat {v} m/s memiliki frekuensi {f} Hz.\nJika gelombang ini memiliki {n} {a1} dan {n} {a2},\nberapakah panjang gelombang ini (dalam m)?")
        t = 30
    
    # TODO: Ngeprint soal-soal
    x = ("".center(100,"="))
    y = ("".center(100,"="))
    
    printprintan = (soal)
    print_window()

def pilih_soal():
    # Membuat pilihan soal
    button1.config(state=DISABLED)
    list_soal = ["operasi", "luas keliling bangun", "matriks penjumlahan",
                 "GLBB", "Momentum", "Listrik", "Energi", "Gelombang"]
    pilihan_soal = choice(list_soal)
    if pilihan_soal == "operasi":
        soal_operasi()
    elif pilihan_soal == "luas keliling bangun":
        soal_Luas_Keliling_Bangun()
    elif pilihan_soal == "matriks penjumlahan":
        soal_matriks_pejumlahan()
    elif pilihan_soal == "GLBB":
        soalGLBB()
    elif pilihan_soal == "Momentum":
        soalMomentum()
    elif pilihan_soal == "Listrik":
        soalListrik()
    elif pilihan_soal == "Energi":
        soalEnergi()
    elif pilihan_soal == "Gelombang":
        soalGelombang()

# TODO: Fungsi Game
def mulai():
    global entry1, validasi_jawaban, root, button1, imgheart1, imgheart2, life, wining, losing, imgenter, outoftime, benarsalah
    entry1 = ""
    validasi_jawaban = ""
    life = 1

    root = Tk()
    root.title("Random Challenge")
    root.geometry('800x600')
    root.resizable(width=False, height=False)

    img = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\FIRST SCREEN.png"))
    imgheart1 = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\CHAL-2 SCREEN.png"))
    imgheart2 = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\CHAL-1 SCREEN.png"))
    wining = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\CORRECT ANSWER.png"))
    losing = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\WRONG ANSWER.png"))
    imgenter = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\SUBMIT BUTTON. - PIXEL png.png"))
    outoftime = ImageTk.PhotoImage(Image.open("Resource\\Challenge\\TIMEOUT.png"))

    button1 = Button(root, pady=15, padx=20, image= img,relief=FLAT, command=pilih_soal)
    button1.pack()

    root.mainloop()
    if benarsalah:
        benarsalah = False
        return True
    return benarsalah

benarsalah = False     