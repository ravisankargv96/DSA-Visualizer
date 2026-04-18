# Excalidraw Prompt: 01-Search X in Sorted Array

## Layout Rules
- **Column 1:** Visualization of variables (`low`, `high`, `mid`, `target`) and the Array `nums` with pointers marking `low`, `high`, and `mid` indices.
- **Column 2:** Step text explaining current state, the index calculation, the value comparison, and the boundary updates.
- (Pseudocode block intentionally omitted per current project preferences)

## Test Case
- `nums = [3, 4, 6, 7, 9, 12, 16, 17]`
- `target = 8`
- `n = 8`

## Frame-by-Frame Dry Run

### Frame 1: Initialization
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| **Initial State**<br>`nums = [3, 4, 6, 7, 9, 12, 16, 17]`<br>`target = 8`<br>`low = 0`<br>`high = 8 - 1 = 7` | **Initialization:** Set up the search boundaries. `low` starts at index `0`, and `high` starts at index `n - 1 = 7`. |

### Frame 2: Iteration 1
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 0, high = 7`<br>---<br>`mid = 0 + (7-0)/2 = 3`<br>`nums[3] = 7`<br><br>`7 < 8 (target)` is **True**<br>`low = 3 + 1 = 4` | **i = 1:** Calculate `mid = 3`. The element at `nums[3]` is `7`.<br>Check with target: `7 < 8` is **True**. This means the target `8` must be in the right half of our search space. We move the lower bound up: `low = mid + 1` (4). |

### Frame 3: Iteration 2
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 4, high = 7`<br>---<br>`mid = 4 + (7-4)/2 = 5`<br>`nums[5] = 12`<br><br>`12 < 8` is **False**<br>`12 == 8` is **False**<br>`12 > 8` so `high = 5 - 1 = 4` | **i = 2:** Calculate `mid = 5`. The element at `nums[5]` is `12`.<br>Check with target: `12 < 8` is False, and `12 == 8` is False. Since `12 > 8`, the target must be in the left half of our active search space. We move the upper bound down: `high = mid - 1` (4). |

### Frame 4: Iteration 3
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 4, high = 4`<br>---<br>`mid = 4 + (4-4)/2 = 4`<br>`nums[4] = 9`<br><br>`9 < 8` is **False**<br>`9 == 8` is **False**<br>`9 > 8` so `high = 4 - 1 = 3` | **i = 3:** Calculate `mid = 4`. The element at `nums[4]` is `9`.<br>Check with target: `9 < 8` is False, and `9 == 8` is False. Since `9 > 8`, we once again move the upper bound down to search to the left: `high = mid - 1` (3). |

### Frame 5: Loop Termination & Result
| [Diagram/Image] | [Step Text] |
| :--- | :--- |
| `low = 4, high = 3`<br>`low <= high` is **False**<br>---<br>**Return `-1`** | **Termination:** `low` (4) is now greater than `high` (3). The `while` loop condition is violated. The search space is exhausted and the target `8` was not found. Return `-1`. |
