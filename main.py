import argparse

p = argparse.ArgumentParser()
p.add_argument("--barbie", type=int, default=50)
p.add_argument("--cars", type=int, default=50)
p.add_argument("--movie", choices=['melodrama', 'football', 'other'], default='other')

arr = p.parse_args()
boy = 0
factors = [100 - arr.barbie, arr.cars]

if arr.barbie < 0 or arr.barbie > 100:
    arr.barbie = 50
if arr.cars < 0 or arr.cars > 100:
    arr.cars = 50
if arr.movie == 'melodrama':
    factors.append(0)
elif arr.movie == 'football':
    factors.append(100)
else:
    factors.append(50)

for f in factors:
    if f < 0:
        boy = 0
    elif f > 100:
        boy += 100
    else:
        boy += f

if boy % 3 > 1.5:
    boy = int(boy / 3) + 1
else:
    boy = int(boy / 3)
print(f"boy: {boy}\ngirl: {100 - boy}")