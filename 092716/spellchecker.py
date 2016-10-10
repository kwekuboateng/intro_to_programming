# Ebenezer Emmanuel Owusu
#Mercy Kinoti
#Frederick Ampomah Boateng
#Duncan Muriithi

def create_file(f_name,text):
	f = open(filename,'w')
	f.write(text)
	f.close()

def read_file(f_name):
	f = open(filename)
	text = f.read().replace("\n"," ").lower()
	f.close()
	return text

def keys_for_dict(dictionary):
	for key in dic.keys():
		return key


def create_dictionary(textfile,dict):
	for word in textfile.split():
		word = word.strip(".,!?();:><?/|}{][*&^%$#@!~`")
		dic[word] = dic.get(word, 0) + 1


def create_list(filename):
	dictext = read_file(filename).split()
	for i in dictext:
		 k = i.strip(".,?/':;{]{]+=-")
		 print(k)

def word_correction(filename,dictname):
 	dic = {}
 	text = read_file(filename)
 	create_dictionary(text,dic)
	valuesOfDic(dic)
	r_word = read_file(dictname).replace(",","").split()
	w_word = dic.keys()
	print("we found these errors")
	for r in r_word:
		for w in w_word:
			d = w + r
			if r != w:
				if (len(w) >= (len(d))/2) and (w[0] == r[0]) and (w[1] == r[1]) and ( ((len(w) - len(r)) <= 2 or (len(r) - len(w)) <= 2)):
			  		print("Wanna Replace", w,  "with", r, "1 if Yes and 2 if No")
			  		user = str(input("1 or 2?:  "))
					try:
						if user == "1":
							text = text.replace(w+"",r + " ")
						elif user == "2":
							text = text
						elif user != "1" and user != "2":
							print("please enter 1 for yes or 2 for no")
					except:
						print("Please input 1 for yes or 2 for no")

	print("All corrections have been made")
	print('No more errors found charlie youre good')
	print("Thanks for using this awesome app")
	create_file("corrected_%s"%filename,text)

word_correction('writing.txt','dictionary.txt')
