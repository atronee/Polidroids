import pygame, os
from States.state import State

class Credits(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))
	def update(self, delta_time, actions):
		if actions["esc"]:
			self.exit_state()
		self.game.reset_keys()

	def render(self, display):
		display.blit(self.background, (0,0))
		self.game.draw_text(display, "Créditos", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/4, 40)
		self.game.draw_text(display, "Gabriel Pereira: Gameplay", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 - 20, 20)
		self.game.draw_text(display, "Iago Dutra: UI", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2, 20)
		self.game.draw_text(display, "Luan: Trilha sonora", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 20, 20)
		self.game.draw_text(display, "Luís Felipe Marques: ", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 40, 20)
		self.game.draw_text(display, "Otávio Augusto: ", (255,255,255), self.game.GAME_W/2, self.game.GAME_H/2 + 60, 20)