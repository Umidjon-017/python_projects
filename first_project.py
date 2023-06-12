non = 0.99
banan = 0.99
sut = 0.68
qatiq = 0.54

a = int(input("Nechta Non oldingiz?: "))

b = float(input("Necha Kg Banan oldingiz?: "))

c = int(input("Nechta Sut oldingiz?: "))

d = int(input("Nechta Qatiq oldingiz?: "))

print("Siz " + str(a) + " ta non, " + str(b) + " kg Banan, " + str(c) + " ta Sut, " + str(d) + " ta Qatiq, " + "sotib oldingiz!")
print("Nonning narxi: ", str(float(a * non)) + " €")
print("Bananning narxi: ", str(float(b * banan)) + " €")
print("Sutning narxi: ", str(float(c * sut)) + " €")
print("Qatiqning narxi: " , str(float(d * qatiq)) + " €")

e = a * non
f = b * banan
g = c * sut
h = d * qatiq
i = e + f + g + h 

print("Ihr gesamt Einkauf kostet: ", str(float(i)) + " €")