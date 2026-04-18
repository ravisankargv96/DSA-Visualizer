## Fundamentals

### 01-Search X in Sorted Array

```java
// int[] nums = {3, 4, 6, 7, 9, 12, 16, 17}; 
// int target = 8;
public int search(int[] nums, int target) {
	int n = nums.length;
	
	// Use : Binary Search

	// search space [l, h]
	int low = 0;
	int high = n - 1;

	// Iterate till a ele exists
	while(low <= high){
	
		int mid = low - (low - high)/2; // m = (l + h)/2

		if(nums[mid] < target){ // nums[mid] < x
			// move to higher search space: [mid + 1, high], 
			low = mid + 1;
		}

		else if(nums[mid] == target){ // nums[mid] = x
			return mid;
		}

		else {  // x < nums[mid];
			// move to lower search space: [low, mid - 1] 
			high = mid - 1;
		}
	}

   // If target not found
   return -1;
}
```

### 02-Lower Bound

```java
// nums[ind] >= x
// nums = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
// x = 11
// eg2:
// nums = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
// x = 9
public int lowerBound(int[] nums, int x) {
	
	int n = nums.length;

	// search space: [l, h]
	int low = 0;
	int high = n - 1;

	// nums[n] >= x is always applicable, so starting from there
	int ans = n;

	/**
	* logic: nums[mid] == x & nums[mid] > x, 
	* track the ans & move to lower search space [l, m - 1]
	*/

	while(low <= high){ // Atleast an ele should exist in an array

		int mid = low - (low - high)/2; // m = (l + h)/2

		if(nums[mid] > x) { // x < nums[mid]
			// grab this ind, & move to lower side for getting optimal number.
			ans = mid;
			high = mid - 1; // [l, m - 1]
		}

		else if(nums[mid] == x) { 
			// equals to target, grab ind & move to lower side
			// since nums[mid] might be repeating
			ans = mid;
			high = mid - 1; // [l, m - 1]
		}

		else { // nums[mid] < x
			// we can ignore this search space
			low = mid + 1; // [m + 1, h]
		}
	}

	return ans; // at worst case it'll return n;
}
```

### 03-Upper Bound

```java
// arr[ind]
// int[] nums = {2, 3, 6, 7, 8, 8, 11, 11, 11, 12}; 
// int x = 9;
public int upperBound(int[] nums, int x) {        
	int n = nums.length;

	// search space: [l, h]
	int low = 0;
	int high = n - 1;

	// nums[n] > x is always applicable, so starting form there
	int ans = n;

	/**
	* logic: nums[mid] > x, 
	* track the ans & move to lower search space [l, m - 1]
	*/

	while(low <= high){ // Atleast an ele should exist in an array

		int mid = low - (low - high)/2; // m = (l + h)/2

		if(x < nums[mid]) {
			// grab this ind, & move to lower side for getting optimal number.
			ans = mid;
			high = mid - 1; // [l, m - 1]
		}

		else if(nums[mid] == x) { 
			// nums[mid] == x, we can ignore this search space
			low = mid + 1; // [m + 1, h]
		}

		else {
			// nums[mid] < x, we can ignore this search space
			low = mid + 1; // [m + 1, h]
		}
	}

	return ans; // at worst case it'll return n;

}
```
## Logic Building
### 01-Search insert position

```java
// nums = [1, 2, 4, 7]
// target = 6

// eg2:
// nums = [1, 2, 4, 7]
// target = 2
public int searchInsert(int[] nums, int target) {
	
	int n = nums.length;

	// search space: [l, h]
	int low = 0;
	int high = n - 1;

	// x <= nums[n] is always applicable, so starting from there
	int ans = n;

	/**
	* logic: nums[mid] == x, return mid
	* x < nums[mid], track ans = mid;
	* nums[mid] < x, ignore this search space
	*/

	while(low <= high){ // Atleast an ele should exist in an array

		int mid = low - (low - high)/2; // m = (l + h)/2

		if(nums[mid] > target){ // x < nums[mid]
			// mid can be a possible answer & move to lower side for getting optimal number.
			ans = mid;
			high = mid - 1; // [l, m - 1]
		}

		else if(nums[mid] == target){
			return mid;
		}

		else { // nums[mid] < x
			// we can ignore this search space
			low = mid + 1; // [m + 1, h]
		}
	}


	return ans; // at worst case it'll return n
}
```
### 02-Floor and Ceil in Sorted Array

```java
// nums =[3, 4, 4, 7, 8, 10], x= 5
// nums[i] <=  x, for highest value of i;

public int[] getFloorAndCeil(int[] nums, int x) {
   return new int[]{ getFloor(nums, x), getCeil(nums, x) };
}

public int getFloor(int[] nums, int x){

	int n = nums.length;

	int low = 0;
	int high = n - 1;

	int ans = -1; // nums[-1] = -inf

	while(low <= high){
		
		int mid = low - (low - high)/2; // mid = (l + h)/2

		if(nums[mid] <= x){
			// it can be a possible answer & move to higher search space
			// [mid + 1, h]

			ans = mid;
			low = mid + 1;
		} else {

			// ignore the search space & move to lower side.
			// i.e. [low, mid - 1]
			high = mid - 1;
		}
	}

	return ans == -1 ? ans : nums[ans];
}

// x <= nums[i], for least value of i;
public int getCeil(int[] nums, int x){
	
	int n = nums.length;

	int low = 0;
	int high = n - 1;

	int ans = n; // nums[n] = +inf

	while(low <= high){

		int mid = low - (low - high)/2; // mid = (l + h)/2

		if(x <= nums[mid]){
			// it's a possible ans & move search space to lower side
			// [l, mid-1]
			ans = mid;
			high = mid - 1;
		} else {
			// ignore the lower search space i.e. [mid + 1, h]
			low = mid + 1;
		}
	}

	// as per condition
	return ans == n ? -1 : nums[ans];
}
```

