import pygame
from sys import exit
from random import randint

def board_update(grid:list):
    #draw the grid with the coin and everything we need
    
    pygame.draw.rect(screen,"blue",[200,75,525,450]) #draw the grid(actually just a blue rectangle)
    
    x_value = [237.5, 312.5, 387.5, 462.5, 537.5, 612.5, 687.5] #storing some value which be use to set the position of our coin
    y_value = [112.5, 187.5, 262.5, 337.5, 412.5, 487.5] #storing some value which be use to set the position of our coin
    for y,line in enumerate(grid) :
        for x,item in enumerate(line) :
            if item == "X": 
                red_coin_surf = red_coin_sprite.get_rect(center = (x_value[x],y_value[y])) # set the coin to a new position
                screen.blit(red_coin_sprite,red_coin_surf) # blit the coin
            elif item =="0":
                blue_coin_surf = blue_coin_sprite.get_rect(center = (x_value[x],y_value[y])) # set the coin to a new position
                screen.blit(blue_coin_sprite,blue_coin_surf) # blit the coin
            else:
                pygame.draw.circle(screen,"white",(x_value[x],y_value[y]),30) #if this case don't have symbol just put while(to look empty) circile
def pointer_pos(mouse_pos:list):
    #return a x value which be used after with a list
    
    x_pos = mouse_pos[0] #we only need the x_axis value
    if x_pos<200:
        x = 0
    elif x_pos<725:
        x_pos -= 200
        x = -1
        while x_pos > 0 :
            x_pos -= 75
            x+=1
    else :
        x = 6
    return x
def pointer_print(color,pointer_x_value,):
    #print the pointer on the top of the grid to know where does the coin will fall
    
    y_pos_value = [237.5, 312.5, 387.5, 462.5, 537.5, 612.5, 687.5]
    
    if color == "red":
        red_pointer_surf = red_pointer_sprite.get_rect(center = (y_pos_value[pointer_x_value],25))
        screen.blit(red_pointer_sprite,red_pointer_surf)
    elif color == "blue":
        blue_pointer_surf = blue_pointer_sprite.get_rect(center = (y_pos_value[pointer_x_value],25))
        screen.blit(blue_pointer_sprite,blue_pointer_surf)
def change_color(color):
    #change the color after each turn 
    if color == "red" :
        return "blue"
    else :
        return "red"
def play(grid:list,pointer_x_value:int,color:str):
    # add to the grid the play of the player
    column = pointer_x_value
    for number_line in range(len(grid)) :
        if grid[0][column] !=  "-": # if the first line is already full we can't play
            return False
        if  number_line == 5 or grid[number_line+1][column] !=  "-" :
            if color == "red":
                grid[number_line][column] = "X"
                return True
            if color == "blue":
                grid[number_line][column] = "0"
                return True
def check_for_victory(color:str,grid: list)->bool:
    """
        check if a player win

        Parameters:
            color:               (str) the color of the player
            grid:                (list) a 2d list
        Return:
            (bool) 'True' if the player win, 'False' otherwise

    """
    if color == "red":
        sign = "X"
    elif color == "blue":
        sign = "0"
    for line_number, line in enumerate(grid):
        for column_number, symbol in enumerate(line) :        # check for every symbol in every line
            if symbol == sign: #if the symbol found is equal to the number of the player
                        vertical_combination = 0
                        horizontal_combination = 0       # create a variable for every
                        right_diagonal_combination = 0   # wining conditions
                        left_diagonal_combination = 0
                        # Check every winning conditions
                        try:
                            for index in range (4): 
                                if grid[line_number + index][column_number] == sign:
                                    vertical_combination += 1
                        except IndexError:
                            # the condition is not satisfied 
                            pass
                        try:
                            for index in range(4) :
                                if grid[line_number][column_number + index] == sign:
                                    horizontal_combination += 1
                        except IndexError:
                            pass
                        try:
                            for index in range(4) :
                                if grid[line_number + index][column_number + index] == sign:
                                    right_diagonal_combination += 1
                        except IndexError:
                            pass
                        try:
                            for index in range(4) :
                                if grid[line_number + index][column_number - index] == sign:
                                    left_diagonal_combination += 1
                        except IndexError:
                            pass
                        # check is one of the condition is satisfied
                        if vertical_combination == 4 or horizontal_combination == 4 or right_diagonal_combination == 4 or left_diagonal_combination == 4:
                            return True
    return False

            
pygame.init() #initalize pygame 
screen = pygame.display.set_mode((1000, 600)) # set the size of the window
pygame.display.set_caption('Puissance 4') # set the name 
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # set the font
game_active = 0 # set the state of the window
grid = ["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"] # creating the grid
x_pointer_value = 0 
pygame.mixer.music.load("music\sound.mp3")#import the music
player_name = []
player_red_score = 0
player_blue_score = 0
color_list = ["red","blue"]
color = color_list[randint(0,1)]#choose a ramdom color to start with

# we intialize the coin and the pointer for each color
red_coin_sprite = pygame.image.load("img\coin-red.png").convert_alpha()
red_coin_sprite = pygame.transform.scale(red_coin_sprite, (60,60))
red_pointer_sprite = pygame.image.load("img\pointer-red.png").convert_alpha()
red_pointer_sprite = pygame.transform.scale(red_pointer_sprite,  (60,60))
blue_coin_sprite = pygame.image.load("img\coin-blue.png").convert_alpha()
blue_coin_sprite = pygame.transform.scale(blue_coin_sprite,  (60,60))
blue_pointer_sprite = pygame.image.load("img\pointer-blue.png").convert_alpha()
blue_pointer_sprite = pygame.transform.scale(blue_pointer_sprite,  (60,60))

