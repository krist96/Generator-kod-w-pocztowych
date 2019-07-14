class Strings:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def taskOne(self):
        self.x = self.string1.split("-") #Zapisuje pierwszy kod pocztowy do tablicy, rozdzielając na dwa indeksy
        self.y = self.string2.split("-") #Zapisuje drugi kod pocztowy do tablicy, rozdzielając na dwa indeksy
        self.xConvert = "".join(self.x) #do zmiennej xConvert konwertuje tablice na stringa
        self.yConvert = "".join(self.y) #do zmiennej yConvert konwertuje tablice na stringa

        if(int(self.xConvert) < int(self.yConvert)):   #Sprawdza czy kod pocztowy 1 zapisany w formacie int jest mniejszy od kodu pocztowego dwa zapisanego w formacie int
            diff1 = int(self.yConvert) - int(self.xConvert) #Zapisujemy do diff1różnicę między mniejszym a większym kodem pocztowym
            print("Wywoluje funkcje 1: ")
            self.fDifference(self.xConvert, diff1)

        if(int(self.xConvert) > int(self.yConvert)):   #Sprawdza czy kod pocztowy 1 zapisany w formacie int jest większy od kodu pocztowego dwa zapisanego w formacie int
            diff2 = int(self.xConvert) - int(self.yConvert) #Zapisujemy do diff1różnicę między mniejszym a większym kodem pocztowym
            print("Wywoluje funkcje 2: ")
            self.fDescending(self.xConvert, diff2)

##Funkcja wypisująca rosnąco różnice
    def fDifference(self, xConvert, diff1):
        x = xConvert
        n = -1
        tab = []
        k = int(str(x))
        while(n < diff1):
            tab.append( str(x[0:2]) + '-' + str(x[2:5]) )
            k += 1
            x = str(k)
            n += 1
        print(tab)

##Funkcja wypisująca malejąco różnicę
    def fDescending(self, xConvert, diff2):
        x = xConvert
        n = -1
        tab = []
        k = int(str(x))
        while(n < diff2):
            tab.append( str(x[0:2]) + '-' + str(x[2:5]) )
            k -= 1
            x = str(k)
            n += 1
        print(tab)
    

##Wywyołanie przypadku dla funkcji wypisującej kody pocztowe rosnąco
strings = Strings("79-900", "80-155")
strings.taskOne()

##Wywyołanie przypadku dla funkcji wypisującej kody pocztowe malejąco
stringss = Strings("80-155", "79-900")
stringss.taskOne()