### 03-First and last occurrence

```java
// nums[i] == x, for smallest i
// nums = [2, 8, 8, 8, 8, 8, 11, 13]
// target = 8
public int[] searchRange(int[] nums, int target) {

	int first = firstOccurrence(nums, target);

	if(first == -1) return new int[]{-1, -1};

	int last = lastOccurrence(nums, target);

	return new int[]{first, last};

}

public int firstOccurrence(int[] nums, int target){

	int low = 0, high = nums.length - 1; // [0, n-1]
	int first = -1;

	while(low <= high) {
		int mid = low - (low - high)/2; // mid = (l + h)/2

		if(nums[mid] == target){

			// mid, could be a possible answer
			// move to low search space [low, mid - 1]

			first = mid;
			high = mid - 1;
		}

		else if(nums[mid] < target){
			low = mid + 1; // [mid + 1, high]
		}

		else {
			high = mid - 1; // [low, mid - 1]
		}
	}

	return first;
}

// nums[i] == x, for largest i;
public int lastOccurrence(int[] nums, int target){
	
	int low = 0, high = nums.length - 1; // [low, high]
	int last = -1;

	while(low <= high) {
		int mid = low - (low - high)/2; // m = (l + h)/2;

		if(nums[mid] == target){
			// mid, could be possible answer
			last = mid;
			
			// move to higher search space, ie. [mid + 1, h]
			low = mid + 1;
		}

		else if(nums[mid] < target){
			low = mid + 1;
		}

		else {
			high = mid - 1;
		}
	}

	return last;
}
```

### 04-Search in rotated sorted array-I

```java
// int[] nums = {7, 8, 9, 1, 2, 3, 4, 5, 6};
// int target = 1;
public int search(int[] nums, int target) {
	int low = 0, high = nums.length - 1;

	// Applying binary search algorithm 
	while (low <= high) {
		int mid = (low + high) / 2;

		// Check if mid points to the target
		if (nums[mid] == target) return mid;

		// Check if the left part is sorted
		if (nums[low] <= nums[mid]) {
			if (nums[low] <= target && target <= nums[mid]) {
				// Target exists in the left sorted part
				high = mid - 1;
			} else {
				// Target does not exist in the left sorted part
				low = mid + 1;
			}
		} else {
			// Check if the right part is sorted
			if (nums[mid] <= target && target <= nums[high]) {
				// Target exists in the right sorted part
				low = mid + 1;
			} else {
				// Target does not exist in the right sorted part
				high = mid - 1;
			}
		}
	}
	// If target is not found
	return -1;
}
```

### 05-Search in rotated sorted array - II

```java
// int[] nums = {7, 8, 1, 2, 3, 3, 3, 4, 5, 6};
// int k = 2;
// eg2:
// int[] nums = {3, 1, 2, 3, 3, 3, 3}
// int k = 2; 
public boolean searchInARotatedSortedArrayII(int[] nums, int k) {
	int n = nums.length;
	int low = 0, high = n - 1;
	
	// Applying binary search algorithm 
	while (low <= high) {
		int mid = (low + high) / 2;

		// Check if mid points to the target
		if (nums[mid] == k) return true;

		// Handle duplicates: if arr[low], arr[mid], and arr[high] are equal
		if (nums[low] == nums[mid] && nums[mid] == nums[high]) {
			low = low + 1;
			high = high - 1;
			continue;
		}

		// Check if the left part is sorted
		if (nums[low] <= nums[mid]) {
			/*  Eliminate the right part if target
				exists in the left sorted part */
			if (nums[low] <= k && k <= nums[mid]) {
				high = mid - 1;
			} 
			// Otherwise eliminate the left part
			else {
				low = mid + 1;
			}
		} else {
			/*  If the right part is sorted and
				target exists in the right sorted
				part, eliminate the left part   */
			if (nums[mid] <= k && k <= nums[high]) {
				low = mid + 1;
			} 
			// Otherwise eliminate the right part
			else {
				high = mid - 1;
			}
		}
	}
	// If target is not found
	return false;
}
```

### 06-Find minimum in Rotated sorted array

```java
// arr[] = [4, 5, 6, 7, 0, 1, 2]
//eg2: arr[] = [4, 5, 1, 2, 3]
//eg3: arr[] = [7, 8, 1, 2, 3, 4, 5, 6]
/* Function to find minimum element
in a rotated sorted array */
public int findMin(ArrayList<Integer> arr) {
	// Initialize low and high indices
	int low = 0, high = arr.size() - 1;
	
	// Initialize ans to maximum integer value
	int ans = Integer.MAX_VALUE;
	while (low <= high) {
		int mid = (low + high) / 2;
		
		// Check if left part is sorted
		if (arr.get(low) <= arr.get(mid)) {
			/* Update ans with minimum 
			of ans and arr[low] */
			ans = Math.min(ans, arr.get(low));
			
			// Move to the right part
			low = mid + 1;
		} else {
			/* Update ans with minimum 
				of ans and arr[mid] */
			ans = Math.min(ans, arr.get(mid));
			
			// Move to the left part
			high = mid - 1;
		}
	}
	// Return the minimum element found
	return ans;
}
```

### 07-Find out how many times the array is rotated

