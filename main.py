class FindPrimaryKey():
	def __init__(self, table):
		self.ans = []
		self.table: list = table
		#table looks like this:
		#[
		# 	{"id": "aaa", "name": "bbbb"},
		# 	,,,,
		# 	{"id": "zzz", "name": "1111"}
		# ]
		pass
	def isEmpty(self, x: set):
		if(len(x) == 0):
			return True
		else:
			return False

	def getNextInputs(self, x: set, y: set):
		nextInputs = []
		for diff in x:
			next_x = x.copy()
			next_y = y.copy()

			next_x.remove(diff)
			next_y.add(diff)

			nextInputs.append((next_x, next_y))

		return nextInputs
	
	def getValues(self, dict: dict,  keys: set):
		values = []
		for key in keys:
			values.append(dict[key])
		return tuple(values)
	
	def isFunctionalDepend(self, x :set, y:set):
		checked = {}
		table = self.table
		x_data = list(map(self.getValues, table, [x] * len(table)))
		y_data = list(map(self.getValues, table, [y] * len(table)))

		for x_line, y_line in zip(x_data, y_data):
			if x_line in checked.keys():
				if checked[x_line] != y_line:
					return False
			else:
				checked[x_line] = y_line
		
		return True

	def nextStep(self, x: set, y: set):
		next_inputs = self.getNextInputs(x, y)
		for next_input in next_inputs:

			next_x, next_y = next_input
			self.recursiveFindPrimaryKey(next_x, next_y)
	
	#x, y　はそれぞれ属性名or属性idを要素として持つ集合
	#テーブルの実態は持たない

	def exec(self):
		x = set(self.table[0].keys())
		y = set()
		self.recursiveFindPrimaryKey(x, y)
	
	def recursiveFindPrimaryKey(self, x, y):
		if self.isEmpty(x):
			return False
		elif self.isEmpty(y):
			self.nextStep(x, y)
		else:
			if self.isFunctionalDepend(x, y):
				self.ans.append((x, y))
				self.nextStep(x, y)
				return True
			else:
				return False


if __name__ == "__main__":
	table = [
				{"id": "aaa", "name": "111"},
				{"id": "bbb", "name": "111"}
			]
	FPK = FindPrimaryKey(table)
	FPK.exec()
	print(FPK.ans)