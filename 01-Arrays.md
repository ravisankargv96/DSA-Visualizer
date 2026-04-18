## Fundamentals
### [[01-Linear Search]]
```java
/**
int[] nums = {2, 3, 4, 5, 3};
int target = 3;
int target = 6; // not found
*/
public int linearSearch(int[] nums, int target){
	// Traverse the entire array, check if you found target
	for(int i = 0; i < nums.length; i++){
		if(nums[i] == target){
			return i;
		}
	}

	return -1; // not found	 
}
```

### [[02-Largest Element]]
```java
// int[] nums = {3,2,1,5,2};
public int maxElement(int[] nums, int target){
	int maxi = Integer.MIN_VALUE; // -inf

	// Traverse through array eles, if ele > maxi, update maxi;
	for(int i = 0; i < nums.length; i++){
		if(nums[i] > maxi){
			maxi = nums[i];
		}
	}

	return maxi;
}
```

### [[03-Second Largest Element]]
```java
// int[] nums = {1, 2, 4, 7, 7, 5};
public int secondLargestElement(int[] nums){
	int maxi1 = Integer.MIN_VALUE; // -inf
	int maxi2 = Integer.MIN_VALUE; // -inf

	// Iterating through nums
	for(int i = 0; i < nums.length; i++){
		if(nums[i] > maxi1){
			maxi2 = maxi1;
			maxi1 = nums[i];
		} else if(maxi1 > nums[i] && nums[i] > maxi2){
			maxi2 = nums[i];
		}
	}
	return maxi2;
}
```

### [[04-Maximum Consecutive Ones]]
```java
// int[] nums = {1, 1, 0, 1, 1, 1, 0, 1, 1};
public int findMaxConsecutiveOnes(int[] nums){

	int cnt = 0;
	int maxi = 0;

	// Traverse the array
	for(int i = 0; i < nums.length; i++){
		if(nums[i] == 1){
			cnt++;   // incr counter, if encountered 1
			maxi = Math.max(maxi, cnt);
		} else {
			cnt = 0; // reset counter, if encountered 0
		}
	}

	return maxi;
}
```

### [[05-Left Rotate Array by One]]
```java
// int[] nums = {1, 2, 3, 4, 5};
public void rotateArrayByOne(int[] nums){
	// store the first num;
	int store = nums[0];

	// Overrite i-1th ele
	for(int i = 1; i < nums.length; i++){
		nums[i-1] = nums[i];
	}

	// place first ele at end.
	nums[nums.length - 1] = store;
}
```

### [[06-Left Rotate Array by K Places]]
```java
// int[] nums = {1, 2, 3, 4, 5, 6, 7};
// int k = 3;
// int k = 7, 8, 9, 15; k = k % n
public void rotateArray(int[] nums, int k){
	int n = nums.length;
	k = k % n; // to avoid unnecessary rotations.

	// reverse first k elems
	// reverse remaining elements
	// reverse whole array.

	reverse(nums, 0, k -1);
	reverse(nums, k, n - 1);
	reverse(nums, 0, n - 1);
}

public void reverse(int[] nums, int low, int high){
	while(low < high){
		// swap
		int copy = nums[low];
		nums[low] = nums[high];
		nums[high] = copy;

		// move pointers farward
		low++;
		high--;
	}
}

```


## Logic Building

### [[01-Move Zeros to End]]
```java
// int[] arr = {1, 0, 2, 3, 2, 0, 0, 4, 5, 1};
public void moveZeroes(int[] nums){
	int left = 0; 

	for(int i = 0; i < nums.length; i++){
		if(nums[i] != 0){
			swap(nums, left, i);
			left++;
		}
	}

	// Fill the remaining elements with zeros, if needed.
	while (left < nums.length){
		nums[left] = 0;
		left++;
	}
}
```


### [[02-Remove duplicates]]
```java
// int[] nums = {1, 1, 2, 2, 2, 3, 3};
public int removeDuplicates(int[] nums){
	int left = 1;

	for(int i = 1; i < nums.length; i++){
		if(nums[i-1] == nums[i]){
			continue;
		} else {
			nums[left] = nums[i];
			left++;
		}
	}

	return i + 1;
}
```

