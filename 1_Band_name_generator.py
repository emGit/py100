name = input("What's your name? \n")
print(f'\nHello, {name}!')
city = input(f'\nSo, {name}, where did you grow up? \n').lower()
pets = input('\nDo you have any pets? \n').lower()

if pets[0]=="y": pet_name = input("\nWhat is your pet's name?\n")
else:
  print("\nAh, I see.")
  import random
  pet_name = random.choice(["Cosmo", "Fluff", "Korra", "Wiggles", "Roach"])
print(f'\nI think {pet_name}{city} would make a sick band name for you.')
