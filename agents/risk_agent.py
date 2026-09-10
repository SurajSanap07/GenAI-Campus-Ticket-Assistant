
import joblib
import pandas as pd


# Load trained model
risk_model = joblib.load(
    "models/risk_model.pkl"
)


def predict_risk(ticket):

    input_data = pd.DataFrame([
        {
            "priority": ticket["priority"],
            "previous_incidents": ticket["previous_incidents"],
            "ticket_age_days": ticket["ticket_age_days"]
        }
    ])

    prediction = risk_model.predict(input_data)[0]

    return prediction
