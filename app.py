import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from uuid import uuid4
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Misinformation Susceptibility Test (MIST)",
    page_icon="🧐"
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

col1, col2 = st.columns([1,2])
with col1:
    image = Image.open('logo.jpg')
    st.image(image,caption=None,output_format="JPEG")
with col2:
    pass



st.subheader("Misinformation Susceptibility Test")
st.markdown("**Think you can beat misinformation? Try this comprehensive test of misinformation susceptibility.**")
st.markdown("It only takes 2 minutes!")
st.markdown("")
st.markdown("Read more: [Cambridge](https://www.cam.ac.uk/stories/mist), [YouGov](https://today.yougov.com/topics/politics/articles-reports/2023/06/28/americans-distinguish-real-fake-news-headline-poll), [Forbes](https://www.forbes.com/sites/conormurray/2023/06/28/gen-z-and-millennials-more-likely-to-fall-for-fake-news-than-older-people-test-finds/amp/)")
st.markdown("*Dr Rakoen Maertens, University of Cambridge, Department of Psychology, rm938@cam.ac.uk*")
st.markdown('<p style="font-size: 10px;">Maertens, R.*, Götz, F. M.*, Golino, H. F., Roozenbeek, J., Schneider, C. R., Kyrychenko, Y., Kerr, J. R., Stieger, S., McClanahan, W. P., Drabot, K., He, J., & van der Linden, S. (2023). The Misinformation Susceptibility Test (MIST): A psychometrically validated measure of news veracity discernment. <i>Behavior Research Methods.</i> Advance online publication. <a href="https://doi.org/10.3758/s13428-023-02124-2">https://doi.org/10.3758/s13428-023-02124-2</a></p>', unsafe_allow_html=True)
placeholder = st.empty()
with placeholder.container():
    with st.expander("Consent", expanded=True):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            In this study, you will be asked to rate 20 news headlines as real or fake and answer a few optional questions about your background. It should take 2-3 minutes to complete. All data will be kept completely anonymous as per the privacy policy below. **You must be 18 years or older to participate.** You can use the app without sharing your data by clicking 'No, I do not consent'.
            
            This study is led by Dr Rakoen Maertens (rm938@cam.ac.uk), Yara Kyrychenko (yk408@cam.ac.uk) and Professor Sander van der Linden (sv395@cam.ac.uk), Department of Psychology, University of Cambridge.
            """)
 
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publicly available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science practices by academic journals. **If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data by emailing Yara Kyrychenko (yk408@cam.ac.uk) with the ID within one year of study completion.** If you lose this ID, you can tell us the Twitter handle you entered instead. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md) or navigate to https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md.

        This privacy policy was last updated on May 13, 2023.
        """)
        
        st.markdown("###### Consent")
        st.radio("**Do you consent to participating in this study and sharing anonymized information?**", ["","Yes, I consent", "No, I do not consent"], key = "consent",label_visibility="visible", horizontal=True)
        agree = st.session_state.consent == "Yes, I consent" 
        disagree = st.session_state.consent == "No, I do not consent" 
      
        

if agree:
    placeholder.empty()
    if "id" not in st.session_state:
        st.session_state.id = datetime.now().strftime('%Y%m-%d%H-%M-') + str(uuid4())
    with st.expander("Privacy and study information", expanded=False):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            All data will be kept completely anonymous as per the privacy policy below. You must be 18 years or older to participate. You can use the app without sharing your data by clicking 'No, I do not consent'.
            
            This study is led by Dr Rakoen Maertens (rm938@cam.ac.uk), Yara Kyrychenko (yk408@cam.ac.uk) and Professor Sander van der Linden (sv395@cam.ac.uk), Department of Psychology, University of Cambridge.
            """)
        st.markdown("**You consented.**")
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publicly available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science practices by academic journals. **If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data by emailing Yara Kyrychenko (yk408@cam.ac.uk) with the ID within one year of study completion.** If you lose this ID, you can tell us the Twitter handle you entered instead. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md) or navigate to https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md.

        This privacy policy was last updated on May 13, 2023.
        """)
        

