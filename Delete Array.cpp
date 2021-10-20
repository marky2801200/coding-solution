/* question link: https://practice.geeksforgeeks.org/problems/delete-array/1/?problemType=functional&difficulty[]=0&page=1&query=problemTypefunctionaldifficulty[]0page1 */ 
//Initial Template for C++

#include <iostream>
using namespace std;

int main() {
	
	int testcase;
	cin >> testcase;
	
	while(testcase--){
	    int N;
	    cin >> N;
        
        // Declaring dynamic 1D array
        int *arr = new int[N];
        
        for(int i = 0;i<N;i++){
            cin >> arr[i];
        }
        
        int sum = 0;
	    for(int i = 0;i<N;i++){
	       sum += arr[i];
	    }
	    
	   


// { Driver Code Starts.
	    
	    cout << sum << endl;
	    
	    cout << arr[0] << endl;
	}
	
	return 0;
}  // } Driver Code Ends
