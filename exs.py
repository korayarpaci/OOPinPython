#Bir Sekil sınıfı tanımla ve bu sınıftan türetilmiş Ucgen ve Kare sınıfları oluştur.
#	•	Ucgen için taban ve yükseklik değerlerini alıp alanı hesaplayan bir alan_hesapla metodu yaz.
#	•	Kare için kenar uzunluğunu alıp alanı hesaplayan bir alan_hesapla metodu yaz.
#Son olarak, her iki şekli içeren bir liste oluştur ve her bir şeklin alanını polimorfizm kullanarak ekrana yazdır.
class Sekil:
    def alan_hesapla(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Ucgen(Sekil):
    def __init__(self,h,a):
        self.h = h
        self.a = a

    def alan_hesapla(self):
        return self.h * self.a / 2

class Kare(Sekil):
    def __init__(self,x):
        self.x = x

    def alan_hesapla(self):
        return self.x ** 2

ucgen = Ucgen(4,6)
kare = Kare(3)
sekil = [ucgen,kare]
for i in sekil:
    print(f"{i.__class__.__name__} alanı : {i.alan_hesapla()}")

#Bir Çalışan sınıfı tanımla ve bu sınıftan türetilmiş Mühendis ve Yönetici sınıflarını oluştur:
#•	Mühendis sınıfında maaşına ek olarak proje sayısını al ve toplam maaşı şu şekilde hesaplayan bir maas_hesapla metodu yaz:
#maaş + (proje_sayisi * 1000).
#•	Yönetici sınıfında maaşına ek olarak prim oranını (%10 gibi) al ve toplam maaşı şu şekilde hesaplayan bir
# maas_hesapla metodu yaz:
#maaş + (maaş * prim_orani).

#Son olarak, hem Mühendis hem de Yönetici nesnelerini içeren bir liste oluştur ve her bir nesnenin toplam maaşını
# polimorfizm kullanarak ekrana yazdır.

class Calisan:
    def maas_hesapla(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Muhendis(Calisan):
    def __init__(self,proje):
        self.proje = proje

    def maas_hesapla(self):
        return self.proje * 1000

class Yonetici(Calisan):
    def __init__(self,maas,primorani):
        self.maas = maas
        self.primorani = primorani

    def maas_hesapla(self):
        return self.maas + (self.maas * self.primorani)

muhendis = Muhendis(10)
yonetici = Yonetici(100,0.1)
maaslar = [muhendis,yonetici]
for i in maaslar:
    print(f"{i.__class__.__name__} maası : {i.maas_hesapla()}")

# Bir Hayvan sınıfı tanımla ve bu sınıftan türetilmiş Kedi ve Köpek sınıflarını oluştur:
# 	•	Kedi sınıfında kedinin türünü (Türk Van, Tekir gibi) ve çıkardığı sesi (miyav) sakla.
# 	Ayrıca, kedinin ses çıkarmasını sağlayan bir ses_cikar metodu tanımla.
# 	•	Köpek sınıfında köpeğin cinsi (Golden, Husky gibi) ve çıkardığı sesi (hav hav) sakla.
# 	Ayrıca, köpeğin ses çıkarmasını sağlayan bir ses_cikar metodu tanımla.
#
# Son olarak, bir kedi ve bir köpek nesnesi oluştur, bu hayvanları bir listeye ekle ve listeyi dolaşarak her
# hayvanın türü/cinsi ve çıkardığı sesi ekrana yazdır.

class Hayvan :
    def ses_cikar(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Kedi(Hayvan):
    def __init__(self,tur,ses):
        self.tur = tur
        self.ses = ses

    def ses_cikar(self):
        return self.ses

class Kopek(Hayvan):
    def __init__(self,tur,ses):
        self.tur = tur
        self.ses = ses

    def ses_cikar(self):
        return self.ses

kedi = Kedi("Tekir","Miyav")
kopek = Kopek("Golden","Hav Hav")
hayvan = [kedi , kopek]
for i in hayvan:
    print(f"{i.__class__.__name__} Türü : {i.tur} , Sesi : {i.ses_cikar()}")

# Bir Taşıt sınıfı tanımla ve bu sınıftan türetilmiş Araba ve Bisiklet sınıflarını oluştur:
# 	•	Araba sınıfında aracın yakıt türü (ör. Benzin, Dizel) ve yakıt deposu kapasitesi (litre) bilgisini sakla.
#Ayrıca, aracın menzil_hesapla metodunu tanımla; bu metod, aracın yakıt tüketim değerini (litre/100km) alarak menzili
# hesaplasın.
# 	•	Bisiklet sınıfında bisiklet türünü (ör. Dağ, Şehir) sakla. Ayrıca, bisiklet için bir pedal_cevir metodu tanımla
# 	ve “Pedal çevriliyor…” mesajı döndürsün.
# Son olarak, bir araba ve bir bisiklet nesnesi oluştur, bu taşıtları bir listeye ekle
# ve listeyi dolaşarak her taşıtın detaylarını (yakıt türü, menzil veya bisiklet türü, pedal durumu) ekrana yazdır.

class Tasit:
    def bilgi_goster(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Araba(Tasit):
    def __init__(self, yakit_turu, depo_kapasitesi):
        self.yakit_turu = yakit_turu
        self.depo_kapasitesi = depo_kapasitesi

    def menzil_hesapla(self, tuketim):
        return (self.depo_kapasitesi / tuketim) * 100

    def bilgi_goster(self):
        return f"Yakıt Türü: {self.yakit_turu}, Depo Kapasitesi: {self.depo_kapasitesi} litre"

class Bisiklet(Tasit):
    def __init__(self, tur):
        self.tur = tur

    def pedal_cevir(self):
        return "Pedal çevriliyor..."

    def bilgi_goster(self):
        return f"Bisiklet Türü: {self.tur}"

araba = Araba("Benzin", 50)
bisiklet = Bisiklet("Dağ")

tasitlar = [araba, bisiklet]

for tasit in tasitlar:
    print(f"{tasit.__class__.__name__} Bilgileri: {tasit.bilgi_goster()}")
    if isinstance(tasit, Araba):
        print(f"Menzil: {tasit.menzil_hesapla(6)} km")
    elif isinstance(tasit, Bisiklet):
        print(tasit.pedal_cevir())



## Abstract metot için örnek

from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def alan_hesapla(self):
        return self.en * self.boy

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * (self.yaricap ** 2)

dikdortgen = Dikdortgen(5, 10)
daire = Daire(7)

sekiller = [dikdortgen, daire]

for sekil in sekiller:
    print(f"{sekil.__class__.__name__} alanı: {sekil.alan_hesapla()}")

#
#Soru:

#- Bir soyut sınıf User oluşturun. User sınıfında ad ve ID attributeları yer alsın. Bu sınıfta introduce ve task adında
# soyut metotlar tanımlayın.
#- Student ve Teacher sınıflarını oluşturun. Her biri User sınıfından türetilmeli ve soyut metotları kendine uygun
# şekilde doldurmalı.
# - ID bilgisine sadece sınıf içinden erişilmesini sağlayın (encapsulation).
from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def introduce(self):
        pass
    def task(self):
        pass

class Student(User):
    def __init__(self, name, id):
        self.name = name
        self.__id = id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

class Teacher(User):
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

ogretmen = Teacher("TALU", 1)
ogrenci = Student("Koray", 2)
print(ogretmen.get_name())
print(ogretmen.get_id())
print(ogrenci.get_name())
print(ogrenci.get_id())



# Soru:
# 	•	Bir soyut sınıf Employee oluşturun. Employee sınıfında ad, ID, ve maas attributeları yer alsın.
# 	Bu sınıfta performans_degerlendir ve maas_arttir adında soyut metotlar tanımlayın.
# 	•	Manager ve Engineer sınıflarını oluşturun. Her biri Employee sınıfından türetilmeli
# 	ve soyut metotları kendine uygun şekilde doldurmalı.
# 	•	Manager sınıfı, Engineer sınıfına göre maaş artışı yaparken %20 daha fazla maaş artırmalıdır.
# 	•	ID bilgisine sadece sınıf içinden erişilmesini sağlayın (encapsulation).
# 	•	Engineer sınıfı ayrıca, mühendislik alanı belirtmek için bolum adında bir atributa sahip olmalı.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, name, id, maas):
        self.name = name
        self.__id = id
        self.maas = maas

    def get_name(self):
        return self.name

    def get_maas(self):
        return self.maas

    @abstractmethod
    def performans_degerlendir(self):
        pass

    @abstractmethod
    def maas_arttir(self):
        pass

class Manager(Employee):
    def __init__(self, name, id, maas):
        super().__init__(name, id, maas)

    def performans_degerlendir(self):
        return "İyi Performans Gösterdi"

    def maas_arttir(self):
        return self.maas + self.maas * 0.2

class Engineer(Employee):
    def __init__(self, name, id, maas, bolum):
        super().__init__(name, id, maas)
        self.bolum = bolum

    def performans_degerlendir(self):
        return "İyi Performans Gösterdi"

    def maas_arttir(self):
        return self.maas + self.maas * 0.1

manager = Manager("Koray", 1, 1000)
engineer = Engineer("Korcan", 2, 2000, "Yazılım")
print(f"Manager Ad: {manager.get_name()}")
print(f"Engineer Ad: {engineer.get_name()}")
print(f"Manager Maaş : {manager.maas_arttir()}")
print(f"Engineer Maaş: {engineer.maas_arttir()}")