```java
// nums[] = [3, 4, 5, 1, 2]
public int findKRotation(ArrayList<Integer> nums) {
	int low = 0, high = nums.size() - 1;
	int ans = Integer.MAX_VALUE;
	int index = -1;
	while (low <= high) {
		int mid = (low + high) / 2;
		
		/* Search space is already sorted
			then nums.get(low) will always be
			the minimum in that search space */
		if (nums.get(low) <= nums.get(high)) {
			if (nums.get(low) < ans) {
				index = low;
				ans = nums.get(low);
			}
			break;
		}
		
		// If left part is sorted update the ans
		if (nums.get(low) <= nums.get(mid)) {
			if (nums.get(low) < ans) {
				index = low;
				ans = nums.get(low);
			}
			// Eliminate left half
			low = mid + 1;
		} else {
			/* update the ans if it 
				is less than nums.get(mid) */
			if (nums.get(mid) < ans) {
				index = mid;
				ans = nums.get(mid);
			}
			// Eliminate right half
			high = mid - 1;
		}
	}
	// Return the index as answer
	return index;
}
```

### 08-Single element in sorted array

```java
// int[] nums = {1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6};
public int singleNonDuplicate(int[] nums) {
	int n = nums.length; // Size of the array.

	// Edge cases:
	if (n == 1) return nums[0];
	if (nums[0] != nums[1]) return nums[0];
	if (nums[n - 1] != nums[n - 2]) return nums[n - 1];

	int low = 1, high = n - 2;
	while (low <= high) {
		int mid = (low + high) / 2;

		// If nums[mid] is the single element:
		if (nums[mid] != nums[mid + 1] && nums[mid] != nums[mid - 1]) {
			return nums[mid];
		}

		// We are in the left part:
		if ((mid % 2 == 1 && nums[mid] == nums[mid - 1])
			|| (mid % 2 == 0 && nums[mid] == nums[mid + 1])) {
			// Eliminate the left half:
			low = mid + 1;
		}
		// We are in the right part:
		else {
			// Eliminate the right half:
			high = mid - 1;
		}
	}

	// Dummy return statement:
	return -1;
}
```
## On Answers

### 01-Find square root of a number

```java
// n = 25
// eg2: n = 28
// Linear Approach
public int floorSqrt(int n) {

	int ans = 0;

	// Linear Search upper bound
	int high = n;
	
	/* CHANGE: Iterate linearly from 1 to n instead of Binary Search */
	for(int mid = 1; mid <= high; mid++){ 
		
		long val = (long)mid * (long)mid; // avoid overflow

		if(val <= n){
			/* If mid*mid is within limits, it's a possible answer.
			   We update ans and continue to check the next higher number. */
			ans = mid;
		} else {
			/* If val > n, we have crossed the square root. 
			   No need to check further. */
			break; 
		}
	}
	return ans;
}

```

```java
// binary Search
public int floorSqrt(int n) {

	int ans = 0;

	// BinarySearch : [0, n]
	int low = 0, high = n;
	
	while(low <= high){ // atleast an ele exists 
		int mid = low - (low - high)/2; // mid = (l + h)/2;
		
		long val = (long)mid * (long)mid; // avoid overflow
		if(val <= n){
			ans = mid;
			low = mid + 1; // [mid + 1, h]
		} else {
			high = mid - 1; // [l, mid - 1]
		}
	}
	return ans;
}
```

### 02-Find Nth root of a number (Incomplete)

```java
// b = 69, exp = 1/4
public long Pow(int b, int exp) {
	long ans = 1;
	long base = b;

	// Exponent squaring method
	while(exp > 0){
		if(exp % 2 == 1){
			exp--;
			ans *= base;
		} else {
			exp /= 2;
			base *= base;
		}
	}
	
	return ans;
}

```

```java
/**
	power is calculated using exponent square method.
	b^e : b * b^(e-1) if e is odd
		: (b^2)^(e/2) if e is even
	
	O(log n) to calculate pow, with this method
	[-1, 0, 1]
*/

public long powModify(int b, int exp, int m) {
	long ans = 1;
	long base = b;

	// Exponent squaring method
	while(exp > 0){
		if(exp % 2 == 1){
			ans *= base;
			if (ans > m) return 1; // Early exit
			exp--;
		} else {
			exp /= 2;
			base *= base;
			if (base > m) return 1;
		}
	}

	if (ans == m) return 0;

	return -1;
}

// LinearSearch:
public int NthRoot(int N, int M) {
	
	// Linear Search Range: [1, M]
	int low = 1, high = M;

	/* CHANGE: Iterate linearly from 1 up to M */
	for(int mid = low; mid <= high; mid++){

		// x^N, may not fit in a variable
		// Note: powModify returns: 0 (equal), 1 (greater), -1 (smaller)
		int midN = (int) powModify(mid, N, M);

		if(midN == 0){
			return mid; // Found exact root
		} else if (midN == 1){
			/* CHANGE: If mid^N > M (powModify returns 1), 
			   we have exceeded the target without finding it. */
			return -1; 
		} 
		// If midN == -1 (less than M), continue to next integer.
	}

	return -1;
}

```

```java
// binarySearch
public int NthRoot(int N, int M) {
	
	// BinarySearch; ss:[0, M]
	int low = 0, high = M;

	while(low <= high){
		int mid = low - (low - mid)/2; // mid = (l + h)/2;

		// x^N, may not fit in a variable
		int midN = powModify(mid, N, M);

		if(midN == 0){
			return mid; // Found exact root
		} else if (midN < 0){
			low = mid + 1; // [mid + 1, h]
		} else {
			high = mid - 1; // [l, mid - 1]
		}
	}

	return -1;
}
```

### 03-Find the smallest divisor (Incomplete)

