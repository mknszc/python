class Çalışan():
    kabiliyetleri = ['sınıf niteliği']
    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']
#sınıf niteliğine erişmek için #sınıf adını kullanıyoruz
print(Çalışan.kabiliyetleri)
#örnek niteliğine erişmek için #örnek adını kullanıyoruz
ahmet = Çalışan()
print(ahmet.kabiliyetleri) 
