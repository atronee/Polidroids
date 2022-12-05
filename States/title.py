import pygame, os
from States.state import State
from States.choose_spaceship import ChooseSpaceship
from States.menu import Menu
from States.utils import load_sound, load_sprite

class Title(State):
    def __init__(self, game):
        """ Inicializa o estado do jogo """
        State.__init__(self, game)
        self.background = load_sprite("background_space", 1)
        self.options = {0 :"Novo Jogo", 1 : "Configurações"}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "cursor.png"))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.game.GAME_H/1.25 - 40
        self.cursor_rect.x, self.cursor_rect.y = self.game.GAME_W/2 - 25, self.cursor_pos_y
        self.soundtrack = load_sound("Game_soundtrack_1")

    def update(self, actions):
        """ Atualiza o estado do jogo
        param actions: dicionário de ações
        type actions: dict
        """
        self.update_cursor(actions)      
        if actions["enter"]:
            self.transition_state()
        if actions["esc"]:
            if len(self.game.state_stack) == 1:
                pygame.QUIT
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        """ Renderiza o estado.
        param display: tela do jogo
        type display: Surface
        """
        self.soundtrack.play()
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Polidroids", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2.35, 40)
        self.game.draw_text(display, "Novo Jogo", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/1.25 - 50, 20)
        self.game.draw_text(display, "Configurações", (255,255,255), self.game.GAME_W/2, (self.game.GAME_H/1.25 - 20), 20)
        display.blit(self.cursor_img, self.cursor_rect)

    def transition_state(self):
        """ Método chamado quando o estado é inserido na pilha de estados """
        if self.options[self.index] == "Novo Jogo": 
            new_state = ChooseSpaceship(self.game, self.soundtrack)
            new_state.enter_state()
        elif self.options[self.index] == "Configurações": 
            new_state = Menu(self.game)
            new_state.enter_state()

    def update_cursor(self, actions):
        """ Atualiza a posição do cursor
        param actions: dicionário de ações
        type actions: dict
        """
        if actions['down']:
            self.index = (self.index + 1) % len(self.options)
        elif actions['up']:
            self.index = (self.index - 1) % len(self.options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index * 30)