from pygame.math import Vector2 # Importa o módulo math do pygame
from pygame.transform import rotozoom # Importa o método rotozoom do módulo transform do pygame
from States.utils import get_random_velocity, load_sound, load_sprite, wrap_position # Importa os métodos do módulo utils


UP = Vector2(0, -1) # Define a direção para cima

class GameObject: # Classe base para todos os objetos do jogo
    def __init__(self, position, sprite, velocity): # Método construtor
        """Construtor da classe GameObject"""
        self.position = Vector2(position) # Define a posição do objeto
        self.sprite = sprite # Define a imagem do objeto
        self.radius = sprite.get_width() / 2 # Define o raio do objeto
        self.velocity = Vector2(velocity) # Define a velocidade do objeto

    def draw(self, surface): # Método desenha o objeto na tela
        """Desenha o objeto na tela
        :param surface: superfície onde o objeto será desenhado
        :type surface: pygame.Surface
        """
        blit_position = self.position - Vector2(self.radius) # Define a posição do objeto
        surface.blit(self.sprite, blit_position) # Desenha o objeto na tela
 
    def move(self, surface): # Método move o objeto
        """Move o objeto
        :param surface: superfície onde o objeto será desenhado
        :type surface: pygame.Surface
        """
        self.position = wrap_position(self.position + self.velocity, surface) # Calcula a nova posição do objeto

    def collides_with(self, other_obj): # Método verifica se o objeto colidiu com outro objeto
        """Verifica se o objeto colidiu com outro objeto
        :param other_obj: outro objeto
        :type other_obj: GameObject
        """
        distance = self.position.distance_to(other_obj.position) # Calcula a distância entre os objetos
        return distance < self.radius + other_obj.radius # Retorna se a distância é menor que a soma dos raios
    
    def set_position(self, position):
        """Define a posição do objeto
        :param position: posição do objeto
        :type position: Vector2
        """
        self.position = Vector2(position)
    
    def set_velocity(self, velocity):
        """Define a velocidade do objeto
        :param velocity: velocidade do objeto
        :type velocity: Vector2
        """
        self.velocity = Vector2(velocity)


class Spaceship(GameObject): # Classe para a nave
    MANEUVERABILITY = 3 # Define a manobrabilidade da nave
    BULLET_SPEED = 3 # Define a velocidade do tiro
    
    def __init__(self, type, position, create_bullet_callback): # Método construtor
        """Construtor da classe Spaceship"""
        self.type = type
        self.lifes = 7-2*self.type # Define a quantidade de vidas
        self.create_bullet_callback = create_bullet_callback # Define o método para criar um tiro
        self.direction = Vector2(UP) # Define a direção da nave
        self.acceleration = self.type/15
        self.max_velocity = 3 + 3*self.type
        sprites_img = ["spaceship", "spaceship_2"]
        super().__init__(position, load_sprite(sprites_img[self.type - 1], (3-self.type)*0.1), Vector2(0)) # Chama o construtor da classe pai
        self.laser_sound = load_sound("laser_1") # Define o método para tocar o som de laser
        
    def rotate(self, clockwise=True): # Método rotaciona a nave
        """Rotaciona a nave
        :param clockwise: se a nave deve rotacionar no sentido horário
        :type clockwise: bool
        """
        sign = 1 if clockwise else -1 # Define o sinal da rotação
        angle = self.MANEUVERABILITY * sign # Calcula o ângulo da rotação
        self.direction.rotate_ip(angle) # Rotaciona a direção da nave
        
    def accelerate(self): # Método acelera a nave
        """Acelera a nave"""
        self.velocity += self.direction * self.acceleration # Atualiza a velocidade da nave
        if self.velocity.magnitude() > self.max_velocity:
            Vector2.normalize_ip(self.velocity)
            self.velocity = self.max_velocity*self.velocity
        
    def draw(self, surface): # Método desenha a nave na tela
        """Desenha a nave na tela
        :param surface: superfície onde a nave será desenhada
        :type surface: pygame.Surface
        """
        angle = self.direction.angle_to(UP) # Calcula o ângulo da direção da nave
        rotated_surface = rotozoom(self.sprite, angle, 1.0) # Rotaciona a imagem da nave
        rotated_surface_size = Vector2(rotated_surface.get_size()) # Calcula o tamanho da imagem rotacionada
        blit_position = self.position - rotated_surface_size * 0.5 # Define a posição da imagem rotacionada
        surface.blit(rotated_surface, blit_position) # Desenha a imagem rotacionada na tela
        
    def shoot(self):
        """Cria um tiro"""
        self.laser_sound.play() # Chama o método para rodar o som de laser quando a nava atirar
        bullet_velocity = 3 * self.direction * self.BULLET_SPEED # Calcula a velocidade do tiro
        bullet = Bullet(self.position, bullet_velocity, self.type) # Cria um tiro
        self.create_bullet_callback(bullet) # Chama o método para criar um tiro
        
    def life_lost(self):
        """Retira uma vida da nave"""
        self.lifes -= 1 # Decrementa a quantidade de vidas

