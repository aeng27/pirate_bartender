questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["a glug of rum", "a slug of whisky", "a splash of gin"],
    "salty": ["an olive on a stick", "a salt-dusted rim", "a rasher of bacon"],
    "bitter": ["a shake of bitters", "a splash of tonic", "a twist of lemon peel"],
    "sweet": ["a sugar cube", "a spoonful of honey", "a spash of cola"],
    "fruity": ["a slice of orange", "a dash of cassis", "a cherry on top"]
}

adjectives = ["Fluffy", "Salty", "Seasick", "Blind", "One-Eyed", "Nautical", "Fantastical"]
nouns = ["Sea Otter", "Shark", "Mermaid", "Sailor", "Pirate", "Whale","Parrot"]

def quest (a):
  """Function to get user input for asking preferences"""
  response = True
  user_input = raw_input ("{} (yes/y or no/n) ".format(questions[a]))
  while response:
    if user_input in ['Yes', 'yes', 'Y','y','No','no','N','n']:
      answer = user_input in ['Yes','yes','Y','y']
      response = False
      return answer
    else:
      user_input = raw_input ("Argh, answer yes or no or ye walk the plank! ")
      
def ask(a, b, c, d, e):
  """I ask what type of drink the person likes"""
  preferences = {}
  preferences [a] = quest (a)
  preferences [b] = quest (b)
  preferences [c] = quest (c)
  preferences [d] = quest (d)
  preferences [e] = quest (e)
  return preferences

def mix (a, b, c, d, e, f):
  """I pick the ingredients for the drink"""
  import random
  drink = []
  if a[b] == True:
    drink.append(random.choice(ingredients[b]))
  if a[c] == True:
    drink.append(random.choice(ingredients[c]))
  if a[d] == True:
    drink.append(random.choice(ingredients[d]))
  if a[e] == True:
    drink.append(random.choice(ingredients[e]))
  if a[f] == True:
    drink.append(random.choice(ingredients[f]))
  return drink

def name():
  """Naming the drink"""
  import random
  drinkname = []
  drinkname.append(random.choice(adjectives))
  drinkname.append(random.choice(nouns))
  return drinkname
  
if __name__ == '__main__':
  preferences = ask ("strong", "salty", "bitter", "sweet", "fruity")
  drink = mix (preferences, "strong", "salty", "bitter", "sweet", "fruity")
  drinkname = name()
  if len(drink) > 1:
    drink.insert(len(drink)-1, "and ")
    print ("Here ye go, one " + ' '.join(drinkname) + ': ' + ', '.join(drink[0:len(drink)-1]) + drink[len(drink)-1]+ "!" +" Drink up!")
  elif len(drink) == 1:
    print ("Here ye go, one " + ' '.join(drinkname) + ': ' + ''.join(drink) + "!" + " Drink up!")
  else:
    print ("Argh, if ye don't like anything drink some water.")
   