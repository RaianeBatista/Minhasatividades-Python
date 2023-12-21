larg=float(input('larguda da parede: '))
alt=float(input('altura da parede: '))
area=larg*alt
print(f'Sua parede tem dimensão de {larg}mx{alt}m e a sua área é de {area}m².')
tinta=area/2
print(f'Para pintar essa parede você precisará de {tinta:.2f}l de tinta')
