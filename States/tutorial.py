import pygame, os
from States.state import State

class Tutorial(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))
        
    def update(self, delta_time, actions):
        if actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Tutorial", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, "Use as setas para se movimentar", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 20)
        self.game.draw_text(display, "Atire usando a barra de espaço", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 20, 20)
        self.game.draw_text(display, "Esc volta para a tela anterior", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 60, 20)
        self.game.draw_text(display, "p pausa o jogo", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 100, 20)