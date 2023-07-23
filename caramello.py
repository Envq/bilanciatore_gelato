import numpy as np
np.set_printoptions(precision=2, suppress=True)

names = np.array([
    "latte",
    "panna",
    "saccarosio",
    "destrosio",
    "latte in polvere",
    "gomma arabica",
    "caramello salato",
])

labels = ["g", "zucc", "gras", "SLNG", "neu", "prot", "tot solidi"]

# zucchero  = np.array([180, 180*1,     0,        0,         0])
# burro     = np.array([ 40, 0,         40*0.82,  0,         0])
# arachidi  = np.array([ 10, 10*0.1,    10*0.53,  0,         10*0.27])
# panna     = np.array([120, 120*0.032, 120*0.35, 120*0.021, 0])


#                     g, zucc, gras, SLNG, prot
zucchero  = np.array([100, 100,  0,   0,  0])
burro     = np.array([100,   0, 82,   0,  0])
arachidi  = np.array([100,  10, 53,   0, 27])
panna     = np.array([100, 3.2, 35, 2.1,  0])
size      = np.array([180, 40, 10, 120]) / 100
tot       = sum(size)
caramelloDosage = np.array([size[0]/tot, size[1]/tot,size[2]/tot,size[3]/tot])
caramello = (zucchero*size[0] + burro*size[1] + arachidi*size[2] + panna*size[3])
caramello = caramello * (1/tot)
# [100.    52.81  22.89   0.72   0.77]
# print(caramello)
# exit(0)


balancer = np.array([
    # g, zucc, gras, SLNG, neu, prot, tot solidi
    [100,  4.5,  3.3,  3.5,   0,    0, 0], # latte
    [100,  3.2,   35,  2.1,   0,    0, 0], # panna
    [100,  100,    0,    0,   0,    0, 0], # saccarosio
    [100,  100,    0,    0,   0,    0, 0], # destrosio
    [100,    0,    0,  100,   0,    0, 0], # latte in polvere
    [100,    0,    0,    0, 100,    0, 0], # gomma arabica
    [100, 52.8, 22.9, 0.72,   0, 0.77, 0], # caramello salato
])

for e in balancer:
    e[-1] = sum(e[1:])


percentage = np.array([
    0.53, # latte
    0.06, # panna
    0.01, # saccarosio
    0.04, # destrosio
    0.05, # latte in polvere
    0.01, # gomma arabica
    0.30, # caramello salato
])
balancer = balancer *  percentage[:, np.newaxis]

limits = ["100", "16-22", "6-10", "8-11", "1-5", "/", "32-43"]


print(f"balancer:\n{labels}\n{balancer}")

tot = np.sum(balancer, axis=0)
print(f"total:\n{tot}")
print(f"limits:\n{limits}")

mult = 7
dosage = balancer[:,0] * mult
print(f"dosage:\n{dosage}")

print("-------")
print(f"dosage for {sum(dosage)}g")
for i in range(len(names)):
    print(f"- {names[i]}: {dosage[i]}")

print(dosage[-1])
print(caramelloDosage)
print(f'  - zucchero:{round(caramelloDosage[0]*dosage[-1], 2)}')
print(f'  - burro:{round(caramelloDosage[1]*dosage[-1], 2)}')
print(f'  - arachidi:{round(caramelloDosage[2]*dosage[-1], 2)}')
print(f'  - panna:{round(caramelloDosage[3]*dosage[-1], 2)}')