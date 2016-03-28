#!/usr/bin/env python3

class Auto:
    def __init__(self, nimi, nopeus, aani):
        # atribuutit jotka alkaa '__' on yksityisiä
        self.__nimi = nimi
        self.__nopeus = nopeus
        self.__aani = aani
    def setNimi(self, aani):
        self.__nimi = nimi
    def getNimi(self):
        return self.__nimi
    def setNopeus(self, nopeus):
        self.__nopeus = nopeus
    def getNopeus(self):
        return self.__nopeus
    def setAani(self, aani):
        self.__aani = aani
    def getAani(self):
        return self.__aani
    def revittele(self):
        print(self.__aani)
    def esittele(self):
        print('{0} on auto ja se sanoo: "{1}". Sen nopeus on {2} km/h'.format(
            self.__nimi,
            self.__aani,
            self.__nopeus))

def main():
    ferrari = Auto("Ferrari", 300, "WRUUMM WRUUUUMMMMM")
    lada = Auto("Lada", 90, "put put put put")
    ferrari.esittele()
    lada.esittele()

if __name__ == "__main__":
    main()
