#include <bits/stdc++.h>


int main(void){
    long long binary_coin;	
    cin >> binary_coin;	
    bitset<64> coin_set (binary_coin);	
    cout << (1LL << coin_set.count()) << endl;
    return 0;
}
