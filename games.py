import random

money = 100

#Write your game of chance functions here
def flip_coin(guess, bet):
    global money
    if money > 0:
        if bet < money:
            payout = 0
            print("It is time to flip a coin!")
            print("You bet " + str(bet) + " and credits on " + str(guess) + ".")
            #Random integer to represent heads / tails
            coin = random.randint(1,2)
            #Assigning heads and tails to generated number
            if coin == 1:
                coin_face = 'Heads'
            else:
                coin_face = 'Tails'
            # printing results of coin flip
            print('You flip the coin...')
            print("...and it lands on " + str(coin_face) + '!')
            if str.lower(guess) == coin_face:
                print("You win " + str(bet) + " credits have been added to yor account!")
                money += bet
                print('Processing transaction...')
                print("Your new account balance is " + str(money) + " credits")
            else:
                print("You lose! " + str(bet) + " credits have been removed from your account")
                money += -1 * bet
                print('Processing transaction...')
                print("Your new account balance is " + str(money) + " credits")
        else:
            print("Bet cannot exceed your balance")
            print("Please lower your bet")
            print("Bet must be less than " + str(money) + " credits")
        
        print("Thanks for playing!")
        print("-------------------------------------")
    else:
         print("Honestly you should probably stop playing; it seems either your luck has run out, or you have a gambling problem.")
#Call your game of chance functions here

flip_coin('Heads', 10)