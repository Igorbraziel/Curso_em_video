m = float(input('Digite um valor em metros: '))
km = m / 1000
hec = m / 100
dec = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{} metros equivalem a {} km, {} hectômetros, {} decâmetros, {} decímetros'.format(m, km, hec, dec, dm), end = ', ')

print('{} centímetros e a {} milímetros'.format(cm, mm))