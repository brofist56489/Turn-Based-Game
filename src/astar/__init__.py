from src.level import *

MOVEMENT_COST = 10

class AStarPathFinder():
	def __init__(self, level, startPos, targetPos):
		self.nodes = []
		self.level = level
		self.start = startPos
		self.target = targetPos
		self.create_nodes()

	def create_nodes(self):
		self.nodes = {}
		for y in range(LEVEL_HEIGHT):
			for x in range(LEVEL_WIDTH):
				node = AStarNode(abs(x - self.target[0]) + abs(y - self.target[0]), x, y)
				self.nodes[(x, y)] = node

	def find_path(self):
		open_list = [self.start]
		closed_list = []
		done = False
		pos = self.start
		while not done:
			if pos in closed_list:
				continue
			del open_list[open_list.index(pos)]
			closed_list.append(pos)
			if pos == self.start:
				self.nodes[pos].g = 0
			for chn in [(0, 1), (1, 0), (0, -1), (-1, 0)]:#, (-1, 1), (1, 1), (1, -1), (-1, -1)]:
				chp = (pos[0] + chn[0], pos[1] + chn[1])
				if self.level.get_tile(chp[0], chp[1]) == None:
					# print("Skipped Tile", chp)
					continue
				if self.level.get_tile(chp[0], chp[1]).solid or chp in closed_list:
					# print("Skipped Tile because of solid", chp)
					continue
				if chp == self.target:
					self.nodes[chp].parentNode = self.nodes[pos]
					done = True
					break
				if chp in open_list:
					# print("Found node in open list", chp)
					if self.nodes[pos].g + MOVEMENT_COST < self.nodes[chp].g:
						self.nodes[chp].parentNode = self.nodes[pos]
						self.nodes[chp].g = self.nodes[pos].g + MOVEMENT_COST
						# print("Faster path calulated", chp)
				else:
					# print("Found Empty node", chp)
					open_list.append(chp)
					if self.nodes[chp].f == -1:
						self.nodes[chp].parentNode = self.nodes[pos]
					self.nodes[chp].g = self.nodes[pos].g + MOVEMENT_COST
				self.nodes[chp].calc_f()

			nn = (0, 0)
			sm = -1
			for pos2 in open_list:
				if sm == -1:
					sm = self.nodes[pos2].f
					nn = pos2
					continue
				if self.nodes[pos2].f < sm:
					sm = self.nodes[pos2].f
					nn = pos2
			pos = nn
		a = self.target
		ns = []
		try:
			while not a == self.start:
				ns.append((self.nodes[a].x, self.nodes[a].y))
				a = (self.nodes[a].parentNode.x, self.nodes[a].parentNode.y)
			ns.append(self.start)
		except AttributeError as e:
			print("A is ", a)
			print("Node Parent is", self.nodes[a].parentNode)
			print("Known nodes", ns)
			raise e
		return ns



class AStarNode():
	def __init__(self, h, x, y):
		self.h = h
		self.g = -1
		self.f = -1
		self.parentNode = None
		self.x = x
		self.y = y

	def calc_f(self):
		self.f = self.h + self.g