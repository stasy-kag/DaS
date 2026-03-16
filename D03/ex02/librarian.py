import os
import subprocess
import sys

def main():
    venv = os.environ.get("VIRTUAL_ENV")
    if not venv:
        raise EnvironmentError("Скрипт запущен вне виртуального окружения!")

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "beautifulsoup4", "pytest"],
        check=True
    )

    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout.strip())

    with open("requirements.txt", "w") as f:
        f.write(result.stdout)

if __name__ == "__main__":
    main()