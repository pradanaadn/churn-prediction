import joblib

loaded_model = joblib.load('artifact/lightgbm_model.pkl')
print(loaded_model)