### [[03-Find Missing Number]]
```java
// int[] nums = {1, 2, 4, 5};
// N = 5

public int missingNumber(int[] nums){
	int xor = 0;
	for(int i = 0; i < nums.length; i++){
		xor ^= nums[i];
	}
	for(int i = 0; i <= nums.length; i++){
		xor ^= i;
	}
	return xor;
}
```


### [[04-Union of two sorted Arrays]]
```java
/**
int[] nums1 = {1, 1, 2, 3, 4, 5};
int[] nums2 = {2, 3, 4, 4, 5, 6};
*/

public int[] unionArray(int[] nums1, int[] nums2){
	List<Integer> UnionList = new ArrayList<>();

	int i = 0, j = 0;
	int m = nums1.length;
	int n = nums2.length;

	while(i < m && j < n){ // both pointers are in Array
		if(nums1[i] < nums2[j]){
			UnionList.add(nums1[i]); // push smaller number.

			// move i to next unique number.
			i++;
			while(i < m && nums1[i - 1] == nums1[i]){
				i++;
			}
		} else if(nums2[j] < nums1[i]){
			UnionList.add(nums2[j]); // push smaller number.

			// move j to next unique number.
			j++;
			while(j < n && nums2[j-1] == nums2[j]){
				j++;
			}
		} else {
			UnionList.add(nums1[i]);

			// move i to next unique number.
			i++;
			while(i < m && nums1[i - 1] == nums1[i]){
				i++;
			}

			// move j to next unique number.
			j++;
			while(j < n && nums2[j-1] == nums2[j]){
				j++;
			}
		}
	}


	while(i < m){
		UnionList.add(nums1[i]);

		// move i to next unique nums1[i]
		i++;
		while(i < m && nums1[i-1] == nums1[i]){
			i++;
		}
	}

	while(j < n){
		UnionList.add(nums2[j]);

		// move j to next unique nums2[j]
		j++;
		while(j < n && nums2[j - 1] == nums2[j]){
			j++;
		}
	}

	// Converting arraylist to array.
	int[] res = new int[arr.size()];

	for(int k = 0; k < arr.size(); k++){
		res[k] = arr.get(k);
	}

	return res;
}
```

### [[05-Intersection of two sorted arrays]]
```java
/**
int[] nums1 = {1, 2, 2, 3, 3, 4, 5, 6};
int[] nums2 = {2, 3, 3, 5, 6, 6, 7};
*/

// Here repeated values are also considered
public int[] intersectionArray(int[] nums1, int[] nums2){
	List<Integer> interSecList = new ArrayList<>();

	int i = 0; j = 0;

	int m = nums1.length;
	int n = nums2.length;

	while(i < m && j < n) {
		if(nums1[i] < nums2[j]){
			i++;

			// while(i < m && nums1[i-1] == nums1[i]){
			//	i++;
			// }
		} else if(nums2[j] < nums1[i]){
			j++;
			// while(j < n && nums2[j - 1] == nums2[j]){
			//	j++;
			// }
		} else {
			// both equal
			interSecList.add(nums1[i]);

			i++;
			j++;
		}
	}

	// convert the res to int[] arr.
	int[] res = new int[arr.size()];
	for(int k = 0; k < arr.size(); k++){
		res[k] = arr.get(k);
	}

	return res;
}
```

## FAQs Medium

### [[01-Leaders in an Array]]
```java
// int[] nums = {10, 22, 12, 3, 0, 6};
public ArrayList<Integer> leaders(int[] nums){
	ArrayList<Integer> ans = new ArrayList<>();

	int maxi = Integer.MIN_VALUE; // -inf

	// Traversing array from backwards.
	for(int i = nums.length - 1; i >= 0; i++){
		if(nums[i] > maxi){ // encounterd a ele > maxi
			ans.add(nums[i]);
			maxi = nums[i];
		} else { // ignore if !(ele > maxi)
			continue;
		}
	}

	// reverse the ans & return.
	Collections.reverse(ans); // reverse(ans)
	return ans;
}
```

