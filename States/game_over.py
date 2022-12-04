import pygame, os
from States.state import State

with open(os.path.join(os.path.abspath(__file__ + "/../../"), 'highscore.txt')) as f:
    lines = f.readlines()

last_player_score = lines[7]

class GameOver(State):
    def __init__(self, game, score_value):
        State.__init__(self, game)
        self.score_value = score_value
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))
        
    def update(self, delta_time, actions):
        if actions["esc"]:
            self.transition_state()
        self.game.reset_keys()

    def transition_state(self):
        while len(self.game.state_stack) > 1:
            self.exit_state()
        # new_state = Title(self.game)
        # new_state.enter_state()
    
    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Game Over!", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, f"Seu score foi de {self.score_value}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 40)