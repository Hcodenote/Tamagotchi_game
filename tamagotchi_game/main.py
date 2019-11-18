import sys
from pygame.locals import *
import time
import images

# 새 창 on / off

new_window = 'off'
info_img = images.info_window_img
setting_img = images.setting_window_img
advice_img = images.advice_img

# 충돌 방지 on / off
menu_crash = 'off'

# 진화 단계
level = 0

# 시간
clock = pygame.time.Clock()

# 실행

running = True
gameover = False
advice = False # 도움말

# 모션 False 설정
walking = True
click = False

cleaning = False
playing = False
eating = False
treatment = False

poop = False
happy = False
sick = False
level_up = False
setting = False
information = False

# 윈도우 창 설정

size = width, height = 300, 400
speed = 10
black = 0, 0, 0
WHITE = (255, 255, 255)
gray = (234, 234, 234)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('추억의 펫 키우기') # 윈도우 타이틀

# 처음 이미지
lens = 0 # 이미지 길이
pet = images.baby_front

# 물체 이미지
ball = images.play_event_img[0]
food_img = images.eat_event_img[0]
clean_tool_img = images.clean_event_img[0]
poop_img = [images.poop_event_img, images.poop_event_img, images.poop_event_img]
medicine_img = images.sick_event_img

# 이펙트 이미지
heart_img = images.heart_event_img
happy_effect_img1 = images.happy_event_img
happy_effect_img2 = images.happy_event_img
sick_effect_img = images.sick_img

# 윈도우 하트 이미지
game_heart_img = [heart_img, heart_img, heart_img, heart_img, heart_img]
eat_heart_img = [heart_img, heart_img, heart_img, heart_img, heart_img]
health_heart_img = [heart_img, heart_img, heart_img, heart_img, heart_img]

heart_x_01 = 100
heart_y_01 = 100

# 게임오버 이미지
gameover_num = 0
#gameover_img = images.gameover_img


# 펫의 상태
play_state = 5
eat_state = 5
clean_state = 3
sick_state = 0
escape = 0 # 3되면 Gameover 도망
death = 5 # 5되면 Gameover 죽음

# 펫 활동 합산
level_sum = 0

#pet_rect = pet.get_rect()

# 몇 번 반복했는가 (시간)
count = 0
poop_count = 0
play_count = 0
eat_count = 0
clean_count = 0
sick_count = 0
escape_count = 0
death_count = 0
sec2_count = 0

# 똥 갯수 / 위치
poop_sum = 0
poop_x = [70, 200, 150]
poop_y = [230, 230, 250]

# 펫 위치
pet_direction = 'right'
pet_x = 120
pet_y = 200
pet_current = 0

# 메뉴 위치
menu_x = 35
menu_y = 35
menu_rect = [None]*6

# 놀이 공 위치
ball_x = 0
ball_y = 0

# 진화 1단계
level_up1 = [images.baby_front, images.kid_front]

# 진화 2단계
level_up2 = [images.kid_front, images.adult_front]

# 텍스트 위치
text_x = 35
text_y = 35


# 기본 움직임
def walk(level):
    global pet_direction, pet_x, pet_y, pet_current, pet, walking

    num = level
    
    if level == 0:
        if pet_direction == 'right' and pet_x < 220:

            pet_current = (pet_current + 1) % len(images.baby_right)
            pet = images.baby_right[ pet_current ]
            pet_x += 10

        elif pet_x >= 220:

            pet_direction = 'left'
            pet_current = 0


        if pet_direction == 'left' and pet_x > 10:

            pet_current = (pet_current + 1) % len(images.baby_left)
            pet = images.baby_left[ pet_current ]
            pet_x -= 10

        elif pet_x <= 10:

            pet_direction = 'right'
            pet_current = 0

    elif level == 1:
        if pet_direction == 'right' and pet_x < 220:

            pet_current = (pet_current + 1) % len(images.kid_right)
            pet = images.kid_right[ pet_current ]
            pet_x += 10
            

        elif pet_x >= 220:

            pet_direction = 'left'
            pet_current = 0


        if pet_direction == 'left' and pet_x > 10:

            pet_current = (pet_current + 1) % len(images.kid_left)
            pet = images.kid_left[ pet_current ]
            pet_x -= 10

        elif pet_x <= 10:

            pet_direction = 'right'
            pet_current = 0

    elif level == 2:
        if pet_direction == 'right' and pet_x < 220:

            pet_current = (pet_current + 1) % len(images.adult_right)
            pet = images.adult_right[ pet_current ]
            pet_x += 10

        elif pet_x >= 220:

            pet_direction = 'left'
            pet_current = 0


        if pet_direction == 'left' and pet_x > 10:

            pet_current = (pet_current + 1) % len(images.adult_left)
            pet = images.adult_left[ pet_current ]
            pet_x -= 10

        elif pet_x <= 10:

            pet_direction = 'right'
            pet_current = 0


