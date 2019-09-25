#include<iostream>
#include<iomanip>
#include<utility>
using namespace std;

struct point{
	double x, y;	
};

double calc_slope(point oldP, point newP){
	// calc_slope receives 2 points
	// returns the slope of the line that passes through the 2 received points
	return (newP.y - oldP.y) / (newP.x - oldP.x);
}

double calc_b(point p, double m){
	// calc_b receives a point and the slope of a line that passes through the received point
	// returns the b (y-axis interception point)
	return p.y - m * p.x;
}

int main(){
	int num_test_cases;
	cin >> num_test_cases;
	for (int i = 0; i < num_test_cases; i++){
		// begin test case

		point old1, old2, new1, new2;
		point center;

		// read input
		cin >> old1.x >> old1.y;
		cin >> old2.x >> old2.y;
		cin >> new1.x >> new1.y;
		cin >> new2.x >> new2.y;

		// line1 -> y = m1 * x + b1 -> points old1 and new1
		// line2 -> y = m2 * x + b2 -> points old2 and new2
		// where m = slope, b = y-axis interception point

		// to find the center, we calculate the midpoints
		// and the perpendicular lines that passes through each respective midpoint.
		// if the perpendicular lines intercept in just one point, this is the center. 
		// if they dont intercept in just one point, they are the same line -> infinte centers

		// check if lines are vertical or horizontal
		bool vertical1 = (old1.x == new1.x);
		bool vertical2 = (old2.x == new2.x);
		bool horizontal1 = (old1.y == new1.y);
		bool horizontal2 = (old2.y == new2.y);
		

		if ( (!vertical1 && vertical2) || (horizontal1 && !horizontal2)){
			// if only one line is vertical, than this is always line number 1
			// if only one line is horizontal, than this is always line number 2
			swap(old1, old2);
			swap(new1, new2);
			swap(vertical1, vertical2);
			swap(horizontal1, horizontal2);
		}
		
		// midpoints
		point mid1;
		mid1.x = (old1.x + new1.x) / 2;
		mid1.y = (old1.y + new1.y) / 2; 
		
		point mid2;
		mid2.x = (old2.x + new2.x) / 2;
		mid2.y = (old2.y + new2.y) / 2;

		// slopes
		double m1, m2;

		// if the line is parallel to the y-axis (vertical), the slope is undefined
		if (!vertical1){
			m1 = calc_slope(old1, new1);
		}
		if (!vertical2){
			m2 = calc_slope(old2, new2);
		}
		
		bool parallel = (vertical1 && vertical2) || (horizontal1 && horizontal2) || (m1 == m2);
		
		// special cases

		// parallel -> infinite circles
		// vertical (parallel to y-axis) -> centerY = midY
		// horizontal (parallel to x-axis) -> centerX = midX

		// if lines are parallel
		if (parallel){
			center.x = (mid1.x + mid2.x) / 2;
			center.y = (mid1.y + mid2.y) / 2;
		}
		// if one is vertical and the other is horizontal
		else if (vertical1 && horizontal2){
			center.x = mid2.x;
			center.y = mid1.y;
		}
		// if one is vertical
		else if (vertical1){
			center.y = mid1.y;

			// center.x = interception from perpendicular line 2 with line y = center.y

			double perpendicular_m2 = -1 / m2;
			double perpendicular_b2 = calc_b(mid2, perpendicular_m2);
			center.x = (center.y - perpendicular_b2) / perpendicular_m2;
		}
		// if one is horizontal
		else if (horizontal2){
			center.x = mid2.x;

			// center.y = interception from perpendicular line 1 with line x = center.x

			double perpendicular_m1 = -1 / m1;
			double perpendicular_b1 = calc_b(mid1, perpendicular_m1);
			center.y = perpendicular_m1 * center.x + perpendicular_b1;
		}
		else{

			// (center.x, center.y) = point where both perpendicular lines intercept

			double perpendicular_m1 = -1 / m1;
			double perpendicular_b1 = calc_b(mid1, perpendicular_m1);

			double perpendicular_m2 = -1 / m2;
			double perpendicular_b2 = calc_b(mid2, perpendicular_m2);

			center.x = (perpendicular_b2 - perpendicular_b1) / (perpendicular_m1 - perpendicular_m2);
			center.y = perpendicular_m1 * center.x + perpendicular_b1;
		}

		// output
		cout << setprecision(2) << fixed;
		cout << "Caso #" << i + 1 << ": " << center.x << " " << center.y << endl;

	}
}