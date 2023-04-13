class isci():
    def __init__(self,ad,soyad,cepno,departman,maas):
        self.ad = ad
        self.soyad = soyad
        self.cepno = cepno
        self.departman = departman
        self.maas = maas
    def bilgigoster(self):
        print("Bilgiler gösteriliyor...")
        print("""
            Ad: {}
            Soyad: {}
            Cep: {}
            Departman: {}
            Maaş: {}
        """.format(self.ad,self.soyad,self.cepno,self.departman,self.maas))
    def yenidep(self,yeni_dep):
        self.departman.append(yeni_dep)
        print("Yeni Departman ekleniyor..")
    def zamyap(self,zaam):
        print("Zam yapılıyor")
        self.maas += zaam
class Yönetici(isci):
    
    def yoneticiata(self):
        pass
calisan1 = isci("ISIM","SOYISIM","CEP",["DEPARTMAN"],63200)
calisan1.zamyap(80522)
calisan1.yenidep("Müdüriyet")
print(calisan1.bilgigoster())

