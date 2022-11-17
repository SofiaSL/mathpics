#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>

double f(double l, double x) {
	return l * x * (1.0 - x);
}

int main() {
	const constexpr double lmin = 3.0;
	const constexpr double lmax = 4.0;
	const constexpr double resl = 0.0005;
	//const constexpr double resl = 0.005;
	
	const constexpr double resx = 0.000001;
	//const constexpr double resx = 0.00001;
	
	const constexpr int n1 = (lmax - lmin) / resl + 1;
	const constexpr int n2 = 1 / resx;
	
	const constexpr int niter = 1000;
	
	//std::vector<std::vector<double>> out (n1, std::vector<double> (n2, 0.0));
	std::vector<std::vector<double>> out;
	
	
	for(int i1 = 0; i1 != n1; ++i1) {
		double l = lmin + i1 * resl;
		
		std::vector<double> outl;
		
		for(int i2 = 0; i2 != n2; ++i2) {
			double x = i2 * resx;
			x = f(l, x);
			
			
			for(int i3 = 0; i3 != niter; ++i3) {
				x = f(l, x);
				//std::cout << l << ", " << x << "\n";
			}
			outl.push_back(x);
			//out[n1][n2] = x;
			//std::cout << out[0] << "\n";
			//std::cout << n1 << ", " << n2 << ", " << x << "\n";
		}
		
		out.push_back(outl);
	}
	
	/*for(int i1 = 0; i1 != n1; ++i1) {
		for(int i2 = 0; i2 != n2; ++i2) {
			std::cout << out[i1][i2] << ", ";
		}
		std::cout << "\n";
	}*/
	
	for(auto &l : out) {
		std::sort(l.begin(), l.end());
	}
	
	const constexpr double epsilon = 0.0001;
	
	int count = 0;
	for(auto outl : out) {
		double crit = 0.5;
		double l = lmin + count * resl;
		for(int n = 0; n != 10; ++n) {
			auto i = std::lower_bound(outl.begin(), outl.end(), crit - epsilon);
			auto j = std::lower_bound(outl.begin(), outl.end(), crit + epsilon);
			
			//std::cout << std::distance(outl.begin(), i) << ", " << *i << ", " << *j << "\n";
			
			
			//std::cout.precision(3);
			//std::cout << std::setw(4) << l << ", " << crit << ", " << std::distance(i, j) / ( n2 * std::sqrt(epsilon) ) << "\n";
			std::cout << std::distance(i, j) / ( n2 * std::sqrt(epsilon) );
			if(n != 9) std::cout << ",";

			crit = f(l, crit);
		}
		std::cout << "\n";
		++count;
	}
	
	/*for(auto x : out[0]) {
		std::cout << x << ", ";
	}*/
	return 0;
}