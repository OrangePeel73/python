def triangles():
	l=[1];
	while True:
		yield l;
		l=[l[i-1]+l[i] for i in range(1,len(l))];
		l.insert(0,1);
		l.append(1);

n=0;
for x in triangles():
	n+=1;
	if n==10:
		break;
	print (x);