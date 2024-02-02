//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    long long Fun(int ind,int sum,int coins[],int n,vector<vector<long long>>&dp){
        if(ind >= n){
            if(sum == 0) return 1;
            return 0;
        }
        if(sum < 0) return 0;
        if(dp[ind][sum] != -1) return dp[ind][sum];
        return dp[ind][sum] = Fun(ind+1,sum,coins,n,dp) + Fun(ind,sum-coins[ind],coins,n,dp);
    }
    long long int count(int coins[], int N, int sum) {

        // code here.
        vector<vector<long long>>dp(N,vector<long long>(sum+1,-1));
        return Fun(0,sum,coins,N,dp);
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int sum, N;
        cin >> sum >> N;
        int coins[N];
        for (int i = 0; i < N; i++) cin >> coins[i];
        Solution ob;
        cout << ob.count(coins, N, sum) << endl;
    }

    return 0;
}


// } Driver Code Ends