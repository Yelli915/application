from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR, OUT_DIR = WORK_DIR/"input", WORK_DIR/"output"

if __name__ == "__main__":
    IN_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)
    # parents=True 추가하면 단독파일에 대해서만 실행성공