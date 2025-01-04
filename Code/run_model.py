
# import streamlit as st
# import pandas as pd
# import joblib

# # Load models and data
# regr = joblib.load('Code/regr.pkl')
# clf = joblib.load('Code/clf.pkl')
# feature_columns = joblib.load('Code/feature_columns.pkl')
# scaler_dict = joblib.load('Code/scaler_dict.pkl')
# catData = joblib.load('Code/catData.pkl')
# label_encoding_dict = joblib.load('Code/label_encoding_dict.pkl')
# numData = joblib.load('Code/numData.pkl')
# unique_values = joblib.load('Code/unique_values.pkl')

# # App Layout
# st.set_page_config(
#     page_title="Stress & Sleep Disorder Predictor",
#     page_icon="🌜",
#     layout="centered"
# )

# st.title("Stress and Sleep Disorder Predictor 🔮")
# st.markdown("""
# ### Understand your health better
# This tool helps predict your stress levels and the likelihood of sleep disorders based on lifestyle and health data.

# Please fill in the details on the sidebar, and let's get started!
# """)
# # use image from directory mindful.png
# st.image('Code/mindful.png', use_container_width =True)
# # Input Section with user-friendly placeholders and emojis
# st.sidebar.header("Input Your Details")

# input_data = {}
# input_data['Gender'] = st.sidebar.selectbox(
#     'Gender 👩‍♂️‍♀️', unique_values['Gender']
# )

# input_data['Age'] = st.sidebar.number_input(
#     'Age 📈', min_value=0, max_value=150, step=1, value=None, placeholder='Enter Age'
# )

# input_data['Occupation'] = st.sidebar.selectbox(
#     'Occupation 💼', unique_values['Occupation']
# )

# input_data['Sleep Duration'] = st.sidebar.number_input(
#     'Sleep Duration (hours) 💤', min_value=0, max_value=24, step=1, value=None, placeholder='Enter Sleep Duration'
# )

# input_data['Quality of Sleep'] = st.sidebar.number_input(
#     'Sleep Quality (out of 10) 💭', min_value=0, max_value=10, step=1, value=None, placeholder='Rate Your Sleep Quality'
# )

# input_data['Physical Activity Level'] = st.sidebar.number_input(
#     'Physical Activity Level (out of 100) 🏃', min_value=0, max_value=100, step=1, value=None, placeholder='Enter Physical Activity Level'
# )

# input_data['BMI Category'] = st.sidebar.selectbox(
#     'BMI Category 🍎', unique_values['BMI Category']
# )

# input_data['Heart Rate'] = st.sidebar.number_input(
#     'Heart Rate (BPM) 💓', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Heart Rate'
# )

# input_data['Daily Steps'] = st.sidebar.number_input(
#     'Daily Step Count 👣', min_value=0, max_value=50000, step=1, value=None, placeholder='Enter Daily Step Count'
# )

# input_data['Diastolic Pressure'] = st.sidebar.number_input(
#     'Diastolic Pressure (mmHg) 🔻', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Diastolic Pressure'
# )

# input_data['Systolic Pressure'] = st.sidebar.number_input(
#     'Systolic Pressure (mmHg) 🔻', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Systolic Pressure'
# )

# # Validate Input
# valid_inputs = all(value is not None for value in input_data.values())

# if valid_inputs:
#     input_df = pd.DataFrame([input_data])
#     st.write("### Your Input Details")
#     st.dataframe(input_df)

#     # Stress Prediction
    
#     if st.button('Predict Stress Level 🔮'):  
#         for category in catData:
#             if category != 'Sleep Disorder':
#                 input_df[category] = label_encoding_dict[category].transform(input_df[category])
#         for f in numData:
#             input_df[f] = scaler_dict[f].transform(input_df[[f]])
#         stress_level = regr.predict(input_df)
#         if stress_level < 4:
#             st.success(f'Predicted Stress Level: {stress_level[0]:.2f} 🌈 Excellent, You are Stress Free. Keep it up!')
#         elif 4 <= stress_level < 5:
#             st.info(f'Predicted Stress Level: {stress_level[0]:.2f} 🌟 Good, stay balanced!')
#         elif 5 <= stress_level < 6:
#             st.info(f'Predicted Stress Level: {stress_level[0]:.2f} ⭐ Absolutely Normal for working professionals.')
#         elif 6 <= stress_level < 7:
#             st.warning(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Are you bit Stressed? Please Take care of yourself.')
#         elif 7 <= stress_level < 8:
#             st.warning(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Do you feel Stressed? Need improvement in stress management.')
#         else:
#             st.error(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Oh, It seems You have high stress, Please Take care of yourself and seek support.')
#         st.error('**This is a prediction and not a substitute for medical advice.**')
#     # Sleep Disorder Prediction
#     if st.button('Predict Sleep Disorder 🔮'):
#         for category in catData:
#             if category != 'Sleep Disorder':
#                 input_df[category] = label_encoding_dict[category].transform(input_df[category])
#         for f in numData:
#             input_df[f] = scaler_dict[f].transform(input_df[[f]])

