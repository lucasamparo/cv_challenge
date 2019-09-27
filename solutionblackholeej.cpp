/* Solution of cv_challenge "Oh no, a Black Hole !"

Author = Edilton Jr */

#include <cmath>
#include <iostream>

using namespace std;

typedef pair<int, int> ii;


struct pto{ 
	
	double x, y;
	
	pto(){}
	
	pto(double x, double y) :x(x), y(y) {}
	
	pto (pto m, pto n) { 
	x=(n.x-m.x); 
	y=(n.y-m.y); }
	
	pto operator +(pto q){ return pto(x+q.x, y+q.y); }
	
	pto operator -(pto q){ return pto(x-q.x, y-q.y); }
	
	pto operator /(double t){ return pto(x/t, y/t); }
	
	void set() { cin >> x >> y; }
	
	void debug() { cout << "x: " << x << " y: " << y << '\n'; }
	
};


int main(){
	
	int j,T;
	
	double epsilon = 1e-12; 
	
	cin >> T;  /* set value of T*/
	
	
	for(j=1; j<=T; j++){    
	
		pto m1, m2, n1, n2;
		m1.set(), n1.set(), m2.set(), n2.set();  /* add 4 coordinates pairs, separated by space.*/
		
		pto m = (m1+m2)/2, n = (n1+n2)/2;
		pto dm = m2-m1, dn = n2-n1;
		pto mp = pto(-dm.y, dm.x), np = pto(-dn.y, dn.x);
		
		
		double total; 
				
		if(fabs(np.y)<=epsilon) total = (n.y-m.y)/(mp.y);
		else total = (m.x-n.x-np.x/np.y*(m.y-n.y))/(np.x*mp.y/np.y - mp.x);
		
		pto output;
		output = pto(m.x+mp.x*total, m.y+mp.y*total);
		
		printf("Caso #%d: %.2lf %.2lf\n", j, output.x+epsilon, output.y+epsilon); /*The result will be shown after adding the ordered pairs  o*/
		
		/* repeat the procedure until the software ends*/
	}
	
		
	return 0;
} 