# set the vs logo
logo_vs_sprite = pygame.image.load("img\Combat-Versus-PNG-Images.png").convert_alpha()
logo_vs_sprite = pygame.transform.scale(logo_vs_sprite, (200,200))
logo_vs_surf = logo_vs_sprite.get_rect(center = (500,250))

#set some string
intro_sprite = test_font.render("bienvenue dans ce puissance 4", True, 'black')
intro_surf = intro_sprite.get_rect(center = (500,100))
intro_red_sprite = test_font.render("Donne moi ton nom joueur Rouge :", True, 'black')
intro_red_surf = intro_red_sprite.get_rect(center = (500,200))
intro_blue_sprite = test_font.render("Donne moi ton nom joueur Bleu :", True, 'black')
intro_blue_surf = intro_blue_sprite.get_rect(center = (500,200))
play_again_sprite = test_font.render("to play again press any key", True, 'black')
play_again_surf = play_again_sprite.get_rect(center = (500,500))

test_font = pygame.font.Font('font/Pixeltype.ttf',70)#we are modifying the size of the font because we want the text to be bigger
connect_4_name_sprite = test_font.render("puissance 4", True, 'black')
connect_4_name_surf = connect_4_name_sprite.get_rect(center = (500,50))

for player in range(2):# we want two player
    texte = ""
    game_parameters = True
    
    while game_parameters:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(texte) != 0 :
                        player_name.append(texte)
                        game_parameters = False
                elif event.key == pygame.K_BACKSPACE:
                    # delete the last key
                    texte = texte[:-1]
                else:
                    if len(texte) <10:
                    # add the key to the string
                        texte += event.unicode
        if player == 0: # the player is red so background in red
            screen.fill("red")
            texte_sprite = test_font.render(texte, True, 'black')
            texte_surface = texte_sprite.get_rect(center = (500,300))
            screen.blit(intro_red_sprite,intro_red_surf)
        else:# the player is blue so background in blue
            screen.fill("blue")
            texte_sprite = test_font.render(texte, True, 'black')
            texte_surface = texte_sprite.get_rect(center = (500,300))
            screen.blit(intro_blue_sprite,intro_blue_surf)
    
        screen.blit(intro_sprite,intro_surf)
        pygame.draw.rect(screen,"black",texte_surface,2 )
        screen.blit(texte_sprite,texte_surface)
        pygame.display.flip()
#we are creating the string for the name
player_red = player_name[0]
player_blue = player_name[1]

test_font = pygame.font.Font('font/Pixeltype.ttf',40)


red_name_sprite = test_font.render(player_red, True, 'black')
red_name_surf = red_name_sprite.get_rect(center = (150,150))

blue_name_sprite = test_font.render(player_blue, True, 'black')
blue_name_surf = blue_name_sprite.get_rect(center = (825,150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == 1: # if the game is playing
            if event.type == pygame.MOUSEMOTION:
                x_pointer_value = pointer_pos(pygame.mouse.get_pos()) 
            if event.type == pygame.MOUSEBUTTONDOWN :# if the player click
                if play(grid,x_pointer_value,color):#if the play is allowed
                    if check_for_victory(color,grid) :#if there is a victory
                        pygame.mixer.music.play(-1)# play the music
                        if color == "blue":
                            player_blue_score += 1
                        else :
                            player_red_score += 1
                        game_active = 2 # set game mode to victory mode
                        color = color_list[randint(0,1)]#choose the new color
                    else :
                        color = change_color(color) #switch the color
                        
        elif game_active == 0:#if game is on menu wait for the play to click for playing the game
            if event.type == pygame.KEYDOWN:
                game_active = 1
        else :
            if event.type == pygame.KEYDOWN:
                game_active = 0
                grid = ["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"]
                pygame.mixer.music.stop()
                
    if game_active == 1:
        #print the game 
        screen.fill("white")
        board_update(grid)
        pointer_print(color,x_pointer_value)
        
    elif game_active == 0 :
        #print the menu
        red_score_sprite = test_font.render("victoire : "+ str(player_red_score), True, 'black')
        red_score_surf = red_score_sprite.get_rect(center = (150,250))
        
        blue_score_sprite = test_font.render("victoire :  "+ str(player_blue_score), True, 'black')
        blue_score_surf = blue_score_sprite.get_rect(center = (825,250))
        
        screen.fill("white")
        screen.blit(logo_vs_sprite,logo_vs_surf)
        screen.blit(connect_4_name_sprite,connect_4_name_surf)
        pygame.draw.rect(screen,"red",[25, 75, 275, 350])
        pygame.draw.rect(screen,"blue",[675, 75, 300, 350])
        screen.blit(red_name_sprite,red_name_surf)
        screen.blit(blue_name_sprite,blue_name_surf)
        screen.blit(red_score_sprite,red_score_surf)
        screen.blit(blue_score_sprite,blue_score_surf)
        screen.blit(play_again_sprite,play_again_surf)
        
    else:
        #print the vicory mode
        screen.fill("white")
        board_update(grid)
        screen.blit(play_again_sprite,play_again_surf)
    pygame.display.flip() #refreshing the window with new element 