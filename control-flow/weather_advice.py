WEATHER = input("What's the weather like today? (sunny/rainy/cold): ")
# check if the user input is sunny
if WEATHER == "sunny":
    print("Wear a t-shirt and sunglasses.")
# check if the user input is rainy
elif WEATHER == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# check if the user input is cold
elif WEATHER == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# Unexpected input by printing
else:
    print("Sorry, I don't have recommendations for this weather.")
