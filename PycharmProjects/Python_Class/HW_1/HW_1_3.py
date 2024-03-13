import random

# Variables to count votes for each candidate
cand1 = 0
cand2 = 0
cand3 = 0

# Number of votes
num_votes = 2500000

random.seed()

for _ in range(num_votes):
    vot = random.randint(0, 2)

    if vot == 0:
        cand1 += 1
    elif vot == 1:
        cand2 += 1
    else:
        cand3 += 1

# Display votes for each candidate
for x in range(3):
    print(f"Candidato {x + 1}: {globals()[f'cand{x + 1}']} votos")

print("\n*********************************************\n")
print("Resultados: ", end="")

# Determine the winner
if cand1 > cand2 and cand1 > cand3:
    print(f"Candidato 1 gano!!! con {cand1} votos")
elif cand2 > cand1 and cand2 > cand3:
    print(f"Candidato 2 gano!!! con {cand2} votos")
else:
    print(f"Candidato 3 gano!!! con {cand3} votos")