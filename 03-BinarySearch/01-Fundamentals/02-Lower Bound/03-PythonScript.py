import json
import uuid
import os

def generate_excalidraw():
    def add_text(x, y, text, size=20, color="#000000", font=1):
        lines = str(text).split("\n")
        max_len = max(len(line) for line in lines)
        return {
            "id": str(uuid.uuid4()), "type": "text", "x": x, "y": y,
            "width": max_len * size * 0.6, 
            "height": len(lines) * size * 1.25, 
            "angle": 0, "strokeColor": color,
            "backgroundColor": "transparent", "fillStyle": "hachure", "strokeWidth": 1,
            "strokeStyle": "solid", "roughness": 1, "opacity": 100, "groupIds": [], 
            "strokeSharpness": "sharp", "seed": 1, "version": 1, "versionNonce": 1, 
            "isDeleted": False, "boundElements": None, "updated": 1, "link": None,  
            "locked": False, "text": str(text), "fontSize": size, "fontFamily": font, "textAlign": "left",
            "verticalAlign": "top", "baseline": size
        }

    def add_rect(x, y, w, h, bg="transparent", color="#000000"):
        return {
            "id": str(uuid.uuid4()), "type": "rectangle", "x": x, "y": y,
            "width": w, "height": h, "angle": 0, "strokeColor": color,
            "backgroundColor": bg, "fillStyle": "solid", "strokeWidth": 1,
            "strokeStyle": "solid", "roughness": 1, "opacity": 100, "groupIds": [], 
            "strokeSharpness": "sharp", "seed": 1, "version": 1, "versionNonce": 1, 
            "isDeleted": False, "boundElements": None, "updated": 1, "link": None,  
            "locked": False
        }

    def add_array(x, y, values, low=-1, high=-1, mid=-1):
        els = []
        w = 60
        h = 60
        for i, v in enumerate(values):
            bg = "transparent"
            if i == mid:
                bg = "#ffeaa7" # yellow for mid
            elif low <= i <= high:
                bg = "#e3f2fd" # light blue for active search space
            else:
                bg = "#f1f2f6" # inactive grey

            els.append(add_rect(x + i*w, y, w, h, bg))
            els.append(add_text(x + i*w + w/2 - 10, y + h/2 - 10, str(v), 20))
            # Pointers
            labels = []
            if i == low: labels.append("L")
            if i == high: labels.append("H")
            if i == mid: labels.append("M")
            if labels:
                pointer_text = ",".join(labels)
                els.append(add_text(x + i*w + w/2 - len(pointer_text)*5, y + h + 10, pointer_text, 16, "#e17055", 3))
        return els

    elements = []
    nums = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
    x = 9

    # Frame spacing adjusted for multiline overlaps
    y_offset = 100
    frame_gap = 290

    # Frame 1: Initialization
    elements.append(add_text(780, y_offset, "Frame 1: Initialization", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 0, 9, -1))
    elements.append(add_text(780, y_offset + 60, "nums=[1,2,3,3,5,8,8,10,10,11]\nx=9, n=10\nlow=0, high=9, ans=10", 20))
    elements.append(add_text(780, y_offset + 150, "Initialization: Set search bounds. low=0, high=9.\nWe set ans=n=10 as a default fallback indicating\nno element is >= x.", 18, "#2d3436"))

    y_offset += frame_gap

    # Frame 2: Iteration 1
    elements.append(add_text(780, y_offset, "Frame 2: Iteration 1", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 0, 9, 4))
    elements.append(add_text(780, y_offset + 60, "low=0, high=9, ans=10\nmid=4, nums[4]=5\n5 < 9, so low=5", 20))
    elements.append(add_text(780, y_offset + 150, "i=1: Calculate mid=4. nums[4]=5.\nCheck: Is 5 >= 9? False. The value at mid is too\nsmall, search right. Move lower bound: low=mid+1 (5).", 18, "#2d3436"))

    y_offset += frame_gap

    # Frame 3: Iteration 2
    elements.append(add_text(780, y_offset, "Frame 3: Iteration 2", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 5, 9, 7))
    elements.append(add_text(780, y_offset + 60, "low=5, high=9, ans=10\nmid=7, nums[7]=10\n10 >= 9 is True! ans=7, high=6", 20))
    elements.append(add_text(780, y_offset + 150, "i=2: Calculate mid=7. nums[7]=10.\nCheck: Is 10 >= 9? True! This is a possible lower\nbound. Record: ans=7. Search left for smaller: high=mid-1 (6).", 18, "#2d3436"))

    y_offset += frame_gap

    # Frame 4: Iteration 3
    elements.append(add_text(780, y_offset, "Frame 4: Iteration 3", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 5, 6, 5))
    elements.append(add_text(780, y_offset + 60, "low=5, high=6, ans=7\nmid=5, nums[5]=8\n8 < 9, so low=6", 20))
    elements.append(add_text(780, y_offset + 150, "i=3: Calculate mid=5. nums[5]=8.\nCheck: Is 8 >= 9? False. The value is too small,\noptimal index is to the right. Move: low=mid+1 (6).", 18, "#2d3436"))

    y_offset += frame_gap

    # Frame 5: Iteration 4
    elements.append(add_text(780, y_offset, "Frame 5: Iteration 4", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 6, 6, 6))
    elements.append(add_text(780, y_offset + 60, "low=6, high=6, ans=7\nmid=6, nums[6]=8\n8 < 9, so low=7", 20))
    elements.append(add_text(780, y_offset + 150, "i=4: Calculate mid=6. nums[6]=8.\nCheck: Is 8 >= 9? False. Still too small.\nMove lower bound: low=mid+1 (7).", 18, "#2d3436"))

    y_offset += frame_gap

    # Frame 6: Loop Termination & Result
    elements.append(add_text(780, y_offset, "Frame 6: Loop Termination & Result", 24))
    elements.extend(add_array(100, y_offset + 60, nums, 7, 6, -1))
    elements.append(add_text(780, y_offset + 60, "low=7, high=6\nlow <= high is False\nReturn ans=7", 20))
    elements.append(add_text(780, y_offset + 150, "Termination: low(7) > high(6). Loop terminates.\nThe optimal index where element is >= x is ans=7.\nReturn 7 (value is 10).", 18, "#2d3436"))

    excalidraw_data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {}
    }

    
    
    , exist_ok=True)

    
    

    output_path = os.path.join(os.path.dirname(__file__), "04-Visual.excalidraw")
    
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2) if "data" in locals() else json.dump(excalidraw_data, f, indent=2)
    
    print(f"File created successfully at: {output_path}")

if __name__ == "__main__":

    generate_excalidraw()

