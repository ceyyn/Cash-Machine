from tkinter import*

window = Tk()
window.geometry("768x480")
window.tk_setPalette("#8B7D6B")
window.title("                                                                                                          Cash Bank")

apply = Frame(window)
apply.grid()

class cash:

    def __init__(self):
        self.mevcut_tutar = 0;
        self.anaekran(),

    def malzemeler(self):
# ekrandaki checkbox ları yok eder ki ekran değiştiğinde görünmesinler
        
        self.faturaode.destroy()
        self.paracek.destroy()
        self.parayatır.destroy()
        self.bakiyesorgula.destroy()
        self.paratransfer.destroy()
        self.exit.destroy()
# geri butonunu koyar her check box komutunda kullanıldığı  için ikisini bir fonksiyona atadım ki kolaylık olsun
        self.geri_buton.place(x = 20, y = 20)

    def para_cek(self):
# gerekli butonu koyar ve ekranı temizler
        self.malzemeler()
# değer girilecek olan entry kutusunu ekrana belirtilen kordinatlara koyar
        self.para_cek_entry.place(x = 320,y = 230)
# labeli ekrana yazdırır
        self.para_cek_label.place(x = 320, y = 170)
        self.buton.config(command=self.cek_onayla)
# onayla butonunu koyar
        self.buton.place(x = 670, y = 420)

    def para_yatır(self):
# gerekli butonu koyar ve ekranı temizler
        self.malzemeler()
        # self.Para_yatır = self.para_yatır_entry.get()
# labeli ekrana yazdırır
        self.para_yatır_label.place(x = 320, y =170)
        self.para_yatır_entry.place(x = 320, y = 230)
        self.buton.config(command=self.yatir_onayla)
# değer girilecek olan entry kutusnu ekrana belirtilen kordinatlara koyar
        self.buton.place(x = 670, y = 420)

    def bakiye_sorgula(self):
        self.faturaode.destroy()
        self.paracek.destroy()
        self.parayatır.destroy()
        self.bakiyesorgula.destroy()
        self.paratransfer.destroy()
        self.exit.destroy()
        self.ekran()
        self.basariLabel.config(text="Bakiye sorgulama işlemi için bir miktar ücret talep edilir.\n Onaylıyor musunuz?")
        self.basari_buton.config(text="Onaylıyorum",command=self.bakiyebuton)

    def geri(self):
        self.geri_buton = Button(window, text="← Geri", bg="#6495ED", fg="white", command = self.Destroy)

    def Yetersiz(self):
        self.yetersiz = Label(window, text="Bakiye yetersiz.", fg="#8B2323")
        
    def fatura_ode(self):
        self.elektrik = Checkbutton(window, text = "Elektrik Faturası →",font=20,command=self.fatura)
        self.elektrik.place(x = 50, y = 50)
# gerekli butonu koyar ve ekranı temizler
        self.malzemeler()
# onayla butonunu ekrana koyar
        self.buton.place(x = 670, y = 420)
    
    def para_transfer(self):
# gerekli butonu koyar ve ekranı temizler
        self.malzemeler()
# onayla butonunu ekrana koyar
        self.buton.place(x = 670, y = 420)
        self.transfer_entry.place(x =320 , y = 230)
        self.transfer_kisi_label.place(x = 300, y = 170)
        self.buton.config(command=self.tranfer_devam)

    def fatura(self):
        self.elektrik.destroy()
# gerekli butonu koyar ve ekranı temizler
        # self.malzemeler()
        

# labeli ekrana yazdırır
        self.fatura_label.place(x = 320, y =170)
        self.para_cek_entry.place(x = 320, y = 230)
        self.buton.config(command=self.cek_onayla)
# değer girilecek olan entry kutusnu ekrana belirtilen kordinatlara koyar
        self.buton.place(x = 670, y = 420)
   
    def anaekran(self):
# bakiye sorgula ya b asıldığında ekranda gösterilcek olan baikye değişkenini mavcut_tutar_label labeline ekler ve label olara tanımlar
        self.mevcut_tutar_label = Label(window, text="Mevcut Tutar " + str(self.mevcut_tutar) + "$", bg="#8B8378", fg="white" ,height=5 , width=20, font=("Times 20 italic"))

# geri_buton butonunu tanımlar
        self.geri()

# para_cek fonksiyonunu entry sini tanımlar
        self.para_cek_entry= Entry(window,  bg="white", fg="black" )

# para_yatır fonksiyonun entry sini tanımlar
        self.para_yatır_entry = Entry(window, bg = "white", fg="black")
# para transferinin entrylerini tanımlar
        self.transfer_entry = Entry(window, bg="white", fg= "black")
        self.transfer_money_entry = Entry(window, bg="white", fg="black")
# ekranda yazılan ne kadar çekecek/yatıracaksınız yazılarını label olarak tanımlar
        self.para_cek_label = Label(window,text = "Ne kadar çekeceksiniz : ", font= 15)
        self.para_yatır_label = Label(window,text = "Ne kadar yatıracaksınız : ", font= 15)
        self.fatura_label = Label(window,text = "Faturanız ne kadar :", font= 15)
        self.transfer_kisi_label = Label(window, text= "Göndermek istediğiniz kişinin IBAN no'sunu giriniz :", font = 15)
        self.transfer_money_label = Label(window, text="Göndermek istediğiniz tutarı giriniz :", font = 15)
