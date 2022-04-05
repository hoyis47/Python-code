import pgzrun
from random import randint

apple = Actor("apple")
banana = Actor("banana1")
strawberry = Actor("strawberry")

score = 0
game_over = False

def draw():
    screen.clear()
    apple.draw()
    banana.draw()
    strawberry.draw()
    screen.draw.text("Apple: " + str(score) , topleft=(10,10))

    if game_over:
        screen.clear()
        screen.draw.text("GAME OVER", topleft=(10,10), fontsize=100)
        

def place_fruits():
    apple.x = randint(10,800)
    apple.y = randint(10,600)
    banana.x = randint(10,800)
    banana.y = randint(10,600)
    strawberry.x = randint(10,800)
    strawberry.y = randint(10,600)

def on_mouse_down(pos):
    global score
    global game_over
    
    if apple.collidepoint(pos):
        print("Good shot!")
        place_fruits()
        score = score + 1
    else:
        print("You missed!")
        place_fruits()
        score = score - 1

        if score == 0:
            game_over = True
            

    
    

place_fruits()

pgzrun.go()
