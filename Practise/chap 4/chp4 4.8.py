cubes=[value**3 for value in range(1,11)]
print(cubes)



players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())