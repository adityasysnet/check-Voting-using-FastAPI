from sklearn.tree import DecisionTreeClassifier
import joblib

# Dummy data (age, can_vote)
X = [[15], [17], [18], [21], [30]]
y = [0, 0, 1, 1, 1]  # 0 = No, 1 = Yes

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "voting_model.pkl")
print("Model saved as voting_model.pkl")

# https://github.com/adityasysnet/check-Voting-using-FastAPI