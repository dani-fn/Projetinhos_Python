print('Aqui, vamos converter metros em centímetros e milímetros')
m = float(input('Quantos metros quer converter? '))
cm = m * 100
mm = m * 1000
dm = m * 10
dam = m * 0.1
hm = m * 0.01
km = m * 0.001
print('{} metro(s) vale(m):\n{} mm (milímetro)\n{} cm (centímetro)\n{} dm (decímetro)\n{:.4f} dam (decâmetro)\n{} hm (hectômetro)\n{} km (quilômetro)'.format(m, mm, cm, dm, dam, hm, km))
