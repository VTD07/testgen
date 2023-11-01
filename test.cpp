#include<bits/stdc++.h>
using namespace std;
typedef long long l2;
const l2 nmax=1e5+9;
l2 n,m,a[nmax],b[nmax];
l2 kq=0;
l2 check(l2 x)
{
    l2 j=1,tmp=0;
    for(int i=1;i<=n;i++)
    {
        if(a[i]<x)
        {
           while(j<=m && a[i]+b[j]<x)
           {
               j++;
           }
           if(j>m) return false;
           j++;
        }
    }
    return true;
}
signed main ()
{
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>a[i];
    }
    cin>>m;
    for(int i=1;i<=m;i++)
    {
        cin>>b[i];
    }
    l2 dau=1,cuoi=1e9;
    while(dau<=cuoi)
    {
        l2 mid=(dau+cuoi)>>1;
        if(check(mid))
        {
            kq=mid,dau=mid+1;
        }
        else cuoi=mid-1;
    }
    cout<<kq;
}

