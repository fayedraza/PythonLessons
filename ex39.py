#creates a mapping of state to abbreviation
states = {'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}

#creates a basic set of states and some cities in them
cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portalnd'

states = states.get('Texas')
print(states)

city= cities.get('TX','Does not exist')
print(city)