### [[02-Rearrange array elements by sign]]
```java
// int[] nums = {3, 1, -2, -5, 2, -4};
public int[] rearrangeArray(int[] nums) {

	if(nums == null || nums.length == 0){
		return nums;
	}

	// nums.length >= 1

	int n = nums.length;
	int[] res = new int[n];

	int pInd = 0;
	int nInd = 1;

	for(int ele: nums){
		if(ele > 0){
			res[pInd] = ele;
			pInd += 2;
		} else if(ele < 0){
			res[nInd] = ele;
			nInd += 2;
		} else {
			continue; // redundant
		}
	}

	return res;
}
```

### [[03-Print the matrix in spiral manner]]

```java
/**
int[][] mat = {
            {1, 2, 3, 4, 5, 6},
            {20, 21, 22, 23, 24, 7},
            {19, 32, 33, 34, 25, 8},
            {18, 31, 36, 35, 26, 9},
			{17, 30, 29, 28, 27, 10},
			{16, 15, 14, 13, 12, 11}
        };
*/
public List<Integer> spiralOrder(int[][] matrix) {
	List<Integer> res = new ArrayList<>();

	// Get Dimensions
	int m = matrix.length;
	int n = matrix[0].length;

	// Init pointers
	int left = 0, right = n - 1;
	int top = 0;
	int bottom = m - 1;

	int dir = 0;
	
	while(top <= bottom && left <= right){ // wrapper loop
		
		if(dir == 0){ // Traverse from left to right

			// i.e. m[top][]; i->[left, right]
			for(int i = left; i <= right; i++){
				res.add(matrix[top][i]);
			}
			top++; // fixed moves closer

			dir = 1;
		} else if(dir == 1) { // Traverse from top to bottom
			
			// i.e. m[][right]; i->[top, bottom]
			for(int i = top; i <= bottom; i++){
				res.add(matrix[i][right]);
			}
			right--; // fixed moves closer
			
			dir = 2;
		} else if(dir == 2) { // Traverse from right to left
			
			// i.e. m[bottom][]; i->[right, left]
			for(int i = right; i >= left; i--){
				res.add(matrix[bottom][i]);
			}
			bottom--; // fixed moves closer

			dir = 3;
		} else if(dir == 3){ // Traverse from bottom to top
		
			// i.e. m[][left]; i -> [bottom, top]
			for(int i = bottom; i >= top; i--){
				res.add(matrix[i][left]);
			}
			left++; // fixed moves closer

			dir = 0;
		}
	}

	return res;
}
```

### [[04-Pascal's Triangle I]]

```java
// r = 5; 
// c = 3;

public int nCr(int n, int r) {
	// choose smaller r 
	// i.e. r or n-r.
	if(r > n - r) r = n-r;


	//num: (n - k); k ->[0, r-1]  // r states
	//deno: p; p ->[1, r]         // r states;

	int res = 1;
	for(int k = 0; k < r; k++){
		res *= (n - k);
		res /= (k + 1); //p 
	}

	return res;
}
    
public int pascalTriangleI(int r, int c) {
	return nCr(r-1, c-1);
}
```

### [[05-Pascal's Triangle II]]

```java
// n = 5;

public int[] pascalTriangleII(int n) {

	int[] row = new int[n]; // 1st row: size = 1; rth row : size = r;

	//first ele = 1
	row[0] = 1;

	//curr = prev * (r - i) / i; i -> [1, r-1]
	for(int i = 1; i < n; i++){
		row[i] = (row[i-1] * (n - i))/i;
	}

	return row;
}
```

### [[06-Pascal's Triangle III]]

