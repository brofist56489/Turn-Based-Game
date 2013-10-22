from src import tiles

LEVEL_WIDTH = 20
LEVEL_HEIGHT = 15


class Level():
	def __init__(self):
		self.__init_tiles()

	def __init_tiles(self):
		self.tiles = []
		for i in range(0, LEVEL_WIDTH * LEVEL_HEIGHT):
			self.tiles.append(0)

	def set_tiles_from_packet(self, data):
		LEVEL_WIDTH = data[0]
		LEVEL_HEIGHT = data[1]
		data = data[2::]
		tiles = data

	def render(self, screen):
		for x in range(0, LEVEL_WIDTH):
			for y in range(0, LEVEL_HEIGHT):
				t = self.tiles[x + y * LEVEL_WIDTH]
				if t != -1:
					tiles.TILES[t].render(screen, x, y)