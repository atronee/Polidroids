import pygame, os
from States.state import State
from States.new_highscore import NewHighscore
from States.utils import load_sprite 

with open(os.path.join(os.path.abspath(__file__ + "/../../"), 'highscore_history.txt')) as f:
    lines = f.readlines()

last_player_score = int(lines[5])

class GameOver(State):
    def __init__(self, game, score_value):
        """Construtor da classe GameOver
        """
        State.__init__(self, game)
        self.score_value = score_value
        self.background = load_sprite("background_space", 1)
        
    def update(self, actions):
        """ Atualiza o estado GameOver
        """
        if actions["esc"] or actions["enter"]:
            self.transition_state()
        self.game.reset_keys()

    def transition_state(self):
        """Transição de estado
        """
        if self.score_value >= last_player_score:
            new_state = NewHighscore(self.game, self.score_value)
            new_state.enter_state()
        else:
            while len(self.game.state_stack) > 1:
                self.exit_state()
        # new_state = Title(self.game)
        # new_state.enter_state()
    
    def render(self, display):
        """Renderiza o estado GameOver
        :param display: superfície onde o jogo será renderizado
        :type display: pygame.Surface
        """
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Game Over!", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, f"Seu score foi de {self.score_value}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 40)