```java
// n = 6;
public List<List<Integer>> pascalTriangleIII(int n){
	List<List<Integer>> pascalTriangle = new ArrayList<>();

	for(int i = 1; i <= n; i++){
		pascalTriangle.add(pascalTriangleII(i));
	}

	return pascalTriangle;
}

public List<Integer> pascalTriangleII(int r) {

	List<Integer> row = new ArrayList<>(); // 1st row: size = 1; rth row : size = r;

	//first ele = 1
	row.add(1);

	long ans = 1;

	//curr = prev * (r - i) / i; i -> [1, r-1]
	for(int i = 1; i < r; i++){
		ans = ans * (r - i);
		ans = ans / i;
		row.add( (int)ans );
	}

	return row;
}
```


### [[07-Rotate Matrix by 90]]

```java
/** 
int[][] mat = {
			{1, 2, 3, 4},
			{5, 6, 7, 8},
			{9, 10, 11, 12},
			{13, 14, 15, 16}
		}
*/
public void rotateMatrix(int[][] mat){
	transpose(mat);
	for(int i = 0; i < mat.length; i++){
		reverse(mat[i]);
	}
}

// transpose: helper methods
public void transpose(int[][] mat){
	int m = mat.length;
	int n = mat[0].length;

	for(int i = 0; i < m; i++){
		for(int j = i + 1; j < n; j++){
			// swap mat[i][j] & mat[j][i]
			int copy = mat[i][j];
			mat[i][j] = mat[j][i];
			mat[j][i] = copy;
		}
	}
}

// reverse: helper method
public void reverse(int[] arr){
	int low = 0;
	int high = arr.length - 1;

	while(low < high){
		// swap arr[low] & arr[high]
		int copy = arr[low];
		arr[low] = arr[high];
		arr[high] = copy;

		// move pointers inward
		low++;
		high--;
	}
}
```


### [[08-Two sum]]
```java
// int[] nums = {2, 6, 5, 8, 11};
// int tar = 14;
public int[] twoSum(int[] nums, int tar){
	Map<Integer, Integer> hm = new HashMap<>(); //past data stored in hm.

	for(int i = 0; i < nums.length; i++){
		int ele = nums[i];

		// (tar - ele) ? seen in past
		if(hm.containsKey(tar - ele)){
			return new int[]{ hm.get(tar - ele), i }
		}
		hm.put(ele, i);
	}

	return new int[]{-1, -1};	
}
```

### [[09-3 Sum]]
```java
// int[] nums = {-1, 0, 1, 2, -1, -4};
// int[] nums = {-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2}
public List<List<Integer>> threeSum(int[] nums){
	List<List<Integer>> ans = new ArrayList<>();

	int n = nums.length;
	Arrays.sort(nums); // make sure input is sorted.

	for(int i = 0; i < n; i++){
		if(i > 0 && nums[i-1] == nums[i]) continue; //skipping duplicates
		
		// Consider unique nums[i]

		// Two pointer approach.
		int l = i + 1;
		int h = n - 1;

		while(l < h){
			if(nums[l] + nums[h] < 0 - nums[i]){
				l++;
			} else if(nums[l] + nums[h] > 0 - nums[i]){
				h--;
			} else {
				// equal case: 
				// [nums[i], nums[l], nums[h]] add to res
				// move both pointers (l, h) inwards, i.e. nums[l], nums[h] should be next unique values
				List<Integer> temp = new Arrays.asList(nums[i], nums[l], nums[h]);
				ans.add(temp);

				l++;
				while(l < h && nums[l-1] == nums[l]) l++;

				h--;
				while(l < h && nums[h] == nums[h+1]) h--;
			}
		}
		// for a unique nums[i] we'll get nums[l], nums[h]
	}
}
```


### [[10-4 Sum]]