################################## 메뉴 모션 ##################################

###### 메뉴 - 놀이 ######
            
def play_motion(level):

    global screen, pet_x, pet_y, pet_direction, pet_current, pet, ball_x, ball_y, ball

    if level == 0:

        if pet_direction == 'up' and pet_y > 100:

            pet_current = (pet_current + 1) % len(images.baby_play)
            pet = images.baby_play[ pet_current ]
            pet_y -= 10
            
        elif pet_y <= 100:

            pet_direction = 'down'
            pet_current = 0

        if pet_direction == 'down' and pet_y < 200:

            pet_current = (pet_current + 1) % len(images.baby_play)
            pet = images.baby_play[ pet_current ]
            pet_y += 10
            
        elif pet_y >= 200:

            pet_direction = 'up'
            pet_current = 0

    elif level == 1:

        if pet_direction == 'up' and pet_y > 100:

            pet_current = (pet_current + 1) % len(images.kid_play)
            pet = images.kid_play[ pet_current ]
            pet_y -= 10
            
        elif pet_y <= 100:

            pet_direction = 'down'
            pet_current = 0

        if pet_direction == 'down' and pet_y < 200:

            pet_current = (pet_current + 1) % len(images.kid_play)
            pet = images.kid_play[ pet_current ]
            pet_y += 10
            
        elif pet_y >= 200:

            pet_direction = 'up'
            pet_current = 0

    elif level == 2:

        if pet_direction == 'up' and pet_y > 100:

            pet_current = (pet_current + 1) % len(images.adult_play)
            pet = images.adult_play[ pet_current ]
            pet_y -= 10
            
        elif pet_y <= 100:

            pet_direction = 'down'
            pet_current = 0

        if pet_direction == 'down' and pet_y < 200:

            pet_current = (pet_current + 1) % len(images.adult_play)
            pet = images.adult_play[ pet_current ]
            pet_y += 10
            
        elif pet_y >= 200:

            pet_direction = 'up'
            pet_current = 0


def ball_motion():
    global screen, ball, pet_x, pet_y, pet_current

    ball = images.play_event_img[ pet_current ]
    
    if playing == True:
        screen.blit(ball, (pet_x - 80, pet_y))

###### 메뉴 - 식사 ######

def eating_motion(level):
    global pet_x, pet_y, pet_current, pet, eating

    pet_x = 150

    if level == 0:
        
        pet = images.baby_eat[pet_current]
        pet_current = (pet_current + 1) % len(images.baby_eat)

    elif level == 1:

        pet = images.kid_eat[pet_current]
        pet_current = (pet_current + 1) % len(images.kid_eat)

    elif level == 2:

        pet = images.adult_eat[pet_current]
        pet_current = (pet_current + 1) % len(images.adult_eat)


def food_motion():
    global screen, eating, food_img, pet_x, pet_y, lens, sec2_count

    if eating == True:
        if sec2_count % 2 == 1:
            lens = (lens + 1) % len(images.eat_event_img) 
            food_img = images.eat_event_img[lens]
        
        screen.blit(food_img, (pet_x - 100, pet_y))
        sec2_count += 1

# 약 모션
def medicine_motion():
    global screen, sick, medicine_img, pet_x, pet_y

    if sick == True:
        screen.blit(medicine_img, (pet_x - 70, pet_y))


###### 메뉴 - 청소 ######

def clean_motion(level):
    global pet_x, pet_y, pet_current, pet, cleaning

    if level == 0:
        if pet_x < 250:
            pet_current = (pet_current + 1) % len(images.baby_right)
            pet = images.baby_right[ pet_current ]
            pet_x += 10

    elif level == 1:
        if pet_x < 250:
            pet_current = (pet_current + 1) % len(images.kid_right)
            pet = images.kid_right[ pet_current ]
            pet_x += 10

    elif level == 2:
        if pet_x < 250:
            pet_current = (pet_current + 1) % len(images.adult_right)
            pet = images.adult_right[ pet_current ]
            pet_x += 10

