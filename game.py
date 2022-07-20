import pygame


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 500))
        pygame.display.set_caption('scroll_game')
        self.back_ground = pygame.image.load('single_background.png').convert_alpha()
        self.back_ground = pygame.transform.scale(self.back_ground, (900, 500))
        self.pressed = {}
        self.scroll_left = False
        self.scroll_right = False
        self.scroll = 0
        self.scroll_speed = 1
        self.ROWS = 16
        self.MAX_COLS = 150
        self.TUlE_SIZE = self.screen.get_height() // self.ROWS

    def scroll_bg(self):
        if self.scroll_right:
            self.scroll += self.scroll_speed
        if self.scroll_left and self.scroll > 0:
            self.scroll -= self.scroll_speed

    def draw(self):
        for i in range(self.MAX_COLS + 1):
            pygame.draw.line(self.screen, (255, 255, 255), (i*self.TUlE_SIZE, 0), (i*self.TUlE_SIZE,
                                                                                   self.screen.get_height()))
        for i in range(self.ROWS + 1):
            pygame.draw.line(self.screen, (255, 255, 255), (0, i * self.TUlE_SIZE), (self.screen.get_width(),
                                                                                     i * self.TUlE_SIZE))



    def run(self):
        timer = pygame.time.Clock()

        running = True
        while running:
            self.screen.fill((144, 201, 120))  # le  fond vert de l'écran
            # pour multiplier l'image du bg et le scrollage
            for i in range(4):
                self.screen.blit(self.back_ground, (i * self.back_ground.get_width() - self.scroll, 0))

            self.scroll_bg()
            self.draw()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.scroll_right = True
                    elif event.key == pygame.K_LEFT:
                        self.scroll_left = True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.scroll_right = False
                    elif event.key == pygame.K_LEFT:
                        self.scroll_left = False



        timer.tick(50)
        pygame.quit()

