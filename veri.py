import mysql.connector
#from PyQt5 import QtWidgets


#fetochone() sorgunun ilk sonucunu getirir.


connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='Ceren594',
                             db='mydb')

myCursor=connection.cursor()
myCursor2=connection.cursor()

kargomaliyetleri=[]
sonuc=[]

def Musteriselect(search):
    search=str(search)
    myCursor = connection.cursor()
    connection.reconnect()
    sql = "Select * from musteri where MusteriAd='{MusteriAd}'".format(MusteriAd=search)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result

def MusteriselectAll():
    myCursor = connection.cursor()
    connection.reconnect()
    myCursor.execute("Select * from musteri")
    result = myCursor.fetchall()
    return result

def showTables():
    myCursor = connection.cursor()
    connection.reconnect()
    sql = "Show tables"
    myCursor.execute(sql)
    result = myCursor.fetchall()
    result = str(result)
    return result

def MusteriInsert(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql = ("Insert Into musteri (MusteriAd) Values('{MusteriAd}')").format(MusteriAd=name)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def TedarikciFinsert(name,country,city):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Insert Into tedarikcifirma (FirmaAd,Ulke,Sehir) Values('{FirmaAd}','{Ulke}','{Sehir}')").format(FirmaAd=name,
                                                                                                         Ulke=country,
                                                                                                         Sehir=city)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def TedarikciFSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()
    myCursor.execute("Select * from tedarikcifirma")
    result = myCursor.fetchall()
    return result

def TedarikciFSelect(name):
    myCursor= connection.cursor()
    connection.reconnect()
    sql=("Select * from tedarikcifirma where FirmaAd='{FirmaAd}'").format(FirmaAd=name)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def tedarikciInsert(id,name,miktar,uretimtarihi,rafomru,satisfiyati):
    myCursor = connection.cursor()
    connection.reconnect()
    id=int(id)
    miktar=int(miktar)
    rafomru=int(rafomru)

    sql = ("Insert Into tedarikci  Values({FirmaID},'{Hamİsim}',"
           "{Miktar},'{UretimTarihi}',{Rafömrü},{SatisFiyati})").format(FirmaID=id,Hamİsim=name,Miktar=miktar,UretimTarihi=uretimtarihi,
                                                                        Rafömrü=rafomru,SatisFiyati=satisfiyati)


    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def tedarikciSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()
    myCursor.execute("Select * from tedarikci")
    result = myCursor.fetchall()
    return result

