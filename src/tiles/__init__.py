from pygame import image, Surface, Rect

TILE_MAP = image.load("res/tilemap.png")
TILE_WIDTH = 32
TILE_HEIGHT = 32

TILES = {}

class Tile():
	def __init__(self, tid, textPos, solid):
		self.id = tid
		if tid in TILES.keys():
			raise RuntimeError("Duplicate tiles: " + tid)
		else:
			TILES[tid] = self
		textRect = Rect(textPos[0] * TILE_WIDTH, textPos[1] * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
		self.solid = solid
		self.texture = Surface((TILE_WIDTH, TILE_HEIGHT))
		self.texture.blit(TILE_MAP, [0, 0], textRect)

	def render(self, screen, x, y):
		""" x and y are absolute coords """
		screen.render(self.texture, x * TILE_WIDTH, y * TILE_HEIGHT)

AIR = Tile(0, [0, 0], False)
WALL = Tile(1, [1, 0], True)