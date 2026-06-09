# Gender Detection ML

A simple machine learning web app for predicting gender based on input features.

## Project Structure

- `app.py` - Flask application entry point
- `train_model.py` - Model training script
- `dataset.csv` - Dataset used for training
- `templates/index.html` - Web UI template
- `static/style.css` - Web UI styles
- `requirements.txt` - Python dependencies

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the environment:
   - Windows:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the App

```bash
python app.py
```

Then open the URL shown in the terminal (usually `http://127.0.0.1:5000`).

## Notes

- If you want to retrain the model, run `python train_model.py`.
- Make sure `dataset.csv` is available in the project root.
