# 💿📲
import pygame
import os
import math
import random  # XD
import asyncio # for in-browser play
import pygame

pygame.init()  # 🎊👾▶️
pygame.mixer.init() # 🎼🎶

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("oopsin: a color UNfriendly game")
#############################################################################################
# 🌍🌎🌏🌍🌎🌏🌍🌎🌏
# ✨📏 DIMS 📐✨
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#############################################################################################
# 🎵🎶🎵🎶🎵🎶🎵🎶🎵
themePath = os.path.join("assets/music","theme.ogg")
pygame.mixer.music.load(themePath) # 8 bit menu - cred fesliyan STUDIOS @ # https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6
pygame.mixer.music.play(-1) # should start and loop

owSound = pygame.mixer.Sound("assets/music/owSound.ogg") # pixel-explosion - cred Lumora_Studios @ https://pixabay.com/users/lumora_studios-39090352/
yaySound = pygame.mixer.Sound("assets/music/yaySound.ogg") # gameboy pluck - cred freesound_community @ https://pixabay.com/users/freesound_community-46691455
overSound = pygame.mixer.Sound("assets/music/overSound.ogg") # 8bit game over - cred Lesiakower @ https://pixabay.com/users/lesiakower-25701529/?
#############################################################################################
# 🎨🖼️🖌️ ASSETS 🎨🖼️🖌️
###### 🩺🏥😷 ASSETS: PLAYER
RUNNING = [pygame.image.load(os.path.join("assets/player/upscaled", "run1.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "run2.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "run3.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "run2.png"))]  # 🏃🏃
JUMPING = pygame.image.load(os.path.join("assets/player/upscaled", "jump.png"))  # ⬆️⬆️
DUCKING = [pygame.image.load(os.path.join("assets/player/upscaled", "duck1.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "duck2.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "duck3.png")),
           pygame.image.load(os.path.join("assets/player/upscaled", "duck2.png"))]  # ⬇️⬇️
###### 🤕❤️ || 🎁💚 ASSETS: OBSTACLES/TREATS
LAND_OBSTACLES = [pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleLarge1.png")),
                  pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleLarge2.png")),
                  pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleLarge3.png")),
                  pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall1.png")),
                  pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall2.png")),
                  pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall3.png"))]  # ⛰️💥🤕
AIR_OBSTACLES = [pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall1.png")),
                 pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall2.png")),
                 pygame.image.load(os.path.join("assets/items/reds/upscaled", "obstacleSmall3.png"))]  # 🌤️💥🤕
AIR_TREATS = [pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall1.png")),
              pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall2.png")),
              pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall3.png"))]  # 🌤️🎁🍴
LAND_TREATS = [pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatLarge1.png")),
               pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatLarge2.png")),
               pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatLarge3.png")),
               pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall1.png")),
               pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall2.png")),
               pygame.image.load(os.path.join("assets/items/greens/upscaled", "treatSmall3.png"))]  # ⛰️🎁🍴
###### 🚦🤎 ASSETS: COLORBLIND VERS
COLORBLIND_LAND_OBSTACLES = [pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleLarge1.png")),
                  pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleLarge2.png")),
                  pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleLarge3.png")),
                  pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall1.png")),
                  pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall2.png")),
                  pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall3.png"))]  # ⛰️💥🤕
COLORBLIND_AIR_OBSTACLES = [pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall1.png")),
                 pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall2.png")),
                 pygame.image.load(os.path.join("assets/items/colorblind-reds/upscaled", "obstacleSmall3.png"))]  # 🌤️💥🤕
COLORBLIND_AIR_TREATS = [pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall1.png")),
              pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall2.png")),
              pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall3.png"))]  # 🌤️🎁🍴
COLORBLIND_LAND_TREATS = [pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatLarge1.png")),
               pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatLarge2.png")),
               pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatLarge3.png")),
               pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall1.png")),
               pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall2.png")),
               pygame.image.load(os.path.join("assets/items/colorblind-greens/upscaled", "treatSmall3.png"))]  # ⛰️🎁🍴
###### 💥‼️ ASSETS: COLLIDE
COLLIDE_TREAT = pygame.image.load(os.path.join("assets/react", "yay.png")) # 💥🎁
COLLIDE_OBSTACLE = pygame.image.load(os.path.join("assets/react", "ow.png")) # 💥🤕
###### 🛣️🏙️ ASSETS: BACKGROUND
CLOUD = pygame.image.load(os.path.join("assets/bg", "cloud.png"))  # ☁️
BG = pygame.image.load(os.path.join("assets/bg", "track.png"))  # 🏥
###### 👾⏯️ ASSETS: MENU TITLE
TITLE = pygame.image.load(os.path.join("assets/menu", "titleScreen.png"))
#############################################################################################
#######  👨‍🎓🎒📚 CLASSES: PLAYER & BACKGROUND 🏫🚌🚸
class Player:  # 🩺🏥😷
    # for stationary start position
    X_POS = 80  # 📐➡️
    Y_POS = 312  # ️️📐⬆️
    Y_POS_DUCK = 350  # 🦆📐 higher y-val bc lower
    JUMP_VEL = 8.7 # ⌚

    # init our imgs
    def __init__(self):
        # 🥇🥇🥇 🩺🏥😷✨🎨🖼️ 🥇🥇🥇
        self.duck_img = DUCKING  # 🩺😷️️️️🦆
        self.run_img = RUNNING  #️ 🩺😷➡️
        self.jump_img = JUMPING  # 🩺😷️️️⬆️

        self.player_run = True  # ✅🩺😷➡️
        self.player_jump = False  # ❌🩺😷⬆️
        self.player_duck = False  # ❌🩺😷⬆🦆

        self.step_index = 0  # 👣🎬
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]  # 🥇️🖼️
        self.player_rect = self.image.get_rect()  # 🎯💥⏹️
        self.player_rect.x = self.X_POS  # 🎯💥📐➡️
        self.player_rect.y = self.Y_POS  # ️️🎯💥📐⬆️

    def update(self, userInput):
        # update every while-loop it
        # KEYBOARD
        if self.player_run:
            self.run()  # ➡️
        if self.player_jump:
            self.jump()  # ⬆️️️
        if self.player_duck:
            self.duck()  # ⬇️

        if self.step_index >= 20:
            # 👣🎬 switch img @ ind=5, reset @ ind=10
            self.step_index = 0

        # ️️✨🎮🕹️✨
        # ⬆️️️🎮🕹️⬆️️️
        if userInput[pygame.K_UP] and not self.player_jump:
            self.player_run = False
            self.player_jump = True
            self.player_duck = False
        # ⬇️🎮🕹️⬇️🦆
        elif userInput[pygame.K_DOWN] and not self.player_jump:
            self.player_run = False
            self.player_jump = False
            self.player_duck = True
        # ️➡️🎮🕹️➡️
        elif not (self.player_jump or userInput[pygame.K_DOWN]):
            self.player_run = True
            self.player_jump = False
            self.player_duck = False

    # 🩺😷➡️
    def run(self):
        self.image = self.run_img[self.step_index // 5]  # 🎬🧠 uses modulus to switch img
        self.player_rect.x = self.X_POS  # 🎯💥📐➡️
        self.player_rect.y = self.Y_POS  # ️️🎯💥📐⬆️️️
        self.step_index += 1  # 👣🎬 switch img @ ind=5, reset @ ind=10

    # 🩺😷⬇️🦆
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]  # 🎬🧠 uses modulus to switch img
        self.player_rect.x = self.X_POS  # 🎯💥📐➡️
        self.player_rect.y = self.Y_POS_DUCK  # ️️🎯💥📐⬇️🦆🦆🦆🪿
        self.step_index += 1  # 👣🎬 switch img @ ind=5, reset @ ind=10

    def jump(self):
        self.image = self.jump_img
        if self.player_jump:
            # y = y + vspeed * timeStep
            self.player_rect.y -= self.jump_vel * 4  # reduce y coord so sprite moves up ⬆️⬆️⬆️
            self.jump_vel -= 0.8  # speed is 0 @ jump peak 🕒
        if self.jump_vel < -self.JUMP_VEL:
            self.player_jump = False  # resets when back to start velo, aka ground
            self.jump_vel = self.JUMP_VEL  # reset part

    # 🖼️🖌️🩺😷
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.player_rect.x, self.player_rect.y))
class Cloud():  # 🌥️🌤️
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(200, 800)  # set cloud X-coords
        self.y = random.randint(25, 150)  # set cloud Y-coords
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed  # ⬅️🌥️⬅️🌤️
        if self.x < -self.width:
            # once cloud is gone, bring it back!!
            self.x = SCREEN_WIDTH + random.randint(200, 800)  # reset cloud X-coords
            self.y = random.randint(25, 150)  # reset cloud Y-coords

    # 🖼️🖌️🌥️🌤️
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
####################################
###### 🧓👴🧬 CLASSES: ITEMS (TREATS & OBSTACLES INHERIT FROM HERE)
class Items():
    def __init__(self, image, type):
        # pull from parent (treat or obstacle)
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH  # created obstacles are just out of screen on right side

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            items.pop()
######  💚🎁💚 CLASSES: ALL TREATS
class Treats(Items):  # 🧑‍🍼🧬🎁 inherits from Items()
    GREENS = 0  # 💚🔰
    def __init__(self, image, type):
        # type is between 1 and 3, determines obstacle img
        self.image = image
        self.type = type
        super().__init__(image, self.type)

    def update(self):
        super().update()  # inherits from Items()
        if self.rect.x < -self.rect.width:  # remove off-screen treats
            treats.pop()
class LandTreats(Treats):
    # child inherits from obstacles
    def __init__(self, image):
        self.type = random.randint(0, 4)  # randomly gen type
        super().__init__(image, self.type)  # use super to init type w parent class
        self.rect.y = 305  # y-coord for where cacti is, smaller y-val bc higher on screen

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)  # draw obstacles
class AirTreats(Treats):  # 🌤️
    def __init__(self, image):  # 🎬 animated! doesnt have a type - disps one at a time
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 200
        self.index = 0

    def draw(self, SCREEN):  # 🎨🖼️🖌️
        SCREEN.blit(self.image[self.type], self.rect)  # 🎨🖼️🖌️🌤️
###### ❤️🤕❤️ CLASSES: ALL OBSTACLES
class Obstacles(Items):  # 🧑‍🍼🧬💥 inherits from Items()
    REDS = 0  # ❤️🔰
    def __init__(self, image, type):
        # type is between 1 and 3, determines obstacle img
        self.image = image
        self.type = type
        super().__init__(image, self.type)  # use super to init type w parent class

    def update(self):
        super().update()
        if self.rect.x < -self.rect.width:  # remove off-screen obstacles
            obstacles.pop()
class LandObstacles(Obstacles):  # 👶⛰️ ⬅️🧬⬅️ 👨‍🍼💥
    # indiv child/obstacles inherits from obstacles
    def __init__(self, image):
        self.type = random.randint(0, 4)  # randomly gen which img
        # type choose if its 1, 2 or 3 cacti, bc 0-index
        super().__init__(image, self.type)  # use super to init type w parent class
        self.rect.y = 305  # y-coord for where obstacle is

    def draw(self, SCREEN):  # 🎨🖼️🖌️
        SCREEN.blit(self.image[self.type], self.rect)  # 🎨🖼️🖌️⛰️💥🤕
class AirObstacles(Obstacles):  # 🌤️💥🤕
    def __init__(self, image):  # 🎬 animated! doesnt have a type - disps one at a time
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 200
        self.index = 0

    def draw(self, SCREEN):  # 🎨🖼️🖌️
        SCREEN.blit(self.image[self.type], self.rect)  # 🎨🖼️🖌️🌤️💥🤕
####################################
###### 💥‼️ CLASSES: COLLIDE
class CollideTreats():  # 🌤️💥🤕
    def __init__(self, image):
        self.x = 250
        self.y = 100
        self.image = COLLIDE_TREAT
    def draw(self, SCREEN):  # 🎨🖼️🖌️
        SCREEN.blit(self.image, (self.x, self.y))  # 🎨🖼️🖌️🌤️💥🤕
class CollideObstacles():  # 🌤️💥🤕
    def __init__(self, image):
        self.x = 250
        self.y = 100
        self.image = COLLIDE_OBSTACLE

    def draw(self, SCREEN):  # 🎨🖼️🖌️
        SCREEN.blit(self.image, (self.x, self.y))  # 🎨🖼️🖌️🌤️💥🤕
##############################################################################################
# 👾🧠💡 GAME START 👾🧠💡
async def main():  # 👾🧠💡
    ####################################
    ####### 🌍🌎🌏 INIT: GLOBAL VARS
    global game_speed, x_pos_bg, y_pos_bg, timePts, obstacles, treats, items, greens, allGreens, reds, obs_CollidedYet
    ###### 🎲❤️💚🤎 INIT: COLORBLIND ODDS
    if random.randint(0, 99) <= 7: # 🎲❤️💚🤎
        COLORBLIND_MODE = True # 🎲🤎
    else:
        COLORBLIND_MODE = False # 🎲❤️💚
    ####### 🌍🌎🌏 INIT: VARS
    run = True  # ✅🏃💦
    clock = pygame.time.Clock() # 👾🕐
    game_speed = 20  # 🏃‍➡️⏩

    x_pos_bg = 0 # ➡️📐
    y_pos_bg = 420 # ⬇️📐

    player = Player() # 🩺🏥😷
    cloud = Cloud()  # 🌥️🌤️

    ###### 🤕❤️ || 🎁💚 INIT: OBSTACLES/TREATS COLLIDE
    collideTreats = CollideTreats(COLLIDE_TREAT) # 💥🎁
    collideObstacles = CollideObstacles(COLLIDE_OBSTACLE) # 💥🤕
    collidingObstacle = False # ❌💥🤕
    collidingTreat = False # ❌💥🎁

    greens = Treats.GREENS # 🎁💚
    reds = Obstacles.REDS # 🤕❤️

    ###### INIT: SCORE & TRACK MOVING ITEMS 💯🔰
    allGreens = 0 # 💯💚
    death_count = 0 # 💯💀
    timePts = 0 # 💯🕐
    items = [] # ⬅️
    obstacles = [] # ⬅️🤕❤️
    treats = [] # ️⬅️🎁💚

    ###### INIT: FONT ✍️🔠
    fontSmol = pygame.font.Font('PKMN_RBYGSC.ttf', 15) # ✍️🦐
    fontTol = pygame.font.Font('PKMN_RBYGSC.ttf', 80) # ✍️🐳

    ####################################
    def score():
        global timePts, game_speed, greens, reds
        ####################################
        ###### SCORE: TIME & GAMESPEED 💯⏱️️⏩
        timePts += 1  # 💯🕐🔄️
        if timePts % 100 == 0:
            game_speed += 1 # ⏱️⏩

        #################################### 💯✍️🔠↗️
        ###### SCORE: RED STRIKES  ✍️🔠💥️🤕❤️
        scoreRed = ("Red Strikes: " + str(reds) + "/3") # ✍️🔠
        text = fontSmol.render(scoreRed, True, (0, 0, 0)) # ✍️📐
        textRect = text.get_rect()
        textRect.midright = (SCREEN_WIDTH - 50, 30)  # ✍️↗️
        SCREEN.blit(text, textRect) # ✍️📺
        ###### SCORE: GREEN STRIKES  ✍️🔠💥️🎁💚
        if allGreens == 0:
            scoreGreen = ("Green Percent: n/a") # ✍️🔠🔰
        else:
            scoreGreen = ("Green Percent: " + str(100*greens/allGreens)[:5]) # ✍️🔠
        text = fontSmol.render(scoreGreen, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.midright = (SCREEN_WIDTH - 50, 60) # ✍️↗️
        SCREEN.blit(text, textRect) # ✍️📺

        #################################### 💯✍️🔠↖️️
        ###### SCORE: TIME 👾🕐
        scoreTime = ("Time: " + str(math.floor(timePts / 30))) # ✍️🔠
        text = fontSmol.render(scoreTime, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.midleft = (50, 30) # ✍️↖️️
        SCREEN.blit(text, textRect) # ✍️📺
        ###### SCORE: SPEED # ⏱️⏩
        gameSpeed = ("Speed: " + str(game_speed))  # ✍️🔠
        text = fontSmol.render(gameSpeed, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.midleft = (50, 60) # ✍️↖️️
        SCREEN.blit(text, textRect) # ✍️📺
    ####################################
    ###### DISPLAY: BACKGROUND ⬅️🖼️
    def background():
        global x_pos_bg, y_pos_bg # 🌍📐🖼️ INIT: GLOBAL VARS
        image_width = BG.get_width() # 🖼️📐↔️
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg)) # 🖌️📺1️⃣
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg)) # 🖌️📺2️⃣ keep 2 ready for when 1 leaves screen
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg)) # 🖌️📺 get another bg-2 ready
            x_pos_bg = 0 # 🖼️📐🔰
        x_pos_bg -= game_speed # ⬅️ 🖼️1️⃣ ⬅️ 🖼️2️⃣
    ####################################
    while run: # 👾🔄️
        ###### 🙅🏳️ exit game """safely"""
        for event in pygame.event.get(): # 🔄️
            if event.type == pygame.QUIT: # 🙅🏳️
                run = False  # 👾⏸️
        ###### 👾▶️
        SCREEN.fill((255, 255, 255)) # 🖼️⬜
        userInput = pygame.key.get_pressed() # 🧑‍💻🎮

        player.draw(SCREEN) # 🖌️📺
        player.update(userInput) # 🎮🔄️🏃‍➡️

        ####################################
        if len(items) <= 0: # 🎲⏹️✨ if no items in list, randomly gen a new one
            if COLORBLIND_MODE == True: # 🎁🤕🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎🤎 simulate 8% colorblind
                if random.randint(0, 3) == 0: # 🎲
                    items.append(LandObstacles(COLORBLIND_LAND_OBSTACLES)) # ⏹️✨
                    obstacles.append(LandObstacles(COLORBLIND_LAND_OBSTACLES)) # 🤕✨
                elif random.randint(0, 3) == 1: # 🎲
                    items.append(LandTreats(COLORBLIND_LAND_TREATS)) # ⏹️✨
                    treats.append(LandTreats(COLORBLIND_LAND_TREATS)) # 🎁✨
                    allGreens += 1 # 💯💚
                elif random.randint(0, 3) == 2: # 🎲
                    items.append(AirObstacles(COLORBLIND_AIR_OBSTACLES)) # ⏹️✨
                    obstacles.append(AirObstacles(COLORBLIND_AIR_OBSTACLES)) # 🤕✨
                elif random.randint(0, 3) == 3: # 🎲
                    items.append(AirTreats(COLORBLIND_AIR_TREATS)) # ⏹️✨
                    treats.append(AirTreats(COLORBLIND_AIR_TREATS)) # 🎁✨
                    allGreens += 1 # 💯💚
            else: # 🎁🤕💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚❤️💚 tru colors
                if random.randint(0, 3) == 0: # 🎲
                    items.append(LandObstacles(LAND_OBSTACLES)) # ⏹️✨
                    obstacles.append(LandObstacles(LAND_OBSTACLES)) # 🤕✨
                elif random.randint(0, 3) == 1: # 🎲
                    items.append(LandTreats(LAND_TREATS)) # ⏹️✨
                    treats.append(LandTreats(LAND_TREATS)) # 🎁✨
                    allGreens += 1 # 💯💚
                elif random.randint(0, 3) == 2: # 🎲
                    items.append(AirObstacles(AIR_OBSTACLES)) # ⏹️✨
                    obstacles.append(AirObstacles(AIR_OBSTACLES)) # 🤕✨
                elif random.randint(0, 3) == 3: # 🎲
                    items.append(AirTreats(AIR_TREATS))  # ⏹️✨
                    treats.append(AirTreats(AIR_TREATS)) # 🎁✨
                    allGreens += 1 # 💯💚
        # ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️️❤️❤️❤️❤️❤️❤️❤️❤️❤️️❤️❤️❤️❤️❤️
        for obstacle in obstacles: # 🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕🤕
            obstacle.draw(SCREEN) # 🤕🖌️📺
            obstacle.update() # 🤕🔄️
            ############## CASE 1 -- collide happening BUT logic doesnt know abt it yet 🧠💥❔
            if player.player_rect.colliderect(obstacle.rect) and not collidingObstacle:
                death_count += 1 # 💯💀
                reds += 1 # 💯💥❤️
                collidingObstacle = True # 💥✅
                owSound.play() # 👎🎵
                collideObstacles.draw(SCREEN) # 💥🖌️
            ############## CASE 2 -- logic knows collide is happening 🧠💥✅
            elif player.player_rect.colliderect(obstacle.rect) and collidingObstacle:
                collideObstacles.draw(SCREEN) # 🤕🖌️📺
                if reds == 3: # 3️⃣❤️💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
                    textA = fontTol.render("GAME", True, (0, 0, 0))  # ✍️🔠
                    textRectA = textA.get_rect()
                    textRectA.center = (SCREEN_WIDTH - 450, SCREEN_HEIGHT - 500)
                    SCREEN.blit(textA, textRectA)  # ✍️📺

                    textB = fontTol.render("OVER", True, (0, 0, 0))  # ✍️🔠
                    textRectB = textB.get_rect()
                    textRectB.center = (SCREEN_WIDTH - 450, SCREEN_HEIGHT - 400)
                    SCREEN.blit(textB, textRectB)  # ✍️📺

                    overSound.play() # 🎵💀

                    pygame.display.update() # 🔄️ update screen
                    pygame.time.delay(3000) # 🕐⏯️
                    menu(death_count) # 💯💀🔄️🔰✨
            ############## CASE 3 -- logic thinks collide is happening, but it's done 🧠💥❌
            elif not player.player_rect.colliderect(obstacle.rect) and collidingObstacle:
                collidingObstacle = False # 💥❌
        # 💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚
        for treat in treats: # 🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁
            treat.draw(SCREEN) # 🎁🖌️📺
            treat.update() # 🎁🔄️
            ############## CASE 1 -- collide happening BUT logic doesnt know abt it yet 🧠💥❔
            if player.player_rect.colliderect(treat.rect) and not collidingTreat: # did collide - game has to know first collide instance
                greens += 1 # 💯💥💚
                collidingTreat = True  # 💥✅
                yaySound.play() # 🎉🎵
                collideTreats.draw(SCREEN) # 💥🖌️
            ############## CASE 2 -- logic knows collide is happening 🧠💥✅
            elif player.player_rect.colliderect(treat.rect) and collidingTreat:
                collideTreats.draw(SCREEN) # 💥🖌️
            ############## CASE 3 -- logic thinks collide is happening, but it's done 🧠💥❌
            elif not player.player_rect.colliderect(treat.rect) and collidingTreat:
                collidingTreat = False  # 💥❌

        background() # 🖼️

        cloud.draw(SCREEN)  # 🖌️🌤️
        cloud.update() # 🌤️🔄️

        score() # 💯

        await asyncio.sleep(0)

        clock.tick(30) # 🕜🔄️ fps
        pygame.display.update() # 🔄️
