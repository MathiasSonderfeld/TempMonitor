#Achsenabschnitte
minusTemps = -70, 10
normalTemps = 0, 100
ueberHundertTemps = 90, 150

#Optik
topMargin = 0.05
botMargin = 0.05
leftMargin = 0.05
rightMargin = 0.05
hspacing = 0.25
vspacing = 0.25

#serielle Schnittstelle
serialPort = 'COM3'
baudrate = 115200

#Messumgebung
systemspannung = 4.97
zeitspanne = 33300
messintervall = 333

#Messpunkt A0
a0_teilerwiederstand = 10023
a0_koeffA = 0.001071848
a0_koeffB = 0.000224467
a0_koeffC = 0.000000278750965602928

#Messpunkt A1
a1_teilerwiederstand = 10023
a1_koeffA = 0.001071848
a1_koeffB = 0.000224467
a1_koeffC = 0.000000278750965602928

#Messpunkt A2
a2_teilerwiederstand = 10023
a2_koeffA = 0.001071848
a2_koeffB = 0.000224467
a2_koeffC = 0.000000278750965602928

#Messpunkt A3
a3_teilerwiederstand = 10023
a3_koeffA = 0.001071848
a3_koeffB = 0.000224467
a3_koeffC = 0.000000278750965602928

#Messpunkt A4
a4_teilerwiederstand = 10023
a4_koeffA = 0.001071848
a4_koeffB = 0.000224467
a4_koeffC = 0.000000278750965602928

#Messpunkt A5
a5_teilerwiederstand = 10023
a5_koeffA = 0.001071848
a5_koeffB = 0.000224467
a5_koeffC = 0.000000278750965602928

#Konstanten
kelvinOffset = 273.15
messwertZuSpannung = systemspannung/1024


#Listen
teilerwiederstaende = [a0_teilerwiederstand, a1_teilerwiederstand, a2_teilerwiederstand, a3_teilerwiederstand, a4_teilerwiederstand, a5_teilerwiederstand]
akoeffs = [a0_koeffA, a1_koeffA, a2_koeffA, a3_koeffA, a4_koeffA, a5_koeffA]
bkoeffs = [a0_koeffB, a1_koeffB, a2_koeffB, a3_koeffB, a4_koeffB, a5_koeffB]
ckoeffs = [a0_koeffC, a1_koeffC, a2_koeffC, a3_koeffC, a4_koeffC, a5_koeffC]