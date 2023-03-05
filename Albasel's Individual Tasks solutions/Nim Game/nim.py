import pygame
from random import shuffle, randint, choice
from sys import exit
pygame.init()
pygame.display.set_caption('Nim Game')
screen = pygame.display.set_mode((800,500))
# Game Functions
def show_buttons():
    for button, button_rect in buttons:
        screen.blit(button, button_rect)
coins = randint(15,40)
score_one = 0
score_two = 0
# Game Vars
game_active = 0
curr_turn = 1
buttons_visible = False
# All Game Variables here
Clock = pygame.time.Clock()
background_y_axis = 0
background_surface = pygame.image.load("assets/scrolling_background.png")
background_rect = background_surface.get_rect(topleft = (0,background_y_axis))
# player surfaces
fhand_xpos = -20
first_hand_surface = pygame.image.load("assets/Hand.png")
first_hand_surface = pygame.transform.scale_by(first_hand_surface,0.25)
first_hand_rect = first_hand_surface.get_rect(topleft = (fhand_xpos,200))
second_hand_surface = pygame.image.load("assets/Hand.png")
second_hand_surface = pygame.transform.scale_by(second_hand_surface,0.25)
second_hand_surface = pygame.transform.flip(second_hand_surface, True, False)
second_hand_rect = second_hand_surface.get_rect(topleft = (550,200))
hand_surfaces = [first_hand_rect,second_hand_rect]
# Game Gui
logo_image = pygame.image.load("assets/lOGO.png")
logo_image_rect = logo_image.get_rect(center=(400,180))
logo_caption = pygame.image.load("assets/caption.png")
logo_caption_rect = logo_caption.get_rect(center=(400,350))
rules_caption = pygame.image.load("assets/rules.png")
rules_caption_rect = rules_caption.get_rect(center=(400,450))
# Setup Game Fonts
game_font = pygame.font.Font('fonts/munro.ttf',26)
game_font_coins = pygame.font.Font('fonts/munro.ttf',36)
game_font_wins = pygame.font.Font('fonts/munro.ttf',50)
# Make Score rects
score_text = game_font.render(f'  {score_one} Coins  ',False,'Black')
score_text_two = game_font.render(f'  {score_two} Coins  ',False,'Black')
score_rect = score_text.get_rect(center =(75,30))
score_rect_two = score_text.get_rect(center =(715,30))
# Making Shadow for score
shadow_surface = pygame.Surface(score_text.get_size(), pygame.SRCALPHA)
shadow_surface.fill((0, 0, 0, 50)) # set the shadow color and alpha
shadow_surface_rect=shadow_surface.get_rect(center = (75,36))
shadow_surface_rect_two=shadow_surface.get_rect(center = (715,36))
# Create a mask with a rounded rectangle shape
mask = pygame.Surface(score_text.get_size(), pygame.SRCALPHA)
pygame.draw.rect(mask, (255, 255, 255), mask.get_rect(), border_radius=5)
# Use the mask to clip the shadow surface
shadow_surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
# Coin GUI
current_coins_gui = pygame.image.load("assets/Coin.png")
current_coins_gui = pygame.transform.scale_by(current_coins_gui,0.13)
current_coins_gui_rect = current_coins_gui.get_rect(center = (140,30))
current_coins_gui_rect_two = current_coins_gui.get_rect(center = (650,30))
pygame.display.set_icon(current_coins_gui)
all_coins = pygame.image.load("assets/Coin.png")
all_coins = pygame.transform.scale_by(all_coins,0.2)
all_coins_rect = all_coins.get_rect(center=(400,50))
if (coins > 10):
    all_coins_text = game_font_coins.render(f'{coins}',False,'#dd9911')
else:
    all_coins_text = game_font_coins.render(f'0{coins}',False,'#dd9911')

all_coins_tect_rect = score_text.get_rect(center = (440,45))

buttons = []
button_positions = [(350 + i * 55, 400) for i in range(10)] # button positions
for i in range(3):
    button = pygame.image.load(f"assets/Button{i}.png")
    button = pygame.transform.scale(button, (button.get_width()*3, button.get_height()*3))
    button_rect = button.get_rect(center=button_positions[i])
    buttons.append((button, button_rect))
one_click_cooldown = 500  # in milliseconds
one_click_time = pygame.time.get_ticks() - one_click_cooldown

# Displaying Turns
current_turn_text = game_font.render(f' It\'s P1 turn ',False,'Black')
current_turn_rect = score_text.get_rect(center =(380,480))


def update_gui():
    global score_text
    global score_one
    global score_text_two
    global all_coins_text
    global all_coins_tect_rect
    global current_turn_text
    global current_turn_rect
    global curr_turn
    score_text = game_font.render(f'  {score_one} Coins  ',False,'Black')
    score_text_two = game_font.render(f'  {score_two} Coins  ',False,'Black')
    if (coins >= 10):
        all_coins_text = game_font_coins.render(f'{coins}',False,'#dd9911')
    else:
        all_coins_text = game_font_coins.render(f'0{coins}',False,'#dd9911')
        all_coins_tect_rect = score_text.get_rect(center = (439.5,45))
    if (curr_turn % 2 == 1):
     current_turn_text = game_font.render(f' It\'s P1 turn ',False,'Black')
    else:
     current_turn_text = game_font.render(f' It\'s P2 turn ',False,'Black')
        