def clean_tool_motion():
    global screen, clean_tool_img, pet_x, pet_y, pet_current

    clean_tool_img = images.clean_event_img[ pet_current ]

    if cleaning == True:
        screen.blit(clean_tool_img, (pet_x + 80, pet_y))

###### 기뻐하는 모션 ######

def happy_motion(level):
    global screen, pet, pet_x, pet_y, pet_current, sec2_count
    pet_x = 115
    pet_y = 200

    if level == 0:
        if sec2_count % 2 == 1:
            pet_y -= 50

        pet = images.baby_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.baby_happy)
        sec2_count +=1

    elif level == 1:
        if sec2_count % 2 == 1:
            pet_y -= 50

        pet = images.kid_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.kid_happy)
        sec2_count +=1

    elif level == 2:
        if sec2_count % 2 == 1:
            pet_y -= 50

        pet = images.adult_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.adult_happy)
        sec2_count +=1

def happy_effect():
    global screen, happy_effect_img1, happy_effect_img2, pet_x, pet_y, sec2_count

    if sec2_count % 2 == 0:
        screen.blit(happy_effect_img1, (pet_x + 60, pet_y - 20))
        screen.blit(happy_effect_img2, (pet_x - 45, pet_y + 30))
    


################################## 추가 모션 ##################################
    
###### 똥 생성 ######
def poop_make():
    global poop, poop_count, poop_sum, poop_x, poop_y, sick_count, screen, level_up, menu_crash, poop_img

    if menu_crash == 'off':
        if poop_sum < 3 and poop_count < 50:
            poop_count += 1
                
        elif poop_count == 50:
            poop_count = 0
            # poop_sum += 1
            # sick_count += 0
            poop = True
            menu_crash = 'on'
            
        if poop_sum == 1:
            num = poop_sum - 1
            screen.blit(poop_img[num], (poop_x[num], poop_y[num]))

        elif poop_sum > 1 and poop_sum <= 3:
            num = poop_sum - 1
            for i in range(num+1):
                screen.blit(poop_img[i], (poop_x[i], poop_y[i]))

###### 똥 캐릭터 모션 ######
def poop_motion(level):
    global pet, pet_x, pet_y, sec2_count, poop_sum

    if poop_sum < 3:
        if level == 0:

            pet = images.baby_poop
            pet_x = 100
            if sec2_count % 2 == 1:
                pet_x =120
            sec2_count += 1
            

        elif level == 1:

            pet = images.kid_poop
            pet_x = 100
            if sec2_count % 2 == 1:
                pet_x =120
            sec2_count += 1

        elif level == 2:

            pet = images.adult_poop
            pet_x = 100
            if sec2_count % 2 == 1:
                pet_x =120
            sec2_count += 1


###### 클릭 모션  ######
def click_motion(level):
    global screen, pet, pet_x, pet_y, pet_current, heart_img, sec2_count

    if level == 0:

        pet = images.baby_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.baby_happy)

    elif level == 1:

        pet = images.kid_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.kid_happy)

    elif level == 2:

        pet = images.adult_happy[pet_current]
        pet_current = (pet_current + 1) % len(images.adult_happy)

    if sec2_count % 2 == 1:
        screen.blit(heart_img, (pet_x + 15, pet_y - 50))
        
    sec2_count +=1 

###### 아픈 모션 ######
def sick_motion(level):
    global pet, pet_x, pet_y, pet_current, sick_effect_img

    if level == 0:

        pet = images.baby_sick[pet_current]
        pet_current = (pet_current + 1) % len(images.baby_sick)

    elif level == 1:

        pet = images.kid_sick[pet_current]
        pet_current = (pet_current + 1) % len(images.kid_sick)

    elif level == 2:

        pet = images.adult_sick[pet_current]
        pet_current = (pet_current + 1) % len(images.adult_sick)

def sick_effect():
    global screen, pet_x, pet_y, sick_effect_img

    if sick == True:
        screen.blit(sick_effect_img, (pet_x + 70, pet_y - 20))


