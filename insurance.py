#import packages
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import base64
import warnings
warnings.filterwarnings("ignore")

#streamlit  background color
page_bg_color='''
<style>
[data-testid="stAppViewContainer"]{
        background-color:#FFDAB9;
}
</style>'''

#streamlit button color
button_style = """
    <style>
        .stButton>button {
            background-color: #ffa089 ; 
            color: black; 
        }
        .stButton>button:hover {
            background-color: #ffddca; 
        }
    </style>    
"""
#streamlit settings
st.set_page_config(
    page_title="Customer Conversion Prediction",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="auto")


st.markdown(page_bg_color,unsafe_allow_html=True)  #calling background color
st.markdown(button_style, unsafe_allow_html=True)  #calling button color

st.title("Customer Conversion Prediction")

#menu
selected = option_menu(menu_title=None,options= ["HOME", "PREDICT STATUS"],icons=["house", "trophy"],
          default_index=0,orientation='horizontal',
          styles={"container": { "background-color": "white", "size": "cover", "width": "100"},
            "icon": {"color": "brown", "font-size": "20px"},

            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#ffe5b4"},
            "nav-link-selected": {"background-color": "#E2838A"}})

#selectbox
Job = ['management', 'technician', 'entrepreneur', 'blue-collar','unknown', 'retired', 'admin.', 'services', 'self-employed',
       'unemployed', 'housemaid', 'student']

Marital = ['single','divorced','married']

qual = ['tertiary', 'secondary', 'unknown', 'primary']

ctype = ['unknown', 'cellular', 'telephone']

date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

mon = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

calls = [1,2,3,4,5,6]

prev = ['unknown', 'failure', 'other', 'success']

#loading saved model and encoder using pickle
file_path_job = r'C:\Users\balak\guvi\customer\job_mapped.pkl'
with open(file_path_job, 'rb') as file1:
    loaded_job=pickle.load(file1)

file_path_marital = r'C:\Users\balak\guvi\customer\marital_mapped.pkl'
with open(file_path_marital, 'rb') as file2:
    loaded_marital=pickle.load(file2)

file_path_educa = r'C:\Users\balak\guvi\customer\educationqual_mapped.pkl'
with open(file_path_educa, 'rb') as file3:
    loaded_education=pickle.load(file3)

file_path_call = r'C:\Users\balak\guvi\customer\calltype_mapped.pkl'
with open(file_path_call, 'rb') as file4:
    loaded_call=pickle.load(file4)

file_path_month = r'C:\Users\balak\guvi\customer\month_mapped.pkl'
with open(file_path_month, 'rb') as file5:
    loaded_month=pickle.load(file5)

file_path_outcome = r'C:\Users\balak\guvi\customer\previous_outcome_mapped.pkl'
with open(file_path_outcome, 'rb') as file6:
    loaded_outcome=pickle.load(file6)

file_xgb_hyp = r'C:\Users\balak\guvi\customer\xgbclassifier_hyp.pkl'
with open(file_xgb_hyp, 'rb') as file:
    loaded_class_model=pickle.load(file)

#function convert gif to base 64
def get_img_base64(file_path):
    with open(file_path, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode()
    return encoded

approved_gif_base64 = get_img_base64(r"C:\Users\balak\guvi\customer\Insurance_anime.gif")
rejected_gif_base64 = get_img_base64(r"C:\Users\balak\guvi\customer\out1.gif")
insurance = get_img_base64(r"C:\Users\balak\guvi\customer\insu.jpg")

@st.cache_resource  

#function predict status
def predict_status(age,job,marital,education,ctype,day,month,duration,no_of_calls,outcome):
    
    job_encoded = loaded_job.get(job)
    marital_encoded = loaded_marital.get(marital)
    education_encoded = loaded_education.get(education)
    call_encoded = loaded_call.get(ctype)
    month_encoded = loaded_month.get(month)
    outcome_encoded = loaded_outcome.get(outcome)
    input_data = pd.DataFrame({
        'age': [int(age)],
        'job': [job_encoded],
        'marital': [marital_encoded],
        'education_qual': [education_encoded],
        'call_type': [call_encoded],
        'day': [int(day)],
        'mon': [month_encoded],
        'dur': [int(duration)],
        'num_calls': [int(no_of_calls)],
        'prev_outcome': [outcome_encoded]
    })
    categorical_columns = ['job', 'marital', 'education_qual', 'call_type', 'mon', 'prev_outcome']
    for column in categorical_columns:
        input_data[column] = input_data[column].astype('category')

    prediction = loaded_class_model.predict(input_data, validate_features=False)

    if prediction[0]==0:
        
        html_content = f"""
        <div style="display: flex; align-items: center;">
            <h4 style='color:red; margin-right: 10px;'>The client will <span style='color:purple;'>✅ SUBSCRIBE </span> to the insurance policy.</h4>
            <img src="data:image/gif;base64,{approved_gif_base64}" width="100" height="150">
            
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True) # calling yes status
    else:
        
        html1_content = f"""
        <div style="display: flex; align-items: center;">
            <h4 style='color:red; margin-right: 10px;'>The client will <span style='color:purple;'>❌ NOT SUBSCRIBE </span> to the insurance policy.</h4>
            <img src="data:image/gif;base64,{rejected_gif_base64}" width="150" height="150">
        </div>
        """
        st.markdown(html1_content,unsafe_allow_html=True)  #calling no status


#home page
if selected=="HOME":
    cola,colb=st.columns(2)
    with cola:
        html_image = f'''
        <img src="data:image/jpg;base64,{insurance}" style="width:600px; height:auto;" alt="Insurance Image">
        '''

        # Display the image using st.markdown
        st.markdown(html_image, unsafe_allow_html=True)
    with colb:
        st.write("")
        st.write('''**A new-age insurance company emplies mutiple outreach plans to sell term insurance to customers. Telephonic marketing campaigns still remain one of the most effective way to reach out to people however they incur a lot of cost. Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call. Given historical marketing data of the insurance company and are required to build a ML model that will predict if a client will subscribe to the insurance.**''')
       
    st.header(f"Classification: :red[ XGBClassifier(Extreme Gradient Boosting)]")
    st.write("*  ML Classification model which predicts whether the client will : :green[**SUBSCRIBE(YES)**]  or : :violet[**NOT SUBSCRIBE(NO)**] to the insurance policy.")
    st.write('- XGBoost, short for Extreme Gradient Boosting, is an optimized machine learning library for gradient boosting, a powerful ensemble technique used primarily for regression and classification tasks. It was developed to provide high performance, speed, and accuracy. The main idea behind gradient boosting is to build an ensemble of trees sequentially, where each subsequent tree corrects the errors of the previous trees.')


#predict status page
if selected=="PREDICT STATUS":
    col1,col2=st.columns(2)
    with col1:
        age = st.text_input("Enter Age")
        job = st.selectbox("Choose Job",Job,key=1)
        marital = st.selectbox("Choose Marital Status",Marital,key=2)
        education = st.selectbox("Choose Education Qualification", qual,key=3)
        calltype = st.selectbox("Choose Call Type", ctype,key=4)
        
        
    with col2:
        day = st.selectbox("Choose Day",date,key=5)
        month = st.selectbox("Choose Month",mon)
        duration = st.text_input("Enter Call Duration in Seconds")
        no_of_calls = st.selectbox("Choose Number of Calls",calls)
        outcome = st.selectbox("Choose Previous Outcome",prev)
        
    
    if st.button("Predict Status"):
        predict_status(age,job,marital,education,ctype,day,month,duration,no_of_calls,outcome) #calling ststus
      