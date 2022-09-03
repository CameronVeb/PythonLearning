import tkinter as tk
from tkinter import ttk

PokemonDict = [
    {"name": "bulbasaur","PokeDexEntryNo": 1,"FirstType": "grass", "SecondType": "poison"},
    {"name": "ivysaur","PokeDexEntryNo": 2,"FirstType": "grass", "SecondType": "poison"},
    {"name": "venusaur","PokeDexEntryNo": 3,"FirstType": "grass", "SecondType": "poison"},
    {"name": "charmander","PokeDexEntryNo": 4,"FirstType": "fire", "SecondType": False},
    {"name": "charmeleon","PokeDexEntryNo": 5,"FirstType": "fire", "SecondType": False},
    {"name": "charizard","PokeDexEntryNo": 6,"FirstType": "fire", "SecondType": "flying"},
    {"name": "squirtle","PokeDexEntryNo": 7,"FirstType": "water", "SecondType": False},
    {"name": "wartortle","PokeDexEntryNo": 8,"FirstType": "water", "SecondType": False},
    {"name": "blastoise","PokeDexEntryNo": 9,"FirstType": "water", "SecondType": False},
    {"name": "caterpie","PokeDexEntryNo": 10,"FirstType": "bug", "SecondType": False},
    {"name": "metapod","PokeDexEntryNo": 11,"FirstType": "bug", "SecondType": False},
    {"name": "butterfree","PokeDexEntryNo": 12,"FirstType": "bug", "SecondType": "flying"},
    {"name": "weedle","PokeDexEntryNo": 13,"FirstType": "bug", "SecondType": "poison"},
    {"name": "kakuna","PokeDexEntryNo": 14,"FirstType": "bug", "SecondType": "poison"},
    {"name": "beedrill","PokeDexEntryNo": 15,"FirstType": "bug", "SecondType": "poison"},
    {"name": "pidgey","PokeDexEntryNo": 16,"FirstType": "normal", "SecondType": "flying"},
    {"name": "pidgeooto","PokeDexEntryNo": 17,"FirstType": "normal", "SecondType": "flying"},
    {"name": "pidgeot","PokeDexEntryNo": 18,"FirstType": "normal", "SecondType": "flying"},
    {"name": "rattata","PokeDexEntryNo": 19,"FirstType": "normal", "SecondType": None},
    {"name": "raticate","PokeDexEntryNo": 20,"FirstType": "normal", "SecondType": None},
    {"name": "spearow","PokeDexEntryNo": 21,"FirstType": "normal", "SecondType": "flying"},
    {"name": "fearow","PokeDexEntryNo": 22,"FirstType": "normal", "SecondType": "flying"},
    {"name": "ekans","PokeDexEntryNo": 23,"FirstType": "poison", "SecondType": None},
    {"name": "arbok","PokeDexEntryNo": 24,"FirstType": "poison", "SecondType": None},
    {"name": "pikachu","PokeDexEntryNo": 25,"FirstType": "electric", "SecondType": None},
    {"name": "raichu","PokeDexEntryNo": 26,"FirstType": "electric", "SecondType": None},
    {"name": "sandshrew","PokeDexEntryNo": 27,"FirstType": "ground", "SecondType": None},
    {"name": "sandslash","PokeDexEntryNo": 28,"FirstType": "ground", "SecondType": None},
    {"name": "nidoran","PokeDexEntryNo": 29,"FirstType": "poison", "SecondType": None},
    {"name": "nidorina","PokeDexEntryNo": 30,"FirstType": "poison", "SecondType": None},
    {"name": "nidoqueen","PokeDexEntryNo": 31,"FirstType": "poison", "SecondType": "ground"},
    {"name": "nidoran","PokeDexEntryNo": 32,"FirstType": "ground", "SecondType": None},
    {"name": "nidorino","PokeDexEntryNo": 33,"FirstType": "poison", "SecondType": None},
    {"name": "nidoking","PokeDexEntryNo": 34,"FirstType": "poison", "SecondType": "ground"},
    {"name": "clefairy","PokeDexEntryNo": 35,"FirstType": "fairy", "SecondType": None},
    {"name": "clefable","PokeDexEntryNo": 36,"FirstType": "fairy", "SecondType": None},
    {"name": "vulpix","PokeDexEntryNo": 37,"FirstType": "fire", "SecondType": None},
    {"name": "ninetales","PokeDexEntryNo": 38,"FirstType": "fire", "SecondType": None},
    {"name": "jigglypuff","PokeDexEntryNo": 39,"FirstType": "normal", "SecondType": "fairy"},
    {"name": "wigglytuff","PokeDexEntryNo": 40,"FirstType": "normal", "SecondType": "fairy"},
    {"name": "zubat","PokeDexEntryNo": 41,"FirstType": "poison", "SecondType": "flying"},
    {"name": "golbat","PokeDexEntryNo": 42,"FirstType": "poison", "SecondType": "flying"},
    {"name": "oddish","PokeDexEntryNo": 43,"FirstType": "grass", "SecondType": "poison"},
    {"name": "gloom","PokeDexEntryNo": 44,"FirstType": "grass", "SecondType": "poison"},
    {"name": "vileplume","PokeDexEntryNo": 45,"FirstType": "grass", "SecondType": "poison"},
    {"name": "paras","PokeDexEntryNo": 46,"FirstType": "bug", "SecondType": "grass"},
    {"name": "parasect","PokeDexEntryNo": 47,"FirstType": "bug", "SecondType": "grass"},
    {"name": "venonat","PokeDexEntryNo": 48,"FirstType": "bug", "SecondType": "poison"},
    {"name": "venemoth","PokeDexEntryNo": 49,"FirstType": "bug", "SecondType": "poison"},
    {"name": "diglett","PokeDexEntryNo": 50,"FirstType": "ground", "SecondType": None},
    {"name": "dugtrio","PokeDexEntryNo": 51,"FirstType": "ground", "SecondType": None},
    {"name": "meowth","PokeDexEntryNo": 52,"FirstType": "normal", "SecondType": None},
    {"name": "persian","PokeDexEntryNo": 53,"FirstType": "normal", "SecondType": None},
    {"name": "psyduck","PokeDexEntryNo": 54,"FirstType": "water", "SecondType": None},
    {"name": "golduck","PokeDexEntryNo": 55,"FirstType": "water", "SecondType": None},
    {"name": "mankey","PokeDexEntryNo": 56,"FirstType": "fight", "SecondType": None},
    {"name": "primeape","PokeDexEntryNo": 57,"FirstType": "fight", "SecondType": None},
    {"name": "growlithe","PokeDexEntryNo": 58,"FirstType": "fire", "SecondType": None},
    {"name": "arcanine","PokeDexEntryNo": 59,"FirstType": "fire", "SecondType": None},
    {"name": "poliwag","PokeDexEntryNo": 60,"FirstType": "water", "SecondType": None},
    {"name": "poliwhirl","PokeDexEntryNo": 61,"FirstType": "water", "SecondType": None},
    {"name": "poliwrath","PokeDexEntryNo": 62,"FirstType": "water", "SecondType": "fight"},
    {"name": "abra","PokeDexEntryNo": 63,"FirstType": "psychic", "SecondType": None},
    {"name": "kadabra","PokeDexEntryNo": 64,"FirstType": "psychic", "SecondType": None},
    {"name": "alakazam","PokeDexEntryNo": 65,"FirstType": "psychic", "SecondType": None},
    {"name": "machop","PokeDexEntryNo": 66,"FirstType": "fight", "SecondType": None},
    {"name": "machoke","PokeDexEntryNo": 67,"FirstType": "fight", "SecondType": None},
    {"name": "machamp","PokeDexEntryNo": 68,"FirstType": "fight", "SecondType": None},
    {"name": "bellsprout","PokeDexEntryNo": 69,"FirstType": "grass", "SecondType": "poison"},
    {"name": "weepinbell","PokeDexEntryNo": 70,"FirstType": "grass", "SecondType": "poison"},
    {"name": "victreebel","PokeDexEntryNo": 71,"FirstType": "grass", "SecondType": "poison"},
    {"name": "tentacool","PokeDexEntryNo": 72,"FirstType": "water", "SecondType": "poison"},
    {"name": "tentacruel","PokeDexEntryNo": 73,"FirstType": "water", "SecondType": "poison"},
    {"name": "geodue","PokeDexEntryNo": 74,"FirstType": "rock", "SecondType": "ground"},
    {"name": "graveler","PokeDexEntryNo": 75,"FirstType": "rock", "SecondType": "ground"},
    {"name": "golem","PokeDexEntryNo": 76,"FirstType": "rock", "SecondType": "ground"},
    {"name": "ponyta","PokeDexEntryNo": 77,"FirstType": "fire", "SecondType": None},
    {"name": "rapidash","PokeDexEntryNo": 78,"FirstType": "fire", "SecondType": None},
    {"name": "slowpoke","PokeDexEntryNo": 79,"FirstType": "water", "SecondType": "psychic"},
    {"name": "slowbro","PokeDexEntryNo": 80,"FirstType": "water", "SecondType": "psychic"},
    {"name": "magnemite","PokeDexEntryNo": 81,"FirstType": "electric", "SecondType": "steel"},
    {"name": "magneton","PokeDexEntryNo": 82,"FirstType": "electric", "SecondType": "steel"},
    {"name": "farfetch'd","PokeDexEntryNo": 83,"FirstType": "normal", "SecondType": "flying"},
    {"name": "doduo","PokeDexEntryNo": 84,"FirstType": "normal", "SecondType": "flying"},
    {"name": "dodrio","PokeDexEntryNo": 85,"FirstType": "normal", "SecondType": "flying"},
    {"name": "seel","PokeDexEntryNo": 86,"FirstType": "water", "SecondType": None},
    {"name": "dewgong","PokeDexEntryNo": 87,"FirstType": "water", "SecondType": "ice"},
    {"name": "grimer","PokeDexEntryNo": 88,"FirstType": "poison", "SecondType": None},
    {"name": "muk","PokeDexEntryNo": 89,"FirstType": "poison", "SecondType": None},
    {"name": "shellder","PokeDexEntryNo": 90,"FirstType": "water", "SecondType": None},
    {"name": "cloyster","PokeDexEntryNo": 91,"FirstType": "water", "SecondType": "ice"},
    {"name": "gastly","PokeDexEntryNo": 92,"FirstType": "ghost", "SecondType": "poison"},
    {"name": "haunter","PokeDexEntryNo": 93,"FirstType": "ghost", "SecondType": "poison"},
    {"name": "gengar","PokeDexEntryNo": 94,"FirstType": "ghost", "SecondType": "poison"},
    {"name": "onix","PokeDexEntryNo": 95,"FirstType": "rock", "SecondType": "ground"},
    {"name": "drowzee","PokeDexEntryNo": 96,"FirstType": "psychic", "SecondType": None},
    {"name": "hypno","PokeDexEntryNo": 97,"FirstType": "psychic", "SecondType": None},
    {"name": "krabby","PokeDexEntryNo": 98,"FirstType": "water", "SecondType": None},
    {"name": "kingler","PokeDexEntryNo": 99,"FirstType": "water", "SecondType": None},
    {"name": "voltorb","PokeDexEntryNo": 100,"FirstType": "electric", "SecondType": None},
    {"name": "electrode","PokeDexEntryNo": 101,"FirstType": "electric", "SecondType": None},
    {"name": "exeggcute","PokeDexEntryNo": 102,"FirstType": "grass", "SecondType": "psychic"},
    {"name": "exeggutor","PokeDexEntryNo": 103,"FirstType": "grass", "SecondType": "psychic"},
    {"name": "cubone","PokeDexEntryNo": 104,"FirstType": "ground", "SecondType": None},
    {"name": "marowak","PokeDexEntryNo": 105,"FirstType": "ground", "SecondType": None},
    {"name": "hitmonlee","PokeDexEntryNo": 106,"FirstType": "fight", "SecondType": None},
    {"name": "hitmonchan","PokeDexEntryNo": 107,"FirstType": "fight", "SecondType": None},
    {"name": "lickitung","PokeDexEntryNo": 108,"FirstType": "normal", "SecondType": None},
    {"name": "koffing","PokeDexEntryNo": 109,"FirstType": "poison", "SecondType": None},
    {"name": "weekzing","PokeDexEntryNo": 110,"FirstType": "poison", "SecondType": None},
    {"name": "rhyhorn","PokeDexEntryNo": 111,"FirstType": "ground", "SecondType": "rock"},
    {"name": "rhydon","PokeDexEntryNo": 112,"FirstType": "ground", "SecondType": "rock"},
    {"name": "chansey","PokeDexEntryNo": 113,"FirstType": "normal", "SecondType": None},
    {"name": "tangela","PokeDexEntryNo": 114,"FirstType": "grass", "SecondType": None},
    {"name": "kangaskhan","PokeDexEntryNo": 115,"FirstType": "normal", "SecondType": None},
    {"name": "horsea","PokeDexEntryNo": 116,"FirstType": "water", "SecondType": None},
    {"name": "seadra","PokeDexEntryNo": 117,"FirstType": "water", "SecondType": None},
    {"name": "goldeen","PokeDexEntryNo": 118,"FirstType": "water", "SecondType": None},
    {"name": "seaking","PokeDexEntryNo": 119,"FirstType": "water", "SecondType": None},
    {"name": "staryu","PokeDexEntryNo": 120,"FirstType": "water", "SecondType": None},
    {"name": "starmie","PokeDexEntryNo": 121,"FirstType": "water", "SecondType": "psychic"},
    {"name": "mr. mime","PokeDexEntryNo": 122,"FirstType": "psychic", "SecondType": "fairy"},
    {"name": "scyther","PokeDexEntryNo": 123,"FirstType": "bug", "SecondType": "flying"},
    {"name": "jynx","PokeDexEntryNo": 124,"FirstType": "ice", "SecondType": "psychic"},
    {"name": "electabuzz","PokeDexEntryNo": 125,"FirstType": "electric", "SecondType": None},
    {"name": "magmar","PokeDexEntryNo": 126,"FirstType": "fire", "SecondType": None},
    {"name": "pinsir","PokeDexEntryNo": 127,"FirstType": "bug", "SecondType": None},
    {"name": "tauros","PokeDexEntryNo": 128,"FirstType": "normal", "SecondType": None},
    {"name": "magikarp","PokeDexEntryNo": 129,"FirstType": "water", "SecondType": None},
    {"name": "gyrados","PokeDexEntryNo": 130,"FirstType": "water", "SecondType": "flying"},
    {"name": "lapras","PokeDexEntryNo": 131,"FirstType": "water", "SecondType": "ice"},
    {"name": "ditto","PokeDexEntryNo": 132,"FirstType": "normal", "SecondType": None},
    {"name": "eevee","PokeDexEntryNo": 133,"FirstType": "normal", "SecondType": None},
    {"name": "vaporeon","PokeDexEntryNo": 134,"FirstType": "water", "SecondType": None},
    {"name": "jolteon","PokeDexEntryNo": 135,"FirstType": "electric", "SecondType": None},
    {"name": "flareon","PokeDexEntryNo": 136,"FirstType": "fire", "SecondType": None},
    {"name": "porygon","PokeDexEntryNo": 137,"FirstType": "normal", "SecondType": None},
    {"name": "omanyte","PokeDexEntryNo": 138,"FirstType": "rock", "SecondType": "water"},
    {"name": "omastar","PokeDexEntryNo": 139,"FirstType": "rock", "SecondType": "water"},
    {"name": "kabuto","PokeDexEntryNo": 140,"FirstType": "rock", "SecondType": "water"},
    {"name": "kabutops","PokeDexEntryNo": 141,"FirstType": "rock", "SecondType": "water"},
    {"name": "aerodactyl","PokeDexEntryNo": 142,"FirstType": "rock", "SecondType": "flying"},
    {"name": "snorlax","PokeDexEntryNo": 143,"FirstType": "normal", "SecondType": None},
    {"name": "articuno","PokeDexEntryNo": 144,"FirstType": "ice", "SecondType": "flying"},
    {"name": "zapdos","PokeDexEntryNo": 145,"FirstType": "electric", "SecondType": "flying"},
    {"name": "moltres","PokeDexEntryNo": 146,"FirstType": "fire", "SecondType": "flying"},
    {"name": "dratini","PokeDexEntryNo": 147,"FirstType": "dragon", "SecondType": None},
    {"name": "dragonair","PokeDexEntryNo": 148,"FirstType": "dragon", "SecondType": None},
    {"name": "dragonite","PokeDexEntryNo": 149,"FirstType": "dragon", "SecondType": "flying"},
    {"name": "Mewtwo","PokeDexEntryNo": 150,"FirstType": "psychic", "SecondType": None},
    {"name": "mew","PokeDexEntryNo": 151,"FirstType": "psychic", "SecondType": None}
]

