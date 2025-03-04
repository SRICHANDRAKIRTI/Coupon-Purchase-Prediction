# Coupon-Purchase-Prediction
 

This project predicts whether a customer will purchase a coupon based on various input features. It uses a **Linear Regression** model and is deployed using **Gradio** for an interactive interface.  

## Files  

- **`coupon_purchase_prediction.csv`**: The dataset used for training the model.  
- **`project_launch.py`**: The main script for data processing, model training, and deployment via Gradio.  

## Requirements  

Ensure you have the following Python packages installed before running the project:  

```bash
pip install numpy pandas matplotlib scikit-learn gradio
```

## How It Works  

1. The dataset is loaded from `coupon_purchase_prediction.csv`.  
2. Features are standardized using `StandardScaler`.  
3. A **Linear Regression** model is trained to predict the likelihood of coupon purchase.  
4. A **Gradio** interface is created for user interaction.  

## Running the Project  

Run the script using:  

```bash
python project_launch.py
```

This will start a Gradio web application where users can input values and get predictions.  

## Inputs Required  

- Customer ID  
- Age  
- Gender (Numerical representation)  
- Income  
- Previous Purchases  
- Coupon Type  
- Coupon Value  
- Coupons Used  
- Days Since Last Purchase  

## Output  

The model predicts the likelihood of a customer purchasing a coupon.  

## Future Improvements  

- Improve model accuracy by testing other algorithms.  
- Add feature engineering techniques.  
- Deploy as a web service.  