```java
// int[] nums = {1, 0, -1, -2, 2, 0};
// int tar = 0;

// int[] nums = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5}
// int tar = 8; 
public List<List<Integer>> fourSum(int[] nums, int tar){
	List<List<Integer>> res = new ArrayList<>();

	int n = nums.length;

	Arrays.sort(nums); // make sure input is sorted.

	for(int i = 0; i < n; i++){

		if(i > 0 && nums[i-1] == nums[i]) continue;
		// for a unique nums[i]

		for(int j = i + 1; j < n; j++){

			if(j > i + 1 && nums[j-1] == nums[j]) continue;
			// for a unique nums[j];

			// Two pointer approach.
			int l = j + 1;
			int h = n - 1;

			while(l < h){
				if(nums[l] + nums[h] < tar - (nums[i] + nums[j]) ){
					l++;
				} else if(nums[l] + nums[h] > tar - (nums[i] + nums[j]) ){
					h--;
				} else {
					// equal case, add [nums[i], nums[j], nums[l], nums[h]] to ans.
					// move l & h inwards to unique values.
					List<Integer> temp = Arrays.asList(nums[i], nums[j], nums[l], nums[h]);
					ans.add(temp);

					// unique nums[l]
					l++;
					while(l < h && nums[l - 1] == nums[l]) l++;
					// unique nums[h]
					h--;
					while(l < h && nums[h] == nums[h+1]) h--;
				
				}
			}
			// for unique nums[i], nums[j] we'll get all possiblities of nums[l], nums[h]
			// i.e. nums[i] + nums[j] + (nums[l] + nums[h]) == tar
		}
	}
}
```


### [[11-Sort an array of 0's 1's and 2's]]
```java
// int[] nums = {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0};
public void sortZeroOneTwo(int[] nums){
	int l = 0;
	int h = nums.length - 1;
	int m = l;

	// l waiting for 0;
	// h waiting for 2;

	while(m <= h){
		if(nums[m] == 2){
			swap(nums, m, h); // throw 2's at h pos
			h--;
		} else if(nums[m] == 1){
			m++; // ignore 1's
		} else {
			// ele == 0; 
			// Note: between l & m there won't be 2's
			swap(nums, m, l);
			l++;
			m++;
		}
	}
}
```

### [[12-Kadane's Algorithm]]
```java
// int[] arr = { -2, -3, 4, -1, -2, 1, 5, -3 };
public int maxSubArraySum(int[] nums){
	// Note: All are int, + or * operation might need long.

	long maxi = Long.MIN_VALUE;
	long sum = 0;

	for(int i = 0; i < nums.length; i++){
		
		sum += nums[i]; // [...] + nums[i]
		maxi = Math.max(maxi, sum); // tracking

		if(sum < 0){
			sum = 0; // []
		}
	}

	return (int)maxi;	
}
```


### [[13-Next Permutation]]
```java
// int[] nums = [2, 1, 5, 4, 3, 0, 0]
public void nextPermutation(int[] nums){
	int n = nums.length;

	int ind = -1;

	// ignore the descending sequence.
	for(int i = n - 2; i >= 0; i--){
		if(nums[i] < nums[i + 1]){
			ind = i;
			break;
		}
	}

	if(ind != -1){ // given order isn't descending

		// find an ele > nums[i] in descending sequence;
		// it should be replaced with nums[i];
		for(int i = n - 1; i > ind; i--){
			if(nums[i] > nums[ind]){
				swap(nums, i, ind); // exchange ele & nums[ind];
				break;
			}
		}

		reverse(nums, ind + 1, n - 1);
	} else {
		// given sequence is desending order.
		reverse(nums, ind + 1, n - 1);
	}
}
```

## FAQs Hard
### [[01-Majority Element - I]]

```java
// eg. [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
public int majorityElement(int[] nums) {
	
	// init mEle & cnt;
	int mEle = -1, cnt = 0;

	for(int i = 0; i < nums.length; i++){        
		if(cnt == 0){
			mEle = nums[i]; // asssume this is a mEle
			cnt = 1;
		} else {
			if(nums[i] == mEle){ 
				cnt++; // add if incoming is majority
			} else { 
				cnt--; // reduce if incoming isn't majority
			}
		}
	}

	// now mostly ele is majority element.
	cnt = 0;
	for(int i = 0; i < nums.length; i++){
		if(nums[i] == mEle) cnt++;
	}

	return cnt > (int)(nums.length / 2) ? mEle : -1;
}
```

### [[02-Majority Element-II]]

