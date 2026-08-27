#include <iostream>
#include <vector>
 
using namespace std;
 
void solve() {
    int n, m;
    cin >> n >> m;
 
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
 
    vector<long long> b(m);
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }
 
    long long moves_bea = a[0] + n - 1;
    long long moves_ver = b[0] + m - 1;
 
    if (moves_bea >= moves_ver) {
        cout << 1 << "
";
    } else {
        cout << 2 << "
";
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
 
    return 0;
}