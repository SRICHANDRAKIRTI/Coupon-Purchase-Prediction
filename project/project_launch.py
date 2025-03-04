import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
#load dataset
A=pd.read_csv('D:/project/coupon_purchase_prediction.csv')
X=A.iloc[:,0:9]
Y=A.iloc[:,9:]
#standardize the features
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
#create a model
model=LinearRegression()
model.fit(X_scaled,Y)
#gradio function
def predict_coupon(CostomerID,Age,Gender,Income,PreviousPurchases,CouponType,CouponValue,Couponused,DaysSinceLastPurchase):
    input_data=np.array([CostomerID,Age,Gender,Income,PreviousPurchases,CouponType,CouponValue,Couponused,DaysSinceLastPurchase])
    input_data_reshape=input_data.reshape(1,-1)
    input_scaled=scaler.transform(input_data_reshape)
    model_predict=model.predict(input_scaled)
    print(model_predict)
    return model_predict
#gradio app
iface=gr.Interface(
    #calling the function
    fn=predict_coupon,
    inputs=[
        gr.Number(label="costomerID"),
        gr.Number(label="Age"),
        gr.Number(label="Gender"),
        gr.Number(label="Income"),
        gr.Number(label="PreviousPurchases"),
        gr.Number(label="CouponType"),
        gr.Number(label="CouponValue"),
        gr.Number(label="CouponUsed"),
        gr.Number(label="DaysSinceLastPurchase")
    ],
    outputs="text",
    title="Coupon Purchase Prediction"
)
#launch the application
iface.launch(share=True)
