import random # psuedo randomness generator
import numpy as np # import numerical python
import matplotlib.pyplot as plt # import matplot library

# Params
the_end = 100 # days to simulate in credland
village_folk = [[np.random.randint(0,10), 0] for i in range(100)] # initialize village folk and their stuff and cred_castle balances
castle = 0 # the cred castle
castle_token_supply = 0 # the amount of castle tokens

# How villagers build the castle 
def build_castle(villager):
    global castle # global castle variable
    global castle_token_supply # global token supply variable 
    
    castle += 1 # make castle more awesome
    castle_token_supply += 1 # increase castle tokens
    villager[1] += 1 # increase villager castle token holdings

# How villagers sell castle tokens
def sell_castle_tokens(villager):
    villager[0] += 1 # villager stuff goes up
    villager [1] -= 1 # villager stuff goes down

# How villagers buy castle tokens 
def buy_castle_tokens(villager):
    villager[0] -= 1 # villager stuff goes down
    villager [1] += 1 # villager stuff goes up

# Everyone in CredLand is crazy 
def villagers_be_crazy():
    global village_folk # global village_folk variable
    for villager in village_folk: # iterate through all the villagers
        fate = random.uniform(0, 1) # random number between 0 and 1 that represents sentiment
        if fate > 0.8: # people really care about the castle
            buy_castle_tokens(villager) # buy castle tokens
        if fate > 0.5: # people care about the castle
            build_castle(villager) # make castle better
        if fate < 0.5: # people do not care about the castle
            sell_castle_tokens(villager) # sell castle tokens

# To Do: Smarter CredLand villagers
def smart_villagers():
    global village_folk # global village_folk variable
    for villager in village_folk: # iterate through all the villagers
        # decisions are made based on invironmental variables such as the liklihood of a raid and the season 

# Feed the dragons
def feed_the_dragons():
    global village_folk # global village_folk variable
    for villager in village_folk: # iterate through all the villagers
        if any(v < 0 for v in villager): # if any of the villager's assets are less than 0
            print('Shame, shame... ', villager) # shame the villager
            village_folk.remove(villager) # let the villager fend for themselves

# Run the model
day = 0 # starting at day 0
if day < the_end: # we're still alive!
    villagers_be_crazy() # run the random villgaer policy
    day += 1 # it's a new day
feed_the_dragons() # feed indebted vilagers to the dragons

# Check the results
print('Castle: ', castle)
print('Total village folk: ', len(village_folk))
print('Village folk: ', village_folk)

# Next Steps
#   Create castle_token marketplace 
#   Environmental variables that affect village_folk sentiment