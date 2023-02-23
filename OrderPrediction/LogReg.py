import numpy as np
import pickle

class inference:
	def __init__(self):
		self.model = pickle.load(open('model.pkl','rb'))

	def pred(self,Age, Gender, freq):
		X = np.array([Age,Gender,freq]).reshape(1,-1)
		out = self.model.predict(X)
		return out
