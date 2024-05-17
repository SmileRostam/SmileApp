import pgzrun
import os
import random
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'Smile App'
# ----------------menu actors-----------------
background = Actor('back',(500,350))
wellcome = Actor('wellcome',(500,200))
close_game_menu = Actor('closee',(670,170))
close_about_menu = Actor('closee',(620,210))
games = Actor('games button',(500,500))
about = Actor('about app button',(500,600))
abut_app_menu = Actor('about app',(500,350))
games_menu = Actor('game menu',(500,350))
goalkeeper_game_button = Actor('goalkeeper1',(500,260))
comming_soon = Actor('comming soon1',(500,450))
sounds_app_button = Actor('sound',(500,400))
sounds_app_mute = Actor('sound mute',(500,400))
# ----------------game actors-----------------------------
ground = Actor('zamin' , (500,350))
ball = Actor('ball' , (500,150))
postL = Actor('postl' , (245,643))
postR = Actor('postr' , (775,643))
post = Actor('postt',(517,644))
gk = Actor('gk',(500,635))

save_icon = Actor('save icon',(75,50))
gaols_icon = Actor('gaols icon',(75,110))
shoots_icon = Actor('shoot',(925,50))
score_icon = Actor('score',(925,110))
pause_icon = Actor('pause',(250,50))
pause_menu = Actor('pause menu',(500,350))
close_pause_goalkeepeing_manu = Actor('close game menu',(650,115))
about_game_button = Actor('about game button1',(500,200))
sounds_game_mute = Actor('sounds game mute',(500,355))
sounds_game_unmute = Actor('sounds game unmute',(500,355))
updating = Actor('updating1',(585,335))
close_about_game_manu = Actor('close game menu',(650,115))
about_game_menu = Actor('about game menu',(500,350))
exit_game = Actor('exit game menu',(500,500))
game_sound_icon = Actor('game sound',(90,190))
game_sound_mute_icon = Actor('game sound mute',(90,190))

# ------------menu bulyan-------------

main_menu = True
about_menu_enable = False
games_menu_enable = False
goalkeeper_game = False
button_game_enable = False
app_sounds = True
app_sounds_enable = True


# --------------game bulyan----------------

main_goalkeeper_game = False
game_enable = False
ball_move = False
pause_goalkeepeing_menu_enable = False
about_game_menu_enable = False
buttons_pause_menu = False
game_sounds = True
pause_goalkeepeing_menu_button = False


# -----------  game Variable -------------

x = random.randrange(200,820,5)
speed_ball = 10
player_move = 5
saves = 0
goals = 0
shoots  = 0
score = 0
level = 1


