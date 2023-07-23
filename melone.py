import numpy as np

names = np.array([
    "latte",
    "panna",
    "saccarosio",
    "destrosio",
    "latte in polvere",
    "gomma arabica",
    "melone",
])

labels = ["g", "zucc", "gras", "SLNG", "neu", "frut", "tot solidi"]

balancer = np.array([
    # g, zucc, gras, SLNG, neu, frut, tot solidi
    [100, 4.5, 3.3, 3.5,   0, 0, 0], # latte
    [100, 3.2,  35, 2.1,   0, 0, 0], # panna
    [100, 100,   0,   0,   0, 0, 0], # saccarosio
    [100, 100,   0,   0,   0, 0, 0], # destrosio
    [100,   0,   0, 100,   0, 0, 0], # latte in polvere
    [100,   0,   0,   0, 100, 0, 0], # gomma arabica
    [100,   8,   0,   0,   0, 5, 0], # melone
])

for e in balancer:
    e[-1] = sum(e[1:])


percentage = np.array([
    0.15, # latte
    0.19, # panna
    0.08, # saccarosio
    0.04, # destrosio
    0.08, # latte in polvere
    0.01, # gomma arabica
    0.45, # melone
])
balancer = balancer *  percentage[:, np.newaxis]

limits = ["100", "16-22", "6-10", "8-11", "1-5", "/", "32-43"]


print(f"balancer:\n{labels}\n{balancer}")

tot = np.sum(balancer, axis=0)
print(f"total:\n{tot}")
print(f"limits:\n{limits}")

mult = 4
dosage = balancer[:,0] * mult
print(f"dosage:\n{dosage}")

print("-------")
print(f"dosage for {sum(dosage)}g")
for i in range(len(names)):
    print(f"- {names[i]}: {dosage[i]}")

#11