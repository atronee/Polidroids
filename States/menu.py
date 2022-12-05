import pygame, os
from States.state import State
from States.tutorial import Tutorial
from States.highscore import Highscore
from States.credits import Credits
from States.utils import load_sound, load_sprite 

class Menu(State):
    def __init__(self, game):
        """Construtor da classe Menu"""
        State.__init__(self, game)
        self.background = load_sprite("background_space", 1)
        self.options = {0:'tutorial', 1:'highscore', 2:'credits'}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "cursor.png"))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.game.GAME_H/2.5 + 10
        self.cursor_rect.x, self.cursor_rect.y = self.game.GAME_W/2 - 25, self.cursor_pos_y
        self.soundtrack = load_sound("Game_soundtrack_1")

    def update(self, actions):
        """Atualiza o estado Menu
        :param actions: dicionário de ações
        :type actions: dict
        """
        self.update_cursor(actions)      
        if actions["enter"]:
            self.transition_state()
        if actions["esc"]:
            if str(type(self.game.state_stack[-2])) == "<class 'States.gameplay.Gameplay'>":
                self.soundtrack.stop()
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        """Renderiza o estado Menu
        :param display: superfície onde o jogo será renderizado
        :type display: pygame.Surface
        """
        if str(type(self.game.state_stack[-2])) == "<class 'States.gameplay.Gameplay'>":
            self.soundtrack.play(20)
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Configurações", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
        self.game.draw_text(display, "Tutorial", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 40, 20)
        self.game.draw_text(display, "Highscore", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 70, 20)
        self.game.draw_text(display, "Créditos", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.5 + 100, 20)
        display.blit(self.cursor_img, self.cursor_rect)

    def transition_state(self):
        """Transição de estado"""
        if self.options[self.index] == "tutorial": 
            new_state = Tutorial(self.game)
            new_state.enter_state()
        elif self.options[self.index] == "highscore": 
            new_state = Highscore(self.game)
            new_state.enter_state()
        elif self.options[self.index] == "credits": 
            new_state = Credits(self.game)
            new_state.enter_state()

    def update_cursor(self, actions):
        """Atualiza a posição do cursor
        :param actions: dicionário de ações
        :type actions: dict
        """
        if actions['down']:
            self.index = (self.index + 1) % len(self.options)
        elif actions['up']:
            self.index = (self.index - 1) % len(self.options)
        if self.index == 0:
            self.cursor_rect.y = self.cursor_pos_y + 40
        elif self.index == 1:
            self.cursor_rect.y = self.cursor_pos_y + 70
        elif self.index == 2:
            self.cursor_rect.y = self.cursor_pos_y + 100
