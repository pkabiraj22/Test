import random

def show_score(scorelist):
    if not scorelist:
        print('This is your 1st attempt')
    else:
        best_score = min(scorelist)
        print(f'Your best score is {best_score}')
    



def start_game():
    attempts = 0
    scorelist = []
    real_num = random.randint(1,10)

    print('Hey!! Traveller, Welcome to the game of guesses....')
    player_name = input('What is your name? ')

    response = input(f'Hi.. {player_name.capitalize()}, \nDo you want to play the game? [Enter yes/no] ')


    if (response.lower() != 'yes'):
        print('Thank you !!')
        exit()
    else:
        show_score(scorelist)


    while (response.lower() == 'yes'):
        if attempts < 4 :    

            print('You have', 4-attempts ,'attempts!!')
            num = int(input('Pick any number between 1 to 10: '))
                
            if num < 1 or num > 10:
                    raise ValueError('Please guess a number between 1 and 10.')
            attempts += 1

            
            if num == real_num:
                    scorelist.append(attempts)
                    print(f'Congratulations !! You guessed it in {attempts} attempts :-)')
                    response = input('Do you want to play again? [yes/no]: ')

                    
                    if response.lower() != 'yes':
                        print('Thank you !!')
                        break
                    else:
                        attempts = 0
                        real_num = random.randint(1,10)
                        show_score(scorelist)
                        continue
                
            else:
                    if num < real_num:
                        if attempts < 4:
                            print('It is higher...')
                    elif num > real_num:
                        if attempts < 4:
                            print('It is lower...')
        else:
            print('Sorry!! Game Over') 
            break  


            
    
       

if __name__ == '__main__':
    start_game()



        





        
        