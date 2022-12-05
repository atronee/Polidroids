import os, pygame
from States.title import Title
from States.gameplay import Gameplay
from States.story import Story
from States.utils import load_sprite
class Game(): 
        def __init__(self):
            """Inicializa o jogo"""
            pygame.init()
            pygame.display.set_caption("Polidroids") # Define o título da janela
            game_icon = pygame.image.load("Docs/Polidroids.png")
            pygame.display.set_icon(game_icon)
            self.GAME_W,self.GAME_H = 480, 270
            self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
            self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            self.running, self.playing = True, True
            self.actions = {"left": False, "right": False, "up" : False, "down" : False, "esc" : False, "space" : False, "enter" : False, "backspace": False}
            self.state_stack = []
            self.load_assets()
            self.load_states()
            self.background = load_sprite("background_space", 0.4, False)

        def game_loop(self):
            """Loop principal do jogo"""
            while self.playing:
                self.get_events()
                self.update()
                self.render()

        def get_events(self):
            """Captura os eventos do jogo"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.actions['esc'] = True
                    if event.key == pygame.K_LEFT:
                        self.actions['left'] = True
                    if event.key == pygame.K_RIGHT:
                        self.actions['right'] = True
                    if event.key == pygame.K_UP:
                        self.actions['up'] = True
                    if event.key == pygame.K_DOWN:
                        self.actions['down'] = True
                    if event.key == pygame.K_ESCAPE:
                        self.actions['esc'] = True
                    if event.key == pygame.K_SPACE:
                        self.actions['space'] = True    
                    if event.key == pygame.K_RETURN:
                        self.actions['enter'] = True
                    if event.key == pygame.K_BACKSPACE:
                        self.actions['backspace'] = True
                    if event.key == pygame.K_p:
                        self.actions['pause'] = True  

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.actions['esc'] = False
                    if event.key == pygame.K_LEFT:
                        self.actions['left'] = False
                    if event.key == pygame.K_RIGHT:
                        self.actions['right'] = False
                    if event.key == pygame.K_UP:
                        self.actions['up'] = False
                    if event.key == pygame.K_DOWN:
                        self.actions['down'] = False
                    if event.key == pygame.K_ESCAPE:
                        self.actions['esc'] = False
                    if event.key == pygame.K_SPACE:
                        self.actions['space'] = False
                    if event.key == pygame.K_RETURN:
                        self.actions['enter'] = False
                    if event.key == pygame.K_BACKSPACE:
                        self.actions['backspace'] = False
                    if event.key == pygame.K_p:
                        self.actions['pause'] = False

        def update(self):
            """Atualiza o jogo"""
            self.state_stack[-1].update(self.actions)

        def render(self):
            """Renderiza o jogo"""
            if len(self.state_stack) == 0:
                exit()
            self.state_stack[-1].render(self.game_canvas)
            # Render current state to the screen
            self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
            if not isinstance(self.state_stack[-1], (Gameplay, Story)):
                pygame.display.flip()

        def draw_text(self, surface, text, color, x, y, size):
            """Desenha o texto na tela
            param surface: superfície onde o texto será desenhado
            type surface: pygame.Surface
            param text: texto a ser desenhado
            type text: str
            param color: cor do texto
            type color: tuple
            param x: posição x do texto
            type x: int
            param y: posição y do texto
            type y: int
            param size: tamanho do texto
            type size: int
            """
            self.font = pygame.font.Font(os.path.join(self.font_dir, "Polybius1981.ttf"), size)
            text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_assets(self):
            """Carrega os assets do jogo"""
            self.assets_dir = os.path.join("Assets")
            self.sprite_dir = os.path.join(self.assets_dir, "Sprites")
            self.font_dir = os.path.join(self.assets_dir, "Font")
            self.font= pygame.font.Font(os.path.join(self.font_dir, "Polybius1981.ttf"), 40)

        def load_states(self):
            """Carrega os estados do jogo"""
            self.title_screen = Title(self)
            self.state_stack.append(self.title_screen)

        def reset_keys(self):
            """Reseta as teclas"""
            for action in self.actions:
                self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()