# the goat door that monti shows

def goat_door (car_door, player_choice):
    i = 1
    while(i==car_door or i==player_choice):
        i = (i+1)%(3)
        # print("i inside while loop =",i)

    return i

print( goat_door(0,1))
print( goat_door(1,1))

# function that the player chnages the door

def change_door(goat, player_choice):
    i = 1
    while(i == goat or i == player_choice):
        i = (i+1)%(3)
    return i

print( change_door(0,1))


import random

# random에는 pure random과 psudo random 존재, pseuso random은 찾을 수 있고 Pure random은 찾을 수 없음 (예로 cosmic ray)
random.seed() # 이 경우는 pure random , 만약 괄호 안에 숫자 넣으면 숫자 넣어서 다시 찾을 수 있음.
count = 0
for i in range(0,10000):
    car_door = random.randint(0,2) # random choice among 0,1,2
    player_choice = random.randint(0,2)
    goat = goat_door(car_door,player_choice) # goat door monty shows
    player_new_choice = change_door(goat,player_choice) #player changes after seeing the goat door

    if (car_door == player_new_choice):
        count += 1

    #results
    print("Car door = ",car_door, "Player Org. choice = ", player_choice,"Monty revealed = ",goat,"plyaer new choice = ",player_new_choice)
print(count)
