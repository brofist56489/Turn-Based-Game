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

	def get_tile(self, x, y):
		if x < 0 or y < 0 or x >= LEVEL_WIDTH or y >= LEVEL_HEIGHT:
			return None
		t = self.tiles[x + y * LEVEL_WIDTH]
		return tiles.TILES[t]

	def set_tile(self, x, y, t):
		if x < 0 or y < 0 or x >= LEVEL_WIDTH or y >= LEVEL_HEIGHT:
			return
		self.tiles[x + y * LEVEL_WIDTH] = t.id

	def render(self, screen):
		for x in range(0, LEVEL_WIDTH):
			for y in range(0, LEVEL_HEIGHT):
				t = self.get_tile(x, y)
				if t != None:
					t.render(screen, x, y)