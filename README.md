
# Titanic Survival Prediction

This is my first Streamlit project for training in Data Science. It uses a Machine Learning model to predict whether a Titanic passenger would have survived based on their class, age, sex, and family size.

## Features:
- User-friendly interface built with Streamlit.
- Takes user input for passenger class, age, sex, and family size.
- Displays the survival prediction with emojis.
- Deployed on Streamlit Community Cloud.

## How to Use:
1. Open the app link (once deployed).
2. Input your details:
   - Passenger class (1, 2, or 3)
   - Age
   - Sex (0 for male, 1 for female)
   - Family size
3. Click on **Predict**.
4. See the prediction and corresponding message (emoji).

## Installation:
To run the app locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/ange2219/titanic-survival-prediction.git

## Dependencies

This project requires the following libraries:

- `streamlit`
- `pandas`
- `scikit-learn`
- `joblib`

### Installing Dependencies

You can install all the required dependencies using the `requirements.txt` file. If you haven't created this file yet, you can generate it with the following command:

```bash
pip freeze > requirements.txt

Then, to install the dependencies, use the following command
pip install -r requirements.txt

Alternatively, if you're not using requirements.txt, you can manually install the libraries with:

pip install streamlit pandas scikit-learn joblib
