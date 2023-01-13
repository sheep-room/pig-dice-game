from random import randint
from random import choice

# 변수 설정
point_player = 0
pooint_computer = 0

player_is_playing = True
computer_is_playing = False


# 사용자가 play하는 함수
def player_game:
    while player_is_playing = True:
        dice_num = randint(1,6)

        if dice_num == 1:
            point_player = 0
            print("Your point is ZERO now. Game is over")
            player_is_playing = False

        elif dice_num != 1:
            point_player += dice_num
            print(f"Your score is {dice_num} now")
            user_choice = input("Enter r(roll) or s(stop) >>")

            if user_choice == "r":
                player_game()

            if user_choice == "s":
                player_is_playing = False
                computer_is_playing = True

# 컴퓨터가 Play하는 함수


# 포인트가 50점이 될 때까지 진행되는 메인 함수
while point_user >= 50 or point_computer >= 50:
    pass


