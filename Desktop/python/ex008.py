# Conversor de Medidas
metros = float(input('Uma distancia em metros: '))
km = metros/1000
hm = metros/100
am = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000

print("A medida de {} metros corresponde a: \n {}km \n {}hm \n {}am \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm" .format(metros, km, hm, am, dm, cm, mm))
