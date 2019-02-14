import serial
from math import log
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from config import *


style.use("Solarize_Light2")

def setScale(achse, intervall):
	if intervall < 0:
		achse.set_ylim(minusTemps[0], minusTemps[1])
	elif intervall > 0:
		achse.set_ylim(ueberHundertTemps[0], ueberHundertTemps[1])
	else:
		achse.set_ylim(normalTemps[0], normalTemps[1])

def messwerteZuWiederstaenden(messwerte):
	spannungenAnThermistoren = [messwert * messwertZuSpannung for messwert in messwerte]
	return [round(teilerwiederstaende[i] * spannungenAnThermistoren[i] / (systemspannung - spannungenAnThermistoren[i]),2) for i in range(6)]

def messwerteZuTemperaturen(messwerte):
	lnTherminstorWiederstaende = []
	wiederstaende = messwerteZuWiederstaenden(messwerte)
	for wiederstand in wiederstaende:
		try:
			val = np.log(wiederstand)
		except ValueError:
			val = 0
		lnTherminstorWiederstaende.append(val)

	return [(1.0/(ckoeffs[i] * lnTherminstorWiederstaende[i]**3 + bkoeffs[i] * lnTherminstorWiederstaende[i] + akoeffs[i]) - kelvinOffset) for i in range(6)]

def initSerial():
    serialConn = serial.Serial(serialPort)
    serialConn.baudrate = baudrate
    return serialConn

def readSerialData(serialConn):
    return [serialConn.read(1)[0] << 8 | serialConn.read(1)[0] for i in range(6)]

def animate(i):
	inp = readSerialData(arduino)
	n = messwerteZuTemperaturen(inp)
	t0data.append(n[0])
	del(t0data[0])
	t1data.append(n[1])
	del (t1data[0])
	t2data.append(n[2])
	del (t2data[0])
	t3data.append(n[3])
	del (t3data[0])
	t4data.append(n[4])
	del (t4data[0])
	t5data.append(n[5])
	del (t5data[0])

	t0.clear()
	t1.clear()
	t2.clear()
	t3.clear()
	t4.clear()
	t5.clear()

	setScale(t0, n[0] // 100)
	setScale(t1, n[1] // 100)
	setScale(t2, n[2] // 100)
	setScale(t3, n[3] // 100)
	setScale(t4, n[4] // 100)
	setScale(t5, n[5] // 100)

	t0.annotate(str(round(n[0], 1)), (x[-1], n[0]), xytext=(x[-1] + 1.5, n[0]), bbox=bboxprops)
	t1.annotate(str(round(n[1], 1)), (x[-1], n[1]), xytext=(x[-1] + 1.5, n[1]), bbox=bboxprops)
	t2.annotate(str(round(n[2], 1)), (x[-1], n[2]), xytext=(x[-1] + 1.5, n[2]), bbox=bboxprops)
	t3.annotate(str(round(n[3], 1)), (x[-1], n[3]), xytext=(x[-1] + 1.5, n[3]), bbox=bboxprops)
	t4.annotate(str(round(n[4], 1)), (x[-1], n[4]), xytext=(x[-1] + 1.5, n[4]), bbox=bboxprops)
	t5.annotate(str(round(n[5], 1)), (x[-1], n[5]), xytext=(x[-1] + 1.5, n[5]), bbox=bboxprops)

	t0.plot(x, t0data)
	t1.plot(x, t1data)
	t2.plot(x, t2data)
	t3.plot(x, t3data)
	t4.plot(x, t4data)
	t5.plot(x, t5data)


arduino = initSerial()

fig = plt.figure()
t0 = plt.subplot2grid((2,3), (0,0))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")
t1 = plt.subplot2grid((2,3), (0,1))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")
t2 = plt.subplot2grid((2,3), (0,2))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")
t3 = plt.subplot2grid((2,3), (1,0))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")
t4 = plt.subplot2grid((2,3), (1,1))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")
t5 = plt.subplot2grid((2,3), (1,2))
plt.xlabel("Zeit")
plt.ylabel("Tenoeratur")



dataSize = zeitspanne//messintervall
t0data = []
t1data = []
t2data = []
t3data = []
t4data = []
t5data = []
for x in range(dataSize):
	t0data.append(0)
	t1data.append(0)
	t2data.append(0)
	t3data.append(0)
	t4data.append(0)
	t5data.append(0)


x = list(range(-1*zeitspanne, 0, messintervall))
x = [a / 1000 for a in x]

bboxprops = dict(boxstyle="round", fc="w", ec="k", lw=1)

h1 = 0.02
h2 = 0.345
h3 = 0.668

v1 = 0.25
v2 = 0.75

fig.text(h1, v1, "A3", ha="center") #3
fig.text(h1, v2, "A0", ha="center") #0
fig.text(h2, v1, "A4", ha="center") #4
fig.text(h2, v2, "A1", ha="center") #1
fig.text(h3, v1, "A5", ha="center") #5
fig.text(h3, v2, "A2", ha="center") #2

if __name__ == "__main__":
	ani = animation.FuncAnimation(fig, animate, interval=1)

	plt.subplots_adjust(left=leftMargin, bottom=botMargin, right=1-rightMargin, top=1-topMargin, wspace=vspacing, hspace=hspacing)
	plt.show()