#         sleep_disorder = clf.predict(input_df)
#         prediction = label_encoding_dict['Sleep Disorder'].inverse_transform([sleep_disorder])[0]

#         if prediction == 'None':
#             st.success(f'Predicted Sleep Disorder: None 🌈 Great! You seem to have no issues with sleep.')
#         elif prediction == 'Sleep Apnea':
#             st.warning(f'Predicted Sleep Disorder: Sleep Apnea 👨‍⚕️ Please consult a doctor.')
#         elif prediction == 'Insomnia':
#             st.warning(f'Predicted Sleep Disorder: Insomnia 👨‍⚕️ Consider seeking professional help.')
#         st.error('**This is a prediction and not a substitute for medical advice.**')
# else:
#     st.error("Please fill in all the input fields to proceed!")

# st.markdown("---")
# # bold text
# # increase the font size of the text

# st.markdown('<p style="font-size: 24px;"> Disclaimer: This is a predictive tool and not a substitute for professional medical advice. Please consult a healthcare provider for accurate diagnosis and treatment.</p>', unsafe_allow_html=True)

# # adding a footer with a link to the credits page
# st.markdown(
#     """
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #f1f1f1;
#         color: black;
#         text-align: center;
#         padding: 10px;
#         font-size: 12px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown('<p class="footer">Made with ❤️ by Team 7</p>', unsafe_allow_html=True)

# # link to another page
# st.markdown(
#     """
#     <style>
#     .credits {
#         position: fixed;
#         right: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #f1f1f1;
#         color: black;
#         text-align: center;
#         padding: 10px;
#         font-size: 12px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown('<p class="credits"> <a href="Stress_Sleep-disorder_predictor\ReadMe.md " target="google">Credits</a></p>', unsafe_allow_html=True)




import streamlit as st
import pandas as pd
import joblib
# Load models and data
regr = joblib.load('Code/regr.pkl')
clf = joblib.load('Code/clf.pkl')
feature_columns = joblib.load('Code/feature_columns.pkl')
scaler_dict = joblib.load('Code/scaler_dict.pkl')
catData = joblib.load('Code/catData.pkl')
label_encoding_dict = joblib.load('Code/label_encoding_dict.pkl')
numData = joblib.load('Code/numData.pkl')
unique_values = joblib.load('Code/unique_values.pkl')

# Set page configuration (must be the first command)
st.set_page_config(
    page_title="Stress & Sleep Disorder Predictor",
    page_icon="🌜",
    layout="centered"
)

