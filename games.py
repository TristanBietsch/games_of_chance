import random

money = 100

#Write your game of chance functions here
def flip_coin(guess, bet):
    global money
    if bet < money:
        payout = 0
        print('It is time to flip a coin!')
        print('You bet ' + str(bet) ' and credits on ' +str.lowercase(str(guess)) + '.')
        #Random integer to represent heads / tails
        coin = random.init(1,2)
        #Assigning heads and tails to generated number
        if coin == 1:
            coin_face = 'Heads'
        else:
            coin_face = 'Tails'
        # printing results of coin flip
        print('You flip the coin...')
        print('...and it lands on ' + str(coin_face) + '!')
        if str.lower(guess) == coin_face:
            



#Call your game of chance functions here
