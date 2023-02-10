import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from datetime import datetime
from uuid import uuid4
import seaborn as sns 
import pandas as pd, numpy as np


st.set_page_config(
    page_title="MIST Misinformation Susceptibility Test",
    page_icon="🧐",
    #layout="wide"
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
    return "Real" if option == "Real" else "Fake"

st.session_state.one_columns_params = (.1, 3.2, .1)
st.session_state.radio_columns_params = (5, 1)

st.header("🧐 MIST Misinformation Susceptibility Test 🧐")
st.subheader("Think you can beat misinformation? Try this test! ")

placeholder = st.empty()
with placeholder.container():
    with st.expander("Consent", expanded=True):
        st.markdown("""
            By submitting the form below you agree to your data being used for research. 
            Your answers will be stored in a private data base and will not be shared with anyone other than the researchers. 
            You can ask for your answers to be deleted by emailing us with an ID number you'll be issued after submitting. 
            """)
        agree = st.checkbox("I understand and consent.")

if agree:
    placeholder.empty()
    with st.expander("Consent", expanded=False):
        st.markdown("""
            By submitting the form below you agree to your data being used for research. 
            Your answers will be stored in a private data base and will not be shared with anyone other than the researchers. 
            You can ask for your answers to be deleted by emailing us with an ID number you'll be issued after submitting. 
            """)
        st.markdown("You have consented.")
      
st.session_state.submitted = False
st.session_state.disable = True 
st.session_state.two_columns_params = (.1, 1.5, .2, 1.5, .1)

if agree:
    import pymongo

    #client = pymongo.MongoClient(st.secrets["mongo"])
    #db = client.polarization
    #st.session_state.collection = db.app


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
            
        with st.expander(" ",expanded=True):
            st.markdown("##### Please categorize the following news headlines as either 'Fake News' or 'Real News'.")
            #formprompt, formchoice = st.columns(st.session_state.radio_columns_params)
            #with formprompt:
            #    st.markdown("")
            #with formchoice:
            #    st.write(f"**{st.session_state.order[1]}**\t**{st.session_state.order[2]}**")
                    
            j =0
            for i in st.session_state.items_order:
                j+=1
                #formprompt, formchoice = st.columns(st.session_state.radio_columns_params)
                #with formprompt:
                    #st.markdown("")
                    #st.markdown(st.session_state.mist_items[i])
                #with formchoice:
                st.session_state.answers.append(st.radio(st.session_state.mist_items[i], st.session_state.order, key = "q"+str(j+1), format_func=format, label_visibility="visible", horizontal=True))
                     
            st.session_state.disable = True if len([answer for answer in st.session_state.answers if answer != '']) != 20 else False
 
                #if st.session_state.disable:
                   # st.warning("Please fill out every field of the form to enable the submit button.")   
            st.session_state.submitted = st.button("Submit", disabled=st.session_state.disable)
        
    if  st.session_state.submitted:
            #form_place.empty()
        pass
 
    with st.expander("Form Submitted",expanded=True):
        if st.session_state.submitted:
            st.session_state.id = datetime.now().strftime('%Y%m-%d%H-%M-') + str(uuid4())
            st.markdown(f"Thanks for submitting your answers! Your app ID is **{st.session_state.id}**. [Email us](mailto:yara@nyu.edu) with it if you want your answers deleted.") 

            user_data = {
                            "id": st.session_state.id, 
                            "answers": st.session_state.answers, 
                            }

                #st.session_state.collection.insert_one(user_data)        

    if st.session_state.submitted:
        st.session_state.graded = []
        st.session_state.r = 0
        st.session_state.f = 0
        st.session_state.d = 0
        st.session_state.n = 0
        
        for i in range(20):
            j = st.session_state.items_order[i]
            if st.session_state.labels[j] == st.session_state.answers[i]:
                st.session_state.graded.append(1)
                st.session_state.r += 1 if st.session_state.labels[j] == 'Real' else 0
                st.session_state.f += 1 if st.session_state.labels[j] == 'Fake' else 0
            else:
                st.session_state.graded.append(0)
            st.session_state.d += 1 if st.session_state.answers[i] == 'Fake' else 0
            st.session_state.n += 1 if st.session_state.answers[i] == 'Real' else 0
        
        st.session_state.d = st.session_state.d - 10 if st.session_state.d - 10 >= 0 else 0
        st.session_state.n = st.session_state.n - 10 if st.session_state.n - 10 >= 0 else 0
        
        st.session_state.ustable = {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:3, 8:6, 9:11, 10:20,
                                    11:28, 12:36, 13:44, 14:53, 15:62, 16:71, 17:81, 18:89, 19:96, 20:100}
        st.session_state.uktable = {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:3, 8:5, 9:10, 10:23,
                                    11:32, 12:43, 13:53, 14:63, 15:73, 16:83, 17:90, 18:95, 19:98, 20:100}
        st.session_state.score = int(np.sum(st.session_state.graded))
        
        if st.session_state.score > 15:
            st.balloons()
            st.markdown("##### 🎉 Congratulations!")
        if st.session_state.score <= 15:
            st.markdown("##### 👍 Good try!")
        
        st.markdown(f"###### You're more resilient to misinformation than **{st.session_state.ustable[st.session_state.score]}%** of the US population and **{st.session_state.uktable[st.session_state.score]}%** of the UK!")
        st.markdown("")
        
        st.session_state.score = st.session_state.score - 10 if st.session_state.score - 10 >= 0 else 0
        st.session_state.dn = st.session_state.n - st.session_state.d
        st.session_state.sign = "" if st.session_state.dn <= 0 else "+"
        
        st.markdown("##### 📈 Your MIST results")
        st.markdown(f"**Veracity Discernment: {10*st.session_state.score}%** *(ability to accurately distinguish real news from fake news)*")
        st.markdown(f"**Real News Detection: {10*st.session_state.r}%** *(ability to correctly identify real news)*")
        st.markdown(f"**Fake News Detection: {10*st.session_state.f}%** *(ability to correctly identify fake news)*")
        st.markdown(f"**Distrust/Naïvité: {st.session_state.sign}{st.session_state.dn}** *(ranges from -10 to +10, overly skeptical to overly gullible)*")
        #st.markdown(f"**Naïvité: {st.session_state.n - st.session_state.d}** *(positive judgment bias or being overly gullible)*")

        
        
        st.markdown("")
        st.markdown("***")
        components.html(
            f"""
            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
            data-text="I scored {10*st.session_state.score}% on veracity discernment, better than {st.session_state.ustable[st.session_state.score]}% of the US population. Test your misinformation susceptibility now! 🧐" 
            data-url="yourmist.streamlit.app"
            data-show-count="false">
            data-size="Large" 
            data-hashtags="misinformation,fakenews"
            Tweet
            </a>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            """
                   )
