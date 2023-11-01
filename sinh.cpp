#include <bits/stdc++.h>
using namespace std;

mt19937_64 rd(chrono::steady_clock::now().time_since_epoch().count());
#define rand rd

long long Rand(long long l, long long h) {
    assert(l <= h);
    return l + rd() * 1LL * rd() % (h - l + 1);
}

int main()
{
    srand(time(NULL));
    int n=Rand(1,1e5),m=Rand(1,1e5);
    cout<<n<<" "<<m<<'\n';
    for(int i=1;i<=m;i++)
    {
        cout<<Rand(0,1e9)<<' ';
    }

}
