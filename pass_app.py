import pandas as pd
import numpy as np
import streamlit as st
password = input("Enter your password:")
if len(password) != 0:
	prediction = helper.result(password)
	def results(prediction):
		if prediction == 0:
			return "weak password"
		elif prediction == 1:
			return "moderate password"
		else:
			return "strong password"
	class_ = "strength: " + results(prediction)
    	st.success(class_)
