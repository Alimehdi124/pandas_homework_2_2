from pathlib import Path
import runpy

base = Path(__file__).resolve().parent

for task in range(1, 7):
    print(f"\n--- Task {task} ---")
    runpy.run_path(str(base / f"task{task}.py"), run_name="__main__")
