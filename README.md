# Expense Tracker

A minimalist "Fintech" inspired expense tracking application built with Flask and SQLite.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- A virtual environment (recommended)

### Installation & Setup
1. **Clone the repository**
2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Start the Flask server by running:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5001`.

### Running Tests
This project uses `pytest` for testing. To run the test suite:
```bash
pytest
```

## 🏗️ Architecture

The project follows a basic MVC-like structure:

- **Controller (`app.py`)**: Handles routing, request processing, and application logic.
- **Model (`database/`)**: Contains SQLite interaction logic (e.g., `db.py`) for data persistence.
- **View (`templates/`)**: Jinja2 HTML templates. `base.html` provides the shared layout.
- **Assets (`static/`)**: CSS and JavaScript files.

## 🎨 UI Guidelines

- **Framework**: Tailwind CSS (via CDN).
- **Aesthetic**: Minimalist "Fintech" look.
- **Typography**: Inter (Sans) and Playfair Display (Serif).
- **Colors**: White, Slate (grayscale), and Emerald (accents).

## 🛠️ Development Commands Summary

| Action | Command |
| :--- | :--- |
| Run App | `python app.py` |
| Install Deps | `pip install -r requirements.txt` |
| Run Tests | `pytest` |
| Activate Env | `source venv/bin/activate` |
