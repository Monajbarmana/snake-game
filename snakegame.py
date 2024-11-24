import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('d.mp3')
pygame.mixer.music.play()

x = pygame.init()


white = ( 255,255,255)
red = (255,0,0)
black = (0,0,0)
pink = (255, 192, 203 )




clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)





def text_screen(text , color , x , y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
 

gamewindow = pygame.display.set_mode((900,500))


pygame.display.set_caption("A SNAKE GAME LIKE YOUR EX")
pygame.display.update()


def  plot_snake(gamewindow ,color , snk_list , snake_size):
     for x,y in snk_list:
        pygame.draw.rect(gamewindow,color ,[ x,y,snake_size,snake_size] ) 

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((250,240,223))
        text_screen("Welcome to your ex game", black, 260,200)
        text_screen("press enter to start", black, 300,250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(108)        
       

def gameloop():
    snake_x = 45 
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 2

    food_x = random.randint(0,900)
    food_y = random.randint(0,500)
    score = 0
    snake_size = 20
    fps = 108
    exit_game = False
    game_quit = False
    game_over = False
    snk_list =[]
    snk_length = 1
    
    
  
    while not exit_game :
        if game_over:
            
            gamewindow.fill(white)
            text_screen("game over! press continue to start",red , 130,200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()    
        else :   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_x = snake_x + 20
                        velocity_x = init_velocity
                        velocity_y = 0  

                    if event.key == pygame.K_LEFT:
                        snake_x = snake_x - 20 
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        snake_y = snake_y - 20 
                        velocity_y = -init_velocity
                        velocity_x = 0
                        

                    if event.key == pygame.K_DOWN:
                        snake_y = snake_y + 20 
                        velocity_y = init_velocity  
                        velocity_x = 0          
            
                    if event.key == pygame.K_q :
                        score +=5
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10
                food_x = random.randint(10,800)
                food_y = random.randint(10,400)
                snk_length +=10
                
            gamewindow.fill(white)
            text_screen("score:"+ str(score) ,black,3,3)
        # pygame.draw.rect(gamewindow,pink ,[ snake_x,snake_y,snake_size,snake_size] )
            
            head = [] 
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True

            if snake_x <0 or snake_x>900 or snake_y <0 or snake_y>500:
                game_over = True
             
            pygame.draw.rect(gamewindow,red , [food_x,food_y,snake_size,snake_size] ) 
            plot_snake(gamewindow,pink , snk_list,snake_size ) 
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()    
   