def update():
    global x , speed_ball , ball_move ,  saves , goals , score , level , player_move , main_goalkeeper_game , save_light_enable , goal_light_enable
    if about_menu_enable and wellcome.y > -50 and games.y < 1000 and about.y < 1000:
        wellcome.y -= 10 
        games.y += 10 
        about.y += 10
    
    elif games_menu_enable and wellcome.y > -50 and games.y < 1000 and about.y < 1000 :
        wellcome.y -= 10 
        games.y += 10 
        about.y += 10
    elif not about_menu_enable and not games_menu_enable:
        wellcome.y = 200
        games.y = 500
        about.y = 600
        #------------------  player moves  ----------------
    if goalkeeper_game == True :
        if keyboard.A and gk.x > 245 and main_goalkeeper_game and game_enable:
            gk.x -= player_move
            
        if keyboard.D and gk.x < 775 and main_goalkeeper_game and game_enable:
            gk.x += player_move
            
        if keyboard.W and gk.y > 620 and main_goalkeeper_game and game_enable:
            gk.y -= 4 

        if keyboard.S and gk.y < 643 and main_goalkeeper_game and game_enable:
            gk.y += 4
        #-------------------  ball moves  ------------------
        if ball_move == True :
            
            if ball.x > x :
                ball.x -= 4
                
            if ball.x < x :
                ball.x += 4

            if ball.y < 700 :
                ball.y += speed_ball 
                ball.angle += 10
        #---------------------  goals  ----------------------
        if ball.y >= 700 :
            
            if score == 100:
                score -= 100
            elif score == 200:
                score -= 200
            elif score == 300:
                score -= 300
            elif score == 400:
                score -= 400
            elif score == 0: 
                score = 0 
            else:
                score-= 500
            x = random.randrange(200,820,5)
            ball_move = False
            ball.y = 150
            ball.x = 500
            goals += 1
            sounds.goal.play()
    #-------------------  saves  ---------------------
        if ball.colliderect(gk):
            x = random.randrange(200,820,5)
            ball_move = False
            ball.y = gk.y - 0.5
            ball.x = gk.x
            time.sleep(0.15)
            ball.y = 150
            ball.x = 500
            saves += 1
            score += 100
            if app_sounds:
                sounds.save.play()
            
    #---------------  collide to postes  ----------------
        if ball.colliderect(postL):
            x = random.randrange(200,820,5)
            ball_move = False
            ball.y = 150
            ball.x = 500
            sounds.post.play()
        elif ball.colliderect(postR):
            x = random.randrange(200,820,5)
            ball_move = False
            ball.y = 150
            ball.x = 500
            sounds.post.play()
    #------  switch level ( playerSpeed , ballSpeed )  ------
        if score < 500 :
            level = 1
            player_move + 0
            speed_ball + 0
        elif 500 <= score < 1500 :
            level = 2
            player_move + 1
            speed_ball + 1
        
        elif 1500 <= score < 3000 :
            level = 3
            player_move + 2
            speed_ball + 2
        
        elif 3000 <= score < 5000 :
            level = 4
            player_move + 3
            speed_ball + 3
        
        elif 5000 <= score < 10000 :
            level = 5
            player_move + 4 
            speed_ball + 4 

        elif score >= 10000 :
            level = 6
            player_move + 5
            speed_ball + 5

def draw():
    
    if main_menu :    
        background.draw()
        wellcome.draw()
        about.draw()
        games.draw()
        if app_sounds :
            sounds_app_button.draw()
        else :
            sounds_app_mute.draw()

        if about_menu_enable == True:
            abut_app_menu.draw()
            close_about_menu.draw()
        
        if games_menu_enable == True:
            games_menu.draw()
            close_game_menu.draw()
            goalkeeper_game_button.draw()
            comming_soon.draw()

    if games_menu_enable == True and goalkeeper_game:
        
        ground.draw()
        ball.draw()
        postL.draw()
        postR.draw()
        gk.draw()
        post.draw()
        post.draw()
        gaols_icon.draw()
        shoots_icon.draw()
        shoots_icon.angle = 30
        score_icon.draw()
        save_icon.draw()
        pause_icon.draw()

    #--------  ( saves , goals , shoots , score , level ) nubers  ------
        screen.draw.text(f' : {saves}', topleft = (100, 40), fontsize = 32, color = (165, 0, 89))
        screen.draw.text(f' : {goals}', topleft = (100, 100), fontsize = 32, color = (165, 0, 89))
        screen.draw.text(f'{shoots} :', topleft = (855,50), fontsize = 32, color = (165, 0, 89))
        screen.draw.text(f'{score} :', topleft = (835, 110), fontsize = 32, color = (165, 0, 89))
        screen.draw.text(f'{level}', topleft = (gk.x-3, gk.y-3), fontsize = 25, color = (255,255,255))

        if pause_goalkeepeing_menu_enable == True:
            pause_menu.draw()
            close_pause_goalkeepeing_manu.draw()
            about_game_button.draw()
            exit_game.draw()
            if app_sounds:
                sounds_game_unmute.draw()
            else:
                sounds_game_mute.draw()
            if about_game_menu_enable == True:
                about_game_menu.draw()
                close_about_game_manu.draw()

                
