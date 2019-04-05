weight = float(input("Enter your weight, please:"))
for i in range(1, 16):
    moon_weight = weight*0.165
    weight += 1
    print('Your wieght in moon in ', i, 'year', moon_weight, "kgs")
