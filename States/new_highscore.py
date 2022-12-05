import pygame, os
from States.state import State
from States.utils import load_sprite 

with open(os.path.join(os.path.abspath(__file__ + "/../../"), 'highscore_history.txt')) as f:
    lines = f.readlines()

class NewHighscore(State):
    def __init__(self, game, new_score):
        State.__init__(self, game)
        self.new_score = new_score
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space_leitura.png"))
        self.index = [0,0]
        self.teclado = [[['1', -20, 10], ['2', 0, 10], ['3', 20, 10], ['4', 40, 10], ['5', 60, 10], ['6', 80, 10], ['7', 100, 10], ['8', 120, 10], ['9', 140, 10], ['0', 160, 10]],
        [['Q', -20, 40], ['W', 0, 40], ['E', 20, 40], ['R', 40, 40], ['T', 60, 40], ['Y', 80, 40], ['U', 100, 40], ['I', 120, 40], ['O', 140, 40], ['P', 160, 40]],
        [['A', -20, 70], ['S', 0, 70], ['D', 20, 70], ['F', 40, 70], ['G', 60, 70], ['H', 80, 70], ['J', 100, 70], ['K', 120, 70], ['L', 140, 70]],
        [['Z', -20, 100], ['X', 0, 100], ['C', 20, 100], ['V', 40, 100], ['B', 60, 100], ['N', 80, 100], ['M', 100, 100], ['_', 120, 100], ['<', 140, 100]]]
        self.cursor_img = load_sprite("caixa_cursor", 0.4)
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.game.GAME_H/2
        self.cursor_pos_x = self.game.GAME_W/3
        self.cursor_rect.x, self.cursor_rect.y = self.cursor_pos_x - 20, self.cursor_pos_y + 10
        self.nome_inserido = "EU"

        
    def update(self, delta_time, actions):
        self.update_cursor(actions)
        caract = self.teclado[self.index[0]][self.index[1]][0]
        if actions['space'] and caract != "<" and len(self.nome_inserido) < 30:
            self.nome_inserido += self.teclado[self.index[0]][self.index[1]][0]
        elif (actions['space'] and caract == "<") or actions['backspace']:
            self.nome_inserido = self.nome_inserido[:-1]
        elif actions["esc"] or actions["enter"]:
            self.transition_state()
        self.game.reset_keys()
    
    def update_cursor(self, actions):
        if actions["right"]:
            self.index[1] = (self.index[1] + 1) % len(self.teclado[self.index[0]])
        elif actions["left"]:
            self.index[1] = (self.index[1] - 1) % len(self.teclado[self.index[0]])
        elif actions["up"]:
            self.index[0] = (self.index[0] - 1) % len(self.teclado)
            self.index[1] = min(self.index[1], len(self.teclado[self.index[0]])-1)
        elif actions["down"]:
            self.index[0] = (self.index[0] + 1) % len(self.teclado)
            self.index[1] = min(self.index[1], len(self.teclado[self.index[0]])-1)
        self.cursor_rect.y = self.game.GAME_H/2 + self.teclado[self.index[0]][self.index[1]][2]
        self.cursor_rect.x = self.game.GAME_W/3 + self.teclado[self.index[0]][self.index[1]][1]

    def transition_state(self):
        with open(os.path.join(os.path.abspath(__file__ + "/../../"), 'highscore_history.txt')) as f:
            lines = f.readlines()
        with open('highscore_history.txt', "w") as f:
            name_1,  name_2,  name_3  = [lines[0], lines[2], lines[4]]
            score_1, score_2, score_3 = [int(_) for _ in [lines[1], lines[3], lines[5]]]
            if self.new_score >= score_1:
                f.write(self.nome_inserido + "\n")
                f.write(str(self.new_score) + "\n")
                f.write(name_1)
                f.write(str(score_1) + "\n")
                f.write(name_2)
                f.write(str(score_2) + "\n")
            elif self.new_score >= score_2:
                f.write(name_1)
                f.write(str(score_1) + "\n")
                f.write(self.nome_inserido + "\n")
                f.write(str(self.new_score) + "\n")
                f.write(name_2)
                f.write(str(score_2) + "\n")
            else:
                f.write(name_1)
                f.write(str(score_1) + "\n")
                f.write(name_2)
                f.write(str(score_2) + "\n")
                f.write(self.nome_inserido + "\n")
                f.write(str(self.new_score) + "\n")

        while len(self.game.state_stack) > 1:
            self.exit_state()
        # new_state = Title(self.game)
        # new_state.enter_state()
    
    def render(self, display):
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Parabéns, você entrou para o Highscore!", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4 - 40, 20)
        self.game.draw_text(display, f"Seu score foi de {self.new_score}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 70, 20)
        self.game.draw_text(display, "Grave seu nome para a posteridade:", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 30, 20)
        self.game.draw_text(display, f"{self.nome_inserido}", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 10, 20)
        self.game.draw_text(display, "1  2  3  4  5  6  7  8  9  0", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 20, 20)
        self.game.draw_text(display, "Q  W  E  R  T  Y  U  I  O  P", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 50, 20)
        self.game.draw_text(display, "A  S  D  F  G  H  J  K  L   ", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 80, 20)
        self.game.draw_text(display, "Z  X  C  V  B  N  M  _  <   ", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 110, 20)
        display.blit(self.cursor_img, self.cursor_rect)