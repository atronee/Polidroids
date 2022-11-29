import pygame, os
from States.state import State
from States.tutorial import Tutorial
from States.highscore import Highscore
from States.credits import Credits

class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))
        self.options = {0 :"music_up", 1 : "music_down", 2:'sfx_up', 3:'sfx_down', 4:'tutorial', 5:'highscore', 6:'credits'}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "cursor.png"))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.game.GAME_H/2.5 + 10
        self.cursor_pos_x = self.game.GAME_W/2 - 25
        self.cursor_rect.x, self.cursor_rect.y = self.cursor_pos_x, self.cursor_pos_y

    def update(self, delta_time, actions):
        self.update_cursor(actions)      
        if actions["enter"]:
            self.transition_state()
        if actions["esc"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Configurações", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, "Música", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5, 20)
        self.game.draw_text(display, "Efeitos Especiais", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 30, 20)
        self.game.draw_text(display, "Tutorial", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 60, 20)
        self.game.draw_text(display, "Highscore", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 90, 20)
        self.game.draw_text(display, "Créditos", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 120, 20)
        display.blit(self.cursor_img, self.cursor_rect)

    def transition_state(self):
        if self.options[self.index] == "music_up":
            #codigo que aumenta o volume
            pass
        elif self.options[self.index] == "music_down":
            #codigo que abaixa o volume
            pass
        elif self.options[self.index] == "sfx_up":
            #codigo que aumenta o sfx
            pass
        elif self.options[self.index] == "music_down":
            #codigo que abaixa o sfx
            pass
        elif self.options[self.index] == "tutorial": 
            new_state = Tutorial(self.game)
            new_state.enter_state()
        elif self.options[self.index] == "highscore": 
            new_state = Highscore(self.game)
            new_state.enter_state()
        elif self.options[self.index] == "credits": 
            new_state = Credits(self.game)
            new_state.enter_state()

    def update_cursor(self, actions):
        if actions['down']:
            self.index = (self.index + 1) % len(self.options)
        elif actions['up']:
            self.index = (self.index - 1) % len(self.options)
        if self.index == 0:
            self.cursor_rect.y = self.cursor_pos_y
            self.cursor_rect.x = self.cursor_pos_x - 85
        elif self.index == 1:
            self.cursor_rect.y = self.cursor_pos_y
            self.cursor_rect.x = self.cursor_pos_x + 85
        elif self.index == 2:
            self.cursor_rect.y = self.cursor_pos_y + 30
            self.cursor_rect.x = self.cursor_pos_x - 85
        elif self.index == 3:
            self.cursor_rect.y = self.cursor_pos_y + 30
            self.cursor_rect.x = self.cursor_pos_x + 85
        elif self.index == 4:
            self.cursor_rect.y = self.cursor_pos_y + 60
            self.cursor_rect.x = self.cursor_pos_x
        elif self.index == 5:
            self.cursor_rect.y = self.cursor_pos_y + 90
            self.cursor_rect.x = self.cursor_pos_x
        elif self.index == 6:
            self.cursor_rect.y = self.cursor_pos_y + 120
            self.cursor_rect.x = self.cursor_pos_x
