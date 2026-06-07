# Light - Class 10 Science

A Streamlit app that provides detailed explanations, formulas, examples, and interactive visualizations for the Class 10 science chapter on Light.

## Features

- Topic selector for key light concepts
- Detailed explanations and formulas for each topic
- Optional extra details: examples, diagrams, real-life applications, historical background
- Interactive `Visualize It` lab experience for reflection, refraction, mirrors, and lenses
- Live Altair charts updated by slider and input controls

## Requirements

- Python 3.8+
- `streamlit`
- `altair`
- `pandas`

## Installation

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

2. Activate the environment:

```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install streamlit altair pandas
```

## Run the app

From the project root:

```bash
streamlit run Light.py
```

Then open the local URL shown in your browser.

## File

- `Light.py`: Main Streamlit app source file

## Notes

- The app uses Streamlit session state to preserve selections when interactive controls are adjusted.
- The `Visualize It` option adds a dynamic lab-like experience for the selected topic.