###### 싫어하는 모션 ######
def unlike_motion(level):
    global pet, pet_x, pet_y, pet_current
    
    if level == 0:

        pet = images.baby_no[pet_current]
        pet_current = (pet_current + 1) % len(images.baby_no)

    elif level == 1:

        pet = images.kid_no[pet_current]
        pet_current = (pet_current + 1) % len(images.kid_no)

    elif level == 2:

        pet = images.adult_no[pet_current]
        pet_current = (pet_current + 1) % len(images.adult_no)
    

################################## 펫 정보 관리 ##################################

###### 펫 메뉴 상태 카운트 ######
def pet_state():
    global sick, poop_sum, menu_crash, walking, pet_x, death
    global play_count, eat_count, clean_count, play_state, eat_state, clean_state, clean_count, sick_state, sick_count, escape, escape_count, death, death_count

    if menu_crash == 'off':
        # 놀이 상태 카운트
        if play_state > 0:
            if play_count > 30:
                play_state -= 1
                play_count = 0
            else:
                play_count += 1
        # 포만감 상태 카운트
        if eat_state > 0:
            if eat_count > 25:
                eat_state -= 1
                eat_count = 0
            else:
                eat_count += 1
        elif eat_state == 0 and sick == False:
            sick = True
            walking = False
            pet_x = 110
            menu_crash = 'on'

        # 청소 상태 카운트
        if poop_sum == 3:
            if clean_state > 0: # 현재 시간 설정
                if clean_count > 30:
                    clean_state -= 1
                    clean_count = 0
                else:
                    clean_count += 1
            elif clean_state == 0 and sick == False:
                sick = True
                walking = False
                pet_x = 110
                death = 3
                menu_crash = 'on'

###### 게임오버 상태 카운트 ######
def gameover_state():
    global gameover_num, running, gameover, sick, poop_sum, menu_crash, walking, pet_x
    global play_state, eat_state, clean_state, clean_count, sick_state, sick_count, escape, escape_count, death, death_count

    # 도망 게임오버
    if play_state == 0:
        
        if escape < 3:
            if escape_count > 20:
                escape += 1
                escape_count = 0
            else:
                 escape_count += 1
        elif escape == 3:
            gameover = True
            running = False
            gameover_num = 1

    # 죽음 게임오버
    if sick == True:
        
        if death > 0:
            if death_count > 20:
                death -= 1
                death_count = 0
            else:
                death_count += 1
        else:
            gameover = True
            running = False
        
###### 게임오버 ######
def gameover_ending():
    global screen, WHITE, gameover_img, gameover, gameover_num
    while gameover:
        for event in pygame.event.get():

            #pet_rect = pet_rect.move(speed)
                    
            if event.type == pygame.QUIT:
                gameover = False
                break

        if gameover == True:
            screen.fill(WHITE)
            screen.blit(images.gameover_img[gameover_num], (0, 0))
            pygame.display.flip()
                
                    
###### 치료 후 반복 작업 ######
def treatment_end():
    global clean_state, eat_state, play_state, clean_count, eat_count, play_count, escape, death

    clean_state = 3
    play_state = 3
    eat_state = 3
    clean_count = 0
    play_count = 0
    eat_count = 0
    escape = 0
    death= 5
                
###### 반복 작업 ######
def motion_end():
    global menu_crash, count, pet_direction, walking, play_state, pet_current, lens, sec2_count

    sec2_count = 0
    lens = 0
    pet_current = 0 # 임시
    menu_crash = 'off'
    count = 0
    pet_direction = 'right'
    walking = True


###### 진화 ######
def level_up_motion():
    global level_sum, count, pet_current, pet, pet_x, pet_y, level, walking, menu_crash

    if level_sum > 10 and level == 0:
        menu_crash = 'on'
        level_up = True
        pet_x = 120
        pet_y = 200
        walking = False
        if count < 9:
            pet_current = (pet_current + 1) % len(level_up1)
            pet = level_up1[ pet_current ]
            count += 1
        else:
            level = 1
            count = 0
            walking = True
            level_up = False
            menu_crash = 'off'
            
    elif level_sum > 20 and level == 1:
        menu_crash = 'on'
        level_up = True
        pet_x = 120
        pet_y = 200
        walking = False
        if count < 9:
            pet_current = (pet_current + 1) % len(level_up2)
            pet = level_up2[ pet_current ]
            count += 1
        else:
            level = 2
            count = 0
            walking = True
            level_up = False
            menu_crash = 'off'

