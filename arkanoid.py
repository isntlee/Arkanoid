import sys, pygame, random 
class Arkanoid():

    def main(self):
        xspeed_init = 6
        yspeed_init = 6
        max_lives = 5
        bat_speed = 30 
        score = 0 
        bgcolour = 0, 0, 0 
        size = width, height = 720, 640 

        pygame.init()
        screen = pygame.display.set_mode(size)

        bat = pygame.image.load("bat.png").convert()
        batrect = bat.get_rect() 

        ball = pygame.image.load("ball.png").convert()
        ball.set_colorkey((255, 255, 255))
        ballrect = ball.get_rect()

        wall = Wall()
        wall.build_wall(width)

        batrect = batrect.move((width/2) -  (batrect.right/2), height - 20)
        xspeed = xspeed_init
        yspeed = yspeed_init
        lives = max_lives
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1,30)
        pygame.mouse.set_visible(0)

        while True: 
            clock.tck(60)

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        batrect = batrect.move(-bat_speed, 0)
                        if (batrect.left < 0):
                            batrect.left = 0 
                    if event.key == pygame.K_RIGHT:
                        batrect = batrect.move(bat_speed, 0)
                        if (batrect.right > width):
                            batrect.right = width

            if ballrect.bottom >= batrect.top and \
                ballrect.bottom <= batrect.bottom and \
                ballrect.right >= batrect.left and \
                ballrect.left <= batrect.right:
                yspeed = -yspeed 
                offset = ballrect.center[0] - batrect.center[0]

                if offset > 0:
                    if offset > 30:
                        xspeed = 7
                    elif offset > 23:
                        xspeed = 6
                    elif offset > 17:
                        xspeed = 5    

                else: 
                    if offset < -30:
                        xspeed = -7
                    elif offset < -23:
                        xspeed = -6
                    elif offset < -17:
                        xspeed = -5

            ballrect = batrect.move(xspeed, yspeed)
            if ballrect.left < 0 or ballrect.right > width:
                xspeed = -xspeed
            if ballrect.top< 0:
                yspeed = -yspeed 

            if ballrect.top > height:
                lives -= 1 

            xspeed = xspeed_init
            rand = random.random()
            if random.random() > 0.5:
                xspeed = - xspeed
            yspeed = yspeed_init
            ballrect.center = width * random.random(), height/3
            if lives == 0:
                msg - pygame.font.Font(None, 70).render("Game Over", True, (0, 240, 0), bgcolour)
                msgrect = msg.get_rect()
                msgrect = msgrect.move(width/2 - (msgrect.center[0]), height/3)
                screen.blit(msg, msgrect)
                pygame.display.flip()


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
                        screen.fill(bgcolor)
                        wall.build_wall(width)
                        lives = max_lives
                        score = 0 
                        break
            
            if xspeed < 0 and ballrect.left < 0:
                xspeed = -xspeed
            
            if xspeed > 0 and ballrect.right > width:
                xspeed = -xspeed 

            index = ballrect.collidelist(wall.brickrect)
            if index != -1:
                if ballrect.center[0] > wall.brickrect[index].right or \
                ballrect.center[0] < wall.brickrect[index].left:
                xspeed = -xspeed 
            else:
                yspeed = - yspeed
            wall.brickrect[index:index + 1] = []
            score += 10

            screen.fill(bgcolor)
            scoretext = pygame.font.Font(None, 40).render("Score: "+str(score), True, (0, 220, 0), bgcolor)
            scoretextrect = scoretext.get_rect()
            screen.blit(scoretext, scoretextrect)

            for i in range(0, len(wall.brickrect)):
                screen.blit(wall.brick, wall.brickrect[i])

            if wall.brickrect == []:
                wall.build_wall(width)
                xspeed = xspeed_init
                yspeed = yspeed_init
                ballrect.center = width/2, height/3

            screen.blit(ball, ballrect)
            screen.blit(bat, batrect)
            pygame.display.flip()

            
