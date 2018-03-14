#求二元方程组
import math
def quad(a,b,c):
	if a!=0:
		if b**2-4*a*c>=0:
			x1=(-b+math.sqrt(b**2-4*a*c))/(2*a);
			x2=(-b-math.sqrt(b**2-4*a*c))/(2*a);
			return x1,x2;
		
		else:
			return '4ac小于0，无解';
	else:
		x=(-c)/b;
		return x;

print(quad(1,-4,3));

#可变参数
def calc(*number):
	sum=0;
	for i in number:
		sum=sum+i;
	return sum;
print(calc(1,2,3,4,5));






























			