# check butonların özelliklerini belirler.
        self.paracek = Checkbutton(apply, text="Para çek →", font= 20 ,height= 5, width= 20, command=self.para_cek)
        self.parayatır = Checkbutton(apply, text="Para yatır →", font = 20, heigh= 5, width=20, command=self.para_yatır)
        self.bakiyesorgula = Checkbutton(apply, text="Bakiye sorgula →", font= 20, height=5, width=20 ,command=self.bakiye_sorgula)
        self.faturaode = Checkbutton(apply, text="Fature öde →", font=20, height=5,width=20, command=self.fatura_ode)
        self.paratransfer = Checkbutton(apply, text="Para transferi →", font=20, height=5,width=20, command=self.para_transfer)
        self.buton = Button(window, text="Onayla", font= 10, bg="#6495ED", fg="white")
# çıkış tuşunu tanımlar 
        self.exit= Button(window, text="Exit ↲", fg="white", bg="#6495ED",command=quit)
# check butonlarını ekrana belirtilen kordinatlarda koyar
        self.paracek.grid(row = 0)
        self.parayatır.grid(row = 100)
        self.faturaode.grid(row = 300)
        self.bakiyesorgula.grid(row = 500) 
        self.paratransfer.grid(padx = 270, pady=0)
# çıkış tuşunu ekrana koyar
        self.exit.place(x = 700,y=450)

    def cek_onayla(self):
        self.Para_cek = str(self.para_cek_entry.get())
        self.Para_cek = int(self.Para_cek)
        if self.Para_cek > self.mevcut_tutar:
                self.Yetersiz()
                self.yetersiz.place(x = 320, y =270)
        else:   
                self.mevcut_tutar -= self.Para_cek
                self.basari()
    
    def yatir_onayla(self):
        self.Para_yatır = str(self.para_yatır_entry.get())
        self.Para_yatır = int(self.Para_yatır)
        self.mevcut_tutar += self.Para_yatır
        self.basari()

    def Destroy(self):
# # ekranı labellerden ve entry kutularından temizler
        try:
            self.fatura_label.destroy()
            self.elektrik.destroy()
        finally:
                try:
                        self.yetersiz.destroy()
                finally:
                        try: 
                                self.para_cek_entry.destroy()
                                self.para_cek_label.destroy()
                        finally:
                                try:
                                        self.para_yatır_entry.destroy()
                                        self.para_yatır_label.destroy() 
                                finally:                         
                                        try:    
                                                self.geri_buton.destroy()              
                                                self.buton.destroy()
                                        finally:
                                                try:
                                                        self.mevcut_tutar_label.destroy()
                                                finally:
                                                        try: 
                                                                self.basariLabel.destroy()
                                                                self.basari_buton.destroy()
                                                        finally:
                                                                try:
                                                                        self.transfer_entry.destroy()
                                                                        self.transfer_kisi_label.destroy()
                                                                finally:
                                                                        try:
                                                                                self.transfer_money_entry.destroy()
                                                                                self.transfer_money_label.destroy()
                                                                        finally:
                                                                                self.anaekran()
    
    def ekran(self):
        self.geri()
        self.geri_buton.place(x = 20, y = 20)
        self.buton.destroy()
        self.basariLabel = Label(window, width="50", height="15", bg="#a52a2a")
        
        self.basari_buton = Button(window, width=12, height=2, command=self.ekranbuton)
        self.basariLabel.place(x = 192, y = 120)
        self.basari_buton.place(x= 440, y = 300)

    def ekranbuton(self):
        self.basariLabel.destroy()
        self.basari_buton.destroy()
        self.Destroy()
        self.anaekran()
   
    def bakiyebuton(self):
        if self.mevcut_tutar < 1:
                self.Yetersiz()
                self.yetersiz.place(x = 190, y = 120)
        else :
                self.mevcut_tutar -= 1
                self.basariLabel.destroy()
                self.basari_buton.destroy()
                self.sorgulaonayla()

        print("whala")
        self.malzemeler()
        
    def basari(self):
        self.ekran()
        self.basariLabel.config(text="İşleminiz başarıyla tamamlanmıştır.")
        self.basari_buton.config(text="Ana Ekrana Dön")

    def sorgulaonayla(self):
        self.geri()
        self.geri_buton.place(x = 20, y = 20)
        self.mevcut_tutar_label.config(text="Mevcut Tutar " + str(self.mevcut_tutar) + "$")
        self.mevcut_tutar_label.place(x = 230, y = 170)
        
    def tranfer_devam(self):
        self.buton.config(command = self.transfer_onayla)
        self.transfer_kisi_label.destroy()
        self.transfer_entry.destroy()
        self.transfer_money_entry.place(x = 320, y = 230)
        self.transfer_money_label.place(x = 300, y = 170)
 
    def transfer_onayla(self):
        self.Para_cek = str(self.transfer_money_entry.get())
        self.Para_cek = int(self.Para_cek)
        if self.Para_cek > self.mevcut_tutar:
                self.Yetersiz()
                self.yetersiz.place(x = 320, y =270)
        else:   
                self.mevcut_tutar -= self.Para_cek
                self.basari()


cash()
mainloop()