@echo off
cd C:\Users\ivan.barot\diktator
call venv\Scripts\activate
python -m uvicorn server.main:app --reload
pause