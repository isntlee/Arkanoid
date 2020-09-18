import os, sys, pygame, random


class Arkanoid:

    def main(self):
        game = Game(7, 7, 60)
        game.setupGame()
        game.startGame()


class Game:

    max_lives = 5
    bat_speed = 30
    x = 320
    y = 75
    bgcolour = 0, 0, 0
    size = width, height = 720, 640

    screen = None

    def __init__(self, initial_x_speed, initial_y_speed, frames_per_second):
        self.initial_xspeed = initial_x_speed
        self.initial_yspeed = initial_y_speed
        self.frames_per_second = frames_per_second

    # Pygame set-up.
    def setupGame(self):
        pygame.init()

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Game.x, Game.y)
        pygame.display.set_caption("Arkanoid")
        pygame.key.set_repeat(1, 30)
        pygame.mouse.set_visible(0)
        Game.screen = pygame.display.set_mode(Game.size)

    # Triggers the game view to be rendered, and game to start.
    def startGame(self):

        score = 0
        current_x_speed = self.initial_xspeed
        current_y_speed = self.initial_yspeed
        lives_remaining = self.max_lives
        clock = pygame.time.Clock()

        # Set images for game entities.
        bat = pygame.image.load("images/bat.png").convert()
        batrect = bat.get_rect()
        ball = pygame.image.load("images/ball.png").convert()
        ballrect = ball.get_rect()

        # Instantiate WallOfBricks class, and construct wall of specified width.
        wall = WallOfBricks()
        wall.build_wall(Game.width)

        batrect = batrect.move((Game.width / 2) - (batrect.right / 2), Game.height - 20)
        ballrect = ballrect.move(Game.width / 3, Game.height / 2.7)

        # Begins Game loop.
        while True:

            clock.tick(self.frames_per_second)
            #Begins Event Loop.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        batrect = batrect.move(-Game.bat_speed, 0)
                        if (batrect.left < 0):
                            batrect.left = 0
                    if event.key == pygame.K_RIGHT:
                        batrect = batrect.move(Game.bat_speed, 0)
                        if (batrect.right > Game.width):
                            batrect.right = Game.width
            #ball/bat bounce action
            if ballrect.bottom >= batrect.top and \
                    ballrect.bottom <= batrect.bottom and \
                    ballrect.right >= batrect.left and \
                    ballrect.left <= batrect.right:
                current_y_speed = -current_y_speed
                offset = ballrect.center[0] - batrect.center[0]

                if offset > 0:
                    if offset > 30:
                        current_x_speed = 7
                    elif offset > 23:
                        current_x_speed = 6
                    elif offset > 17:
                        current_x_speed = 5
                else:
                    if offset < -30:
                        current_x_speed = -7
                    elif offset < -23:
                        current_x_speed = -6
                    elif current_x_speed < -17:
                        current_x_speed = -5
                        
            #ball/wall bounce actions; out of bounds conditions
            ballrect = ballrect.move(current_x_speed, current_y_speed)
            if ballrect.left < 0 or ballrect.right > Game.width:
                current_x_speed = -current_x_speed
            if ballrect.top < 0:
                current_y_speed = -current_y_speed
            
            if ballrect.top > Game.height:
                lives_remaining -= 1
                current_x_speed = self.initial_xspeed
                if random.random() > 0.5:
                    current_x_speed = -current_x_speed
                current_y_speed = self.initial_yspeed
                ballrect.center = Game.width * random.random(), Game.height / 2.7
                if lives_remaining == 0:
                    msg = pygame.font.Font(None, 70).render("Game Over", True, (0, 240, 0), Game.bgcolour)
                    msgrect = msg.get_rect()
                    msgrect = msgrect.move(Game.width / 2 - (msgrect.center[0]), Game.height / 2)
                    Game.screen.blit(msg, msgrect)
                    pygame.display.flip()
                    
                    #restart process/conditions
                    while True:
                        restart = False
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    sys.exit()
                                if not (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                                    restart = True
                        if restart:
                            Game.screen.fill(Game.bgcolour)
                            wall.build_wall(Game.width)
                            lives_remaining = Game.max_lives
                            score = 0
                            break

            if current_x_speed < 0 and ballrect.left < 0:
                current_x_speed = -current_x_speed
            if current_x_speed > 0 and ballrect.right > Game.width:
                current_x_speed = -current_x_speed
            
            #collisions/deleting bricks 
            index = ballrect.collidelist(wall.brickrect)
            if index != -1:
                if ballrect.center[0] > wall.brickrect[index].right or \
                        ballrect.center[0] < wall.brickrect[index].left:
                    current_x_speed = -current_x_speed
                else:
                    current_y_speed = -current_y_speed
                wall.brickrect[index:index + 1] = []
                score += 10

            self.displayScore(score)
            self.displayLivesRemaining(lives_remaining)

            #displaying brickwall
            for i in range(0, len(wall.brickrect)):
                Game.screen.blit(wall.brick, wall.brickrect[i])

            if not wall.brickrect:
                wall.build_wall(Game.width)
                current_x_speed = self.initial_xspeed
                current_y_speed = self.initial_yspeed
                ballrect.center = Game.width / 2, Game.height / 3

            Game.screen.blit(ball, ballrect)
            Game.screen.blit(bat, batrect)
            pygame.display.flip()

    def displayScore(self, score):
        Game.screen.fill(Game.bgcolour)
        scoretext = pygame.font.Font(None, 40).render("Score: " + str(score), True, (0, 220, 0), Game.bgcolour)
        scoretextrect = scoretext.get_rect()
        Game.screen.blit(scoretext, scoretextrect)

    def displayLivesRemaining(self, lives_remaining):
        livestext = pygame.font.Font(None, 40).render("Lives: " + str(lives_remaining), True, (0, 220, 0), Game.bgcolour)
        livestextrect = livestext.get_rect()
        livestextrect = livestextrect.move(Game.width - livestextrect.right, 0)
        Game.screen.blit(livestext, livestextrect)


class WallOfBricks():

    def __init__(self):
        self.brick = pygame.image.load("images/brick.png").convert()
        self.brickrect = self.brick.get_rect()
        self.bricklength = self.brickrect.right - self.brickrect.left
        self.brickheight = self.brickrect.bottom - self.brickrect.top

    def build_wall(self, width):
        x_position = 0
        y_position = 60
        fitBrick = 0
        self.brickrect = []

        #fitting the wall/number of bricks 
        for i in range(0, 116):
            if x_position > width:
                if fitBrick == 0:
                    fitBrick = self.bricklength / 2
                else:
                    fitBrick = 0
                x_position = -fitBrick
                y_position += self.brickheight

            self.brickrect.append(self.brick.get_rect())
            self.brickrect[i] = self.brickrect[i].move(x_position, y_position)
            x_position = x_position + self.bricklength


if __name__ == '__main__':
    br = Arkanoid()
    br.main()