class grade_calc():
	def __init__ (self):
		self.twelvec = 12
		self.ninec = 9
		self.sixc = 6
		self.eighteenc = 18
		self.threec = 3
		self.fifteenc = 15
		self.perf_credit=0
		self.act_credit=0
		self.credit_list = {'3':self.threec,'6':self.sixc,'9':self.ninec,'12':self.twelvec,'15':self.fifteenc,'18':self.eighteenc}
		self.classes_taken={}
	def ask(self,Q):
		if Q == "Class":
				a= input("What Class did you take?")
				if type(a) != str:
					return None
				else:
					return a
		if Q == "Credits":
			return self.credit_list[input("How Many Credits was it?")]
		else:
			return self.credit_list[input("What Grade did you get?")]
	def calculate(self):
		while self.ask("Class") != None:
			self.classes_taken.update[self.ask("Class"):(self.ask("Credits"),self.ask("Grade"))]
		
		return self.classes_taken
			 

		

		# for i in range(len(self.credit_list)):
		# 	while type(input("How many {} classes have you taken?".format(i))) != int:
		# 	 	input("How many {} classes have you taken?".format(i))
		# 	self.perf_credit += input("How many {} classes have you taken?".format(i))
		
		# while type(input("How many {} classes have you taken?".format(i))) != int or input("How many {} classes have you taken?".format(i)) > 5:
		# 		input(what was your grade in {}class?)


if __name__ == "__main__":
	calc_grade = grade_calc()

	grade= calc_grade.calculate()

	print(grade)