```java
// int[] nums = [1, 2, 5, 9]
// limit = 7
// linear approach
public int smallestDivisor(int[] nums, int limit) {
   
	int n = nums.length;

	// sum(ceil(nums/mid)) -> [nums.length, sum(nums)]
	if(limit < n) {
		// limit < nums.length; isn't possible 
		return -1;
	}

	// O(logn) -> effectively O(max(nums)) in Linear Search
	int low = 1, high = findMax(nums);
	
	/* CHANGE: Iterate linearly from low (1) to high (max element).
	   We are looking for the smallest divisor 'mid'. */
	for(int mid = low; mid <= high; mid++){
		
		if( sumByD(nums, mid) <= limit ){
			/* If condition is met, this is the smallest possible divisor
			   because we are iterating upwards from 1. */
			return mid; 
		}
		// No 'else' block needed (no high/low adjustment)
	}

	return -1;
}

private int findMax(int[] v) {
	int maxi = Integer.MIN_VALUE;
	int n = v.length;

	// Find the maximum element
	for (int i = 0; i < n; i++) {
		maxi = Math.max(maxi, v[i]);
	}
	return maxi;
}

public int sumByD(int[] nums, int mid){
	int n = nums.length;

	int sum = 0;
	for(int i = 0; i < n; i++){
		sum += Math.ceil( (double)nums[i]/ (double)mid );
	}
	return sum;
}
```

```java
// int[] nums = [1, 2, 5, 9]
// limit = 7
public int smallestDivisor(int[] nums, int limit) {
   
	int n = nums.length;

	// sum(ceil(nums/mid)) -> [nums.length, sum(nums)]
	if(limit < n) {
		// limit < nums.length; isn't possible 
		return -1;
	}

	// O(logn)
	int low = 1, high = findMax(nums);
	int ans = maxEle; // always possible ans.

	// Apply Binary Search
	while(low <= high){
		int mid = low - (low - high)/2; // (l + h)/2

		if( sumByD(nums, mid) <= limit ){
			ans = mid; // possible ans 
			high = mid - 1; // increase sum, i.e. [l, mid - 1]
		} else {
			low = mid + 1; // decrease sum, i.e. [mid + 1, h]
		}
	}

	return ans;
}
```

### 04-Koko eating bananas

```java
// int[] nums = [3, 6, 7, 11];
// h = 8;

// Linear Search : [1, maxi] -> time: [high, low]
public int minimumRateToEatBananas(int[] nums, int h) {
	
	int maxi = findMax(nums);

	for (int i = 1; i <= maxi; i++) {
		long reqTime = calculateTotalHours(nums, i);
		if (reqTime <= (long) h) {
			return i;
		}
	}

	return maxi;
}

// sum(ceil(nums/hourly))
private long calculateTotalHours(int[] v, int hourly) {
	long totalH = 0;
	int n = v.length;

	for (int i = 0; i < n; i++) {
		totalH += Math.ceil((double) v[i] / (double) hourly);
	}
	return totalH;
}

private int findMax(int[] v) {
	int maxi = Integer.MIN_VALUE;
	int n = v.length;

	// Find the maximum element
	for (int i = 0; i < n; i++) {
		maxi = Math.max(maxi, v[i]);
	}
	return maxi;
}
```

```java
// int[] nums = [3, 6, 7, 11];
// h = 8;
// Binary Search:
public int minimumRateToEatBananas(int[] nums, int h) {
	
	int low = 1, high = findMax(nums);

	// Apply binary search
	while (low <= high) {
		int mid = (low + high) / 2;
		long totalH = calculateTotalHours(nums, mid);
		if (totalH <= h) { // accepted case
			high = mid - 1; // move to lower side
		} else {
			low = mid + 1; // move to higher side
		}
	}
	return low;
}
```

### 05-Minimum days to make M bouquets

```java

// int[] nums = {7, 7, 7, 7, 13, 11, 12, 7};
// m = 2, k = 3 

// LinearSearch
public int roseGarden(int n, int[] nums, int k, int m) {
	
	long val = (long) m * k; // flowers needed to complete bouquet
	
	if (val > n) return -1; // can't get needed flowers, so no bouquet 
	
	int mini = Integer.MAX_VALUE, maxi = Integer.MIN_VALUE;
	for (int i = 0; i < n; i++) {
		mini = Math.min(mini, nums[i]); 
		maxi = Math.max(maxi, nums[i]); 
	}

	// LinearSearch: [mini, maxi]
	for (int i = mini; i <= maxi; i++) {
		if (possible(nums, i, m, k))
			return i; // returns possible day
	}
	
	return -1; // returns even after max day we can't make bouquet
}

private boolean possible(int[] nums, int day, int m, int k) {
	int n = nums.length; 
	
	// Count of flowers bloomed
	int cnt = 0; 
	
	// Count of bouquets formed
	int noOfB = 0; 

	// Count number of bouquets that can be formed
	for (int i = 0; i < n; i++) {
		if (nums[i] <= day) {
			// Increment flower count
			cnt++; 
		} else {
			/* Calculate number of bouquets
			formed with flowers <= day */
			noOfB += (cnt / k);
			
			// Reset flower count
			cnt = 0; 
		}
	}
	// Add remaining flowers as a bouquet
	noOfB += (cnt / k); 

	/* Return true if enough 
	bouquets can be formed */
	return noOfB >= m; 
}
```

```java
// int[] nums = {7, 7, 7, 7, 13, 11, 12, 7};
// m = 2, k = 3 
// binarySearch
public int roseGarden(int n, int[] nums, int k, int m) { // might be duplicate
	
	long val = (long) m * k; // flowers needed to complete bouquet 
	
	if (val > n) return -1; // can't get needed flowers, so no bouquet 

	int mini = Integer.MAX_VALUE, maxi = Integer.MIN_VALUE;
	for (int i = 0; i < n; i++) {
		mini = Math.min(mini, nums[i]); 
		maxi = Math.max(maxi, nums[i]); 
	}

	// BinarySearch : [mini, maxi]
	int left = mini, right = maxi, ans = -1;
	while (left <= right) {
		
		int mid = left + (right - left) / 2; // mid
		
		if (possible(nums, mid, m, k)) { // mid accepted.
			ans = mid; // possible ans 
			right = mid - 1; // move to lower side
		} else {
			left = mid + 1; // won't possible, move to higher side
		}
	}
	
	return ans; // return the most possible answer, or -1;
}
```

