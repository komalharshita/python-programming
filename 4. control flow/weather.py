weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

match weather:
    case "sunny":
        print("Great day for a picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Perfect time for a walk.")
    case "snowy":
        print("Build a snowman or go skiing!")
    case _:
        print("Unknown weather condition.")