class Enemy(GameObject):
    ENEMY_BULLET_SPEED = 2
    def __init__(self, position, create_bullet_callback):
        """Construtor da classe Enemy"""
        super().__init__(position, load_sprite("enemy_spaceship", 0.09), get_random_velocity(1, 2)) 
        self.create_bullet_callback = create_bullet_callback # Define o método para criar um tiro
        self.laser_sound = load_sound("laser_1") # Define o método para tocar o som de laser

    def shoot(self):
        """Cria um tiro"""
        bullet_velocity = get_random_velocity(1,2) * self.ENEMY_BULLET_SPEED # Calcula a velocidade do tiro     
        bullet = Bullet(self.position, bullet_velocity, 3) # Cria um tiro
        self.create_bullet_callback(bullet) # Chama o método para criar um tiro
        self.laser_sound.play() # Chama o método para rodar o som de laser quando a nava atirar


class Life(GameObject): # Classe para a vida
    def __init__(self, position): # Método construtor
        """Construtor da classe Life"""
        super().__init__(position, load_sprite("heart", 0.1), Vector2(0)) # Chama o construtor da classe pai

class Asteroids(GameObject): # Classe para os asteroides
    def __init__(self, position, create_asteroid_callback, size=4): # Método construtor
        """Construtor da classe Asteroids"""
        self.create_asteroid_callback = create_asteroid_callback  # Recursão para a quebra de asteroid
        self.size = size  # "Tamanho"

        size_scale = {
            4:1,
            3:0.75,
            2:0.5,
            1:0.25
        }  # Escala em relação ao tamanho
        scale = size_scale[self.size]
        
        sprite_size = {
            4:"hexagoid",
            3:"pentagoid",
            2:"quadroid",
            1:"trianguloid"
        }  # Formato em relação ao tamanho
        sprite_img = sprite_size[size]

        sprite = rotozoom(load_sprite(sprite_img, 0.3), 0, scale)

        super().__init__(position, sprite, get_random_velocity(1, 3)) # Chama o construtor da classe pai
    
    def split(self):
        """Quebra o asteroide em pedaços menores"""
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroids(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)
        
class Bullet(GameObject): # Classe para os tiros
    def __init__(self, position, velocity, type): # Método construtor
        """Construtor da classe Bullet"""
        self.type = type
        self.sprite_img = ["bullet_1", "bullet_2", "bullet_3"]
        super().__init__(position, load_sprite(self.sprite_img[self.type - 1], 0.2), velocity) # Chama o construtor da classe pai
        
    def move(self, surface): # Método move o tiro
        """Move o tiro
        :param surface: superfície onde o tiro será desenhado
        :type surface: pygame.Surface
        """
        self.position = self.position + self.velocity # Calcula a nova posição do tiro
