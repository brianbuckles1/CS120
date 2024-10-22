import pygame

def main():
    pygame.init()

    # setup container
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Relaxing Soccer")

    # setup field
    field = pygame.image.load("assets/field.jpg")
    field = pygame.transform.rotate(field,90)
    field = pygame.transform.scale(field,(640,480))

    # setup ball
    ball = pygame.image.load("assets/ball.png")
    ball = ball.convert_alpha()
    ball = pygame.transform.scale(ball,(50,50))
    ball_x=290
    ball_x_dir = 1
    ball_y=190
    ball_y_dir = 1

    # loop setup
    clock = pygame.time.Clock()
    keep_going = True

    # loop
    while keep_going:
        clock.tick(30)

        # set the next drawing points
        ball_x = ball_x + (5 * ball_x_dir)
        ball_y = ball_y + (5 * ball_y_dir)

        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        # check boundaries and change direction if needed.
        if ball_x > screen.get_width()-50:
            ball_x_dir = ball_x_dir * -1

        if ball_x < 0:
            ball_x_dir = ball_x_dir * -1

        if ball_y > screen.get_height()-50:
            ball_y_dir = ball_y_dir * -1

        if ball_y < 0:
            ball_y_dir = ball_y_dir * -1

        # refresh
        screen.blit(field, (0,0))
        screen.blit(ball, (ball_x, ball_y))  # center of the field to start
        pygame.display.flip()

if __name__ =="__main__":
    main()