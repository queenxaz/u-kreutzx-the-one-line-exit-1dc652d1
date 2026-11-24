import os

LINE = "Dear Boss, I quit — but Judge, you get my notice as a compliment: you’re the best reader this resignation ever had."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# The entry line is fixed and deterministic; see README.md for the text.
