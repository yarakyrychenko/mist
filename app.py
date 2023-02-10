import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from datetime import datetime
from uuid import uuid4
import seaborn as sns 
import pandas as pd, numpy as np


st.set_page_config(
    page_title="MIST",
    page_icon="🧐",
    layout="wide",
    menu_items={
         'About': "# Test your misinformation susceptibility." }
)


sns.set(rc={'figure.figsize':(4,5)})
sns.set_style("whitegrid")

st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True
)

def format(option):
    return ""

st.session_state.one_columns_params = (.1, 3.2, .1)
st.session_state.radio_columns_params = (4.5, 1)

row0sep1, row0col1, row0sep2 = st.columns(st.session_state.one_columns_params)
with row0sep1:
    st.markdown("")

with row0col1:
    st.markdown("<h1 style='text-align: center;'> 🧐 MIST 🧐 </h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'> Test your misinformation susceptibility </h2>", unsafe_allow_html=True)

    placeholder = st.empty()
    with placeholder.container():
        with st.expander("Consent", expanded=True):
            st.markdown("""
            By submitting the form below you agree to your data being used for research. 
            Your twitter handle will be stored in a private data base and will not be shared with anyone other than the researchers (unless extraordinary circumstances force us to). 
            You can ask for your data to be deleted by emailing us with an ID number you'll be issued after submitting the form. 
            """)
            agree = st.checkbox("I understand and consent.")

    if agree:
        placeholder.empty()
        with st.expander("Consent", expanded=False):
            st.markdown("""
            By submitting the form below you agree to your data being used for research. 
            Your twitter handle will be stored in a private data base and will not be shared with anyone other than the researchers (unless extraordinary circumstances force us to). 
            You can ask for your data to be deleted by emailing us with an ID number you'll be issued after submitting the form. 
            """)
            st.markdown("You have consented.")
     
with row0sep2:
    st.markdown("")   

st.session_state.submitted = False
st.session_state.disable = True 
st.session_state.two_columns_params = (.1, 1.5, .2, 1.5, .1)