def pick_coins():
    global coins
    global score_one
    global score_text
    global curr_turn
    global score_two
    global one_click_time
    global one_click_cooldown
    global buttons_visible
    if(buttons_visible):
        if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if one click button is cooling down
                        for i, (button, button_rect) in enumerate(buttons):
                            if button_rect.collidepoint(event.pos):
                                current_time = pygame.time.get_ticks()
                                if current_time - one_click_time >= one_click_cooldown:
                                    # Button i was clicked
                                    if i in range(3):
                                        if ( coins - i >= 1):
                                            if ( i == 0):
                                                coins -=  1
                                            else:
                                                coins = (coins-i) - 1
                                            print(coins)
                                            if(curr_turn % 2 == 1):
                                                score_one += i + 1
                                            else:
                                                score_two += i + 1
                                            curr_turn +=1
                                            buttons_visible = not buttons_visible
                                            update_gui()
                                        one_click_time = current_time
                                        break
                                    
while True:
    #This is event loop it checks for all player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active == 1:
        if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if one click button is cooling down
                current_time = pygame.time.get_ticks()
                if current_time - one_click_time >= one_click_cooldown:
                    for hand in hand_surfaces:
                        if hand.collidepoint(event.pos):
                            buttons_visible = not buttons_visible
                            one_click_time = current_time
    else:
       if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                current_time = pygame.time.get_ticks()
                if current_time - one_click_time >= one_click_cooldown:
                    coins = randint(15,40)
                    score_one = 0
                    score_two = 0
                    curr_turn = 1
                    game_active = 1
                    all_coins_tect_rect = score_text.get_rect(center = (440,45))
                    
                    update_gui()
                    print("Game activated")
                    one_click_time = current_time
                start_time = int(pygame.time.get_ticks()/1000)

    if (game_active == 1):
        pick_coins()
        if(coins == 1):
            game_active = 2
        # Draw all the elements in this section
        screen.fill((255, 255, 255))
        screen.blit(background_surface,(0, background_y_axis))
        
        screen.blit(first_hand_surface,(fhand_xpos,200))
        screen.blit(second_hand_surface,second_hand_rect)

        # Drawing Score Rectangles

        # Making the Overlay
        screen.blit(shadow_surface, shadow_surface_rect) # blit the shadow surface onto the screen
        screen.blit(shadow_surface, shadow_surface_rect_two) # blit the shadow surface onto the screen
        pygame.draw.rect(screen,'#ffffff',score_rect)
        pygame.draw.rect(screen,'#000000',score_rect,3,3)
        pygame.draw.rect(screen,'#ffffff',score_rect_two)
        pygame.draw.rect(screen,'#000000',score_rect_two,3,3)

        screen.blit(score_text,score_rect)
        screen.blit(score_text_two,score_rect_two)
        # Making the coin
        screen.blit(all_coins,all_coins_rect)
        screen.blit(all_coins_text,all_coins_tect_rect)
        screen.blit(current_coins_gui,current_coins_gui_rect)
        screen.blit(current_coins_gui,current_coins_gui_rect_two)
        screen.blit(current_turn_text,current_turn_rect)
        
        # Update the y-axis position of the background
        background_y_axis -= 2
    
        # If the background goes off the screen, wrap it back around
        if background_y_axis <= -800:
            background_y_axis = 0

        # Displaying the buttons on screen : 

        if (buttons_visible):
            show_buttons()
    elif (game_active == 0):
        # Drawing Main Screen
        screen.fill((255, 255, 255))
        screen.blit(background_surface,(0, background_y_axis))
        screen.blit(logo_image,logo_image_rect)
        screen.blit(logo_caption,logo_caption_rect)
        screen.blit(rules_caption,rules_caption_rect)
         # Update the y-axis position of the background
        background_y_axis -= 2
    
        # If the background goes off the screen, wrap it back around
        if background_y_axis <= -800:
            background_y_axis = 0
    else:
        # Drawing Main Screen
        screen.fill((255, 255, 255))
        screen.blit(background_surface,(0, background_y_axis))
         # Update the y-axis position of the background
        background_y_axis -= 2
        # If the background goes off the screen, wrap it back around
        if background_y_axis <= -800:
            background_y_axis = 0
        winner = pygame.image.load("assets/Winner.png")
        winner_rect = winner.get_rect(center = (400,250))
        screen.blit(winner,winner_rect)
        if (curr_turn % 2 == 0):
            winner_text = game_font_wins.render(f'P1',False,'#dd9911')
            screen.blit(winner_text,(380,240))
        else:
            winner_text = game_font_wins.render(f'P2',False,'#dd9911')
            screen.blit(winner_text,(380,240))



    pygame.display.update()
    Clock.tick(90)