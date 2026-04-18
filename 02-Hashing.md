### 01-Longest Consecutive Sequence in an Array

```java
// nums = [102, 4, 100, 1, 101, 3, 2, 1, 1]
public int longestConsecutive(int[] nums){
	int n = nums.length;

	if(n == 0) return 0; // edge case

	int longest = 1;
	Set<Integer> st = new HashSet<>();

	// set(nums)
	for(int num : nums){
		st.add(num);
	}

	// iterate through set
	for(int num : st){

		// first ele in seq
		if(!st.contains(num - 1)){
			int cnt = 1;
			int x = num;

			// generating seq, present in the set.
			while(st.contains(x + 1)){
				x = x + 1;
				cnt++; 
			}

			longest = Math.max(longest, cnt);
		}
	}

	return longest;
}
```


### 02-Longest subarray with Sum K

```java
// nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]; k = 3
public int longestSubarray(int[] nums, int k){
	int n = nums.length;

	Map<Integer, Integer> preSumMap = new HashMap<>();

	int sum = 0;
	int maxLen = 0;

	for(int i = 0; i < n; i++){
		sum += nums[i];

		if(sum == k){
			maxLen = Math.max(maxLen, i + 1)
		}

		int comp = sum - k;

		if(preSumMap.containsKey(comp)){
			int len = i - preSumMap.get(comp);
			maxLen = Math.max(maxLen, len);
		}


		if(!preSumMap.containsKey(sum)){ // it'll only store the least indexed values
			preSumMap.put(sum,i);
		}
	}

	return maxLen;
}
```

### 03-Count subarrays with given sum
```java
// nums = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]; k = 3
public int subarraySum(int[] nums, int k) {
	int n = nums.length;

	HashMap<Integer, Integer> prefixSumMap = new HashMap<>();

	int sum = 0;
	int cnt = 0;

	for(int i = 0; i < n; i++){
		sum += nums[i];  // prefixSum

		if(sum == k){	// arr[0:i] is valid
			cnt += 1;
		}

		int comp = sum - k;

		// Map[comp] pairs will be generated
		cnt += prefixSumMap.getOrDefault(comp, 0);
		
		prefixSumMap.put(sum, prefixSumMap.getOrDefault(sum, 0) + 1); // Map[sum]++
	}

	return cnt;
}
```

### 04-Count subarrays with given xor k
```java
// nums = [4, 2, 2, 6, 4]; k = 6
public int subarraysWithXorK(int[] nums, int k) {
	int n = nums.length;
	
	HashMap<Integer, Integer> map = new HashMap<>();
	
	int xr = 0;
	int cnt = 0;

	for (int i = 0; i < n; i++) {	
		xr = xr ^ nums[i]; // prefix XOR

		if(xr == k){ // arr[0:i] is valid
			cnt +=1;
		}

		int comp = xr ^ k;

		// Map[comp] pairs will get generated
		cnt += map.getOrDefault(comp, 0); 

		map.put(xr, map.getOrDefault(xr, 0) + 1); // Map[sum]++
	}

	return cnt;
}
```

