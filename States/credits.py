import pygame, os
from States.state import State
from States.utils import load_sprite 

class Credits(State):
	def __init__(self, game):
		"""Construtor da classe Credits"""
		State.__init__(self, game)
		self.background = load_sprite("background_space", 1)

	def update(self, actions):
		"""Atualiza o estado Credits"""
		if actions["esc"]:
			self.exit_state()
		self.game.reset_keys()

	def render(self, display):
		"""Renderiza o estado Credits
		:param display: superfície onde o jogo será renderizado
		:type display: pygame.Surface
		"""
		display.blit(self.background, (0,0))
		self.game.draw_text(display, "Créditos", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
		self.game.draw_text(display, "Gabriel Pereira: Gameplay e Docs", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 20)
		self.game.draw_text(display, "Iago Dutra: UI e UML", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2, 20)
		self.game.draw_text(display, "Luan: Trilha sonora e Testes", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 20, 20)
		self.game.draw_text(display, "Luís Felipe Marques: Gameplay e Debugging", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 40, 20)
		self.game.draw_text(display, "Otávio Augusto: Gameplay e História", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 60, 20)