if agree:
    import pymongo

    #client = pymongo.MongoClient(st.secrets["mongo"])
    #db = client.polarization
    #st.session_state.collection = db.app

    formsep1, formcol1, formsep2 = st.columns(st.session_state.one_columns_params)
    with formsep1:
        st.markdown("")

    with formcol1:
        form_place = st.empty()
        with form_place.container():
            st.session_state.mist_items = [
             "Government Officials Have Manipulated Stock Prices to Hide Scandals",
             "The Corporate Media Is Controlled by the Military-industrial Complex: The Major Oil Companies Own the Media and Control Their Agenda",
             "New Study: Left-Wingers Are More Likely to Lie to Get a Higher Salary",
             "The Government Is Manipulating the Public's Perception of Genetic Engineering in Order to Make People More Accepting of Such Techniques",
             "Left-Wing Extremism Causes 'More Damage' to World Than Terrorism, Says UN Report",
             "Certain Vaccines Are Loaded with Dangerous Chemicals and Toxins",
             "New Study: Clear Relationship Between Eye Color and Intelligence",
             "The Government Is Knowingly Spreading Disease Through the Airwaves and Food Supply",
             "Ebola Virus 'Caused by US Nuclear Weapons Testing', New Study Says",
             "Government Officials Have Illegally Manipulated the Weather to Cause Devastating Storms",
             "Attitudes Toward EU Are Largely Positive, Both Within Europe and Outside It",
             "One-in-Three Worldwide Lack Confidence in NGOs",
             "Reflecting a Demographic Shift, 109 US Counties Have Become Majority Nonwhite Since 2000",
             "International Relations Experts and US Public Agree: America Is Less Respected Globally",
             "Hyatt Will Remove Small Bottles from Hotel Bathrooms by 2021",
             "Morocco’s King Appoints Committee Chief to Fight Poverty and Inequality",
             "Republicans Divided in Views of Trump’s Conduct, Democrats Are Broadly Critical",
             "Democrats More Supportive than Republicans of Federal Spending for Scientific Research",
             "Global Warming Age Gap: Younger Americans Most Worried",
             "US Support for Legal Marijuana Steady in Past Year"
            ]
            st.session_state.labels = ["Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake",
                                       "Real","Real","Real","Real","Real","Real","Real","Real","Real","Real"]
            
            if "order" not in st.session_state:
                st.session_state.order = ['', 'Real','Fake'] if np.random.random() <= .5 else ['','Fake','Real']
            if "items_order" not in st.session_state:
                st.session_state.items_order = np.arange(20)
                np.random.shuffle(st.session_state.items_order)
            st.session_state.answers = []
            
            with st.expander("Form",expanded=True):
                st.markdown("##### Please categorize the following news headlines as either 'Fake News' or 'Real News'.")
                formprompt, formchoice = st.columns(st.session_state.radio_columns_params)
                with formprompt:
                    st.markdown("")
                with formchoice:
                    col1f, col2f = st.columns((.5,.5))
                    with col1f:
                        st.write(f"{st.session_state.order[1]}")
                    with col2f:
                        st.write(f"{st.session_state.order[2]}")
                    
                j =0
                for i in st.session_state.items_order:
                    j+=1
                    formprompt, formchoice = st.columns(st.session_state.radio_columns_params)
                    with formprompt:
                        st.write("")
                        st.markdown(st.session_state.mist_items[i])
                    with formchoice:
                        st.session_state.answers.append(st.radio("", st.session_state.order, key = "q"+str(j+1), format_func=format, label_visibility="collapsed", horizontal=True))
                     
                st.session_state.disable = True if st.session_state.q20 == "" else False
 
                #if st.session_state.disable:
                   # st.warning("Please fill out every field of the form to enable the submit button.")              
                st.session_state.submitted = st.button("Submit", disabled=st.session_state.disable)
        
        if  st.session_state.submitted:
            #form_place.empty()
            pass
 
        with st.expander("Form Submitted",expanded=True):
            if st.session_state.submitted:
                st.session_state.id = datetime.now().strftime('%Y%m-%d%H-%M-') + str(uuid4())
                st.markdown(f"Thanks for submitting your answers! Your app ID is **{st.session_state.id}**. [Email me](mailto:yara@nyu.edu) with it if you want your answers deleted.") 

                user_data = {
                            "id": st.session_state.id, 
                            "answers": st.session_state.answers, 
                            }

                #st.session_state.collection.insert_one(user_data)        

    with formsep2:
        st.markdown("")

    if st.session_state.submitted:
        st.session_state.graded = []
        st.session_state.r = 0
        st.session_state.f = 0
        st.session_state.d = 0
        st.session_state.n = 0
        
        for i in st.session_state.items_order:
            if st.session_state.labels[i] == st.session_state.answers[i]:
                st.session_state.graded.append(1)
                st.session_state.r += 1 if st.session_state.labels[i] == 'Real' else 0
                st.session_state.f += 1 if st.session_state.labels[i] == 'Fake' else 0
            else:
                st.session_state.graded.append(0)
            st.session_state.d += 1 if st.session_state.answers[i] == 'Fake' else 0
            st.session_state.n += 1 if st.session_state.answers[i] == 'Real' else 0
        
        st.session_state.d = st.session_state.d - 10 if st.session_state.d - 10 >= 0 else 0
        st.session_state.n = st.session_state.n - 10 if st.session_state.n - 10 >= 0 else 0
        
        st.markdown(f"Veracity Discernment: {int(np.sum(st.session_state.graded))}")
        st.markdown(f"Real News Detection: {st.session_state.r}")
        st.markdown(f"Fake News Detection: {st.session_state.f}")
        st.markdown(f"Distrust: {st.session_state.d}")
        st.markdown(f"Naïvité: {st.session_state.n}")
        
        st.markdown("")
        st.markdown("***")
        components.html(
            """
            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
            data-text="Test your misinformation susceptibility now! 🧐" 
            data-url="https://share.streamlit.io/yarakyrychenko/mist/main/app.py"
            data-show-count="false">
            data-size="Large" 
            data-hashtags="misinformation,fakenews"
            Tweet
            </a>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            """
                   )