```java
// nums = [1, 1, 1, 1, 3, 2, 2, 2] Majority Element Exists
// nums = [2, 1, 1, 3, 1, 4, 5, 6] Majority Element Not Exists
public List<Integer> majorityElementTwo(int[] nums){
	int n = nums.length;
	int ele1 = -1, cnt1 = 0;
	int ele2 = -2, cnt2 = 0;

	for(int i = 0; i < n; i++){
		if(cnt1 == 0 && nums[i] != ele2){
			ele1 = nums[i];
			cnt1++;
		} else if(cnt2 == 0 && nums[i] != ele1){
			ele2 = nums[i];
			cnt2++;
		} else if(nums[i] == ele1){
			cnt1++;
		} else if(nums[i] == ele2){
			cnt2++;
		} else {
			cnt1--;
			cnt2--;
		}
	}

	// validation
	cnt1 = 0;
	cnt2 = 0;

	for(int i = 0; i < n; i++){
		if(nums[i] == ele1) cnt1++;
		if(nums[i] == ele2) cnt2++;
	}

	int magicNum = nums.length/3;

	List<Integer> ans = new ArrayList<>();

	if(cnt1 > magicNum) ans.add(ele1);
	if(cnt2 > magicNum) ans.add(ele2);
}
```

### [[03-Find the repeating and missing number]]

```java
// nums = [4, 3, 6, 2, 1, 1]
public int[] findMissingRepeatingNumbers(int[] nums){
	int n = nums.length;
	
	int xr = 0;
	for(int i = 0; i < n; i++){
		xr ^= nums[i];
		xr ^= (i + 1);
	}

	// xr = rep^mis

	int setBit = (xr & ~(xr-1));

	int zero = 0; // bucket0
	int one = 0; // bucket1

	for(int i = 0; i < n; i++){
		if((nums[i] & setBit) != 0){
			one ^= nums[i];
		} else {
			zero ^= nums[i];
		}
	}


	for(int i = 0; i < n; i++){
		if((i & setBit) != 0){
			one ^= i;
		} else {
			zero ^= i;
		}
	}

	int cnt = 0;

	for(int i = 0; i < n; i++){
		if(nums[i] == zero) cnt++;
	}

	return cnt == 2 ? new int[] {zero, one} : new int[] {one, zero};
}
```

### 04-Count Inversions
```java
// Below example is for conquer() method, for better understanding.
// nums1[] = [2, 3, 5, 6]
// nums2[] = [2, 2, 4, 4, 8]
public void conquer(int[] nums, int low, int mid, int high, long[] cnt){
	
	int i = low; //[low, mid]; n = mid - low + 1; 
	int j = mid+1; //[mid+1, high]; m = high - (mid);

	int[] temp = new int[high - low + 1];
	int k = 0;

	while(i <= mid && j <= high){
		if(nums[i] <= nums[j]){
			temp[k++] = nums[i];
			i++;
		} else{
			cnt[0] += mid - (i) + 1; // extraStep
			temp[k++] = nums[j];
			j++;
		}
	}

	while(i <= mid){
		temp[k++] = nums[i];
		i++;
	}

	while(j <= high){
		temp[k++] = nums[j];
		j++;
	}

	// copy the temp in original array.
	for(k = 0; k < temp.length; k++){
		nums[low + k] = temp[k];
	}
}

// Eg: nums[] = [5, 3, 2, 4, 1]
public long numberOfInversions(int[] nums) {
	long[] cnt = new long[1];
	int n = nums.length;

	divide(nums, 0, n-1, cnt);

	return cnt[0];
}

public void divide(int[] nums, int low, int high, long[] cnt){
	if(low < high){
		int mid = low - (low - high)/2;

		divide(nums, low, mid, cnt);
		divide(nums, mid+1, high, cnt);

		conquer(nums, low, mid, high, cnt);
	}
}
```

