from States.state import State
from States.utils import load_sprite 

class Tutorial(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = load_sprite("background_space", 1)
        
    def update(self, actions):
        if actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Tutorial", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, "Use as setas para se movimentar", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 20)
        self.game.draw_text(display, "Atire usando a barra de espaço", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 20, 20)
        self.game.draw_text(display, "Esc volta para a tela anterior", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 60, 20)
        self.game.draw_text(display, "Enter pausa o jogo", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 100, 20)