## FAQs
### 01-Aggressive Cows

```java
// nums = [0, 3, 4, 7, 10, 9]
// k = 4

// LinearSearch:
public int aggressiveCows(int[] nums, int k) {
    int n = nums.length;
    Arrays.sort(nums); // sort the given array.

    int maxLimit = nums[n - 1] - nums[0];

    //Range of possible dist is [1, (max - min)]
    for (int dist = 1; dist <= maxLimit; dist++) {
        
        /* Check if it is possible to place cows with 'dist' gap. */
        if (canWePlace(nums, dist, k) == false) {
            /* CRITICAL LOGIC: 
               If 'dist' fails, it means the gap is too wide.
               Therefore, the *previous* distance (dist - 1) 
               was the largest valid one. */
            return dist - 1;
        }
    }

    return maxLimit;
}

// Focus to learn the below helper method.
public boolean canWePlace(int[] nums, int dist, int cows){
	int n = nums.length;

	int cntCows = 1; // first cow placed at nums[0]
	int last = nums[0]; // tracking it's position.

	for(int i = 1; i < n; i++){	

		// is good to place cow here
		if(nums[i] - last >= dist){            
			cntCows++; // place cow
			last = nums[i]; // update last position
		}

		// place all cows or more cows it's acceptable.
		if(cntCows >= cows){ 
			return true;
		}
	}

	return false;
}
```

```java
// nums = [0, 3, 4, 7, 10, 9]
// k = 4

// BinarySearch:
public int aggressiveCows(int[] nums, int k) {
	
	int n = nums.length;
	
	Arrays.sort(nums); // sort the given array.

	//Range of possible dist is [1, (max - min)]
	int low = 1;
	int high = nums[n - 1] - nums[0];

	int ans = 1;

	while(low <= high){
		int mid = low - (low - high)/2;
		if (canWePlace(nums, mid, k) == true){
			// it's a possible ans & move to higher side, since we need max of possible ans
			ans = mid;
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}

	return high;
}
```

### 02-Book Allocation Problem

```java
// int[] nums = [25, 46, 28, 49, 24]
// m = 4

// Linear Search:
public int findPages(int[] nums, int m) {
	
	int n = nums.length;

	// if students > Books, allocation isn't possible.
	if (m > n) return -1;

	// range: [max(nums), sum(nums)]
	int low = Integer.MIN_VALUE; // -inf
	int high = 0;
	for(int i = 0; i < n; i++){
		low = Math.max(low, nums[i]);
		high += nums[i];
	}

	/* CHANGE: Iterate linearly from low (min possible max pages) to high (sum).
	   We look for the first 'mid' that allows allocation to <= m students. */
	for(int mid = low; mid <= high; mid++){
		int students = countStudents(nums, mid);
		if(students <= m){ 
			/* If students needed is within limit m, return current mid immediately.
			   Since we are iterating upwards, the first valid one is the minimum. */
			return mid;
		}
	}

	return low;
}

public int countStudents(int[] nums, int total){
	int n = nums.length;

	int student = 1;
	int pages = 0; // started with empty pages.

	for(int i = 0; i < n; i++){
		if(pages + nums[i] <= total){
			// student accepting incoming pages.
			pages += nums[i];
		} else {
			student++; // move to next student
			pages = nums[i]; // assign incoming pages to this student.
		}
	}
	return student;
}
```

```java
// int[] nums = [25, 46, 28, 49, 24]
// m = 4

// Binary Search:
public int findPages(int[] nums, int m) {
	
	int n = nums.length;

	// if students > Books, allocation isn't possible.
	if (m > n) return -1;

	// range: [max(nums), sum(nums)]
	int low = Integer.MIN_VALUE; // -inf
	int high = 0;
	for(int i = 0; i < n; i++){
		low = Math.max(low, nums[i]);
		high += nums[i];
	}

	int ans = low;

	while(low <= high){
		int mid = low - (low - high)/2;
		int students = countStudents(nums, mid);
		if(students > m){ // pages remained.
			// increase threshold.
			low = mid + 1;
		} else { // pages got allocated.
			ans = mid;
			// decrease threshold.
			high = mid - 1;
		}
	}
	return ans;
}
```

### 03-Find peak element

```java
// int[] arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
// eg2: int[] arr = [1, 2, 1, 3, 5, 6, 4]
public int findPeakElement(int[] arr) {
	int n = arr.length;

	if(n == 1) return 0;
	if(arr[0] > arr[1]) return 0;
	if(arr[n - 2] < arr[n - 1]) return n - 1;

	int low = 1;
	int high = n - 2;

	while(low <= high){
		int mid = low - (low - high)/2;

		if(arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1]){
			return mid;
		} else if ( arr[mid - 1] < arr[mid]) {
			low = mid + 1;
		} else { // arr[mid - 1] > arr[mid]
			high = mid - 1;
		}
	}

	return -1;
}
```

### 04-Median of 2 sorted arrays

