import random

money = 100

print('-----------------------------------------------')
# COIN FLIP GAME
def flip_coin(guess, bet):
    global money
    if money > 0:
        if bet < money:
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
         print('You have no money :(')

#  CHO - HAN GAME
def cho_han(guess, bet):
  global money
  if bet < money:
    payout = 0
    print("Let's play Cho-Han!")
    print("In this game, you must guess the sum of two dice rolls is even or odd.")
    print("You guessed: " + str(str.upper(guess)) + " and bet " + str(bet) + " credits.")
    #Roll dice and find the total
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    total = die_1 + die_2
    print("Rolling die......")
    print("Die 1: " + str(die_1))
    print("Die 2: " + str(die_2))
    print("Sum of roll: " + str(total))
    #Assign odd/even value to die roll (mod 2 being 0 means even number)
    if total % 2 > 0:
      result = "odd"
    else:
      result = "even"
    #Did the player win?
    if str.lower(guess) == result:
      print("You win! " + str(bet) + " credits have been added to your account!")
      money += bet
      print('Processing transaction...')
      print("Your new account balance is: " + str(money) + " credits.")
    else:
      print("You lose! " + str(bet) + " credits have been subtracted from your account!")
      payout += -1 * bet
      money += payout
      print('Processing transaction...')
      print("Your new account balance is: " + str(money) + " credits.")
  else:
    print("Bet cannot exceed account balance!")
    print("Please lower your bet.")
    print("Bet must be less than " + str(money) + " credits.")
  print("Thanks for playing!")
  print("------------------------------")  


#Call your game of chance functions here

flip_coin('Heads', 10)
cho_han('odd', 15)

