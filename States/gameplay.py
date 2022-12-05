import pygame, os
from States.state import State
from States.menu import Menu
from States.utils import get_random_position, load_sound, load_sprite
from States.models import GameObject, Spaceship, Asteroids, Life, Enemy
from States.game_over import GameOver
from States.utils import load_sound, load_sprite

class Gameplay(State):
    MIN_ASTEROID_DISTANCE = 250
    
    def __init__(self, game, nave):
        """Construtor da classe Gameplay"""
        State.__init__(self,game)
        self.background = load_sprite("background_space", 0.6, True)
        self.GAME_W,self.GAME_H = 480, 270
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.nave = nave
        self.clock = pygame.time.Clock() # Cria um objeto Clock
        self.life = []
        self.asteroids = [] # Cria uma lista de asteroides
        self.bullets = [] # Cria uma lista de tiros
        self.enemy_bullets = []
        self.spaceship = Spaceship(self.nave, (self.screen.get_size()[0]/2, self.screen.get_size()[1]/2), self.bullets.append) # Cria uma instância da classe Spaceship
        self.score_value = 0 # Inicializa a pontuação com 0
        self.explosion_sound = load_sound("explosion_1") # Define o método para gerar um som de explosão
        self.enemy = Enemy((0,0), self.enemy_bullets.append)
        self.soundtrack = load_sound("Game_soundtrack_3")
        for i in range(self.spaceship.lifes):
            self.life.append(Life((30+(i * 50)+10*i, 25)))
        
        
    def show_score(self,x,y): # Método para mostrar o placar
        """Método para mostrar o placar
        param x: posição x do placar
        type x: int
        param y: posição y do placar
        type y: int
        """
        score_font = pygame.font.Font('Assets/Font/Polybius1981.ttf', 32) # Define a fonte e o tamanho da pontuação
        score = score_font.render("Score : " + str(self.score_value), True, (255,255,255)) # Define o texto do placar
        self.screen.blit(score, (x, y)) # Mostra o placar na tela

    def update(self, actions):
        """Método atualiza o estado do jogo
        param actions: dicionario de ações
        type actions: dict
        """
        if actions["enter"]:
            self.soundtrack.stop()
            new_state = Menu(self.game)
            new_state.enter_state()
        if actions["up"]:
            self.spaceship.accelerate() # Acelera a nave
        if actions["left"]:
            self.spaceship.rotate(clockwise=False)
        if actions["right"]:
            self.spaceship.rotate(clockwise=True)
        if actions["space"]:
            self.spaceship.shoot()
            actions["space"] = False

        self._process_game_logic() # Processa a lógica do jogo

    def _process_game_logic(self): # Método processa a lógica do jogo
        """Método processa a lógica do jogo"""
        for game_object in self._get_game_objects(): # Percorre todos os objetos do jogo
            game_object.move(self.screen) # Move o objeto
        
        if self.enemy:     
            if pygame.time.get_ticks() % 1000 == 0:
                self.enemy.shoot()

        while self.enemy == None:
            if len(self.asteroids)==7:
                while True:
                    position = get_random_position(self.screen) # Pega uma posição aleatória
                    if (
                        position.distance_to(self.spaceship.position)
                        > self.MIN_ASTEROID_DISTANCE
                    ): # Verifica se a posição do asteroide está a uma distância mínima da nave
                        break
                self.enemy = Enemy(position, self.enemy_bullets.append)
            else:
                break

        while len(self.asteroids) < 5: # Enquanto a quantidade de asteroides for menor que 5
            while True:
                position = get_random_position(self.screen) # Pega uma posição aleatória
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ): # Verifica se a posição do asteroide está a uma distância mínima da nave
                    break
            self.asteroids.append(Asteroids(position, self.asteroids.append)) # Adiciona o asteroide na lista de asteroides
            
        if self.spaceship: # Verifica se a nave existe
            for asteroid in self.asteroids: # Percorre todos os asteroides
                if asteroid.collides_with(self.spaceship): # Verifica se o asteroide colidiu com a nave
                    pygame.mixer.Channel(1).play(self.explosion_sound) # Toca o som de explosão
                    self.spaceship.life_lost() # Chama o método life_lost da nave
                    if self.spaceship.lifes == 0:
                        self.soundtrack.stop()
                        new_state = GameOver(self.game, self.score_value)
                        new_state.enter_state()
                    else:
                        self.life.pop() # Remove uma vida da lista de vidas
                        self.spaceship.set_velocity((0, 0)) # Zera a velocidade da nave
                        for asteroid in self.asteroids:
                            while True:
                                position = get_random_position(self.screen)
                                if (
                                    position.distance_to(asteroid.position)
                                    > self.MIN_ASTEROID_DISTANCE
                                ):
                                    break
                            self.spaceship.position = position
                    
        
        for bullet in self.bullets[:]: # Percorre todos os tiros
            for asteroid in self.asteroids[:]: # Percorre todos os asteroides
                if asteroid.collides_with(bullet): # Verifica se o asteroide colidiu com o tiro
                    pygame.mixer.Channel(1).play(self.explosion_sound) # Toca o som de explosão
                    self.asteroids.remove(asteroid) # Remove o asteroide
                    self.bullets.remove(bullet) # Remove o tiro
                    asteroid.split() # Divide o asteroide em 2
                    if asteroid.size == 1:
                        self.score_value += 100
                    elif asteroid.size == 2:
                        self.score_value += 50
                    elif asteroid.size == 3:
                        self.score_value += 20
                    elif asteroid.size == 4:
                        self.score_value += 10
                    break
        
        for bullet in self.bullets[:]:
            if self.enemy:
                if bullet.collides_with(self.enemy):
                    pygame.mixer.Channel(1).play(self.explosion_sound) # Toca o som de explosão
                    self.bullets.remove(bullet)
                    self.enemy = None
                    self.score_value += 500
        

        if self.enemy and self.spaceship:
            if self.enemy.collides_with(self.spaceship):
                pygame.mixer.Channel(1).play(self.explosion_sound) # Toca o som de explosão
                self.spaceship.life_lost()
                if self.spaceship.lifes == 0:
                    self.soundtrack.stop()
                    new_state = GameOver(self.game, self.score_value)
                    new_state.enter_state()
                else:
                    self.life.pop()
                    self.spaceship.set_velocity((0, 0))
                    for asteroid in self.asteroids:
                        while True:
                            position = get_random_position(self.screen)
                            if (
                                position.distance_to(asteroid.position)
                                > self.MIN_ASTEROID_DISTANCE
                            ):
                                break
                        self.spaceship.position = position

        for bullet in self.enemy_bullets[:]: # Percorre todos os tiros
            if bullet.collides_with(self.spaceship): # Verifica se uma bala inimiga colidiu com a nave
                pygame.mixer.Channel(1).play(self.explosion_sound) # Toca o som de explosão
                self.spaceship.life_lost() # Chama o método life_lost da nave
                self.enemy_bullets.remove(bullet) # Remove o tiro
                if self.spaceship.lifes == 0:
                    self.soundtrack.stop()
                    new_state = GameOver(self.game, self.score_value)
                    new_state.enter_state()
                else:
                    self.life.pop() # Remove uma vida da lista de vidas
                    self.spaceship.set_velocity((0, 0)) # Zera a velocidade da nave
                    for asteroid in self.asteroids:
                        while True:
                            position = get_random_position(self.screen)
                            if (
                                position.distance_to(asteroid.position)
                                > self.MIN_ASTEROID_DISTANCE
                            ):
                                break
                        self.spaceship.position = position

        for bullet in self.bullets[:]: # Percorre todos os tiros
            if not self.screen.get_rect().collidepoint(bullet.position): # Verifica se o tiro saiu da tela
                self.bullets.remove(bullet) # Remove o tiro da lista de tiros
        
        for bullet in self.enemy_bullets[:]: # Percorre todos os tiros
            if not self.screen.get_rect().collidepoint(bullet.position): # Verifica se o tiro saiu da tela
                self.enemy_bullets.remove(bullet) # Remove o tiro da lista de tiros
    
    def _get_game_objects(self): # Método retorna todos os objetos do jogo
        """Retorna todos os objetos do jogo
        return param: lista de objetos do jogo
        return type: list
        """
        game_objects = [*self.asteroids, *self.bullets, *self.life, *self.enemy_bullets] # Cria uma lista com todos os asteroides e tiros
        
        if self.spaceship:
            game_objects.append(self.spaceship) # Adiciona a nave na lista de objetos do jogo
        if self.enemy:
            game_objects.append(self.enemy)

        return game_objects # Retorna a lista de objetos do jogo
    
    def render(self, display): # Método desenha na tela
        """Desenha na tela
        param display: tela
        param type: pygame.Surface
        """
        self.screen.blit(self.background, (0, 0)) # Desenha a imagem de fundo na tela
        
        for game_object in self._get_game_objects(): # Percorre todos os objetos do jogo
            game_object.draw(self.screen) # Desenha o objeto na tela
        
        self.show_score(self.screen.get_size()[0]-200, 25) # Mostra o placar na tela
        self.soundtrack.play() # Toca a música de fundo
        pygame.display.flip() # Atualiza a tela
        self.clock.tick(60) # Define o FPS