################################################################################################
def menu(death_count): # 💯💀
    global timePts # 🌍💯🕐
    run = True # 👾▶️
    while run:
        #################################### WRITE TITLE CARD
        SCREEN.fill((255, 255, 255))  # # 🖼️⬜
        SCREEN.blit(TITLE, (SCREEN_WIDTH // 2 - 550, SCREEN_HEIGHT // 2 - 300)) # ✍️📺

        fontTol = pygame.font.Font('PKMN_RBYGSC.ttf', 20) # ✍️🔠🐳
        fontSmol = pygame.font.Font('PKMN_RBYGSC.ttf', 15) # ✍️🔠🦐

        text = fontTol.render("Press Any Key to Play Again", True, (0, 0, 0)) # ✍️🔠
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH - 550, SCREEN_HEIGHT - 210)
        SCREEN.blit(text, textRect)

        textB = fontTol.render("Press ESC to Quit", True, (0, 0, 0)) # ✍️🔠
        textRectB = textB.get_rect()
        textRectB.center = (SCREEN_WIDTH - 550, SCREEN_HEIGHT - 170)
        SCREEN.blit(textB, textRectB)

        textA = fontTol.render("A Color UNfriendly Game", True, (0, 0, 0)) # ✍️🔠
        textRectA = textA.get_rect()
        textRectA.center = (SCREEN_WIDTH - 550, SCREEN_HEIGHT - 130)
        SCREEN.blit(textA, textRectA)
        # 💀🖼️🖌️💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯
        if death_count > 0: # is there a past score to report?
            # 💯💯💯💯💯💯💯💯💯💯💯💯💯💯💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚
            if greens == 0: # 💚🔰
                greenScore = "n/a"
            else: # 💚💥
                greenScore = str(100 * greens / allGreens)[:5]
            score = fontSmol.render(("Green Percent: " + greenScore), True, (0, 0, 0)) # ✍️🔠
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH - 550, SCREEN_HEIGHT - 30)
            SCREEN.blit(score, scoreRect) # ✍️📺
            # 💯💯💯💯💯💯💯💯💯💯💯💯💯💯🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐🕐
            timeScore = str(math.floor(timePts / 30)) # 💯🕐
            score = fontSmol.render(("Time Playing: " + timeScore + " sec"), True, (0, 0, 0)) # ✍️🔠
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH - 550, SCREEN_HEIGHT - 60)
            SCREEN.blit(score, scoreRect) # ✍️📺

        pygame.display.update()  # 🖼️🔄️

        for event in pygame.event.get(): # 🔄
            if event.type == pygame.QUIT: # 🙅🏳️ safe quit
                run = False # ⏸️
            if event.type == pygame.KEYDOWN: # 🎮 if any key
                if event.key == pygame.K_ESCAPE:  # 🚨 if hit escape
                    run = False # ⏸️
                    pygame.quit()  # 🙅🏳️ will trigger during next pygame.event.get()
                else:
                    main() # restart game

menu(death_count=0)
asyncio.run(main())
