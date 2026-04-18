# Excalidraw Generation Rules for DSA Visualization

When generating Excalidraw diagrams for dry runs of data structures and algorithms, adhere to the following layout and formatting rules:

## 1. Columnar / Tabular Layout
- Organize the visualization in a tabular manner, treating the different sections as columns.
- Do **not** draw visible table borders; just align the contents horizontally and vertically.

## 2. Positioning of Elements
- **Pseudocode (Leftmost Column):** 
  - Generate a simple, human-readable pseudocode for the given code.
  - Place this pseudocode on the far left side of the entire visualization to serve as a reference.
- **Images / Diagrams (Middle Column):** 
  - Place the visual representation (the arrays, boxes, highlights, pointers) in the center, to the right of the pseudocode.
- **Steps and Explanations (Rightmost Column):** 
  - The descriptive text for the steps (e.g., "Initialization", "i = 0", "i=1, nums[1]=2.. Continue") must be placed to the right side of the diagrams.
  - Do not place descriptions above or below the array graphics; align them directly to the right of the corresponding iteration state.

## 3. Frame-by-Frame Structure
- For every step of the algorithm (iterations, condition checks), the row should consistently follow the [Pseudocode] [Diagram/Image] [Step Text] pattern.
  - *Note: Pseudocode block has been temporarily removed per current preferences.*

## 4. Python to Excalidraw Constraints
To avoid text overlapping in Excalidraw visualizations:
- Calculate text block heights dynamically based on the number of newline (\n) characters.
- Use a rame_gap of at least 400px between iterative frames to condense vertical spacing properly without making it clumsy.
- For Linked Lists specifically, ensure starting y_offset pushes down at least 110px below the Frame Title so top-aligned pointer texts (e.g., 	emp) do not overlap the title.
- Ensure step text blocks have adequate horizontal spacing: **	ext_x_base must be dynamically calculated** to guarantee it trails the longest node element (e.g. x_start + max_nodes_length * 160 + 150 or uniformly > 1200px) to prevent any text and arrow overlapping.
- **Linked List Arrows:** Expand the length of the straight linking arrows so they extend explicitly by the node's explicit gap value (e.g., gap = 80). The arrowhead must correctly touch the edge of the next node instead of leaving a visible gap.
- **Colors & Theming:** Use distinct, visually appealing colors to distinguish elements properly: Standard nodes (bg: #f8f9fa, border: #adb5bd), target/found nodes (bg: #e3fafc, border: #1098ad), and dummy/null nodes (bg: #e9ecef, text: #adb5bd). Use red (#e03131) for fast/curr/l2 pointers and blue (#1971c2) for slow/prev/l1 pointers. To completely avoid text overlapping on images, maintain a **decent gap strictly between frames. i.e. frame_gap minimum 400px**.

## 5. Project Folder Structure
This repository scales out to cover 339 DSA problems. Always maintain and save relevant files within these designated modular directories based on the problem hierarchy:
- **\TopicName\** (e.g. \01-Arrays\): Contains the overarching markdown logic files (e.g. \01-Arrays.md).
  - **\SubTopicName\** (e.g. \01-Fundamentals\): Subdirectories dictated by H2 tags.
    - **\ProblemName\** (e.g. \01-Linear Search\): Individual problem subdirectories dictated by H3 tags.
      - **\02-Prompt.md**: The AI generation prompt template mapped for the problem.
      - **\03-PythonScript.py**: The python script executing the Excalidraw generation logic.
      - **\04-Visual.excalidraw**: The rendered and generated Excalidraw JSON file.

Additionally, maintain the ProjectTrackerSheet.md at the root directory up-to-date with new problems mapped. Columns included: S.No, Topic, Subtopic, Problem, Prompts, Python, Excalidraw tracking tick boxes like [x] or [ ].

When writing generation scripts 03-PythonScript.py, ensure the export path directly generates 04-Visual.excalidraw in relative placement to the script execution os.path.join(os.path.dirname(__file__), '04-Visual.excalidraw').

## 6. Workflow & Assistant Handoff Context
When an AI Assistant session begins, or when working through multiple problems, follow this protocol:
1. **Target File Verification:** Read the active DSA markdown file under 
