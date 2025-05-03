import mlflow
print("Printing tracking uri scheme below")
print(mlflow.get_tracking_uri())
print("\n")

mlflow.set_tracking_uri("http://127.0.0.1:5000/#/experiments/0")
print("Printing tracking uri scheme below")
print(mlflow.get_tracking_uri())
print("\n")