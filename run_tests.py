import os
from robot import run

if __name__ == "__main__":
    result_dir = "results"
    os.makedirs(result_dir, exist_ok=True)
    run("test_cases", outputdir=result_dir)
    print("✅ Test Execution Complete! Check results folder for report.html")
