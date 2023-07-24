import numpy as np

names = np.array([
    "latte",
    "panna",
    "saccarosio",
    "destrosio",
    "latte in polvere",
    "gomma arabica",
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
])

for e in balancer:
    e[-1] = sum(e[1:])


percentage = np.array([
    0.55, # latte
    0.20, # panna
    0.11, # saccarosio
    0.05, # destrosio
    0.08, # latte in polvere
    0.01, # gomma arabica
])

# percentage = np.array([
#     0.38, # latte
#     0.38, # panna
#     0.10, # saccarosio
#     0.05, # destrosio
#     0.08, # latte in polvere
#     0.01, # gomma arabica
# ])
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

#11