###### 캐릭터 정보 창 ######

def information_window():
    global running, gray, screen, menu_crash, information, info_img, new_window, walking, clean_state, eat_state, death
    global game_heart_img, eat_heart_img, health_heart_img, heart_x_01, heart_y_01
    
    if information == True:
        # screen.fill(gray)
        screen.blit(info_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                    running = False
                    break
            elif event.type == pygame.MOUSEBUTTONUP:

                new_window = 'off'
                information = False
        for i in range(play_state):
            screen.blit(game_heart_img[i], (heart_x_01 + i * 30, heart_y_01))
        for i in range(eat_state):
            screen.blit(eat_heart_img[i], (heart_x_01 + i * 30, heart_y_01 + 90))
        for i in range(death):
            screen.blit(health_heart_img[i], (heart_x_01 + i * 30, heart_y_01 + 180))    

###### 설정창 ######

def setting_window():
    global running, advice, gray, screen, setting, setting_img, advice_img, new_window

    if setting == True:
        screen.blit(setting_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                    running = False
                    break
            # 버튼 메뉴 구현
            elif event.type == pygame.MOUSEBUTTONUP:

                mouse_pos = pygame.mouse.get_pos()

                # 화면돌아가기
                if mouse_pos[0] > 70 and mouse_pos[0] < 230 and mouse_pos[1] > 120 and mouse_pos[1] < 170:
                    new_window = 'off'
                    setting = False
                    break

                # 도움말
                elif mouse_pos[0] > 70 and mouse_pos[0] < 230 and mouse_pos[1] > 200 and mouse_pos[1] < 250:
                    setting = False
                    advice = True
                # 게임종료
                elif mouse_pos[0] > 70 and mouse_pos[0] < 230 and mouse_pos[1] > 280 and mouse_pos[1] < 330:
                    running = False
                    break  
                
    # 도움말 활성화
    elif advice == True:
        screen.blit(advice_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    break
            elif event.type == pygame.MOUSEBUTTONUP:
                    setting = True
                    advice = False


###### 메뉴 이미지 ###### 
def background_menu(x,y):
    global screen
    
    for i in range(len(images.menu_img)):

        menu = images.menu_img[i]

        if i < 4:
            screen.blit(menu, (x, y))
            x += 58
        elif i == 4:
            x = 100
            y = 335
            screen.blit(menu, (x, y))
        elif i == 5:
            x = 158
            y = 335
            screen.blit(menu, (x, y))
        
################################## 게임 실행 ##################################

def runGame():
    global pet_x, pet_y, menu_x, menu_y, pet_direction, pet_current, count, running, information, new_window, level_sum
    global menu_crash, walking, playing, cleaning, eating, treatment, happy, sec2_count, poop_sum, click, poop, sick, setting
    global play_state, eat_state
    
    while running:

        if new_window == 'off':
            clock.tick(3)
            
            for event in pygame.event.get():

                #pet_rect = pet_rect.move(speed)
                
                if event.type == pygame.QUIT:

                    running = False
                    break

                elif event.type == pygame.MOUSEBUTTONUP:

                    mouse_pos = pygame.mouse.get_pos()
                    ### 상단 메뉴 ###
                    # 플레이 아이콘 클릭시
                    if mouse_pos[0] > 35 and mouse_pos[0] < 80 and mouse_pos[1] > 35 and mouse_pos[1] < 80:
                        if playing == False and menu_crash == 'off':
                            walking = False
                            menu_crash = 'on'
                            pet_direction = 'up'
                            pet_current = 0
                            playing = True

                    # 식사 아이콘 클릭시
                    elif mouse_pos[0] > 93 and mouse_pos[0] < 138 and mouse_pos[1] > 35 and mouse_pos[1] < 80:
                        if eating == False and menu_crash == 'off':
                            walking = False
                            menu_crash = 'on'
                            pet_current = 0
                            eating = True

                    # 청소 아이콘 클릭시
                    elif mouse_pos[0] > 151 and mouse_pos[0] < 196 and mouse_pos[1] > 35 and mouse_pos[1] < 80:
                        if cleaning == False and menu_crash == 'off':
                            walking = False
                            menu_crash = 'on'
                            pet_current = 0
                            cleaning = True
                            if poop_sum != 0:
                                pet_x = 0
                    
                    # 치료 아이콘 클릭시 (treatment)
                    elif mouse_pos[0] > 209 and mouse_pos[0] < 254 and mouse_pos[1] > 35 and mouse_pos[1] < 80:
                        if treatment == False:
                            if menu_crash == 'off':
                                walking = False
                                menu_crash = 'on'
                                pet_current = 0
                                treatment = True
                            elif menu_crash == 'on' and sick == True:
                                walking = False
                                pet_current = 0
                                treatment = True

                    ### 하단 메뉴 ###

                    # info 아이콘 클릭시
                    elif mouse_pos[0] > 93 and mouse_pos[0] < 151 and mouse_pos[1] > 335 and mouse_pos[1] < 385:
                        
                        information = True
                        new_window = 'on'

                    # setting 아이콘 클릭시
                    elif mouse_pos[0] > 151 and mouse_pos[0] < 196 and mouse_pos[1] > 335 and mouse_pos[1] < 385:
                        
                        setting = True
                        new_window = 'on'

                    # 캐릭터 클릭시
                    elif mouse_pos[0] > pet_x and mouse_pos[0] < pet_x + 70 and mouse_pos[1] > pet_y and mouse_pos[1] < pet_y + 70:
                        if click == False and menu_crash == 'off':
                            walking = False
                            menu_crash = 'on'
                            pet_current = 0
                            click = True
                            # pet_x = 115
                        

            screen.fill(WHITE)
                        
            if walking == True:
           
                walk(level)

            # 아픈 모션
            if sick == True and treatment == False:
                sick_motion(level)
                sick_effect()

            ### 메뉴 모션 ###
            # 플레이
            if playing == True:
                if play_state == 5:
                    if count < 11:
                        unlike_motion(level)
                        count += 1
                    else:
                        playing = False
                        motion_end()
                else:
                    if count < 21:
                        play_motion(level)
                        count += 1
                        ball_motion()
                    else:
                        playing = False
                        happy = True
                        play_state += 1
                        pet_current = 0
                        count = 0

            # 식사
            if eating == True:
                if eat_state == 5:
                    if count < 11:
                        unlike_motion(level)
                        count += 1
                    else:
                        eating = False
                        motion_end()
                else:
                    if count < 24:
                        eating_motion(level)
                        count += 1
                        food_motion()

                    else:
                        eating = False
                        eat_state += 1
                        happy = True
                        pet_current = 0
                        count = 0

            # 청소
            if cleaning == True:
                if poop_sum != 0:
                    if count < 21:
                        clean_motion(level)
                        count += 1
                        clean_tool_motion()

                    else:
                        cleaning = False
                        happy = True
                        count = 0
                        pet_current = 0
                        poop_sum = 0
                else:
                    if count < 11:
                        unlike_motion(level)
                        count += 1
                    else:
                        cleaning = False
                        motion_end()

            # 치료
            if treatment == True:
                if sick == False:

                    if count < 11:
                        unlike_motion(level)
                        count += 1
                    else:
                        treatment = False
                        motion_end()

                else:
                    if count < 11:
                        eating_motion(level)
                        count += 1
                        medicine_motion()

                    else:
                        treatment = False
                        sick = False
                        happy = True
                        pet_current = 0
                        count = 0
                        treatment_end()

            ### 추가 모션 ###


            # 캐릭터 클릭
            if click == True:

                if count < 10:
                    click_motion(level)
                    count += 1
                else:
                    click = False
                    motion_end()
                        
            # 똥 캐릭터 모션
            if poop == True:

                if count < 10:
                    poop_motion(level)
                    count += 1
                else:
                    poop = False
                    poop_sum += 1
                    motion_end()

            else:
                poop_make()


            # 기쁜 모션
            if happy == True:

                if count < 11:
                    happy_motion(level)
                    happy_effect()
                    count += 1
                else:
                    happy = False
                    happy_count = 0
                    level_sum += 1
                    motion_end()


            level_up_motion()
            pet_state()
            screen.blit(pet, (pet_x, pet_y))
            # poop_make()
            background_menu(menu_x, menu_y)
            gameover_state()
            pygame.display.flip()


        elif new_window == 'on':


            information_window()
            setting_window()
            pygame.display.flip()

def initGame():
    global size, menu_x, menu_y, screen

    try:
        pygame.init()
        runGame()
        gameover_ending()
    finally:
        pygame.quit()


initGame()