```java
// int[] arr1 = [1, 3, 4, 7, 10, 12];
// int[] arr2 = [2, 3, 6, 15];

// eg2:
// int[] arr1 = [7, 12, 14, 15]
// int[] arr2 = [1, 2, 3, 4, 9, 11]

// linearSearch:
//Function to find the median of two sorted arrays.
public double median(int[] arr1, int[] arr2) {
	// Size of two given arrays
	int n1 = arr1.length, n2 = arr2.length;

	/* Ensure arr1 is not larger than 
	arr2 to simplify implementation*/
	if (n1 > n2) return median(arr2, arr1);

	int n = n1 + n2;
	
	// Length of left half
	int left = (n1 + n2 + 1) / 2; 

	/* CHANGE: Instead of Binary Search (low/high), 
	we iterate linearly through every possible partition of arr1 */
	for (int mid1 = 0; mid1 <= n1; mid1++) {
		
		// Calculate mid index for arr2
		int mid2 = left - mid1; 

		// Calculate l1, l2, r1, and r2
		int l1 = (mid1 > 0) ? arr1[mid1 - 1] : Integer.MIN_VALUE;
		int r1 = (mid1 < n1) ? arr1[mid1] : Integer.MAX_VALUE;
		int l2 = (mid2 > 0) ? arr2[mid2 - 1] : Integer.MIN_VALUE;
		int r2 = (mid2 < n2) ? arr2[mid2] : Integer.MAX_VALUE;

		if (l1 <= r2 && l2 <= r1) {
			// If condition for finding median
			if (n % 2 == 1) return Math.max(l1, l2);
			else return (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
		} 
		// Removed 'else if' blocks for binary elimination; loop continues linearly
	}
	// Dummy statement
	return 0; 
}
```

```java
// int[] arr1 = [1, 3, 4, 7, 10, 12];
// int[] arr2 = [2, 3, 6, 15];

// eg2:
// int[] arr1 = [7, 12, 14, 15]
// int[] arr2 = [1, 2, 3, 4, 9, 11]

// binarySearch:
//Function to find the median of two sorted arrays.
public double median(int[] arr1, int[] arr2) {
	// Size of two given arrays
	int n1 = arr1.length, n2 = arr2.length;

	/* Ensure arr1 is not larger than 
	arr2 to simplify implementation*/
	if (n1 > n2) return median(arr2, arr1);

	int n = n1 + n2;
	
	// Length of left half
	int left = (n1 + n2 + 1) / 2; 

	// Apply binary search
	int low = 0, high = n1;
	while (low <= high) {
		
		// Calculate mid index for arr1
		int mid1 = (low + high) >>> 1; 
		
		// Calculate mid index for arr2
		int mid2 = left - mid1; 

		// Calculate l1, l2, r1, and r2
		int l1 = (mid1 > 0) ? arr1[mid1 - 1] : Integer.MIN_VALUE;
		int r1 = (mid1 < n1) ? arr1[mid1] : Integer.MAX_VALUE;
		int l2 = (mid2 > 0) ? arr2[mid2 - 1] : Integer.MIN_VALUE;
		int r2 = (mid2 < n2) ? arr2[mid2] : Integer.MAX_VALUE;

		if (l1 <= r2 && l2 <= r1) {
			// If condition for finding median
			if (n % 2 == 1) return Math.max(l1, l2);
			else return (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
		} 
		else if (l1 > r2) {
			// Eliminate the right half of arr1
			high = mid1 - 1;
		} else {
			// Eliminate the left half of arr1
			low = mid1 + 1;
		}
	}
	// Dummy statement
	return 0; 
}
```

### 05-Kth element of 2 sorted arrays

```java
// int[] a = [2, 3, 6, 7, 9], int[] b = [1, 4, 8, 10], k = 4
// LinearSearch
public int kthElement(int[] a, int[] b, int k) {
    int m = a.length;
    int n = b.length;

    // Ensure a is smaller array for optimization
    if (m > n) {
        // Swap a and b
        return kthElement(b, a, k); 
    }
    
    // Length of the left half
    int left = k; 

    /* CHANGE: Iterate linearly through the valid range of partitions for 'a'.
       We start from the minimum necessary elements in 'a' up to the maximum possible. */
    int start = Math.max(0, k - n), end = Math.min(k, m);
    
    for (int mid1 = start; mid1 <= end; mid1++) {
        
        int mid2 = left - mid1;

        // Initialize l1, l2, r1, r2
        int l1 = (mid1 > 0) ? a[mid1 - 1] : Integer.MIN_VALUE;
        int l2 = (mid2 > 0) ? b[mid2 - 1] : Integer.MIN_VALUE;
        int r1 = (mid1 < m) ? a[mid1] : Integer.MAX_VALUE;
        int r2 = (mid2 < n) ? b[mid2] : Integer.MAX_VALUE;

        // Check if we have found the answer
        if (l1 <= r2 && l2 <= r1) {
            return Math.max(l1, l2);
        } 
        // Removed binary search 'else if' blocks as we are just incrementing linearly
    }
    
     // Dummy return statement 
    return -1;
}
```

```java
// int[] a = [2, 3, 6, 7, 9], int[] b = [1, 4, 8, 10], k = 4
// binarySearch
public int kthElement(int[] a, int[] b, int k) {
    int m = a.length;
    int n = b.length;

    // Ensure a is smaller array for optimization
    if (m > n) {
        // Swap a and b
        return kthElement(b, a, k); 
    }
    
    // Length of the left half
    int left = k; 

    // Apply binary search
    int low = Math.max(0, k - n), high = Math.min(k, m);
    while (low <= high) {
        int mid1 = (low + high) >> 1;
        int mid2 = left - mid1;

        // Initialize l1, l2, r1, r2
        int l1 = (mid1 > 0) ? a[mid1 - 1] : Integer.MIN_VALUE;
        int l2 = (mid2 > 0) ? b[mid2 - 1] : Integer.MIN_VALUE;
        int r1 = (mid1 < m) ? a[mid1] : Integer.MAX_VALUE;
        int r2 = (mid2 < n) ? b[mid2] : Integer.MAX_VALUE;

        // Check if we have found the answer
        if (l1 <= r2 && l2 <= r1) {
            return Math.max(l1, l2);
        } 
        else if (l1 > r2) {
            // Eliminate the right half
            high = mid1 - 1;
        } 
        else {
            // Eliminate the left half
            low = mid1 + 1;
        }
    }
    
     // Dummy return statement 
    return -1;
}
```

### 06-Minimize Max Distance to Gas Station

