import pygame, os
from States.state import State
from States.gameplay import Gameplay
from States.story import Story
from States.utils import load_sprite 

class ChooseSpaceship(State):
	def __init__(self, game, soundtrack):
		""" Construtor da classe
		"""
		State.__init__(self, game)
		self.background = load_sprite("background_space", 1)
		self.spaceship = pygame.transform.scale(pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "spaceship.png")), (50, 73))
		self.five_hearts = pygame.transform.scale(pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "five_hearts.png")), (50, 10))
		self.spaceship_2 = pygame.transform.scale(pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "spaceship_2.png")), (50, 50))
		self.three_hearts = pygame.transform.scale(pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "three_hearts.png")), (30, 10))
		self.options = {0 :"spaceship", 1 : "spaceship_2"}
		self.index = 0
		self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "cursor.png"))
		self.cursor_rect = self.cursor_img.get_rect()
		self.cursor_pos_x = self.game.GAME_W/2 - 25
		self.cursor_pos_y = self.game.GAME_H/1.25 - 20
		self.cursor_rect.x, self.cursor_rect.y = self.cursor_pos_x, self.cursor_pos_y
		self.soundtrack = soundtrack

	def update(self, actions):
		""" Atualiza o estado do jogo
    	:param actions: dicionário com as ações do jogador
    	:type actions: dict
    	"""    
		self.update_cursor(actions)
		if actions["enter"]:
			self.transition_state()
		if actions["esc"]:
			self.exit_state()
		self.game.reset_keys()

	def render(self, display):
		""" Renderiza o estado do jogo
		:param display: superfície onde o jogo será renderizado
		:type display: pygame.Surface
		"""
		display.blit(self.background, (0,0))
		self.game.draw_text(display, "Escolha sua Nave", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
		display.blit(self.spaceship, (self.game.GAME_W/2 - 100, self.game.GAME_H/2))
		self.game.draw_text(display, "Lenta", (255,255,255), self.game.GAME_W/2 - 75, self.game.GAME_H/2 + 100, 20)
		display.blit(self.five_hearts, (self.game.GAME_W/2 - 100, self.game.GAME_H/2 + 75))
		display.blit(self.spaceship_2, (self.game.GAME_W/2 + 50, self.game.GAME_H/2))
		self.game.draw_text(display, "Rápida", (255,255,255), self.game.GAME_W/2 + 75, self.game.GAME_H/2 + 100, 20)
		display.blit(self.three_hearts, (self.game.GAME_W/2 + 60, self.game.GAME_H/2 + 75))
		display.blit(self.cursor_img, self.cursor_rect)

	def transition_state(self):
		""" Transisiona para o próximo estado do jogo
		"""
		if self.options[self.index] == "spaceship":
			self.soundtrack.stop()
			new_state = Story(self.game, 1)
			new_state.enter_state()
		elif self.options[self.index] == "spaceship_2":
			self.soundtrack.stop()
			new_state = Story(self.game, 2)
			new_state.enter_state()

	def update_cursor(self, actions):
		""" Atualiza a posição do cursor
		:param actions: dicionário com as ações do jogador
		:type actions: dict
		"""
		if actions['right']:
			self.index = (self.index + 1) % len(self.options)
		elif actions['left']:
			self.index = (self.index - 1) % len(self.options)
		if self.index == 0:
			self.cursor_rect.x = self.cursor_pos_x - 75
		elif self.index == 1:
			self.cursor_rect.x = self.cursor_pos_x + 75