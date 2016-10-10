def minim(arr):
	high = arr[0]
	for i in arr:
		if high > i:
			high = i
	return high



def maxim(arr):
	low = arr[0]
	for i in arr:
		if low < i:
			low = i
	return low	


def big_small_pair(arr):
	high = maxim(arr) 
	low  = minim(arr) 
	a = arr.index(high)
	b = arr.index(low)
	c = [arr[b+1],arr[a-1]]
	return c

a = [11,-1,1,2,3,10,34,0,4,5,6,9]
print(big_small_pair(a))



def sort_ascending(arr):
	h = []
	for a in range(len(arr)):
		min = minim(arr)
		h.append(min)
		arr.remove(min)
	return h

def sort_descending(arr):
	h = []
	for a in range(len(arr)):
		max = maxim(arr)
		h.append(max)
		arr.remove(max)
	return h	



def up_down_sort(arr):
		b = sort_ascending(arr)
		c = int(round((len(b)/2)-1))
		d = (b[:c])
		e = (sort_descending(b[(c+1):]))
		g = d + e
		return g

			
a = [11,-1,1,2,3,10,34,0,4,5,6]
b = up_down_sort(a)	
print(b)




def create_array(string):
	a = string.split()
	for i in a:
		b = " ".join(i)
	return b.split(" ")	

def capital_position(arr):
	h = []
	for x in arr:
		if x.isupper():
			h.append(arr.index(x))
	return h

		
def replace_capitals(string):
	m = create_array(string)
	k = capital_position(m)
	for i in k:
		m[i] = "_%s" % (m[i].lower())
	return m	

def snake_case(string):
	k = replace_capitals(string)
	return "".join(k)

m = "camelCaseNowThenIs"
print(snake_case(m))
