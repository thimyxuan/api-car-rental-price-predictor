import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import joblib

if __name__ == '__main__':

    print('Training model...')
    
    # Time execution
    start_time = time.time()

    # Import dataset
    df = pd.read_csv('src/get_around_pricing_project.csv')

    # X, y split
    X = df.drop(['rental_price_per_day'], axis=1)
    y = df.loc[:, ["rental_price_per_day"]]

    # Train / test split 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

    # Numeric / categorical features
    numeric_features = ['mileage', 'engine_power']
    categorical_features = ['model_key', 'fuel', 'paint_color', 'car_type', 'private_parking_available', 'has_gps', 'has_air_conditioning', 'automatic_car', 'has_getaround_connect', 'has_speed_regulator', 'winter_tires']

    # Pipeline
    numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    categorical_transformer = Pipeline(steps=[('encoder', OneHotEncoder(drop='first', handle_unknown='ignore'))])

    # Preprocessor
    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features)])

    # Apply preprocessings
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Print scores
    print('R2 score on train set:', model.score(X_train, y_train))
    print('R2 score on test set:', model.score(X_test, y_test))

    mse = mean_squared_error(y_train, y_pred)
    mse_test = mean_squared_error(y_test, y_pred_test)

    print('MSE score on train set:', mse)
    print('MSE score on test set:', mse_test)
    print('RMSE score on train set:', np.sqrt(mse))
    print('RMSE score on test set:', np.sqrt(mse_test))
    
    # Persist the model
    joblib.dump(model, 'src/model.pkl')
    joblib.dump(preprocessor, 'src/preprocessor.pkl')

    print("...Done!")
    print(f"---Total training time: {time.time()-start_time}")