def on_mouse_down(pos):
    global about_menu_enable, game_enable , pause_goalkeepeing_menu_button, games_menu_enable , goalkeeper_game, button_game_enable ,ball_move , shoots , main_goalkeeper_game , pause_goalkeepeing_menu_enable , close_pause_goalkeepeing_manu , about_game_menu_enable , buttons_pause_menu ,  game_sounds , app_sounds ,app_sounds_enable
    if about.collidepoint(pos):
        about_menu_enable = True
        app_sounds_enable = False
        if app_sounds:
            sounds.select.play()
    if about_menu_enable and close_about_menu.collidepoint(pos):
        about_menu_enable = False
        if app_sounds:
            sounds.exit_menu.play()

    
    if games.collidepoint(pos):
        games_menu_enable = True
        button_game_enable = True
        app_sounds_enable = False
        if app_sounds:
            sounds.select.play()
    elif games_menu_enable and button_game_enable and close_game_menu.collidepoint(pos):
        games_menu_enable = False
        app_sounds_enable = True
        if app_sounds:
            sounds.exit_menu.play()

    #---------------   game start
    if games_menu_enable == True and button_game_enable == True and goalkeeper_game_button.collidepoint(pos):
        goalkeeper_game = True
        game_enable = True
        button_game_enable = False
        sounds_app_button.y = 2000
        
        if app_sounds :
            sounds.select.play()

    
#-----------------  app sound  ------------------------
    if app_sounds and (sounds_app_button.collidepoint(pos) or sounds_game_unmute.collidepoint(pos)) and app_sounds_enable :
        app_sounds = False
        sounds.select.play()
    elif app_sounds == False and (sounds_app_mute.collidepoint(pos) or sounds_game_mute.collidepoint(pos)) and app_sounds_enable:
        app_sounds = True

    #-----------------  shoot  ----------------------
    if goalkeeper_game == True :
        main_goalkeeper_game = True
        app_sounds_enable = False
        if ball.collidepoint(pos) and main_goalkeeper_game and game_enable:
            ball_move = True
            shoots += 1
            if app_sounds:
                sounds.shoot.play()
    #---------------  game pause  -------------------
        if pause_icon.collidepoint(pos):
            game_enable = False
            pause_goalkeepeing_menu_button = True
            main_goalkeeper_game = False
            pause_goalkeepeing_menu_enable = True
            buttons_pause_menu = True



        if pause_goalkeepeing_menu_enable and pause_goalkeepeing_menu_button and app_sounds and sounds_game_unmute.collidepoint(pos):
            app_sounds = False
            sounds.close.play()
        elif pause_goalkeepeing_menu_enable and pause_goalkeepeing_menu_button and not app_sounds and sounds_game_mute.collidepoint(pos) :
            app_sounds = True

            
        if buttons_pause_menu == True and close_pause_goalkeepeing_manu.collidepoint(pos):
            pause_goalkeepeing_menu_enable = False
            game_enable = True
            main_goalkeeper_game = True
            if app_sounds:
                sounds.close.play()
        if pause_goalkeepeing_menu_enable == True and pause_goalkeepeing_menu_button and about_game_button.collidepoint(pos):
            buttons_pause_menu = False
            pause_goalkeepeing_menu_button = False
            about_game_menu_enable = True
            if app_sounds:
                sounds.click.play()
        if about_game_menu_enable == True and close_about_game_manu.collidepoint(pos):
            about_game_menu_enable = False 
            pause_goalkeepeing_menu_button = True
            buttons_pause_menu = True
            if app_sounds:
                sounds.close.play()
        if pause_goalkeepeing_menu_enable == True and pause_goalkeepeing_menu_button and exit_game.collidepoint(pos):
            goalkeeper_game = False
            button_game_enable = True
            pause_goalkeepeing_menu_enable = False
            main_goalkeeper_game = False
            sounds_app_button.y = 400
            if app_sounds:
                sounds.click.play()
        
        
    
    if goalkeeper_game == True and pause_icon.collidepoint(pos) and app_sounds:
        sounds.pause.play()
    


        
    
            
pgzrun.go()