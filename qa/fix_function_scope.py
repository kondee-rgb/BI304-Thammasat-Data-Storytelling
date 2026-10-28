import os, sys

def fix_scope():
    path = r'assets/js/app.js'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the function definition
    fn_start = content.find("    // ==========================================================================\n    // INTER-CHAPTER GRAPH & CHART SEAMLESS TRANSITIONS")
    fn_end = content.find("      // Smooth Inter-Chapter Navigation via Narrative Connector Bridges")

    if fn_start != -1 and fn_end != -1:
        fn_code = content[fn_start:fn_end].strip()
        # Remove from current location
        content = content[:fn_start] + "\n      " + content[fn_end:]
        
        # Place before // Window Onload Initialization
        target = "    // Window Onload Initialization\n    window.addEventListener('DOMContentLoaded', () => {"
        replacement = fn_code + "\n\n" + target
        
        if target in content:
            content = content.replace(target, replacement)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully moved initInterTopicGraphTransitions to module scope in app.js")
        else:
            print("Could not find window.addEventListener target in app.js")
    else:
        print(f"Indices not found: fn_start={fn_start}, fn_end={fn_end}")

if __name__ == '__main__':
    fix_scope()