#Create The GUI Frame
frame = tk.Tk()
frame.title("PokeDex_V1.a")
frame.geometry('400x400')

def checking(self):
    UserInput = self.user_input.get('1.0',tk.END) 

    

def printInput():
    inpt = inputtxt.get(1.0,"end-1c")
    result = None

    for pokemon in PokemonDict:
        
        if  inpt.lower() == pokemon['name']:
            result = 'Pokemon Name: ' + pokemon['name'] + '\nPokeDex Entry Number: ' + str(pokemon['PokeDexEntryNo']) + '\nFirst Type: ' + pokemon['FirstType'] + '\nSecond Type: ' + str(pokemon['SecondType'] or '')
            break
        else:
            result = "Not a valid pokemon name"

    #capitalize the first letter of each word with title()
    lbl.config(text = result.title())

#Create the text box
inputtxt = tk.Text(frame,height=1, width=30)

#load the GUI to the screen
inputtxt.pack()

PrintButton = tk.Button(frame, text = 'Enter Pokemon Name', command = printInput)




# #clear the screen for new input
# def clearScreen(self):
#     self.user_input.delete('1.0',tk.END)

PrintButton.pack()

#label creation
lbl = tk.Label(frame, text = "")
lbl.pack()

#continuously executing app call
frame.mainloop()