def TedarikciSelect(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql = ("Select * from tedarikci where Hamİsim='{Hamİsim}'").format(Hamİsim=name)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result

def KimyasalUrunInsert(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Insert Into kimyasalurunler (UrunAd) Values ('{UrunAd}')").format(UrunAd=name)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

    sql=("select max(UrunId) from kimyasalurunler where UrunAd='{name}'").format(name=name)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    print("id",result)
    return result

def urunInsert(name,tarih,omur,id,stok):
    myCursor = connection.cursor()
    #connection.reconnect()
    omur=int(omur)
    sql = ("Insert Into urun Values ('{UrunAd}','{UretimTarih}',{RafOmru},{UrunID},{Stok},0)").format(UrunAd=name,UretimTarih=tarih,
                                                                                             RafOmru=omur,UrunID=id[0],Stok=stok)

    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()
def gelistirilenUrunInsert(name,stok):
    print("calisiyo")
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from gelistirilenurun where GelistirilenUrunAdi='{name}'").format(name=name)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    print("result",result)
    if(result==None):
         sql = ("Insert Into gelistirilenurun  Values ('{FirmaAdi}','{GelistirilenUrunAdi}',{Stok})").format(FirmaAdi="Bercer",
                                                                                              GelistirilenUrunAdi=name,
                                                                                                            Stok=stok)
    else:
        sql=("Update gelistirilenurun set Stok=Stok+{stok} where GelistirilenUrunAdi='{name}'").format(stok=stok,name=name)

    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def urunSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()
    myCursor.execute("Select * from urun")
    result = myCursor.fetchall()
    return result

def selectStok(name):
    myCursor=connection.cursor()
    connection.reconnect()
    sql=("Select Stok from gelistirilenurun where GelistirilenUrunAdi='{isim}'").format(isim=name)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    return result

def urunSelect(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from urun where UrunAd='{UrunAd}'").format(UrunAd=name)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def tedarikciSelectAll2(name,miktar):  ##bir yerden toptan hammadde alma
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from tedarikci where Hamİsim='{Hamİsim}' and Miktar>={Miktar}").format(Hamİsim=name,Miktar=miktar)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    alisFiyati=[]
    alisFiyati.clear()

    for i in result:
            alisFiyati.append([i[0],i[5]*miktar])

    k=0

    for i in alisFiyati:
        for k in kargomaliyetleri:
         if(i[0]==k[0]):
                i[1]=i[1]+k[2]

    min=alisFiyati[0]
    for i in alisFiyati:
       if(i[1]<min[1]):
           min=i

    print(alisFiyati)
    print(min)
    print(min[1])

    return min

def parcaliSatinAlma(isim,miktar):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from tedarikci where Hamİsim='{Hamİsim}' and Miktar>0 order by SatisFiyati asc").format(Hamİsim=isim)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    parcaliSatinAl=[]
    parcaliSatinAl.clear()
    print(miktar)
    print("sql sonucu")
    print(result)

    for i in result:
        parcaliSatinAl.append([i[0],i[5],i[2]])

    k=0
    print("ilk hali")
    print(parcaliSatinAl)

    while(k < len(result)):
      if(parcaliSatinAl[k][2]<miktar):
          parcaliSatinAl[k][1]=parcaliSatinAl[k][1]*parcaliSatinAl[k][2]
          k=k+1

      elif(parcaliSatinAl[k][2]>= miktar):
          parcaliSatinAl[k][1] = parcaliSatinAl[k][1] * miktar
          parcaliSatinAl[k][2]=miktar
          k = k + 1

    print("miktarla carpılmış hali ")
    print(parcaliSatinAl)

    for i in parcaliSatinAl:
        for k in kargomaliyetleri:
            if (i[0] == k[0]):
                i[1] = i[1] + k[2]

    print("kargo eklenmiş hali")
    print(parcaliSatinAl)
    parcaliSatinAl=siralama(parcaliSatinAl)
    print("sıralanmış hali")
    print(parcaliSatinAl)
    toplamFiyat=0
    temp=0
    k=1
    if(parcaliSatinAl[0][2]<miktar):
        temp=parcaliSatinAl[0][2]
        k=1
        toplamFiyat=parcaliSatinAl[0][1]
        while(temp<miktar):
           temp=temp+parcaliSatinAl[k][2]
           toplamFiyat=parcaliSatinAl[k][1]+toplamFiyat
           k=k+1



    if(temp>miktar):
        fark=temp-miktar
        for i in result:
            if(i[0]==parcaliSatinAl[k-1][0]):
                birimFiyat=i[5]

        parcaliSatinAl[k-1][1]=  parcaliSatinAl[k-1][1]-(birimFiyat*fark)
        toplamFiyat= toplamFiyat-(birimFiyat*fark)
        parcaliSatinAl[k - 1][2]=parcaliSatinAl[k - 1][2]-fark

    parcaliSonuc(parcaliSatinAl,k)
    return toplamFiyat

def parcaliSonuc(parcaliSatinAl,len):
    sonuc.clear()
    i=0
    while(i<len):
        sonuc.append(parcaliSatinAl[i])
        i=i+1

    print(sonuc)
    return sonuc

def siralama(dizi):
    i=0
    j=0
    for i in range(len(dizi)): ## selection sort
        j=i
        while(j>0 and (dizi[j-1][1]> dizi[j][1])):
            dizi[j-1],dizi[j] = dizi[j],dizi[j-1]
            j-=1

    return dizi


def searchHammadde(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select Miktar,SatisFiyati from tedarikci where Hamİsim='{isim}' order by SatisFiyati asc").format(isim=name)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result

def kargoMaliyetiHesaplama():
    connection.reconnect()
    sql=("Select uzaklik,FirmaAd,FirmaID,Ulke,kargo.Sehir from kargo,tedarikcifirma where tedarikcifirma.sehir=kargo.sehir order by uzaklik asc")
    myCursor.execute(sql)
    result=myCursor.fetchall()
    k=0
    for i in result:
        if(i[3] != "Türkiye"):
            kargomaliyetleri.append([i[2],i[1],i[0],i[4]])
        else:
            kargomaliyetleri.append([i[2], i[1], i[0]*0.5,i[4]])

    print(kargomaliyetleri)

def hammaddeSatinAl(id,name,miktar,fiyat):
    connection.reconnect()
    sql=("Update tedarikci set Miktar=Miktar-{miktar} where Hamİsim='{name}' and FirmaID={id}").format(miktar=miktar,id=id,name=name)
    hammaddeInsert("Bercer",name,fiyat,miktar)
    myCursor2.execute(sql)
    connection.commit()


def hammaddeSelectAll():

    connection.reconnect()
    sql=("Select * from hammadde where Stok != 0")
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def clearList():
    sonuc.clear()
    print(sonuc)


def hammaddeInsert(FirmaAdi,Hammadde,Fiyat,Stok):
    myCursor = connection.cursor()
    connection.reconnect()
    sql0=("Select * from hammadde where AlinanHammade='{isim}' and AlisFiyati={fiyat}").format(isim=Hammadde,fiyat=Fiyat)
    myCursor2.execute(sql0)
    result=myCursor2.fetchone()

    if(result != None):
        sql=("Update hammadde set Stok={new}+Stok where AlinanHammade='{isim}' and AlisFiyati={fiyat}").format(new=Stok,isim=Hammadde,fiyat=Fiyat)

    else:
        sql=("Insert into hammadde (FirmaAdi,AlinanHammade,AlisFiyati,Stok) values ('{FirmaAdi}','{AlinanHammade}',"
         "{AlisFiyati},{Stok})").format(FirmaAdi=FirmaAdi,AlinanHammade=Hammadde, AlisFiyati=Fiyat, Stok=Stok)

    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def bilesenSelect(ad,bilesen):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from bilesenler where GelistirilenUrunAdi='{name}' and BilesenAdi='{bilesen}'").format(name=ad,bilesen=bilesen)

    myCursor.execute(sql)
    result=myCursor.fetchone()
    return result

def bilesenSelect2(ad):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from bilesenler where GelistirilenUrunAdi='{name}'").format(name=ad)

    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def bilesenInsert(ad,bilesen,miktar):
    myCursor = connection.cursor()
    #connection.reconnect()
    print("calisiyo")
    print(ad,bilesen,miktar)

    result = bilesenSelect(ad, bilesen)
    print(result)

    if(result == None):
        print("if")
        sql=("Insert into bilesenler Values ('{GelistirilenUrunAdi}','{BilesenAdi}',{Miktar})")\
            .format(GelistirilenUrunAdi=ad,BilesenAdi=bilesen,Miktar=miktar)
        myCursor.execute(sql)
        connection.commit()
        connection.reconnect()

def bilesenKontrol(name):
    myCursor = connection.cursor()
    connection.reconnect()
    print(name)
    sql=("Select Stok from hammadde where AlinanHammade='{AlinanHammade}' ").format(AlinanHammade=name)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    toplamStok=0
    for i in result:
        toplamStok=toplamStok+i[0]

    return toplamStok

def BilesenSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from bilesenler")
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def BilesenSelect(name):
    myCursor = connection.cursor()
    connection.reconnect()
    sql = ("Select * from bilesenler where GelistirilenUrunAdi='{name}'").format(name=name)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result

def insertMaliyetler(id,hamToplam):
    print("eklendi",id[0],hamToplam)
    myCursor = connection.cursor()
    connection.reconnect()
    kosul=selectMaliyetler(id[0])
    print(kosul)

    if(kosul==None):
        sql=("Insert into maliyetler (UrunID,HamToplam) values ({id},{hamtoplam})").format(id=id[0],hamtoplam=hamToplam)
        myCursor.execute(sql)
        connection.commit()
        connection.reconnect()
    else:
        print("guncellendi")
        print(hamToplam)
        sql=("Update maliyetler set HamToplam=HamToplam+{HamToplam} where UrunID={UrunID}").format(HamToplam=hamToplam,UrunID=id[0])
        myCursor.execute(sql)
        connection.commit()
        connection.reconnect()

def selectMaliyetler(id):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from maliyetler where UrunID={UrunID}").format(UrunID=id)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    return result


def updateHammadde(isim,miktar,fiyat,id,birimfiyat):
    #myCursor = connection.cursor()
    connection.reconnect()
    sql=("Update hammadde set Stok=Stok-{miktar} where AlisFiyati={fiyat} and AlinanHammade='{name}'").format(miktar=miktar,fiyat=fiyat,name=isim)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()
    insertMaliyetler(id,birimfiyat*miktar)

def updateAlisFiyati(name,fiyat,birimfiyat,miktar):
    myCursor = connection.cursor()
    connection.reconnect()
    birim=birimfiyat*miktar
    sql=("Update hammadde set AlisFiyati=AlisFiyati-{birim} where AlinanHammade='{name}' and AlisFiyati={fiyat}").format(name=name,fiyat=fiyat,birim=birim)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def setIscilik(id,fiyat):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Update maliyetler set Iscilik={fiyat} where UrunID={id} ").format(fiyat=fiyat,id=id[0])
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

    sql=("Update maliyetler set Toplam=HamToplam+İscilik where UrunID={id} ").format(id=id[0])
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def hammaddeDusme(isim,miktar,id):
    myCursor = connection.cursor()
    connection.reconnect()
    print(isim,miktar)
    sql=("Select * from hammadde where AlinanHammade='{name}' and Stok>0 order by AlisFiyati asc ").format(name=isim)

    while(miktar>0):
        print(miktar)
        myCursor.execute(sql)
        result = myCursor.fetchone()
        print(result)
        if(result[2]>miktar):
            birimFiyat=result[4]/result[2]
            updateHammadde(isim,miktar,result[4],id,birimFiyat)
            updateAlisFiyati(isim,result[4],birimFiyat,miktar)
            miktar=0
        else:
            birimFiyat = result[4] / result[2]
            updateHammadde(isim, result[2], result[4],id,birimFiyat)
            miktar=miktar-result[3]
            updateAlisFiyati(isim,result[4],birimFiyat,result[2])

def maliyetSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from maliyetler")
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def updateKar(kar,urunId):
    myCursor = connection.cursor()
    connection.reconnect()
    sql = ("Update maliyetler set karOrani={kar} where UrunID={id} ").format(kar=kar,id=urunId)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

    sql = ("Update maliyetler set SatisFiyati=Toplam+((Toplam/100)*karOrani) where UrunID={id} ").format(id=urunId)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

    sql= ("Select SatisFiyati,Toplam from maliyetler where UrunID={id}").format(id=urunId)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    toplamKar=result[0]-result[1]

    sql=("Update urun set SatisFiyati={result} where UrunID={id}").format(result=result[0],id=urunId)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

    sql=("Select Stok from urun where UrunID={id}").format(id=urunId)
    myCursor.execute(sql)
    result2=myCursor.fetchone()

    birimKar=toplamKar/result2[0]
    return birimKar


def SelectMaliyetler(id):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Select * from maliyetler where UrunID={UrunID}").format(UrunID=id)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    print(result)
    return result

def insertSiparis(id,adres,talep,miktar):
    myCursor = connection.cursor()
    connection.reconnect()
    sql=("Insert into siparis values({id},'{adres}','{talep}',{miktar})").format(id=id,adres=adres,talep=talep,miktar=miktar)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def selectStok(name):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select Stok from gelistirilenUrun where GelistirilenUrunAdi='{name}'").format(name=name)
    myCursor.execute(sql)
    result=myCursor.fetchone()
    print(result)
    return result

def selectMinFiyat(name):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select UrunID,Stok from urun where UrunAd='{name}' order by SatisFiyati asc").format(name=name)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result

def updateStok(id,miktar):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Update urun set Stok=Stok-{Miktar} where UrunID={id}").format(Miktar=miktar,id=id)
    myCursor.execute(sql)
    connection.commit()
    connection.reconnect()

def siparisSelectAll():
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from siparis")
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result

def siparisSelect(id):
    myCursor = connection.cursor()
    connection.reconnect()

    sql=("Select * from siparis where MusteriId={id}").format(id=id)
    myCursor.execute(sql)
    result=myCursor.fetchall()
    return result