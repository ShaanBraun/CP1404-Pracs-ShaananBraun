HEX_COLORS = {"ALICEBLUE": "#f0f8ff", "BEIGE": "#f5f5dc", "BLUEVIOLET": "#8a2be2", "BROWN": "#a52a2a",
              "CADETBLUE": "#5f9ea0", "CHOCOLATE": "#d2691e", "CORAL": "#ff7f50", "DARKGREEN": "#006400",
              "DARKSALMON": "#e9967a", "DARKVIOLET": "#9400d3"}

color = input("Enter color: ")
while color != "":
    colorUpper = color.upper()
    if colorUpper in HEX_COLORS:
        print(color, "is", HEX_COLORS[colorUpper])
    else:
        print("Invalid color")
    color = input("Enter color: ")
