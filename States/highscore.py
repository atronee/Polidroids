import pygame, os
from States.state import State
from States.utils import load_sprite 

class Highscore(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = load_sprite("background_space", 1)
        
    def update(self, actions):
        if actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        with open('highscore_history.txt') as f:
            lines = f.readlines()

        player_1 = lines[0][0:-1]
        player_1_score = lines[1][0:-1]
        player_2 = lines[2][0:-1]
        player_2_score = lines[3][0:-1]
        player_3 = lines[4][0:-1]
        player_3_score = lines[5][0:-1]

        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Highscore", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, f"{player_1}: {player_1_score}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 20)
        self.game.draw_text(display, f"{player_2}: {player_2_score}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 30, 20)
        self.game.draw_text(display, f"{player_3}: {player_3_score}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 80, 20)