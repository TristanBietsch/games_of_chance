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

#Card game
def cards(bet):
  global money
  if bet < money:
    payout = 0
    print("Let's play a card game!")
    print("Do you think you can draw a higher card than me? Let's play!")
    #4 suits of cards, each with 13 cards in them
    suit1 = list(range(1,14))
    suit2 = list(range(1,14))
    suit3 = list(range(1,14))
    suit4 = list(range(1,14))
    #full deck of cards
    card_deck = suit1 + suit2 + suit3 + suit4
    #player 1 draws a card
    player1_draw = random.randint(0,51)
    player1_card = card_deck[player1_draw]
    #changing the display for the face cards
    if player1_card == 1:
      player1_card_disp = "A"
    elif player1_card == 11:
      player1_card_disp = "J"
    elif player1_card == 12:
      player1_card_disp = "Q"
    elif player1_card == 13:
      player1_card_disp = "K"
    else:
      player1_card_disp = player1_card
    print("You reach into the deck of cards and pull out a " + str(player1_card_disp) + ".")
    #remove the card player 1 drew from the deck:
    card_deck2 = card_deck[:player1_draw] + card_deck[player1_draw + 1:]
    player2_draw = random.randint(0,50)
    player2_card = card_deck2[player2_draw]
    if player2_card == 1:
      player2_card_disp = "A"
    elif player2_card == 11:
      player2_card_disp = "J"
    elif player2_card == 12:
      player2_card_disp = "Q"
    elif player2_card == 13:
      player2_card_disp = "K"
    else:
      player2_card_disp = player2_card
    print("I reach into the deck of cards and pull out a " + str(player2_card_disp) + ".")
    #determine the winner:
    if player1_card > player2_card:
      print("You win!") 
      print('Processing transaction...')
      print(str(bet) + " credits have been added to your account.")
      money += bet
      print("Your new account balance is: " + str(money) + " credits.")
    elif player1_card < player2_card:
      print("You lose!")
      print('Processing transaction...')
      print(str(bet) + " credits have been subtracted from your account.")
      payout += -1 * bet
      money += payout
      print("Your new account balance is: " + str(money) + " credits.")
    else:
      print("It's a tie!")
      print("No money has been added or subtracted from your account.")
  else:
    print("Bet cannot exceed account balance!")
    print("Please lower your bet.")
    print("Bet must be less than " + str(money) + " credits.")
  print("Thanks for playing!")
  print("------------------------------")  

def roulette(guess, bet):
  global money
  if bet < money:
    print("Let's play a game of Roulette!")
    payout = 0
    #roulette "wheel":
    roulette_numbers = list(range(0, 38))
    roulette_ball = random.randint(0,37)
    #Convert guess to a string:
    guess = str(guess)
    #Create the display numbers:
    if roulette_ball == 0:
      roulette_display_num = "0"
    elif roulette_ball == 37:
      roulette_display_num = "00"
    else:
      roulette_display_num = str(roulette_ball)
    # Bet names
    Red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    Black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    first_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    third_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    # Single number -- win if ball lands on chosen number
    # 0 bet -- only win if lands on 0
    # 00 bet -- only win if lands on 00
    # Determine if the player wins:
    print("You guessed that the ball would land on: " + str.lower(guess))
    print("The ball is going around the wheel...")
    print("It lands on " + str(roulette_display_num) + ".")
    if (str.lower(guess) == "red" and roulette_ball in Red) or (str.lower(guess) == "black" and roulette_ball in Black):
      print("You win!")
      payout += bet
    elif (str.lower(guess) == "odd" and roulette_ball % 2 > 0) or (str.lower(guess) == "even" and roulette_ball % 2 == 0):
      print("You win!")
      payout += bet
    elif ((str.lower(guess) == "first" or str.lower(guess) == "1st") and roulette_ball in first_column) or ((str.lower(guess) == "second" or str.lower(guess) == "2nd") and roulette_ball in second_column) or ((str.lower(guess) == "third" or str.lower(guess) == "3rd") and roulette_ball in third_column):
      print("You win!")
      payout += 2 * bet
    elif str.lower(guess) == roulette_display_num:
      print("You win!")
      payout += 35 * bet
    else:
      print("You lose!")
      payout += -1 * bet
    money += payout
    #Payout print:
    if payout < 0:
      print(str(abs(payout)) + " credits have been subtracted from your account!")
    else:
      print(str(payout) + " credits have been added to your account.")
    print("Your new account balance is: " + str(money) + " credits")
  else:
    print("Bet cannot exceed account balance!")
    print("Please lower your bet.")
    print("Bet must be less than " + str(money) + " credits.")
  print("Thanks for playing!")
  print("------------------------------")  

# game of chance functions

flip_coin('Heads', 10)
cho_han('odd', 15)
cards(10)
roulette('Red', 30)