# Function to show the main app
def main_page():
    st.title("Stress and Sleep Disorder Predictor 🔮")
    st.markdown("""
    ### Understand your health better
    This tool helps predict your stress levels and the likelihood of sleep disorders based on lifestyle and health data.

    Please fill in the details on the **sidebar**, and let's get started!
    """)
    st.image('Code/mindful.png', use_container_width=True)

    # Sidebar inputs and main logic as in your provided code...
    st.sidebar.header("Input Your Details")

    input_data = {}
    input_data['Gender'] = st.sidebar.selectbox(
        'Gender 👩‍♂️‍♀️', unique_values['Gender']
    )

    input_data['Age'] = st.sidebar.number_input(
        'Age 📈', min_value=0, max_value=150, step=1, value=None, placeholder='Enter Age'
    )

    input_data['Occupation'] = st.sidebar.selectbox(
        'Occupation 💼', unique_values['Occupation']
    )

    input_data['Sleep Duration'] = st.sidebar.number_input(
        'Sleep Duration (hours) 💤', min_value=0, max_value=24, step=1, value=None, placeholder='Enter Sleep Duration'
    )

    input_data['Quality of Sleep'] = st.sidebar.number_input(
        'Sleep Quality (out of 10) 💭', min_value=0, max_value=10, step=1, value=None, placeholder='Rate Your Sleep Quality'
    )

    input_data['Physical Activity Level'] = st.sidebar.number_input(
        'Physical Activity Level (out of 100) 🏃', min_value=0, max_value=100, step=1, value=None, placeholder='Enter Physical Activity Level'
    )

    input_data['BMI Category'] = st.sidebar.selectbox(
        'BMI Category 🍎', unique_values['BMI Category']
    )

    input_data['Heart Rate'] = st.sidebar.number_input(
        'Heart Rate (BPM) 💓', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Heart Rate'
    )

    input_data['Daily Steps'] = st.sidebar.number_input(
        'Daily Step Count 👣', min_value=0, max_value=50000, step=1, value=None, placeholder='Enter Daily Step Count'
    )

    input_data['Diastolic Pressure'] = st.sidebar.number_input(
        'Diastolic Pressure (mmHg) 🔻', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Diastolic Pressure'
    )

    input_data['Systolic Pressure'] = st.sidebar.number_input(
        'Systolic Pressure (mmHg) 🔻', min_value=0, max_value=200, step=1, value=None, placeholder='Enter Systolic Pressure'
    )

    # Validate Input
    valid_inputs = all(value is not None for value in input_data.values())

    if valid_inputs:
        input_df = pd.DataFrame([input_data])
        st.write("### Your Input Details")
        st.dataframe(input_df)

        # Stress Prediction
        
        if st.button('Predict Stress Level 🔮'):  
            for category in catData:
                if category != 'Sleep Disorder':
                    input_df[category] = label_encoding_dict[category].transform(input_df[category])
            for f in numData:
                input_df[f] = scaler_dict[f].transform(input_df[[f]])
            stress_level = regr.predict(input_df)
            if stress_level < 4:
                st.success(f'Predicted Stress Level: {stress_level[0]:.2f} 🌈 Excellent, You are Stress Free. Keep it up!')
            elif 4 <= stress_level < 5:
                st.info(f'Predicted Stress Level: {stress_level[0]:.2f} 🌟 Good, stay balanced!')
            elif 5 <= stress_level < 6:
                st.info(f'Predicted Stress Level: {stress_level[0]:.2f} ⭐ Absolutely Normal for working professionals.')
            elif 6 <= stress_level < 7:
                st.warning(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Are you bit Stressed? Please Take care of yourself.')
            elif 7 <= stress_level < 8:
                st.warning(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Do you feel Stressed? Need improvement in stress management.')
            else:
                st.error(f'Predicted Stress Level: {stress_level[0]:.2f} 🤔Oh, It seems You have high stress, Please Take care of yourself and seek support.')
            st.error('**This is a prediction and not a substitute for medical advice.**')
        # Sleep Disorder Prediction
        if st.button('Predict Sleep Disorder 🔮'):
            for category in catData:
                if category != 'Sleep Disorder':
                    input_df[category] = label_encoding_dict[category].transform(input_df[category])
            for f in numData:
                input_df[f] = scaler_dict[f].transform(input_df[[f]])

            sleep_disorder = clf.predict(input_df)
            prediction = label_encoding_dict['Sleep Disorder'].inverse_transform([sleep_disorder])[0]

            if prediction == 'None':
                st.success(f'Predicted Sleep Disorder: None 🌈 Great! You seem to have no issues with sleep.')
            elif prediction == 'Sleep Apnea':
                st.warning(f'Predicted Sleep Disorder: Sleep Apnea 👨‍⚕️ Please consult a doctor.')
            elif prediction == 'Insomnia':
                st.warning(f'Predicted Sleep Disorder: Insomnia 👨‍⚕️ Consider seeking professional help.')
            st.error('**This is a prediction and not a substitute for medical advice.**')
    else:
        st.error("Please fill in all the input fields to proceed!")
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-size: 16px;">'
        '<a href="/?page=credits" target="_self" style="text-decoration: none; color: #4CAF50;">'
        'Made by Vishnu & Team</a></p>', 
        unsafe_allow_html=True
    )

# Function to show the credits page
def credits_page():
    st.title("Credits")
    st.markdown("""
    ### Meet the Team
    - **Vishnu Shreeram M P**: [LinkedIn](https://www.linkedin.com/in/vishnu-shreeram/) | [GitHub](https://github.com/VISHNU-SHREERAM) | [Portfolio](https://vishnu-shreeram.github.io/my_portfolio/)
    - **Bhupathi Varun**: [LinkedIn](https://www.linkedin.com/in/bhupathi-varun-17b65a259/) | [GitHub](https://github.com/cvbshcbad)
    - **Bhogaraju Shanmukha Sri Krishna**: [LinkedIn](https://www.linkedin.com/in/shanmukha-sri-krishna-135316284/) | [GitHub](https://github.com/wanderer3519)

    ### About the Project
    This project is done under the course, DS3010: Introduction to Machine Learning
    at IIT Palakkad.
    This project was created to assist individuals in better understanding their stress levels and sleep patterns. By leveraging data and predictive modeling, we aim to promote health awareness and preventive care.
    """)
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-size: 16px;">'
        '<a href="/?page=main" target="_self" style="text-decoration: none; color: #4CAF50;">'
        'Back to Main Page</a></p>', 
        unsafe_allow_html=True
    )

# Handle navigation using st.query_params
page = st.query_params.get("page", "main")

if page == "main":
    main_page()
elif page == "credits":
    credits_page()

