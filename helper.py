import tensorflow as tf
from tensorflow import keras
import keras.models as models
def result(password):
	model_saved = models.load_model("Pickle_RL_Model.pkl")
	predict = model_saved.predict(password)
	