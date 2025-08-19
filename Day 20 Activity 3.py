weather = (1, 0, 0, 0, 1, 1, 0)

rainy = 0
sunny = 0

for day in weather:
    if day == 1:
        rainy += 1
    else:
        sunny += 1

if rainy > sunny:
    print("It is likely to be rainy.")
elif sunny > rainy:
    print("It is likely to be sunny.")
else:
    print("The weather is balanced between rainy and sunny.")