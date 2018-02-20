import random


class Mastermind:

	def __init__(self, colors_number = 4, rounds = 10):
		self.color_dict = ['R', 'J', 'B', 'O', 'V', 'N']
		self.colors = self.generate_colors(colors_number)
		self.current_round = 0
		self.max_rounds = rounds
		self.tries = [] #Store user tries with number of correct colors
		

	def generate_colors(self, colors_number):
		return ['R', 'O', 'O', 'J']#[self.color_dict[random.randrange(len(self.color_dict))] for x in range(colors_number)]

	def is_correct_input(self, line_input):
		#Returns true if input match this masterming play
		if len(line_input)==len(self.colors) and 1==1:
			return True
		print('Please enter a correct input ({} colors)'.format(len(self.colors)))
		return False

	def count_colors(self, p_input):
		#returns the number of correct colors in the input
		#a optimiser
		total_good = 0
		total_perfect = 0
		temp_colors = list(self.colors)
		for i,c in enumerate(p_input):
			if c in temp_colors:
				total_good += 1
				temp_colors.remove(c)
			if c == self.colors[i]:
				total_perfect += 1

		return total_good-total_perfect, total_perfect


	def next_round(self):
		p_input = raw_input()
		while not self.is_correct_input(p_input):
			p_input = raw_input()

		#We have a correct input, let's compute tries and store it
		good_colors, perfect_colors = self.count_colors(p_input)
		self.tries.append([p_input, perfect_colors, good_colors])
		if perfect_colors==len(self.colors):
			print('WIN !!')
			return False
		if len(self.tries)==self.max_rounds:
			print('Lost, over')
			print('Answer was : '+''.join(self.colors))
			return False
		return True


	def make_line(self, i, line):
		s = '|'
		s += line[0]
		s += '| '
		s += str(line[1])
		s += ' | '
		s += str(line[2])
		s += ' | '
		s += str(i)+'/'+str(self.max_rounds)+' |\n'
		return s

	def __str__(self):
		s = '|-------------------|\n'
		for i, line in enumerate(self.tries):
			s += self.make_line(i, line)
		s += '|-------------------|\n'
		return s

m = Mastermind()
n = True
while n:
	n = m.next_round()
	print(m)
