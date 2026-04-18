# Excalidraw Prompt: 02-Lower Bound

## Layout Rules
- **Column 1:** Visualization of variables (`low`, `high`, `mid`, `ans`, `x`) and the Array `nums` with pointers marking `low`, `high`, and `mid` indices.
- **Column 2:** Step text explaining current state, checking the lower bound condition `nums[mid] >= x`, and boundary adjustments.
- (Pseudocode block intentionally omitted per current project preferences)

## Test Case
- `nums = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]`
- `x = 9`
- `n = 10`

## Frame-by-Frame Dry Run

### Frame 1: Initialization
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| **Initial State**<br>`nums = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]`<br>`x = 9`<br>`n = 10`<br>`low = 0`<br>`high = 10 - 1 = 9`<br>`ans = n = 10` | **Initialization:** Set search bounds. `low = 0`, `high = 9`. We set `ans = n = 10` as a default fallback indicating no element is `>= x`. |

### Frame 2: Iteration 1
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 0, high = 9, ans = 10`<br>---<br>`mid = 0 + (9-0)/2 = 4`<br>`nums[4] = 5`<br><br>`5 > 9` is **False**<br>`5 == 9` is **False**<br>So `5 < 9`, `low = 4 + 1 = 5` | **i = 1:** Calculate `mid = 4`. `nums[4] = 5`.<br>Check lower bound logic: Is `5 >= 9`? **False**. The value at `mid` is too small, so we must search to the right. Move lower bound: `low = mid + 1` (5). |

### Frame 3: Iteration 2
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 5, high = 9, ans = 10`<br>---<br>`mid = 5 + (9-5)/2 = 7`<br>`nums[7] = 10`<br><br>`10 > 9` is **True**<br>`ans = 7`<br>`high = 7 - 1 = 6` | **i = 2:** Calculate `mid = 7`. `nums[7] = 10`.<br>Check condition: Is `10 >= 9`? **True**. This is a possible lower bound! We record the index: `ans = mid = 7`. Now, check if there's a smaller index that satisfies the condition by moving left: `high = mid - 1` (6). |

### Frame 4: Iteration 3
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 5, high = 6, ans = 7`<br>---<br>`mid = 5 + (6-5)/2 = 5`<br>`nums[5] = 8`<br><br>`8 > 9` is **False**<br>`8 == 9` is **False**<br>So `8 < 9`, `low = 5 + 1 = 6` | **i = 3:** Calculate `mid = 5`. `nums[5] = 8`.<br>Check condition: Is `8 >= 9`? **False**. The value is too small, meaning our optimal index is to the right. Move lower bound: `low = mid + 1` (6). |

### Frame 5: Iteration 4
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 6, high = 6, ans = 7`<br>---<br>`mid = 6 + (6-6)/2 = 6`<br>`nums[6] = 8`<br><br>`8 > 9` is **False**<br>`8 == 9` is **False**<br>So `8 < 9`, `low = 6 + 1 = 7` | **i = 4:** Calculate `mid = 6`. `nums[6] = 8`.<br>Check condition: Is `8 >= 9`? **False**. The value is still too small. Move lower bound: `low = mid + 1` (7). |

### Frame 6: Loop Termination & Result
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 7, high = 6, ans = 7`<br>`low <= high` is **False**<br>---<br>**Return `ans = 7`** | **Termination:** `low` (7) is now greater than `high` (6). Loop terminates. The optimal index where the element is `>= x` is `ans = 7`. Return `7` (value is 10). |
