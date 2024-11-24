import pygame
from .constants import *
from .direction import Direction
from .element import Element

class infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, SCALE)
        
    def is_quit_event (self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Good bye')
                return True
        return False
    
    def get_pressed_key (self) -> None | Direction:  # Direction | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.DOWN
        if key[pygame.K_DOWN]:
            return Direction.UP
        if key[pygame.K_LEFT]:
            return Direction.LEFT
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        else:
            return None
    
    def fill_screen (self) -> None:
        self.screen.fill(SCREEN_COLOR)
        
    def draw_element(self, e: Element, color) -> None:
        pygame.draw.rect(self.screen, pygame.Color (color), (e.x * SCALE, e.y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE), 0, ELEMENT_RADIUS)
        
    def draw_score (self, score: int) -> None:
        self.screen.blit(self.font.render (f'Score: {score}', True, pygame.Color (SCORE_COLOR)), (5, 5))
        
    def draw_game_over (self) -> None:
        massege = self.font.render ('Game Over', True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit (massege, massege.get_rect (center = ((WIDTH // 2) * SCALE, (HEIGHT // 2) * SCALE)))
        
    def update_and_tik (self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)
        
    def quit (self) -> None:
        pygame.quit()