from pygame.math import Vector2 # Importa o módulo math do pygame
from pygame.transform import rotozoom # Importa o método rotozoom do módulo transform do pygame
from utils import get_random_velocity, load_sprite, wrap_position # Importa os métodos do módulo utils

UP = Vector2(0, -1) # Define a direção para cima

class GameObject: # Classe base para todos os objetos do jogo
    def __init__(self, position, sprite, velocity): # Método construtor
        self.position = Vector2(position) # Define a posição do objeto
        self.sprite = sprite # Define a imagem do objeto
        self.radius = sprite.get_width() / 2 # Define o raio do objeto
        self.velocity = Vector2(velocity) # Define a velocidade do objeto

    def draw(self, surface): # Método desenha o objeto na tela
        blit_position = self.position - Vector2(self.radius) # Define a posição do objeto
        surface.blit(self.sprite, blit_position) # Desenha o objeto na tela
 
    def move(self, surface): # Método move o objeto
        self.position = wrap_position(self.position + self.velocity, surface) # Calcula a nova posição do objeto

    def collides_with(self, other_obj): # Método verifica se o objeto colidiu com outro objeto
        distance = self.position.distance_to(other_obj.position) # Calcula a distância entre os objetos
        return distance < self.radius + other_obj.radius # Retorna se a distância é menor que a soma dos raios
    
class Spaceship(GameObject): # Classe para a nave
    MANEUVERABILITY = 3 # Define a manobrabilidade da nave
    ACCELERATION = 0.25 # Define a aceleração da nave
    
    def __init__(self, position): # Método construtor
        self.direction = Vector2(UP) # Define a direção da nave
        super().__init__(position, load_sprite("spaceship"), Vector2(0)) # Chama o construtor da classe pai
        
    def rotate(self, clockwise=True): # Método rotaciona a nave
        sign = 1 if clockwise else -1 # Define o sinal da rotação
        angle = self.MANEUVERABILITY * sign # Calcula o ângulo da rotação
        self.direction.rotate_ip(angle) # Rotaciona a direção da nave
        
    def accelerate(self): # Método acelera a nave
        self.velocity += self.direction * self.ACCELERATION # Atualiza a velocidade da nave
        
    def draw(self, surface): # Método desenha a nave na tela
        angle = self.direction.angle_to(UP) # Calcula o ângulo da direção da nave
        rotated_surface = rotozoom(self.sprite, angle, 1.0) # Rotaciona a imagem da nave
        rotated_surface_size = Vector2(rotated_surface.get_size()) # Calcula o tamanho da imagem rotacionada
        blit_position = self.position - rotated_surface_size * 0.5 # Define a posição da imagem rotacionada
        surface.blit(rotated_surface, blit_position) # Desenha a imagem rotacionada na tela
        
class Asteroids(GameObject): # Classe para os asteroides
    def __init__(self, position): # Método construtor
        super().__init__(position, load_sprite("hexagoid"), get_random_velocity(1, 3)) # Chama o construtor da classe pai