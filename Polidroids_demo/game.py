import pygame # Importa o módulo pygame

from utils import load_sprite # Importa o método load_sprite do módulo utils

class Polidroids: # Classe principal do jogo
    def __init__(self): # Método construtor
        self._init_pygame() # Inicializa o pygame
        self.screen = pygame.display.set_mode((800, 600)) # Cria uma tela de 800x600
        self.background = load_sprite("background", False) # Carrega a imagem de fundo

    def main_loop(self): # Método principal do jogo
        while True: # Cria um loop infinito
            self._handle_input() # Trata os eventos
            self._process_game_logic() # Processa a lógica do jogo
            self._draw() # Desenha na tela

    def _init_pygame(self): # Método inicializa o pygame
        pygame.init() # Inicializa o pygame
        pygame.display.set_caption("Polidroids") # Define o título da janela

    def _handle_input(self): # Método trata os eventos
        for event in pygame.event.get(): # Percorre todos os eventos
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ): # Verifica se o evento é de fechar a janela ou apertar a tecla ESC
                pygame.quit() # Fecha o jogo

    def _process_game_logic(self): # Método processa a lógica do jogo
        pass

    def _draw(self): # Método desenha na tela
        self.screen.blit(self.background, (0, 0)) # Desenha a imagem de fundo na tela
        pygame.display.flip() # Atualiza a tela