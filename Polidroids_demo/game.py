import pygame # Importa o módulo pygame

from models import GameObject, Spaceship, Asteroids # Importa as classes GameObject, Spaceship e Asteroids
from utils import get_random_position, load_sprite # Importa os métodos get_random_position e load_sprite

class Polidroids: # Classe principal do jogo
    MIN_ASTEROID_DISTANCE = 250
    
    def __init__(self): # Método construtor
        self._init_pygame() # Inicializa o pygame
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Cria a tela do jogo
        self.background = load_sprite("background_space", 1, False) # Carrega a imagem de fundo
        self.clock = pygame.time.Clock() # Cria um objeto Clock
        
        self.asteroids = [] # Cria uma lista de asteroides
        self.bullets = [] # Cria uma lista de tiros
        self.spaceship = Spaceship((400, 300), self.bullets.append) # Cria uma instância da classe Spaceship
        
        for _ in range(6): # Cria 6 asteroides
            while True:
                position = get_random_position(self.screen) # Pega uma posição aleatória
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ): # Verifica se a posição do asteroide está a uma distância mínima da nave
                    break

        self.asteroids.append(Asteroids(position)) # Adiciona o asteroide na lista de asteroides
                
        self.enemy = GameObject(
            (400, 300), load_sprite("enemy_spaceship", 0.1), (0, 1)
        ) # Cria uma instância da classe GameObject para o inimigo

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
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ): # Verifica se a nave existe e se o evento é de apertar a tecla ESPAÇO
                self.spaceship.shoot() # Chama o método shoot da nave
                
        is_key_pressed = pygame.key.get_pressed() # Pega todas as teclas pressionadas

        if self.spaceship: # Verifica se a nave existe
            if is_key_pressed[pygame.K_RIGHT]: # Verifica se a tecla direita está pressionada
                self.spaceship.rotate(clockwise=True) # Rotaciona a nave no sentido horário
            elif is_key_pressed[pygame.K_LEFT]: # Verifica se a tecla esquerda está pressionada
                self.spaceship.rotate(clockwise=False) # Rotaciona a nave no sentido anti-horário
            if is_key_pressed[pygame.K_UP]: # Verifica se a tecla para cima está pressionada
                self.spaceship.accelerate() # Acelera a nave

    def _process_game_logic(self): # Método processa a lógica do jogo
        for game_object in self._get_game_objects(): # Percorre todos os objetos do jogo
            game_object.move(self.screen) # Move o objeto
            
        if self.spaceship: # Verifica se a nave existe
            for asteroid in self.asteroids: # Percorre todos os asteroides
                if asteroid.collides_with(self.spaceship): # Verifica se o asteroide colidiu com a nave
                    self.spaceship = None # Remove a nave
                    break
        
        for bullet in self.bullets[:]: # Percorre todos os tiros
            for asteroid in self.asteroids[:]: # Percorre todos os asteroides
                if asteroid.collides_with(bullet): # Verifica se o asteroide colidiu com o tiro
                    self.asteroids.remove(asteroid) # Remove o asteroide
                    self.bullets.remove(bullet) # Remove o tiro
                    asteroid.split() # Divide o asteroide em 2
                    break
                
        for bullet in self.bullets[:]: # Percorre todos os tiros
            if not self.screen.get_rect().collidepoint(bullet.position): # Verifica se o tiro saiu da tela
                self.bullets.remove(bullet) # Remove o tiro da lista de tiros

    def _draw(self): # Método desenha na tela
        self.screen.blit(self.background, (0, 0)) # Desenha a imagem de fundo na tela
        
        for game_object in self._get_game_objects(): # Percorre todos os objetos do jogo
            game_object.draw(self.screen) # Desenha o objeto na tela
        
        pygame.display.flip() # Atualiza a tela
        self.clock.tick(60) # Define o FPS
        
    def _get_game_objects(self): # Método retorna todos os objetos do jogo
        game_objects = [*self.asteroids, *self.bullets] # Cria uma lista com todos os asteroides e tiros
        
        if self.spaceship:
            game_objects.append(self.spaceship) # Adiciona a nave na lista de objetos do jogo
            
        return game_objects # Retorna a lista de objetos do jogo