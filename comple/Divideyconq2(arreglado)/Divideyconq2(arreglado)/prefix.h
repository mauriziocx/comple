#pragma once
#pragma once
#ifndef COMMON_PREFIX_H
#define COMMON_PREFIX_H
#include<string>
using namespace std;

class Prefix {
public:
	string comonPrefixUtil(string str1,string str2) {
		string result;
		int n1 = str1.length();
		int n2 = str2.length();
		for (int i = 0, j = 0;i <= n1 - 1 && j <= n2;i++,j++) {
			if (str1[i] != str2[j])
				break;
			result.push_back(str1[i]);
		}
		return(result);
	}
	string findCommonPrefix(string arr[], int low, int high) {
		if (low == high)return (arr[low]);
		if (high > low) {
			int mid = low + (high - low) / 2;
			string str1 = findCommonPrefix(arr, low, mid);
			string str2 = findCommonPrefix(arr, mid+1, high);
			return (comonPrefixUtil(str1, str2));
		
		}
	}
}
;
#endif