import gradio as gr
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load and prepare model
df = pd.read_csv('../data/winequality-red.csv')
X = df.drop("quality", axis=1)
df['quality']=df['quality'].apply(lambda x: 1 if x >= 6 else 0)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Prediction function (accepts *args now)
def predict_wine_quality(*args):
    input_df = pd.DataFrame([args], columns=X.columns)
    pred = model.predict(input_df)[0]
    return "🍷 Good Quality" if pred == 1 else "❌ Not Good Quality"

# Gradio sliders
inputs = [
    gr.Slider(minimum=float(df[col].min()), maximum=float(df[col].max()),
              value=float(df[col].mean()), label=col)
    for col in X.columns
]

# Interface
demo = gr.Interface(fn=predict_wine_quality, inputs=inputs, outputs="text", title="Wine Quality Predictor")
demo.launch()

# Save the model
import joblib
joblib.dump(model, "../Outputs/models/wine_quality_model.pkl")

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Model saved as 'wine_quality_model.pkl'")

# Classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

