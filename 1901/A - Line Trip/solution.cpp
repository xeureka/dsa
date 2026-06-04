#include <bits/stdc++.h>
using namespace std;
 
int solve(vector<int> &a, int x) {
  int n = a.size();
  int max_dist_between_2_gas_station = max(a[0] - 0, 2 * (x - a[n - 1]));
  for (int i = 1; i < n; i++) {
    max_dist_between_2_gas_station =
        max(max_dist_between_2_gas_station, a[i] - a[i - 1]);
  }
  return max_dist_between_2_gas_station;
}
 
int main() {
  int t;
  cin >> t;
 
  for (int zz = 0; zz < t; zz++) {
    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    int res = solve(a, x);
    cout << res << endl;
  }
}