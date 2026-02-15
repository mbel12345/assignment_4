# Project Setup

## Set up Repo
In WSL/VS Code Terminal:
```bash
mkdir assignment_3
cd assignment_3/
git init
git branch -m main
git remote add origin git@github.com:mbel12345/assignment_4.git
vim README.md
git add . -v
git commit -m "Initial commit"
git push -u origin main
```

## Set up virtual environment
In WSL/VS Code Terminal:
```bash
python -m venv venv
```

## Run test cases
In WSL/VS Code Terminal:
```bash
pytest
```

## Run the calculator
In WSL/VS Code Terminal:
```bash
python3 main.py
```
