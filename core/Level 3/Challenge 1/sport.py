class sport():
    def __init__(self,name_of_sport, sport_type, no_of_players, equipment_needed, country_of_origin, year_of_international_recognization):
        self.name_of_sport = name_of_sport
        self.sport_type = sport_type
        self.no_of_players = no_of_players
        self.equipment_needed = equipment_needed
        self.country_of_origin = country_of_origin
        self.year_of_international_recognization = year_of_international_recognization
        self.legends = []
        self.subsports = []
        
    class legendsknown:
        def __init__(self, nameofLegend,countryoflegend,currentstatusoflegend):
            self.nameofLegend = nameofLegend
            self.countryoflegend = countryoflegend
            self.currentstatusoflegend = currentstatusoflegend

    class subsport:
        def __init__(self, nameofsubsport, variationsofsubsport):
            self.nameofsubsport = nameofsubsport
            self.variationsofsubsport = variationsofsubsport

    def addalegend(self):
        name = input('Enter the name of legend : ')
        country = input('Enter the country of origin : ')
        isplaying = input('Is he still playing the sport (Y/N) : ')
        if(isplaying == 'Y'):
            isplaying = True
        else:
            isplaying = False
        self.legends.append(self.legendsknown(name, country, isplaying))
        
    def printlegends(self):
        print('S.no\t\tName\t\tCountry of Origin\t\tCurrent Status')
        for x in range(len(self.legends)):
            v = self.legends[x]
            print(x+1,'.\t\t',v.nameofLegend,'\t\t',v.countryoflegend,'\t\t\t',v.currentstatusoflegend)
    
    def printsubsports(self):
        for x in range(len(self.subsports)):
            v = self.subsports[x]
            print('Subsport ',x+1)
            print('Name : \t',v.nameofsubsport)
            print('Variations :\t ',v.variationsofsubsport)

    def addfields(self):
        n = int(input('Enter the number of fields you want to add : '))
        d = {}
        for i in range(n):
            field = input('Enter the name of field : ')
            values = input('Enter the corresponding value of the field : ')
            d[field] = values
        return d

    def addasubsport(self):
        name = input('Enter the name : ')
        variations = self.addfields()
        self.subsports.append(self.subsport(name, variations))

v = sport('','',0,'','',0)
listofsports = []
listofsports.append(sport('Cricket','outdoor',11,'bat & ball','England',1859))
def printallsports():
    print('S.No\t\tName')
    for x in range(len(listofsports)):
        v = listofsports[x]
        print(x+1,'\t\t',v.name_of_sport)
        
def createasport():
    name = str(input('Enter the name of the sport : '))
    typeofsport = str(input('Enter the type of sport : '))
    noofplayers = int(input('Enter the number of players required for the sport : '))
    equipment = str(input('Enter the equipment needed with "," as a seperator : '))
    country = str(input('Enter the country of the origin of the sport : '))
    year = int(input('Please enter the year in which ',name,' got international recognition : '))
    listofsports.append(sport(name,typeofsport,noofplayers,equipment,country,year))
    
def chooseasport(v):
    print('Choose the number of a sport : ')
    printallsports()
    i = int(input())
    v = listofsports[i-1]

def addalegend(v):
    v.addalegend()

def addasubsport(v):
    v.addasubsport()

def printasport(v):
    print('Details : ')
    print('Name : ',v.name_of_sport)
    print('Type : ',v.sport_type)
    print('Players : ', v.no_of_players)
    print('Equipment : ',v.equipment_needed)
    print('Country of origin : ',v.country_of_origin)
    print('First played : ',v.year_of_international_recognization)
    
def printlegendsofsport(v):
    v.printlegends()

def printsubsportsofsport(v):
    v.printsubsports()

def home():
    if(len(listofsports)==0):
        print('Choose one option : ')
        print('1. Create a sport')
        print('2. Exit')
        i = int(input())
        if(i==1):
            createsport()
            home()
        elif(i==0):
            return
        else:
            print('Its an invalid option : ')
            home()
    else:
        print('Choose one option :')
        print('1. Create a sport')
        print('2. Add a legend in a sport')
        print('3. Add a subsport in a sport')
        print('4. Print the details of the sport')
        print('5. Print the legends of the sport')
        print('6. Print the subsports of the sport')
        print('7. Exit')
        i = int(input())
        if(i==1):
            createasport()
            home()
        elif(i==2):
            chooseasport(v)
            addalegend(v)
            home()
        elif(i==3):
            chooseasport(v)
            addasubsport(v)
            home()
        elif(i==4):
            chooseasport(v)
            printasport(v)
            home()
        elif(i==5):
            chooseasport(v)
            printlegendsofsport(v)
            home()
        elif(i==6):
            chooseasport(v)
            printsubsportsofsport(v)
            home()
        elif(i==7):
            return
        else:
            print('Ivalid option!!!')
            home()
        
def printdict():
    for x in range(len(listofsports)):
        v = listofsports[x]
        print('Details of sport : ')
        printasport(v)
        print('Subtypes : ')
        printsubsportsofsport(v)
        print('Legends : ')
        printlegendsofsport(v)
        
 
home()
printdict()