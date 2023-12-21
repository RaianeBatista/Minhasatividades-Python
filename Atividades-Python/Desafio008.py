medida=float(input('Uma distância em metros: '))
km=medida/1000
hm=medida/100
dam=medida/10
dc=medida*10
cm=medida*100
mm=medida*1000
print(f'A medida em {medida}m corresponde a {km}km , {hm}hm, {dam:.0f}dam, {dc:.0f}dc,{cm:.0f}cm e {mm:.0f}mm')
