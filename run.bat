@echo off

echo Installing required libraries...
pip install -r requirements.txt

echo Starting the Flask server...
python app.py