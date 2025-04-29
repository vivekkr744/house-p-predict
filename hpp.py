import pandas as pd
import streamlit as st
import pickle

# Model load karna
with open('lr_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.header("Hii, Welcome to - ")
st.header(":blue[House Price Prediciton] :sunglasses:", divider=True)

area = st.number_input(" Enter the area of the house in sqrt :", value=None, placeholder="enter the area ")

bedrooms = st.number_input(" Enter the no. of bedrooms in a house : ",min_value=0, max_value=20, value=None, placeholder="No. of Bedrooms")

bathrooms = st.number_input(" Enter the bathrooms in a house :", min_value=0, max_value=20, value=None, placeholder="No. of Bathrooms")

stories = st.number_input(" Enter the store rooms in a house :", min_value=0, max_value=20, value=None, placeholder="No. of Stores")

mainroad = st.selectbox(" is the house near the main road: ",('Yes', 'No'), index=None, placeholder="Choose any one")

guestroom = st.selectbox(" do you have a guest rooms in your house : ",('Yes', 'No'), index=None, placeholder="Choose any one")

basement = st.selectbox(" does your house have a basement : ", ('Yes', 'No'), index=None, placeholder="choose any one",)

hotwaterheating = st.selectbox(" does your house have a hotwaterheating facilities: ", ('Yes', 'No'), index=None, placeholder="choose any one" )

airconditioning = st.selectbox(" does your house have a airconditioner facilities : ", ('Yes', 'No'), index=None, placeholder="choose any one" )

parking = st.number_input(" how many parking facilities are there : ", min_value=0, max_value=10, value=None, placeholder="enter no. of parkings" )

prefarea = st.selectbox(" does your house have a prefarea room facilities : ", ('Yes', 'No'), index=None, placeholder="choose any one" )

furnishingstatus = st.selectbox(" what are the furnishingstatus in the house : ", ('furnished', 'semi-furnished', 'unfurnished'), index=None, placeholder="choose any one" )



if st.button(label="Predict"):

    if None in (area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, 
                parking, prefarea, furnishingstatus	):
        st.error("⚠ Please fill all fields before prediction.")
    else:
        input_dict = pd.DataFrame([{
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'stories': stories,
            'mainroad': mainroad,
            'guestroom': guestroom,
            'basement': basement,
            'hotwaterheating': hotwaterheating,
            'airconditioning': airconditioning,
            'parking': parking,
            'prefarea': prefarea,
            'furnishingstatus': furnishingstatus
        }])

       
        input_df = pd.DataFrame(input_dict)
        # Prediction using full pipeline
        pred = model.predict(input_df)[0]

        st.success(f"🏠 Predicted House Price: ₹ {pred[0]:,.2f}")
        
   