import re

files = [
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\architecture\architecture.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\information-architecture\ia-sitemaps.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\information-architecture\ia-strategy-navigation.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\information-architecture\ia-user-flows.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\prd\prd-v2.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\.taskmaster\docs\prd\prd-v3.md",
    r"d:\CLAUDE-PROJECT\awesome-website-test\README.md"
]

class_assignments = {
    "architecture.md": {
        0: {"U": "entry", "L1": "entry", "L2": "entry", "L3": "entry", "WA": "conversion"}
    },
    "ia-sitemaps.md": {
        0: {"H5": "conversion", "RG": "conversion", "RB": "conversion"},
        1: {"SH4": "conversion", "PDP5": "conversion", "PDP6": "conversion", "SRF": "conversion"}
    },
    "ia-strategy-navigation.md": {
        0: {"H_CTA": "conversion"},
        1: {"S_CTA": "conversion"}
    },
    "ia-user-flows.md": {
        0: {"START": "entry", "B2GFORM": "conversion", "SUBMIT": "conversion", "CONFIRM": "conversion", "FALLBACK": "conversion", "PROVISION": "conversion"},
        1: {"START": "entry", "WHATSAPP": "conversion", "B2BFORM": "conversion", "SUBMIT": "conversion", "CONFIRM": "conversion", "FALLBACK": "conversion", "PROVISION": "conversion"},
        2: {"SUBMIT": "conversion", "SUCCESS": "conversion", "FAIL": "conversion", "WAUI": "conversion", "WACLICK": "conversion", "TGALERT": "conversion"}
    },
    "prd-v2.md": {
        0: {"Legacy1": "entry", "Legacy2": "entry", "Legacy3": "entry"},
        1: {"A": "entry", "K": "conversion", "M": "conversion", "N": "conversion", "O": "conversion", "P": "conversion"},
        2: {"A": "entry", "I": "conversion", "J": "conversion", "L": "conversion", "M": "conversion", "N": "conversion", "O": "conversion"}
    },
    "prd-v3.md": {
        0: {"Legacy1": "entry", "Legacy2": "entry", "Legacy3": "entry"},
        1: {"A": "entry", "K": "conversion", "M": "conversion", "N": "conversion", "O": "conversion", "P": "conversion", "R": "conversion"},
        2: {"A": "entry", "I": "conversion", "J": "conversion", "L": "conversion", "M": "conversion", "N": "conversion", "O": "conversion", "R": "conversion"}
    },
    "README.md": {
        0: {"U": "entry"}
    }
}

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"(```mermaid\n.*?\n```)", content, flags=re.DOTALL)
    filename = file_path.split("\\")[-1]
    
    for i, block in enumerate(blocks):
        if block.startswith("```mermaid"):
            diagram_idx = i // 2
            
            # Replace frontmatter
            fm_match = re.search(r"^---\nconfig:(.*?)\n---", block, flags=re.DOTALL | re.MULTILINE)
            if fm_match:
                fm_content = fm_match.group(1)
                layout_match = re.search(r"\s+layout:\s+(\w+)", fm_content)
                layout_str = f"\n  layout: {layout_match.group(1)}" if layout_match else ""
                new_fm = f"---\nconfig:{layout_str}\n  theme: neutral\n---"
                block = block[:fm_match.start()] + new_fm + block[fm_match.end():]
            
            # Remove inline styles
            block = re.sub(r"^\s*style\s+\w+\s+fill:.*?$", "", block, flags=re.MULTILINE)
            # Remove empty lines left by style removal
            block = re.sub(r"\n\s*\n", "\n", block)
            
            is_flowchart = re.search(r"^(flowchart|graph)\s+\w+", block, flags=re.MULTILINE)
            if is_flowchart:
                classdefs = "\n    classDef entry fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#92400e\n    classDef conversion fill:#fff7ed,stroke:#ea580c,stroke-width:2px,color:#9a3412\n"
                block = block[:is_flowchart.end()] + classdefs + block[is_flowchart.end():]
                
                if filename in class_assignments and diagram_idx in class_assignments[filename]:
                    assignments = class_assignments[filename][diagram_idx]
                    classes_str = "\n"
                    for node, cls in assignments.items():
                        classes_str += f"    class {node} {cls}\n"
                    
                    block = block[:-4] + classes_str + "```"
            
            blocks[i] = block

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("".join(blocks))
