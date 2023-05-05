import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from uuid import uuid4
import numpy as np


st.set_page_config(
    page_title="MIST Misinformation Susceptibility Test",
    page_icon="🧐",
    #layout="wide"
)

st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True
)

st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 16px;
}
    </style>
    """, unsafe_allow_html=True)

def format(option):
    return "Real" if option == "Real" else "Fake"


st.header("🧐 MIST Misinformation Susceptibility Test")
st.subheader("Think you can beat misinformation? Try this comprehensive test of misinformation susceptibility.")
st.markdown("*It only takes 2 minutes!*")

placeholder = st.empty()
with placeholder.container():
    with st.expander("Consent", expanded=True):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            All data will be kept completely anonymous as per the privacy policy below. You must be 18 years or older to participate. You can use the app without sharing your data by clicking 'No, I do not consent'.
            """)
        st.radio("**Do you consent to participating in this study and sharing anonymized information?**", ["","Yes, I consent", "No, I do not consent"], key = "consent",label_visibility="visible", horizontal=True)
        agree = st.session_state.consent == "Yes, I consent" 
        disagree = st.session_state.consent == "No, I do not consent" 
        
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publically available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science pratices by academic journals. If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data. Alternatively, if you lose this ID, you can tell us the Twitter handle that you entered and we can delete the data. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md).

        This privacy policy was updated on Feb 11, 2023.
        """)
        

if agree:
    placeholder.empty()
    with st.expander("Consent", expanded=False):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            All data will be kept completely anonymous as per the privacy policy below. You must be 18 years or older to participate. You can use the app without sharing your data by clicking 'No, I do not consent'.
            """)
        st.markdown("**You consented.**")
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publically available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science pratices by academic journals. If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data. Alternatively, if you lose this ID, you can tell us the Twitter handle that you entered and we can delete the data. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md).

        This privacy policy was updated on Feb 11, 2023.
        """)
        

if disagree:
    st.session_state.dem_submitted = False
    placeholder.empty()
    with st.expander("Consent", expanded=False):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            All data will be kept completely anonymous as per the privacy policy below. You must be 18 years or older to participate. You can use the app without sharing your data by clicking 'No, I do not consent'.
            """)
        st.markdown("**You did not consent.**")
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publically available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science pratices by academic journals. If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data. Alternatively, if you lose this ID, you can tell us the Twitter handle that you entered and we can delete the data. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md).

        This privacy policy was updated on Feb 11, 2023.
        """)

if "submitted" not in st.session_state:
    st.session_state.submitted = False        
if "dem_submitted" not in st.session_state:
    st.session_state.dem_submitted = False        
st.session_state.disable = True 

if agree or disagree:
    if True:
        st.session_state.mist_items = [
             "Government Officials Have Manipulated Stock Prices to Hide Scandals",
             "The Corporate Media Is Controlled by the Military-Industrial Complex: The Major Oil Companies Own the Media and Control Their Agenda",
             "New Study: Left-Wingers Are More Likely to Lie to Get a Higher Salary",
             "The Government Is Manipulating the Public's Perception of Genetic Engineering in Order to Make People More Accepting of Such Techniques",
             "Left-Wing Extremism Causes 'More Damage' to World Than Terrorism, Says UN Report",
             "Certain Vaccines Are Loaded with Dangerous Chemicals and Toxins",
             "New Study: Clear Relationship Between Eye Color and Intelligence",
             "The Government Is Knowingly Spreading Disease Through the Airwaves and Food Supply",
             "Ebola Virus 'Caused by US Nuclear Weapons Testing', New Study Says",
             "Government Officials Have Illegally Manipulated the Weather to Cause Devastating Storms",
             "Attitudes Toward EU Are Largely Positive, Both Within Europe and Outside It",
             "One-in-Three Worldwide Lack Confidence in Non-Governmental Organizations",
             "Reflecting a Demographic Shift, 109 US Counties Have Become Majority Nonwhite Since 2000",
             "International Relations Experts and US Public Agree: America Is Less Respected Globally",
             "Hyatt Will Remove Small Bottles from Hotel Bathrooms",
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
            
        with st.expander("Test",expanded=True):
            st.markdown("##### Please categorize the following news headlines as either 'Fake News' or 'Real News'.") 
            j=0
            for i in st.session_state.items_order:
                j+=1
                st.session_state.answers.append(st.radio(st.session_state.mist_items[i], st.session_state.order, key = "q"+str(j+1), format_func=format, label_visibility="visible", horizontal=True))
                     
            st.session_state.disable = True if len([answer for answer in st.session_state.answers if answer != '']) != 20 else False
            if not st.session_state.submitted:
                st.session_state.submitted = st.button("Submit", disabled=st.session_state.disable, key="sub")
            else:
                st.button("Submit", disabled=st.session_state.disable, key="sub")
         
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

        if agree:
            demplaceholder = st.empty()
        if agree and not st.session_state.dem_submitted:
            with demplaceholder.container():
                with st.expander("Optional Questions", expanded=True):
                    st.markdown("*Your answers to these questions are not taken into considerations when calculating your MIST results.*")
                    st.text_input('What is your Twitter handle?', key="twitter_handle")
                    st.text_input('What is your age?', key="age")
                    st.radio('What is your gender?', ['', 'Male', 'Female', 'Other'],key="gender")
                    st.radio('What the highest level of education you completed?', ['', 'High School or Less', 'Some College', 'Higher Degree'], key="education")
                    st.radio('What is your political orientation?', ['', 'Extremely liberal', 'Liberal', 'Slightly liberal', 'Moderate', 'Slightly conservative', 'Conservative', 'Extremely conservative'],key="politics")
                    st.radio('How good do you think your ability to distinguish real news from fake news is?', ['', 'Extremely poor', 'Poor', 'Average', 'Good', 'Extremely good'],key="perceived_ability")
                
                    st.session_state.dem_submitted = st.button("Submit",key="dem_sub")

        if st.session_state.dem_submitted:
            demplaceholder.empty()
            with st.expander("Optional Questions", expanded=True):
                st.session_state.id = datetime.now().strftime('%Y%m-%d%H-%M-') + str(uuid4())
                st.markdown(f"Thanks for participating in our study! Your app ID is **{st.session_state.id}**. [Email us](mailto:yk408@cam.ac.uk) with it if you want your answers deleted.") 
                st.markdown("*Your answers to the questions are not taken into considerations when calculating your MIST results.*")

        if st.session_state.dem_submitted or disagree:
            #with st.expander("scores", expanded=True):
            st.session_state.score_print = st.session_state.score - 10 if st.session_state.score - 10 >= 0 else 0
            components.html(
            f"""
            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
            data-text="I scored {10*st.session_state.score_print}% on veracity discernment, better than {st.session_state.ustable[st.session_state.score]}% of the US population. Test your misinformation susceptibility now! 🧐" 
            data-url="yourmist.streamlit.app"
            data-hashtags="misinformation,fakenews"> Tweet </a>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            """)
            
            if st.session_state.score > 16:
                st.balloons()
                st.header("🎉 Congratulations!")
            elif 13 < st.session_state.score <= 16:
                st.header("👍 Good try!")
            else:
                st.header("⚠️ You might be susceptible!")
        
            st.subheader(f"You're more resilient to misinformation than **{st.session_state.ustable[st.session_state.score]}%** of the US population and **{st.session_state.uktable[st.session_state.score]}%** of the UK!")
            st.markdown("")
        
            st.session_state.dn = st.session_state.n - st.session_state.d
            st.session_state.sign = "" if st.session_state.dn <= 0 else "+"
        
            st.header("📈 Your MIST results")
            st.markdown(f"**Veracity Discernment: {10*st.session_state.score_print}%** *(ability to accurately distinguish real news from fake news)*")
            st.markdown(f"**Real News Detection: {10*st.session_state.r}%** *(ability to correctly identify real news)*")
            st.markdown(f"**Fake News Detection: {10*st.session_state.f}%** *(ability to correctly identify fake news)*")
            st.markdown(f"**Distrust/Naïvité: {st.session_state.sign}{st.session_state.dn}** *(ranges from -10 to +10, overly skeptical to overly gullible)*")
            st.session_state.good = "is **great**!" if st.session_state.score > 16 else "is **good**!" if st.session_state.score > 13 else "**needs some work**..."
            st.session_state.skeptical = "skeptical" if st.session_state.dn < 0 else "trusting" if st.session_state.dn > 0 else "neither too skeptical nor too gullible"
            st.session_state.how = "might be **a bit " if np.linalg.norm(st.session_state.dn) < 4 else "might be **very " if np.linalg.norm(st.session_state.dn) < 8 else "might be **overly "
            st.session_state.how = st.session_state.how if st.session_state.dn != 0 else "are **"
            st.markdown(f"👉 Your ability to recognize real and fake news {st.session_state.good} You {st.session_state.how}{st.session_state.skeptical}** when it comes to the news.")
        
        if st.session_state.dem_submitted:
            #from pymongo.mongo_client import MongoClient
            #from pymongo.server_api import ServerApi

            #client = MongoClient(st.secrets["mongo"],server_api=ServerApi('1'))
            #db = client.mist
            #st.session_state.collection = db.app
           
            user_data = {
                            "id": st.session_state.id, 
                            "score": st.session_state.score, 
                            "r": st.session_state.r,
                            "f": st.session_state.f,
                            "n": st.session_state.n,
                            "d": st.session_state.d,
                            "twitter_handle": st.session_state.twitter_handle,
                            "age": st.session_state.age,
                            "gender": st.session_state.gender,
                            "education": st.session_state.education,
                            "politics": st.session_state.politics,
                            "perceived_ability": st.session_state.perceived_ability
                            }
            
            if "inserted" not in st.session_state:
                st.session_state.inserted = True
                #st.session_state.collection.insert_one(user_data)  
