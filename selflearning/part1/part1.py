cards = [13, 11, 10, 7, 4, 3, 1]
query = 7

def locate_card(cards, query):
  pass

tests = []
test = {
  'input' : {
      'cards': [13, 11, 10, 7, 4, 3, 1, 0],
      'query': 7
  },
  'output': 3
}

locate_card(**test['input']==test['output'])

#Consider variantions we might encounter witht the inputs
#1. query in the middle or first or last
#2. empty,...

tests = tests.append(test)