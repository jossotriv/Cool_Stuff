import random
#Created Dic of Students with Kerberos Attachments
students = {"Abdulmalik H Alghonaim":"abdulmlk@mit.edu","Anjolaoluwa A Fayemi ":"fanjola@mit.edu","Arnav Y Patel":"arnavp@mit.edu","Barry J Ryan":"barryr","Cole C Legg":"colelegg@mit.edu","Cynthia T. Lo":"cyntio@mit.edu","David J. Mackay":"djmackay@mit.edu","Ebrahim D Al Johani":"ebrahim@mit.edu","Eliza K Khokhar":"ekhokhar@mit.edu","Jeremy C. Cowham":"jcowham@mit.edu","Jesse Hinricher":"jhinrich@mit.edu","Jimmy T Tran":"jtran1@mit.edu","Jose D. Soto Rivera":"jodosori@mit.edu","Wellesley1":"acode@wellesley.edu","Wellesley2":"cblazey@wellesley.edu","W3":"jwainwri@wellesley.edu","W4":"zma@wellesley.edu","Kebar M Geleta": "kgeleta@mit.edu","Luke S Hartnett":"revhart@mit.edu","Madeline E Bundy":"mbundy@mit.edu","Philip J Murzynowski":"philipm@mit.edu","Phoebe L Li":"phoebeli@mit.edu","Rebecca A Agustin":"agustinr@mit.edu","Taimor M Williams":"taimor@mit.edu","Veronica J Ripper":"vripper@mit.edu","Woonyong Bae":"wbae@mit.edu"}

#Kept track of student names in order to randomly distribute stuff
student_names = list(students.values())

#random student names

random.shuffle(student_names)

#partitions into multiple thinghies
def partition(lst, n): 
    division = len(lst) / float(n) 
    return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]

# print(partition(student_names,7))

#Result of First Pairing

results = [['colelegg@mit.edu', 'kgeleta@mit.edu', 'agustinr@mit.edu', 'mbundy@mit.edu'], ['jodosori@mit.edu', 'ekhokhar@mit.edu', 'taimor@mit.edu'], ['jtran1@mit.edu', 'ebrahim@mit.edu', 'cblazey@wellesley.edu', 'acode@wellesley.edu'], ['philipm@mit.edu', 'jwainwri@wellesley.edu', 'jhinrich@mit.edu', 'abdulmlk@mit.edu'], ['zma@wellesley.edu', 'cyntio@mit.edu', 'barryr', 'wbae@mit.edu'], ['phoebeli@mit.edu', 'fanjola@mit.edu', 'vripper@mit.edu'], ['revhart@mit.edu', 'djmackay@mit.edu', 'jcowham@mit.edu', 'arnavp@mit.edu']]

current_matches= {}
#Constructs a tree of current matches
for i in results:
	for j in range(len(i)):
		counter = j+1
		while counter % len(i) != j% len(i):
			person = i[j]
			connection = i[counter%len(i)]
			
			#you can add tuples
			if person in current_matches.keys():
				current_matches[person] += (connection,)
			else:
				current_matches[person] = ()
				current_matches[person] += (connection,)
			counter +=1
print(current_matches)
