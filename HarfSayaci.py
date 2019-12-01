class HarfSayaci:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuüAEIİOÖUÜ'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ'
        self.bosluk_karekteri = ' '
        self.sayac_sesli = 0
        self.sayac_sessiz = 0
        self.sayac_bosluk = 0
        
    def kelime_sor(self):
        return input('Bir kelime veya cümle girin: ')
    
    def seslidir(self, harf):
        return harf in self.sesli_harfler
    
    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def bosluktur(self, harf):
        return harf in self.bosluk_karekteri
    
    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            elif self.sessizdir(harf):
                self.sayac_sessiz += 1
            elif self.bosluktur(harf):
                self.sayac_bosluk += 1
        return (self.sayac_sesli, self.sayac_sessiz, self.sayac_bosluk)
                
    def ekrana_bas(self):
        sesli, sessiz, bosluk = self.artir()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf ve {} bosluk var."
        print(mesaj.format(self.kelime, sesli, sessiz, bosluk))
        
    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()
