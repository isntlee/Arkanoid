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
                    elif: offset > 23:
                        xspeed = 6
                    elif: offset > 17:
                        xspeed = 5    

                else: 
                    if offset < -30:
                        xspeed = -7
                    elif offset < -23:
                        xspeed = -6
                    elif offset < -17:
                        xspeed = -5

            ballrect = battrect.move(xspeed, yspeed)
            if ballrect.left < 0 or ballrect.right > width:
                xspeed = -xspeed
            if ballrect.top< 0:
                yspeed = -yspeed 

            if ballrect.top > height:
                lives -= 1 
                