### 05-Reverse Pairs
```java
// Focus on below example: cntRevPairs() + conquer() is called.
// nums1[] = [6, 13, 21, 25]
// nums2[] = [1, 2, 3, 4, 4, 5, 9, 11, 13]
public void cntRevPairs(int[] nums, int l, int m, int r, int[] cnt){
	int j = m + 1;
	for(int i = l; i <= m; i++){
		while(j <= r && nums[i] > 2 * nums[j]){
			j++;
		}
		cnt[0] += (j - m - 1);
	}
}

public void conquer(int[] nums, int l, int m, int r){
	int i = l, j = m + 1, k = 0;
	int[] temp = new int[r - l + 1];

	while(i <= m && j <= r){
		if(nums[i] <= nums[j]){
			temp[k++] = nums[i++];
		} else{
			temp[k++] = nums[j++];
		}
	}

	while(i <= m){
		temp[k++] = nums[i++];
	}
	while(j <= r){
		temp[k++] = nums[j++];
	}

	for(k = 0; k < temp.length; k++){
		nums[l + k] = temp[k];
	}
}

public void divide(int[] nums, int l, int r, int[] cnt){
	if(l < r){
		int m = l + (r - l)/2;

		divide(nums, l, m, cnt);
		divide(nums, m+1, r, cnt);
		cntRevPairs(nums, l, m, r, cnt);
		conquer(nums, l, m, r); 
	}
}

// Eg: nums[] = [40, 25, 19, 12, 9, 6, 2]
public int reversePairs(int[] nums) {
	int[] cnt = new int[]{0};
	divide(nums, 0, nums.length - 1, cnt);
	return cnt[0];
}
```

### 06-Maximum Product Subarray in an Array
```java
// nums[] = [2, 3, -2, 4]
// nums[] = [-2, 3, 4, -1, 0, -2, 3, 1, 4, 0, 4, 6, -1, 4]
public int maxProduct(int[] nums) {
	
	int ans = Integer.MIN_VALUE; // -inf

	// create a prefix
	int prefix = 1;
	int suffix = 1;

	// Iterate nums farward
	for(int i = 0; i < nums.length; i++){
		
		// update prefix
		prefix *= nums[i];
		
		// track max value as ans
		ans = Math.max(ans, prefix);

		// if prefix == 0: prefix = 1
		if(prefix == 0) prefix = 1;
	}

	// Iterate nums backward
	for(int i = nums.length - 1; i >= 0; i--){
		// update suffix
		suffix *= nums[i];

		// track max value as ans
		ans = Math.max(ans, suffix);

		// if suffix == 0: suffix = 1
		if(suffix == 0) suffix = 1;
	}

	return ans;
}
```

### 07-Merge two sorted arrays without extra space
```java
/*
	int[] nums1 = {1, 3, 5, 7};
	int[] nums2 = {0, 2, 6, 8, 9};
	int m = 4, n = 3;
*/

// Function to merge two sorted arrays nums1 and nums2
public void merge(int[] nums1, int m, int[] nums2, int n) {
	
	int len = n + m;
	int gap = (len / 2) + (len % 2);

	while (gap > 0) {
		int left = 0;
		int right = left + gap;
		while (right < len) {
			
			// When left in nums1[] and right in nums2[]
			if (left < m && right >= m) {
				swapIfGreater(nums1, nums2, left, right - m);
			}
			// When both pointers in nums2[]
			else if (left >= m) {
				swapIfGreater(nums2, nums2, left - m, right - m);
			}
			// When both pointers in nums1[]
			else {
				swapIfGreater(nums1, nums1, left, right);
			}
			// Increment the pointers by 1 each
			left++;
			right++;
		}
		// If gap is equal, break out of the loop
		if (gap == 1)
			break;
		gap = (gap / 2) + (gap % 2);
	}

	// Copy elements of nums2 into nums1
	for (int i = m; i < m + n; i++) {
		nums1[i] = nums2[i - m];
	}
}

// Utility function to swap elements if needed
private void swapIfGreater(int[] arr1, int[] arr2, int idx1, int idx2) {
	if (arr1[idx1] > arr2[idx2]) {
		
		int temp = arr1[idx1];
		arr1[idx1] = arr2[idx2];
		arr2[idx2] = temp;
	}
}
```
