import pygame, os
from States.state import State
from States.title import Title

with open(os.path.join(os.path.abspath(__file__ + "/../../"), 'highscore_history.txt')) as f:
    lines = f.readlines()

last_player_score = lines[7]

class NewHighscore(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))
        
    def update(self, delta_time, actions):
        if actions["esc"]:
            self.transition_state()
        self.game.reset_keys()

    def transition_state(self):
        new_state = Title(self.game)
        new_state.enter_state()
    
    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Parabéns, você entrou para o Highscore!", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, f"Seu score foi de {last_player_score}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 40)
        self.game.draw_text(display, "Grave seu nome para a posteridade:", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 40, 40)