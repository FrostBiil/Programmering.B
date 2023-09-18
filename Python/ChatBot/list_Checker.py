def remove_duplicates(input_list):
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Your custom_color_palette list
custom_color_palette = {
    "White": "#FFFFFF",
    "Silver": "#C0C0C0",
    "Gray": "#808080",
    "Black": "#000000",
    "Red": "#FF0000",
    "Maroon": "#800000",
    "Yellow": "#FFFF00",
    "Olive": "#808000",
    "Lime": "#00FF00",
    "Green": "#008000",
    "Aqua": "#00FFFF",
    "Teal": "#008080",
    "Blue": "#0000FF",
    "Navy": "#000080",
    "Fuchsia": "#FF00FF",
    "Purple": "#800080",
    "Magenta": "#FF00FF",
    "Tulip Pink": "#FF8E8E",
    "Piggy Pink": "#FDDDE6",
    "Cotton Candy": "#FFBCD9",
    "Cameo Pink": "#EFBBCC",
    "French Pink": "#F64A8A",
    "Persian Pink": "#F77FBE",
    "Candy Pink": "#E4717A",
    "Cherry Pink": "#DE3163",
    "Dark Terra Cotta": "#CC4E5C",
    "Deep Pink": "#FF1493",
    "Dust Storm": "#E5CCC9",
    "Nadeshiko Pink": "#F6ADC6",
    "Wild Strawberry": "#FF43A4",
    "Rubine Red": "#D10056",
    "Hollywood Cerise": "#F400A1",
    "Mexican Pink": "#E4007C",
    "Steel Pink": "#CC3366",
    "Rose Bonbon": "#F9429E",
    "Orange": "#ED7014",
    "Tangerine": "#FA8128",
    "Merigold": "#FCAE1E",
    "Cider": "#B56727",
    "Rust": "#8D4004",
    "Ginger": "#BE5504",
    "Tiger": "#FC6A03",
    "Fire": "#DD571C",
    "Bronze": "#B2560D",
    "Cantaloupe": "#FDA172",
    "Apricot": "#ED820E",
    "Clay": "#80400B",
    "Honey": "#EC9706",
    "Carrot": "#ED7117",
    "Squash": "#C95B0C",
    "Spice": "#7A3803",
    "Marmalade": "#D16002",
    "Amber": "#893101",
    "Sandstone": "#D67229",
    "Yam": "#CC5801",
    "Tangelo": "#FC4C02",
    "Flame": "#E34A27",
    "Fulvous": "#E68000",
    "Dark Orange": "#FF8C00",
    "Vivid Orange": "#FF5E0E",
    "Orange-Red": "#FF4500",
    "Metallic Orange": "#E26310",
    "Pumpkin": "#F5761A",
    "Smashed Pumpkin": "#FD673A",
    "International Orange": "#FF4F00",
    "Spanish Orange": "#F06105",
    "Princeton Orange": "#FF8F00",
    "Deep Saffron": "#FFA52C",
    "Alloy Orange": "#C35214",
    "Halloween Orange": "#EE5921",
    "Gamboge": "#E89611",
    "Medium Vermilion": "#CF5B2E",
    "Pastel Orange": "#FEBA4F",
    "Philippine Orange": "#F26E01",
    "Royal Orange": "#FF9944",
    "Coral": "#FF7F50",
    "Dark Coral": "#D75341",
    "Cadmium Orange": "#E6812F",
    "Rajah": "#FABA5F",
    "Mango Tango": "#FB8842",
    "Orange Peel": "#FF9F00",
    "Vivid Tangelo": "#EC7625",
    "Persimmon": "#EC5800",
    "Browns Orange": "#FF3C00",
    "Burnt Orange": "#CC5500",
    "Tan": "#E6DBAC",
    "Beige": "#EEDC9A",
    "Macaroon": "#F9E076",
    "Hazel Wood": "#C9BB8E",
    "Granola": "#D6B85A",
    "Oat": "#DFC98A",
    "Egg Nog": "#FAE29C",
    "Fawn": "#C8A951",
    "Sugar Cookie": "#F3EAAF",
    "Sand": "#D8B863",
    "Sepia": "#E3B778",
    "Latte": "#E7C27D",
    "Oyster": "#DCD7A0",
    "Biscotti": "#E3C565",
    "Parmesan": "#FDE992",
    "Hazelnut": "#BDA55D",
    "Sandcastle": "#DAC17C",
    "Buttermilk": "#FDEFB2",
    "Sand Dollar": "#EDE8BA",
    "Shortbread": "#FBE790",
    "Citrine": "#E4D00A",
    "Flax": "#EEDC82",
    "Xanthic": "#EEED09",
    "Sunshine Yellow": "#FFFD37",
    "Canary Yellow": "#FFEF00",
    "Lemon Yellow": "#FDFF00",
    "Pale Goldenrod": "#EEE8AA",
    "Light Khaki": "#F0E68C",
    "Clover Lime": "#FCE883",
    "Royal Yellow": "#FADA5E",
    "Gold": "#FFD700",
    "Safety Yellow": "#EED202",
    "Laguna": "#F8E473",
    "Bright Yellow": "#FFFD01",
    "Greenish Yellow": "#EEEA62",
    "Sunflower": "#FFDA03",
    "Bumblebee": "#FCE205",
    "Butter": "#FFFD74",
    "Yellow Tan": "#FFE36E",
    "Banana": "#FFE135",
    "Tuscany": "#FCD12A",
    "Dijon": "#C49102",
    "Mustard": "#FEDC56",
    "Maximum Yellow": "#FAFA37",
    "Mellow Yellow": "#F8DE7E",
    "Unmellow Yellow": "#FFFF66",
    "Lemon Curry": "#CCA01D",
    "Aureolin": "#FDEE00",
    "Electric Yellow": "#FFFF33",
    "Pastel Yellow": "#FFFE71",
    "Green": "#3CB043",
    "Chartreuse": "#B0FC38",
    "Juniper": "#3A5311",
        "Olive Drab": "#6B8E23",
    "Sap Green": "#507D2A",
    "Grass Green": "#3F9142",
    "Green Thumb": "#49A34D",
    "Apple Green": "#8DB600",
    "Yellow Green": "#C5E17A",
    "Kelly Green": "#4CBB17",
    "Mantis": "#74C365",
    "Pistachio": "#9DC209",
    "Emerald": "#50C878",
    "Forest Green": "#228B22",
    "Green Peas": "#3EAF76",
    "Jade": "#00A86B",
    "Magic Mint": "#AEDD81",
    "Greenery": "#88B04B",
    "Lime Green": "#32CD32",
    "Celadon": "#ACE1AF",
    "Mint": "#3EB489",
    "Honeydew": "#F0FFF0",
    "Pastel Green": "#77DD77",
    "Spring Green": "#00FF7F",
    "Light Green": "#90EE90",
    "Chartreuse Green": "#7FFF00",
    "Green Yellow": "#ADFF2F",
    "Lawn Green": "#7CFC00",
    "Bright Green": "#66FF00",
    "Medium Spring Green": "#00FA9A",
    "Electric Green": "#00FF00",
    "Neon Green": "#39FF14",
    "Harlequin": "#3FFF00",
    "Yellow Green": "#32CD32",
    "Dark Green": "#006400",
    "Forest": "#228B22",
    "Pine Green": "#01796F",
    "Jungle Green": "#29AB87",
    "Teal Green": "#006D5B",
    "Blue Green": "#007D65",
    "Turquoise": "#40E0D0",
    "Light Sea Green": "#20B2AA",
    "Medium Aquamarine": "#66CDAA",
    "Medium Turquoise": "#48D1CC",
    "Aquamarine": "#7FFFD4",
    "Turquoise Blue": "#00CED1",
    "Dark Turquoise": "#00CED1",
    "Cadet Blue": "#5F9EA0",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Sky Blue": "#87CEEB",
    "Light Sky Blue": "#87CEFA",
    "Deep Sky Blue": "#00BFFF",
    "Dodger Blue": "#1E90FF",
    "Cornflower Blue": "#6495ED",
    "Steel Blue": "#4682B4",
    "Royal Blue": "#4169E1",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Navy Blue": "#000080",
    "Midnight Blue": "#191970",
    "Ice Blue": "#D4F1F9",
    "Baby Blue": "#89CFF0",
    "Cerulean Blue": "#007BA7",
    "Azure": "#F0FFFF",
    "Light Cyan": "#E0FFFF",
    "Pale Turquoise": "#AFEEEE",
    "Aqua Blue": "#00FFFF",
    "Turquoise Green": "#00CED1",
    "Aquamarine Blue": "#71D9E2",
    "Iceberg": "#71A6D2",
    "Baby Blue Eyes": "#A1CAF1",
    "Bice Blue": "#CFECEC",
    "Columbia Blue": "#C4D8E2",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Ghost White": "#F8F8FF",
    "Lavender": "#E6E6FA",
    "Lilac": "#C8A2C8",
    "Glitter": "#E6E8FA",
    "Lavender Gray": "#C4C3D0",
    "Black": "#000000",
    "Ebony": "#555D50",
    "Crow": "#696969",
    "Charcoal": "#36454F",
    "Midnight": "#191970",
    "Ink": "#4B0082",
    "Raven": "#727272",
    "Oil": "#0A0A0A",
    "Grease": "#171717",
    "Onyx": "#0F0F0F",
    "Pitch": "#313131",
    "Soot": "#313131",
    "Sable": "#051317",
    "Jet Black": "#010101",
    "Coal": "#080808",
    "Metal": "#0E0C0A",
    "Obsidian": "#020403",
    "Jade": "#000302",
    "Spider": "#040200",
    "Leather": "#0B0705",
    "Asphalt": "#0C0404",
    "Licorice": "#1A1110",
    "Night": "#0C090A",
    "Charleston Green": "#232B2B",
    "Dark Jungle Green": "#1A2421",
    "Eerie Black": "#1B1B1B",
    "Raisin Black": "#242124",
    "Smoky Black": "#100C08",
    "Black Rock": "#010127",
    "Neutral Black": "#0B0B0B",
    "Black Denim": "#191C27",
    "Vampire Black": "#0F0404",
    "Cool Black": "#151922",
    "Frost Black": "#191C20",
    "Power Black": "#0E0C01",
    "Premium Black": "#100E09",
    "Black Magic": "#0B0510",
    "Alien Black": "#1A2228",
    "Black Chocolate": "#1B1811",
    "Gothic Grape": "#120321",
    "Metropolis": "#1A1A1A",
    "Night Shadow": "#1C1C1C",
    "Dark Raisin": "#1A0F0F",
    "Tea Bag": "#161311",
    "Tech Black": "#0D0E0E",
    "Dull Black": "#161616",
    "Dark Black": "#010203",
    "Natural Black": "#07000B",
    "Retro Black": "#1F201F",
        "Deep Black": "#050203",
    "Natural Black": "#07000B",
    "Retro Black": "#1F201F",
    "Deep Space Sparkle": "#4A646C",
    "Black Cat": "#4D0135",
    "Eerie Black": "#1B1B1B",
    "Green Black": "#03231E",
    "Space Black": "#0D041E",
    "Blackberry": "#4D0135",
    "Black Coffee": "#3B2F2F",
    "Blast Off Bronze": "#A57164",
    "Bronze": "#CD7F32",
    "Dark Bronze": "#804A00",
    "Copper": "#B87333",
    "Bronze Gold": "#85754E",
    "Fool's Gold": "#FFD700",
    "Golden Yellow": "#FFDF00",
    "Harvest Gold": "#DA9100",
    "Midas Gold": "#E6BE8A",
    "Old Gold": "#CFB53B",
    "Rich Gold": "#A96217",
    "School Bus Yellow": "#FFD800",
    "Sun Yellow": "#FFCC00",
    "Yellow Orange": "#FFAE42",
    "Golden Poppy": "#FCC200",
    "Orange": "#FFA500",
    "Amber": "#FFBF00",
    "Bittersweet": "#FF6F61",
    "Burnt Orange": "#FF7034",
    "Cadmium Orange": "#ED872D",
    "Carrot Orange": "#ED9121",
    "Dark Orange": "#FF8C00",
    "Mango Tango": "#FF8243",
    "Neon Carrot": "#FFA343",
    "Orange Peel": "#FF9F00",
    "Persimmon": "#FF6347",
    "Pumpkin": "#FF7518",
    "Red Orange": "#FF5349",
    "Tangerine": "#FFA07A",
    "Tomato": "#FF6347",
    "Vermilion": "#E34234",
    "Red": "#FF0000",
    "Brick Red": "#CB4154",
    "Cadmium Red": "#E30022",
    "Candy Apple Red": "#FF0800",
    "Cardinal Red": "#C41E3A",
    "Carmine": "#960018",
    "Dark Red": "#8B0000",
    "Fire Engine Red": "#CE2029",
    "Maroon": "#800000",
    "Scarlet": "#FF2400",
    "Vermilion": "#E34234",
    "Alizarin Crimson": "#E32636",
    "Amaranth": "#E52B50",
    "Cerise": "#DE3163",
    "Crimson": "#DC143C",
    "Raspberry": "#E30B5C",
    "Ruby": "#E0115F",
    "Red Violet": "#C71585",
    "Mulberry": "#C54B8C",
    "Medium Red Violet": "#BB3385",
    "Medium Violet Red": "#DB7093",
    "Orchid": "#DA70D6",
    "Thistle": "#D8BFD8",
    "Plum": "#8E4585",
    "Lavender Purple": "#967BB6",
    "Violet": "#8B00FF",
    "Blue Violet": "#8A2BE2",
    "Dark Magenta": "#8B008B",
    "Dark Orchid": "#9932CC",
    "Fuchsia": "#FF00FF",
    "Lilac": "#C8A2C8",
    "Medium Orchid": "#BA55D3",
    "Medium Purple": "#9370DB",
    "Medium Slate Blue": "#7B68EE",
    "Medium Violet Red": "#C71585",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Blue Violet": "#8A2BE2",
    "Navy Purple": "#9457EB",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Dark Violet": "#9400D3",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Dark Violet": "#9400D3",
    "Medium Purple": "#9370DB",
    "Wisteria": "#C9A0DC",
    "Lavender": "#E6E6FA",
    "Ghost White": "#F8F8FF",
    "Lavender": "#E6E6FA",
    "Lilac": "#C8A2C8",
    "Glitter": "#E6E8FA",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Ghost White": "#F8F8FF",
    "Lavender": "#E6E6FA",
    "Lilac": "#C8A2C8",
    "Glitter": "#E6E8FA",
    "Lavender Gray": "#C4C3D0",
    "Black": "#000000",
    "Ebony": "#555D50",
    "Crow": "#696969",
        "Charcoal": "#36454F",
    "Midnight": "#2D3142",
    "Ink": "#191970",
    "Raven": "#303030",
    "Oil": "#000000",
    "Grease": "#1C1C1C",
    "Onyx": "#0F0F0F",
    "Pitch": "#1C1C1C",
    "Soot": "#2C3539",
    "Sable": "#1B0200",
    "Jet Black": "#0F0F0F",
    "Coal": "#080808",
    "Metal": "#1E1E1E",
    "Obsidian": "#1D1F21",
    "Jade": "#00A86B",
    "Spider": "#1A1A1A",
    "Leather": "#2B322B",
    "Asphalt": "#130E07",
    "Licorice": "#0E0E0E",
    "Night": "#020B0B",
    "Charleston Green": "#232B2B",
    "Dark Jungle Green": "#1A2421",
    "Eerie Black": "#1B1B1B",
    "Raisin Black": "#242124",
    "Smoky Black": "#100C08",
    "Black Rock": "#010127",
    "Neutral Black": "#0B0B0B",
    "Black Denim": "#191C27",
    "Vampire Black": "#0F0404",
    "Cool Black": "#151922",
    "Frost Black": "#191C20",
    "Power Black": "#0E0C01",
    "Premium Black": "#100E09",
    "Black Magic": "#0B0510",
    "Alien Black": "#1A2228",
    "Black Chocolate": "#1B1811",
    "Gothic Grape": "#120321",
    "Metropolis": "#1A1A1A",
    "Night Shadow": "#1C1C1C",
    "Dark Raisin": "#1A0F0F",
    "Tea Bag": "#161311",
    "Tech Black": "#0D0E0E",
    "Dull Black": "#161616",
    "Natural Black": "#07000B",
    "Retro Black": "#1F201F",
    "Deep Space Sparkle": "#4A646C",
    "Black Cat": "#4D0135",
    "Eerie Black": "#1B1B1B",
    "Green Black": "#03231E",
    "Space Black": "#0D041E",
    "Blackberry": "#4D0135",
    "Black Coffee": "#3B2F2F",
    "Blast Off Bronze": "#A57164",
    "Bronze": "#CD7F32",
    "Dark Bronze": "#804A00",
    "Copper": "#B87333",
    "Bronze Gold": "#85754E",
    "Fool's Gold": "#FFD700",
    "Golden Yellow": "#FFDF00",
    "Harvest Gold": "#DA9100",
    "Midas Gold": "#E6BE8A",
    "Old Gold": "#CFB53B",
    "Rich Gold": "#A96217",
    "School Bus Yellow": "#FFD800",
    "Sun Yellow": "#FFCC00",
    "Yellow Orange": "#FFAE42",
    "Golden Poppy": "#FCC200",
    "Orange": "#FFA500",
    "Amber": "#FFBF00",
    "Bittersweet": "#FF6F61",
    "Burnt Orange": "#FF7034",
    "Cadmium Orange": "#ED872D",
    "Carrot Orange": "#ED9121",
    "Dark Orange": "#FF8C00",
    "Mango Tango": "#FF8243",
    "Neon Carrot": "#FFA343",
    "Orange Peel": "#FF9F00",
    "Persimmon": "#FF6347",
    "Pumpkin": "#FF7518",
    "Red Orange": "#FF5349",
    "Tangerine": "#FFA07A",
    "Tomato": "#FF6347",
    "Vermilion": "#E34234",
    "Red": "#FF0000",
    "Brick Red": "#CB4154",
    "Cadmium Red": "#E30022",
    "Candy Apple Red": "#FF0800",
    "Cardinal Red": "#C41E3A",
    "Carmine": "#960018",
    "Dark Red": "#8B0000",
    "Fire Engine Red": "#CE2029",
    "Maroon": "#800000",
    "Scarlet": "#FF2400",
    "Vermilion": "#E34234",
    "Alizarin Crimson": "#E32636",
    "Amaranth": "#E52B50",
    "Cerise": "#DE3163",
    "Crimson": "#DC143C",
    "Raspberry": "#E30B5C",
    "Ruby": "#E0115F",
    "Red Violet": "#C71585",
    "Mulberry": "#C54B8C",
    "Medium Red Violet": "#BB3385",
    "Medium Violet Red": "#DB7093",
    "Orchid": "#DA70D6",
    "Thistle": "#D8BFD8",
    "Plum": "#8E4585",
    "Lavender Purple": "#967BB6",
    "Violet": "#8B00FF",
    "Blue Violet": "#8A2BE2",
    "Dark Magenta": "#8B008B",
    "Dark Orchid": "#9932CC",
    "Fuchsia": "#FF00FF",
    "Lilac": "#C8A2C8",
    "Medium Orchid": "#BA55D3",
    "Medium Purple": "#9370DB",
    "Medium Slate Blue": "#7B68EE",
    "Medium Violet Red": "#C71585",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Blue Violet": "#8A2BE2",
    "Navy Purple": "#9457EB",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
        "Iris": "#5A4FCF",
    "Blue Violet": "#8A2BE2",
    "Navy Purple": "#9457EB",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Dark Violet": "#9400D3",
    "Purple": "#800080",
    "Purple Heart": "#69359C",
    "Purple Mountain's Majesty": "#9678B6",
    "Purple Pizzazz": "#FE4EDA",
    "Violet Red": "#F75394",
    "Electric Indigo": "#6F00FF",
    "Indigo": "#4B0082",
    "Iris": "#5A4FCF",
    "Dark Violet": "#9400D3",
    "Medium Purple": "#9370DB",
    "Wisteria": "#C9A0DC",
    "Lavender": "#E6E6FA",
    "Ghost White": "#F8F8FF",
    "Lavender": "#E6E6FA",
    "Lilac": "#C8A2C8",
    "Glitter": "#E6E8FA",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
        "Lavender Blue": "#CCCCFF",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Ghost White": "#F8F8FF",
    "Lavender": "#E6E6FA",
    "Lilac": "#C8A2C8",
    "Glitter": "#E6E8FA",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Lavender Gray": "#C4C3D0",
    "Thistle": "#D8BFD8",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
    "Light Blue": "#ADD8E6",
    "Blue Bell": "#A2A2D0",
    "Lavender Blue": "#CCCCFF",
    "Light Steel Blue": "#B0C4DE",
    "Slate Gray": "#708090",
    "Steel Blue": "#4682B4",
    "Azure": "#007FFF",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Turquoise Blue": "#00FFEF",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Turquoise Blue": "#00FFEF",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Turquoise Blue": "#00FFEF",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
        "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
        "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Dodger Blue": "#1E90FF",
    "Light Blue": "#ADD8E6",
    "Royal Blue": "#4169E1",
    "Sapphire": "#0F52BA",
    "Navy Blue": "#000080",
    "Blue": "#0000FF",
    "Medium Blue": "#0000CD",
    "Electric Blue": "#7DF9FF",
    "Baby Blue Eyes": "#A1CAF1",
    "Turquoise": "#40E0D0",
    "Cyan": "#00FFFF",
    "Aqua": "#00FFFF",
    "Robin Egg Blue": "#00CCCC",
    "Tiffany Blue": "#0ABAB5",
    "Pacific Blue": "#1CA9C9",
    "Powder Blue": "#B0E0E6",
    "Sky Blue": "#87CEEB",
    "Iceberg": "#71A6D2",
    "Cerulean Blue": "#2A52BE",
    "Sapphire Blue": "#0067A5",
    "Denim": "#1560BD",
    "Blue Jeans": "#5DADEC",
    "Teal Blue": "#367588",
    "Baby Blue": "#89CFF0",
    "Celestial Blue": "#4997D0",
    "Cerulean": "#007BA7",
    "Cornflower Blue": "#6495ED",
    "Periwinkle": "#C3CDE6",
    "Powder Blue": "#B0E0E6",
}

# Remove duplicates from custom_color_palette
custom_color_palette_no_duplicates = remove_duplicates(custom_color_palette)

# Print the result
for color in custom_color_palette_no_duplicates:
    print(color)
