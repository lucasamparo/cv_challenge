#include <iostream>
#include <utility>
#include <iomanip>

//epsilon to deal with precision on comparisons
const double EPS = 1e-9;

//Structure representing a 2D Point / Vector
struct Point {
  double x, y;
  Point() {}
  Point(const double x, const double y) : x(x), y(y) {};
};

//Structure for Line Equation in form ax+by+c=0
struct Line {
  double a,b,c;
  Line() {}

  //Construct Line Equation using the Direction Vector and a Point
  Line(const Point direction_vector, const Point point){
    this->a = -direction_vector.y;
    this->b = direction_vector.x;
    this->c = -(this->a*point.x + this->b*point.y);
  }
};

//Function to find line-line intersection using Cramer's Rule
std::pair<double, double> line_intersection(const Line line1, const Line line2){
  std::pair<double, double> solution;

  //Find x point
  //check if the answer is zero (or near zero)
  if(abs(line1.c*line2.b - line2.c*line1.b) <= EPS or abs(line1.a*line2.b - line2.a*line1.b) <= EPS)
    solution.first = 0;
  else 
    solution.first = -(line1.c*line2.b - line2.c*line1.b)/(line1.a*line2.b - line2.a*line1.b);

  //Find y point
  //check if the answer is zero (or near zero)
  if(abs(line1.a*line2.c - line2.a*line1.c) <= EPS or abs(line1.a*line2.b - line2.a*line1.b) <= EPS)
    solution.second = 0;
  else
    solution.second = -(line1.a*line2.c - line2.a*line1.c)/(line1.a*line2.b - line2.a*line1.b);
  return solution;
}


//Function to solve each test case
void solve_case(const int case_number){
  Point star1_before, star1_after, star2_before, star2_after;

  std::cin >> star1_before.x >> star1_before.y;
  std::cin >> star2_before.x >> star2_before.y;

  std::cin >> star1_after.x >> star1_after.y;
  std::cin >> star2_after.x >> star2_after.y;

  //Calculate mid point for each star
  Point star1_mid((star1_before.x + star1_after.x)/2., (star1_before.y + star1_after.y)/2.);

  Point star2_mid((star2_before.x + star2_after.x)/2., (star2_before.y + star2_after.y)/2.);

  //Calculate Direction Vector for each star
  Point star1_vector(star1_after.x - star1_before.x, star1_after.y - star1_before.y);

  Point star2_vector(star2_after.x - star2_before.x, star2_after.y - star2_before.y);

  //Calculate Perpendicular Vector for each star
  Point star1_perpendicular_vector(-star1_vector.y, star1_vector.x);

  Point star2_perpendicular_vector(-star2_vector.y, star2_vector.x);

  //Find equation of the line that passes through the center of the circle and the mid point of each star

  Line line1(star1_perpendicular_vector, star1_mid);

  Line line2(star2_perpendicular_vector, star2_mid);

  //Find the intersection point of the lines(the center of the circle)
  std::pair<double, double> answer = line_intersection(line1, line2);

  std::cout << std::fixed << std::setprecision(2) << "Caso #" << case_number << ": " << answer.first << " " << answer.second << std::endl;
}

int main(){
  int number_of_cases;
  std::cin >> number_of_cases;
  //Solve each case
  for(int case_number=1; case_number<=number_of_cases; case_number++)
    solve_case(case_number);
}