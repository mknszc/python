class HarfSayacı:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuüAEIİOÖUÜ'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ'
        self.bosluk_karekteri = ' '
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0
        self.sayaç_bosluk = 0
        
    def kelime_sor(self):
        return input('Bir kelime veya cümle girin: ')
    
    def seslidir(self, harf):
        return harf in self.sesli_harfler
    
    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def bosluktur(self, harf):
        return harf in self.bosluk_karekteri
    
    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            elif self.sessizdir(harf):
                self.sayaç_sessiz += 1
            elif self.bosluktur(harf):
                self.sayaç_bosluk += 1
        return (self.sayaç_sesli, self.sayaç_sessiz, self.sayaç_bosluk)
                
    def ekrana_bas(self):
        sesli, sessiz, bosluk = self.artır()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf ve {} bosluk var."
        print(mesaj.format(self.kelime, sesli, sessiz, bosluk))
        
    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayaç = HarfSayacı()
    sayaç.çalıştır() 