if disagree:
    st.session_state.dem_submitted = False
    placeholder.empty()
    with st.expander("Privacy and study information", expanded=False):
        st.markdown("##### Take Part in Our Study")
        st.markdown("""
            Please consider participating in our research study about misinformation susceptibility online.
            
            In this study, you will be asked to rate 20 news headlines as real or fake and answer a few optional questions about your background. It should take 2-3 minutes to complete. All data will be kept completely anonymous as per the privacy policy below. You must be 18 years or older to participate. You can use the app without sharing your data by clicking 'No, I do not consent'.
            
            This study is led by Dr Rakoen Maertens (rm938@cam.ac.uk), Yara Kyrychenko (yk408@cam.ac.uk) and Professor Sander van der Linden (sv395@cam.ac.uk), Department of Psychology, University of Cambridge.
            """)
        st.markdown("**You did not consent.**")
        st.markdown("")
        st.markdown("###### Privacy Policy")
        st.markdown("""
        To safeguard your privacy, we will only collect data on information you choose to share with us if you consent to participating in the study. This may include your Twitter handle, publicly available information on your Twitter timeline, and any questions you voluntarily choose to answer. Aggregate data will be used for research purposes to understand people's social media behavior. Limited, de-identified raw data may also be shared (with strict privacy protections to ensure no personal data is identifiable) to conform with open science practices by academic journals. **If you wish to delete your data, we will generate an anonymous ID you can use to request deletion of your data by emailing Yara Kyrychenko (yk408@cam.ac.uk) with the ID within one year of study completion.** If you lose this ID, you can tell us the Twitter handle you entered instead. This project has been reviewed by the Cambridge Psychology Research Ethics Committee. Please direct all inquiries about this consent form or privacy policy to Yara Kyrychenko (yk408@cam.ac.uk).
        
        To view the full privacy policy, please click [here](https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md) or navigate to https://github.com/yarakyrychenko/mist/blob/main/PrivacyPolicy.md.

        This privacy policy was last updated on May 13, 2023.
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
        st.session_state.mist_item_labels = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10",
                                                "t1","t2","t3","t4","t5","t6","t7","t8","t9","t10"] 
        st.session_state.labels = ["Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake","Fake",
                                       "Real","Real","Real","Real","Real","Real","Real","Real","Real","Real"]
            
        if "order" not in st.session_state:
            st.session_state.order = ['', 'Real','Fake'] if np.random.random() <= .5 else ['','Fake','Real']
        if "items_order" not in st.session_state:
            st.session_state.items_order = np.arange(20)
            np.random.shuffle(st.session_state.items_order)
        st.session_state.answers = []
            
        with st.form("my_form"): #st.expander("**Start the test!** 🧐",expanded=False):
            st.markdown("##### Please categorize the following news headlines as either 'Fake News' or 'Real News'.") 
            
            j=0
            for i in st.session_state.items_order:
                j+=1
                st.session_state.answers.append(st.radio(st.session_state.mist_items[i], st.session_state.order, key = "q"+str(j+1), format_func=format, label_visibility="visible", horizontal=True))

            st.session_state.disable = True if len([answer for answer in st.session_state.answers if answer != '']) != 20 else False		             
            if not st.session_state.submitted:
                st.session_state.submitted = st.form_submit_button("Submit")#st.button("Submit", disabled=st.session_state.disable, key="sub")
            else:
                st.form_submit_button("Submit") #st.button("Submit", disabled=st.session_state.disable, key="sub")
         
    if st.session_state.submitted and not st.session_state.disable:
        
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
                countries = ["Select Country","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Channel Islands","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Côte d'Ivoire",
                             "Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Faeroe Islands","Fiji","Finland","France","French Guiana","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kosovo","Kuwait","Kyrgyzstan",
                             "Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mayotte","Mexico","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Pakistan","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Réunion","Saint Helena","Saint Kitts and Nevis",
                             "Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","State of Palestine","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","The Bahamas","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Western Sahara","Yemen","Zambia","Zimbabwe"]
                with st.expander("Optional Questions", expanded=True):
                    st.markdown("*Your answers to these questions are not taken into considerations when calculating your MIST results.*")
                    st.text_input('What is your Twitter handle?', key="twitter_handle")
                    st.slider('What is your age?', 0, 130, key="age")
                    st.radio('What is your gender?', ['', 'Male', 'Female', 'Non-binary/Third'],key="gender")
                    st.radio('What is the highest level of education you completed?', ['', 'High School or Less', 'Some University but no degree', 'University Bachelors Degree','Graduate or professional degree (e.g., MA, PhD, MD)' ], key="education")
                    st.radio('What is your political orientation?', ['', 'Extremely liberal', 'Liberal', 'Slightly liberal', 'Moderate', 'Slightly conservative', 'Conservative', 'Extremely conservative'],key="politics")
                    st.selectbox('Which country do you live in?', countries,key="country")
                    st.radio('How good do you think your ability to distinguish real news from fake news is?', ['', 'Very poor', 'Poor', 'Average', 'Good', 'Very good'],key="perceived_ability")
                
                    st.session_state.dem_submitted = st.button("Submit",key="dem_sub")

        if st.session_state.dem_submitted:
            demplaceholder.empty()
            with st.expander("Your app ID", expanded=True):
                st.markdown(f"Thanks for participating in our study! Your app ID is **{st.session_state.id}**. Email Yara Kyrychenko ([yk408@cam.ac.uk](mailto:yk408@cam.ac.uk)) with it within one year if you want your answers deleted.") 
                st.markdown("*Your answers to the optional questions are not taken into considerations when calculating your MIST results.*")


        if st.session_state.dem_submitted or disagree:
            if "country" not in st.session_state:
                st.session_state.UKorUS = "US" 
                st.session_state.table =  st.session_state.ustable
            elif st.session_state.country == "United Kingdom":
                st.session_state.UKorUS = "UK" 
                st.session_state.table =  st.session_state.uktable
            else:
                st.session_state.UKorUS = "US" 
                st.session_state.table =  st.session_state.ustable
                
            #with st.expander("scores", expanded=True):
            st.session_state.score_print = st.session_state.score - 10 if st.session_state.score - 10 >= 0 else 0
            
            st.session_state.dn = st.session_state.n - st.session_state.d
            st.session_state.sign = "" if st.session_state.dn <= 0 else "+"
            st.session_state.good = "is **great**!" if st.session_state.score > 16 else "is **good**!" if st.session_state.score > 13 else "**needs some work**..."
            st.session_state.skeptical = "skeptical" if st.session_state.dn < 0 else "trusting" if st.session_state.dn > 0 else "neither too skeptical nor too gullible"
            st.session_state.how = "might be **a bit " if np.linalg.norm(st.session_state.dn) < 4 else "might be **very " if np.linalg.norm(st.session_state.dn) < 8 else "might be **overly "
            st.session_state.how = st.session_state.how if st.session_state.dn != 0 else "are **"
            if st.session_state.score > 16:
                st.balloons()
                with st.expander("", expanded=True):
                    st.subheader("🎉 Congratulations!")
                    st.markdown(f"**You're more resilient to misinformation than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population!**") 
                    st.subheader(f"📈 Your MIST results: {st.session_state.score}/20")
                    st.markdown(f"**Veracity Discernment: {10*st.session_state.score_print}%** *(ability to accurately distinguish real news from fake news)*")
                    st.markdown(f"**Real News Detection: {10*st.session_state.r}%** *(ability to correctly identify real news)*")
                    st.markdown(f"**Fake News Detection: {10*st.session_state.f}%** *(ability to correctly identify fake news)*")
                    st.markdown(f"**Distrust/Naïvité: {st.session_state.sign}{st.session_state.dn}** *(ranges from -10 to +10, overly skeptical to overly gullible)*")
                    st.markdown(f"👉 Your ability to recognize real and fake news {st.session_state.good} You {st.session_state.how}{st.session_state.skeptical}** when it comes to the news.")
                    components.html(
            f"""<a class="twitter-share-button" href="https://twitter.com/intent/tweet" data-text="I scored {st.session_state.score}/20 on MIST, better than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population. Test your misinformation susceptibility now! What is #YourMIST? 🧐"  data-url="yourmist.streamlit.app" data-hashtags="misinformation,fakenews"> 
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></a>
            """, width=100, height=30)
                    
            elif 13 < st.session_state.score <= 16:
                with st.expander("", expanded=True):
                    st.subheader("👍 Good try!")
                    st.markdown(f"**You're more resilient to misinformation than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population!**")  
                    st.subheader(f"📈 Your MIST results: {st.session_state.score}/20")
                    st.markdown(f"**Veracity Discernment: {10*st.session_state.score_print}%** *(ability to accurately distinguish real news from fake news)*")
                    st.markdown(f"**Real News Detection: {10*st.session_state.r}%** *(ability to correctly identify real news)*")
                    st.markdown(f"**Fake News Detection: {10*st.session_state.f}%** *(ability to correctly identify fake news)*")
                    st.markdown(f"**Distrust/Naïvité: {st.session_state.sign}{st.session_state.dn}** *(ranges from -10 to +10, overly skeptical to overly gullible)*")
                    st.markdown(f"👉 Your ability to recognize real and fake news {st.session_state.good} You {st.session_state.how}{st.session_state.skeptical}** when it comes to the news.")
                    components.html(
            f"""<a class="twitter-share-button" href="https://twitter.com/intent/tweet" data-text="I scored {st.session_state.score}/20 on MIST, better than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population. Test your misinformation susceptibility now! What is #YourMIST? 🧐"  data-url="yourmist.streamlit.app" data-hashtags="misinformation,fakenews"> 
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></a>
            """, width=100, height=30)
                    
            else:
                with st.expander("", expanded=True):
                    st.subheader("⚠️ You might be susceptible!")
                    st.markdown(f"**You're more resilient to misinformation than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population!**")
                    st.subheader(f"📈 Your MIST results: {st.session_state.score}/20")
                    st.markdown(f"**Veracity Discernment: {10*st.session_state.score_print}%** *(ability to accurately distinguish real news from fake news)*")
                    st.markdown(f"**Real News Detection: {10*st.session_state.r}%** *(ability to correctly identify real news)*")
                    st.markdown(f"**Fake News Detection: {10*st.session_state.f}%** *(ability to correctly identify fake news)*")
                    st.markdown(f"**Distrust/Naïvité: {st.session_state.sign}{st.session_state.dn}** *(ranges from -10 to +10, overly skeptical to overly gullible)*")
                    st.markdown(f"👉 Your ability to recognize real and fake news {st.session_state.good} You {st.session_state.how}{st.session_state.skeptical}** when it comes to the news.")
                    components.html(
            f"""<a class="twitter-share-button" href="https://twitter.com/intent/tweet" data-text="I scored {st.session_state.score}/20 on MIST, better than {st.session_state.table[st.session_state.score-1]}% of the {st.session_state.UKorUS} population. Test your misinformation susceptibility now! What is #YourMIST? 🧐"  data-url="yourmist.streamlit.app" data-hashtags="misinformation,fakenews"> 
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></a>
            """, width=100, height=30)
          
  

        if st.session_state.dem_submitted:
            if "inserted" not in st.session_state:
                if st.session_state.twitter_handle != "":
                    from cryptography.fernet import Fernet
                    fernet = Fernet(st.secrets["key"].encode())
                    st.session_state.twitter_handle_hash = fernet.encrypt(st.session_state.twitter_handle.encode()).decode()
                else:
                    st.session_state.twitter_handle_hash = ""
                    
                user_data = {
                            "id": st.session_state.id, 
                            "score": st.session_state.score, 
                            "r": st.session_state.r,
                            "f": st.session_state.f,
                            "n": st.session_state.n,
                            "d": st.session_state.d,
                            "twitter_handle": st.session_state.twitter_handle_hash,
                            "age": st.session_state.age,
                            "gender": st.session_state.gender,
                            "education": st.session_state.education,
                            "politics": st.session_state.politics,
                            "country": st.session_state.country,
                            "perceived_ability": st.session_state.perceived_ability
                            }
                item_data = {st.session_state.mist_item_labels[st.session_state.items_order[i]]: st.session_state.answers[i] for i in range(20)}
                user_data.update(item_data)
                
                from pymongo.mongo_client import MongoClient
                from pymongo.server_api import ServerApi
                with MongoClient(st.secrets["mongo"],server_api=ServerApi('1')) as client:
                    db = client.mist
                    collection = db.app
                    collection.insert_one(user_data)  
                    st.session_state.inserted = True