```java
// arr[] = [1, 2, 3, 4, 5], k = 4

// Linear Search
/* Function to minimize the maximum 
distance between gas stations */
public double minimiseMaxDistance(int[] arr, int k) {
    int n = arr.length; 
    double high = 0;

    /* Find the maximum distance between
    consecutive gas stations (Upper Bound) */
    for (int i = 0; i < n - 1; i++) {
        high = Math.max(high, (double)arr[i + 1] - arr[i]);
    }

    /* CHANGE: Instead of Binary Search (halving the range),
       we iterate linearly from 0 upwards by the precision step. */
    
    // The precision step (step size)
    double step = 1e-6; 

    // We start from a very small distance and increase it
    for (double dist = step; dist <= high; dist += step) {
        
        int cnt = numberOfGasStationsRequired(dist, arr);

        /* If the number of stations required is within our limit k,
           this is the smallest (minimum) valid max distance. */
        if (cnt <= k) {
            return dist;
        }
    }

    return high;
}

private int numberOfGasStationsRequired(double dist, int[] arr) {
	// Size of the array
	int n = arr.length;
	int cnt = 0;
	for (int i = 1; i < n; i++) {
		
		/* Calculate number of gas stations
		needed between two points*/
		int numberInBetween = (int) ((arr[i] - arr[i - 1]) / dist);

		// Adjust if exact distance fits perfectly
		if ((arr[i] - arr[i - 1]) == (dist * numberInBetween)) {
			numberInBetween--;
		}

		cnt += numberInBetween;
	}
	return cnt;
}
```

```java
// arr[] = [1, 2, 3, 4, 5], k = 4

// BinarySearch
public double minimiseMaxDistance(int[] arr, int k) {
	int n = arr.length; 
	double low = 0;
	double high = 0;

	/* Find the maximum distance between
	consecutive gas stations*/
	for (int i = 0; i < n - 1; i++) {
		high = Math.max(high, arr[i + 1] - arr[i]);
	}

	/* Apply Binary search to find the 
	minimum possible maximum distance*/
	double diff = 1e-6;
	while (high - low > diff) {
		double mid = (low + high) / 2.0;
		int cnt = numberOfGasStationsRequired(mid, arr);

		/* Adjust the search range based on
		the number of gas stations required*/
		if (cnt > k) {
			low = mid;
		} else {
			high = mid;
		}
	}

	// Return smallest maximum distance found
	return high;
}
```

### 07-Split array - largest sum

```java
// arr[] = [10, 20, 30, 40], k = 2

// Linear Search
public int largestSubarraySumMinimized(int[] a, int k) {
    
    int low = a[0];
    int high = 0;
    
    // Find maximum and summation (Bounds calculation)
    for (int i = 0; i < a.length; i++) {
        low = Math.max(low, a[i]);
        high += a[i];
    }

    /* CHANGE: Iterate linearly from the lowest possible answer ('low')
       up to the highest ('high'). */
    for (int mid = low; mid <= high; mid++) {
        
        int partitions = countPartitions(a, mid);

        /* CHANGE: The first time we find a sum that allows 
           partitions <= k, that is our minimum possible max-sum. */
        if (partitions <= k) {
            return mid;
        }
        // No 'else' block needed; just continue to the next number
    }

    return low;
}

private int countPartitions(int[] a, int maxSum) {
	int n = a.length;
	int partitions = 1;
	long subarraySum = 0;

	for (int i = 0; i < n; i++) {
		if (subarraySum + a[i] <= maxSum) {
			// Add element to the current subarray
			subarraySum += a[i];
		} else {
			// Start a new subarray with current element
			partitions++;
			subarraySum = a[i];
		}
	}

	return partitions;
}
```

```java
// arr[] = [10, 20, 30, 40], k = 2

// BinarySearch
public int largestSubarraySumMinimized(int[] a, int k) {
	
	// Initialize binary search boundaries
	int low = a[0];
	int high = 0;
	
	//Find maximum and summation
	for (int i = 0; i < a.length; i++) {
		low = Math.max(low, a[i]);
		high += a[i];
	}
	// Apply binary search
	while (low <= high) {
		int mid = (low + high) / 2;
		int partitions = countPartitions(a, mid);

		if (partitions > k) {
			/* If partitions exceed k, increase
			the minimum possible subarray sum*/
			low = mid + 1;
		} 
		else {
			/* If partitions are within k, try to
			minimize the subarray sum further*/
			high = mid - 1;
		}
	}

	/* After binary search, 'low' will 
	be the largest minimum subarray sum
	with at most k partitions*/
	return low;
}
```

## 2D Arrays

### 01-Find row with maximum 1's

```java
/* int[][] mat = [
	[0, 0, 1, 1, 1],
	[0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1],
	[0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1]
]
*/

public int rowWithMax1s(int[][] mat) {
	int n = mat.length;
	int m = mat[0].length;
	
	/* Variable to store the 
	maximum count of 1's found*/
	int cnt_max = 0; 
	
	/* Variable to store the index
	of the row with max 1's*/
	int index = -1;  

	// Traverse each row of the matrix
	for (int i = 0; i < n; i++) {
		// Get the number of 1's
		int cnt_ones = m - lowerBound(mat[i], m, 1);
		
		/* If the current count is greater than 
		maximum, store the index of current row
		and update the maximum count.*/
		if (cnt_ones > cnt_max) {
			cnt_max = cnt_ones;
			index = i;
		}
	}

	/* Return the index of the row 
	with the maximum number of 1's*/
	return index;
}

// Helper function to find the lower bound of 1.
private int lowerBound(int[] arr, int n, int x) {
	int low = 0, high = n - 1;
	int ans = n;

	while (low <= high) {
		int mid = (low + high) / 2;
		
		/* If element at mid is greater than or equal 
		to x then it counld be a possible answer.*/
		if (arr[mid] >= x) {
			ans = mid;
			
			// Look for smaller index on the left
			high = mid - 1;
		} else {
			low = mid + 1;
		}
	}
	// Return the answer
	return ans;
}
```

