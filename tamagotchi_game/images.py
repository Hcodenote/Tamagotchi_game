import pygame

# 유아기 이미지 로드

# 유아기 정면
baby_front = pygame.image.load('baby_front.png')

# 유아기 왼쪽
baby_left = ['baby_left1.png', 'baby_left2.png']
for i in range(len(baby_left)):

    baby_left[i] = pygame.image.load(baby_left[i])

# 유아기 오른쪽
baby_right = ['baby_right1.png', 'baby_right2.png']
for i in range(len(baby_right)):

    baby_right[i] = pygame.image.load(baby_right[i])

# 유아기 식사
baby_eat = ['baby_eat1.png','baby_eat2.png']
for i in range(len(baby_eat)):

    baby_eat[i] = pygame.image.load(baby_eat[i])

# 유아기 행복
baby_happy = ['baby_front.png', 'baby_happy.png']
for i in range(len(baby_happy)):

    baby_happy[i] = pygame.image.load(baby_happy[i])

# 유아기 병듦
baby_sick = ['baby_sick1.png', 'baby_sick2.png']
for i in range(len(baby_sick)):

    baby_sick[i] = pygame.image.load(baby_sick[i])

# 유아기 놀이
baby_play = ['baby_play1.png', 'baby_play2.png']
for i in range(len(baby_play)):

    baby_play[i] = pygame.image.load(baby_play[i])

# 유아기 똥
baby_poop = pygame.image.load('baby_poop.png')

# 유아기 싫어함
baby_no = ['baby_no1.png', 'baby_no2.png']
for i in range(len(baby_no)):

    baby_no[i] = pygame.image.load(baby_no[i])

# 청소년기 이미지 로드

# 청소년기 정면
kid_front = pygame.image.load('kid_front.png')

# 청소년기 왼쪽
kid_left = ['kid_left1.png', 'kid_left2.png']
for i in range(len(kid_left)):

    kid_left[i] = pygame.image.load(kid_left[i])

# 청소년기 오른쪽
kid_right = ['kid_right1.png', 'kid_right2.png']
for i in range(len(kid_right)):

    kid_right[i] = pygame.image.load(kid_right[i])

# 청소년기 식사
kid_eat = ['kid_eat1.png','kid_eat2.png']
for i in range(len(kid_eat)):

    kid_eat[i] = pygame.image.load(kid_eat[i])

# 청소년기 행복
kid_happy = ['kid_front.png','kid_happy.png']
for i in range(len(kid_happy)):

    kid_happy[i] = pygame.image.load(kid_happy[i])

# 청소년기 병듦
kid_sick = ['kid_sick1.png', 'kid_sick2.png']
for i in range(len(kid_sick)):

    kid_sick[i] = pygame.image.load(kid_sick[i])

# 청소년기 놀이
kid_play = ['kid_play1.png', 'kid_play2.png']
for i in range(len(kid_play)):

    kid_play[i] = pygame.image.load(kid_play[i])

# 청소년기 똥
kid_poop = pygame.image.load('kid_poop.png')

# 청소년기 싫어함
kid_no = ['kid_no1.png', 'kid_no2.png']
for i in range(len(kid_no)):

    kid_no[i] = pygame.image.load(kid_no[i])


# 성체 이미지 로드

# 성체 정면
adult_front = pygame.image.load('adult_front.png')

# 성체 왼쪽
adult_left = ['adult_left1.png', 'adult_left2.png']
for i in range(len(adult_left)):

    adult_left[i] = pygame.image.load(adult_left[i])

# 성체 오른쪽
adult_right = ['adult_right1.png', 'adult_right2.png']
for i in range(len(adult_right)):

    adult_right[i] = pygame.image.load(adult_right[i])

# 성체 식사
adult_eat = ['adult_eat1.png','adult_eat2.png']
for i in range(len(adult_eat)):

    adult_eat[i] = pygame.image.load(adult_eat[i])

# 성체 행복
adult_happy = ['adult_happy1.png','adult_happy2.png']
for i in range(len(adult_eat)):

    adult_happy[i] = pygame.image.load(adult_happy[i])

# 성체 병듦
adult_sick = ['adult_sick1.png', 'adult_sick2.png']
for i in range(len(adult_sick)):

    adult_sick[i] = pygame.image.load(adult_sick[i])

# 성체 놀이
adult_play = ['adult_play1.png', 'adult_play2.png']
for i in range(len(adult_play)):

    adult_play[i] = pygame.image.load(adult_play[i])

# 성체 똥
adult_poop = pygame.image.load('adult_poop.png')

# 성체 싫어함
adult_no = ['adult_no1.png', 'adult_no2.png']
for i in range(len(adult_no)):

    adult_no[i] = pygame.image.load(adult_no[i])


# 메뉴 이미지 로드
menu_img = ['play.png', 'eat.png', 'toilet.png', 'treatment.png', 'info.png', 'setting.png']

for i in range(len(menu_img)):

    menu_img[i] = pygame.image.load(menu_img[i])


# 놀이(공)이벤트 이미지
play_event_img = ['ball1.png', 'ball2.png']
for i in range(len(play_event_img)):

    play_event_img[i] = pygame.image.load(play_event_img[i])

# 청소 이벤트 이미지
clean_event_img = ['clean1.png', 'clean2.png']
for i in range(len(clean_event_img)):

    clean_event_img[i] = pygame.image.load(clean_event_img[i])

# 식사 이벤트 이미지
eat_event_img = ['food1.png', 'food2.png', 'food3.png', 'food4.png']
for i in range(len(eat_event_img)):

    eat_event_img[i] = pygame.image.load(eat_event_img[i])

# 만족 이벤트 이미지
happy_event_img = pygame.image.load('happy.png')

# 아픔(알약) 이벤트 이미지
sick_event_img = pygame.image.load('medicine.png')

# 해골 이펙트 이미지
sick_img = pygame.image.load('sick.png')

# 똥 이벤트 이미지
poop_event_img = pygame.image.load('poop.png')

# 게임오버 이미지
gameover_img = ['gameover.png', 'gameover_escape.png']
for i in range(len(gameover_img)):

    gameover_img[i] = pygame.image.load(gameover_img[i])

# new_window 이미지
info_window_img = pygame.image.load('info_window.png')
setting_window_img = pygame.image.load('setting_window.png')
advice_img = pygame.image.load('advice.png')
heart_event_img = pygame.image.load('heart.png')