### 02-Search in a 2D matrix

```java
/* int[][] matrix = [
	[3, 4, 7, 9],
	[12, 13, 14, 18],
	[20, 21, 23, 29]
]
int target = 23;
*/
// Function to search for a given target in matrix
public boolean searchMatrix(int[][] mat, int target) {
	int n = mat.length;
	int m = mat[0].length;

	int low = 0, high = n * m - 1;
	
	// Perform binary search
	while (low <= high) {
		int mid = (low + high) / 2;
		
		// Calculate the row and column
		int row = mid / m;
		int col = mid % m;
		
		// If target is found return true
		if (mat[row][col] == target) return true;
		else if (mat[row][col] < target) low = mid + 1;
		else high = mid - 1;
	}
	
	// Return false if target is not found
	return false; 
}
```

### 03-Search in 2D matrix - II

```java
/**
int[][] matrix = [
	[1, 4, 7, 11, 15],
	[2, 5, 8, 12, 19],
	[3, 6, 9, 16, 22],
	[10, 13, 14, 17, 24],
	[18, 21, 23, 26, 30]
];
int target = 8;
*/

// Function to search for a given target in matrix
public boolean searchMatrix(int[][] matrix, int target) {
	int n = matrix.length;
	int m = matrix[0].length;
	
	// Initialize the row and col
	int row = 0, col = m - 1;

	// Traverse the matrix from (0, m-1):
	while (row < n && col >= 0) {
		
		// Return true if target is found
		if (matrix[row][col] == target) return true;
		else if (matrix[row][col] < target) row++;
		else col--;
	}
	// Return false if target not found
	return false;
}
```

### 04-Find Peak Element - II

```java
/**
// Example usage
int[][] arr = [
	[4, 2, 5, 1, 4, 5],
	[2, 9, 3, 2, 3, 2],
	[1, 7, 6, 0, 1, 3],
	[3, 6, 2, 3, 7, 2]
];
*/

/* Function to find a peak element in 
the 2D matrix using binary search */
public int[] findPeakGrid(int[][] arr) {
	int n = arr.length;   
	int m = arr[0].length; 
	
	/* Initialize the lower bound for 
	and upper bound for binary search */
	int low = 0;           
	int high = m - 1;      
	
	// Perform binary search on columns
	while (low <= high) {
		int mid = (low + high) / 2;  
		
		/* Find the index of the row with the 
		maximum element in the middle column*/
		int row = maxElement(arr, mid);
		
		/* Determine the elements to left and 
		right of middle element in the found row */
		int left = mid - 1 >= 0 ? arr[row][mid - 1] : Integer.MIN_VALUE;
		int right = mid + 1 < m ? arr[row][mid + 1] : Integer.MIN_VALUE;
		
		/* Check if the middle element 
		is greater than its neighbors */
		if (arr[row][mid] > left && arr[row][mid] > right) {
			return new int[]{row,mid};  
		} 
		else if (left > arr[row][mid]) {
			high = mid - 1;  
		} 
		else {
			low = mid + 1;
		}
	}
	
	// Return -1 if no peak element is found
	return new int[]{-1,-1};  
}

/* Helper function to find the index of the row
with the maximum element in a given column*/
public int maxElement(int[][] arr, int col) {
	int n = arr.length;
	int max = Integer.MIN_VALUE;
	int index = -1;
	
	/* Iterate through each row to find the
	maximum element in the specified column*/
	for (int i = 0; i < n; i++) {
		if (arr[i][col] > max) {
			max = arr[i][col];
			index = i;
		}
	}
	//Return the index
	return index; 
}
```

### 05-Matrix Median

```java
/**
int[][] matrix = [
	[1, 5, 7, 9, 11],
	[2, 3, 4, 5, 10],
	[9, 10, 12, 14, 16]
];
*/

// Brute force Approach
public int findMedian(int[][] matrix) {
	// Step 1: Flatten the matrix into a list
	List<Integer> flattened = new ArrayList<>();
	for (int[] row : matrix) {
		for (int val : row) {
			flattened.add(val);
		}
	}

	// Step 2: Sort the list
	Collections.sort(flattened);

	// Step 3: Return the middle element
	int n = flattened.size();
	return flattened.get(n / 2);
}

// Binary Search
// Function to find the median element in the matrix
public int findMedian(int[][] matrix) {
	int n = matrix.length; // Number of rows
	int m = matrix[0].length; // Number of columns

	int low = Integer.MAX_VALUE, high = Integer.MIN_VALUE;

	// Initialize low and high
	for (int i = 0; i < n; i++) {
		low = Math.min(low, matrix[i][0]);
		high = Math.max(high, matrix[i][m - 1]);
	}

	int req = (n * m) / 2;

	// Perform binary search to find the median
	while (low <= high) {
		int mid = low + (high - low) / 2;

		int smallEqual = countSmallEqual(matrix, n, m, mid);

		if (smallEqual <= req) low = mid + 1;
		else high = mid - 1;
	}

	return low;
}

// Function to find the upper bound of an element in a sorted row
private int upperBound(int[] arr, int x, int m) {
	int low = 0, high = m - 1;
	int ans = m;

	// Apply binary search
	while (low <= high) {
		int mid = (low + high) / 2;

		// If arr[mid] > x, it can be a possible upper bound
		if (arr[mid] > x) {
			ans = mid;
			// Look for a smaller upper bound on the left
			high = mid - 1;
		} else {
			low = mid + 1;
		}
	}

	return ans;
}

// Function to count how many elements in the matrix are less than or equal to x
private int countSmallEqual(int[][] matrix, int n, int m, int x) {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		cnt += upperBound(matrix[i], x, m);
	}
	return cnt;
}
```
