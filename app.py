import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Loai abdalslam | Data Scientist", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


mkt_image = Image.open("images/mkt.js.png")
tdd_image = Image.open("images/tdd.png")
vgg_image = Image.open("images/vgg.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Loaii  :wave:")
    st.title("A Data Data Scientist From Egyot")
st.write("""
📈 **Data Scientist | Finance & Marketing Enthusiast | Stock Market Aficionado** 📊

Welcome to the world of numbers, trends, and market dynamics! I'm a passionate Data Scientist with a keen interest in the intersection of finance and marketing. Armed with a robust background in data analytics and machine learning, I navigate the intricate landscape of the stock market, transforming raw data into actionable insights.

🔍 **Expertise:**
My expertise lies in deciphering complex financial data, identifying patterns, and leveraging predictive modeling to make informed decisions. I thrive on extracting valuable insights that drive strategic initiatives in both finance and marketing realms.

💡 **Innovation in Finance:**
In the dynamic realm of finance, I specialize in developing cutting-edge algorithms and models to forecast market trends, risk analysis, and optimize investment portfolios. Whether it's predicting stock movements or optimizing trading strategies, I'm at the forefront of harnessing data for financial innovation.

📊 **Marketing Intelligence:**
On the marketing front, I leverage data to uncover consumer behaviors, preferences, and market trends. My proficiency in data-driven marketing strategies ensures that every campaign is meticulously crafted for maximum impact, targeting the right audience with precision.

🤖 **Tech Savvy:**
I am adept at utilizing advanced data science tools and technologies, including but not limited to Python, R, TensorFlow, and PyTorch. My skills extend to data preprocessing, feature engineering, and deploying models for real-world applications.

📈 **Continuous Learning:**
The fast-paced nature of finance and marketing demands perpetual learning. I stay ahead by constantly updating my skill set and staying abreast of the latest developments in data science, machine learning, and financial technologies.

🌐 **Global Perspective:**
Having worked in diverse financial markets, I bring a global perspective to my analyses. This broad view enables me to understand and adapt to different market dynamics and capitalize on emerging opportunities.

🚀 **Passion for Impact:**
Beyond numbers and algorithms, my ultimate passion lies in making a real-world impact. Whether it's optimizing investment strategies, enhancing marketing ROI, or contributing to financial innovation, I'm driven by a commitment to results that matter.

Let's connect and explore the endless possibilities at the intersection of data, finance, and marketing. Together, we can navigate the complexities of the stock market and shape data-driven success stories. 🚀💹
""")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating small mooc about datascience and machine learning for people who:
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/@GeekOasis_)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(mkt_image)
    with text_column:
        st.subheader("MKT.JS Automated Stock Prediction library")
        st.write(
            """
    
MKT.JS is a cutting-edge Automated Stock Prediction library designed to empower developers and financial enthusiasts with advanced tools for
 predicting stock market trends. Leveraging sophisticated algorithms and machine learning techniques, MKT.JS analyzes historical stock data,
  market indicators, and relevant financial information to generate accurate predictions regarding future stock movements. With its user-friendly
   interface and seamless integration capabilities, MKT.JS makes stock prediction accessible to a wide range of users, from seasoned traders to 
   beginners looking to explore the dynamic world of financial markets. Stay ahead of market fluctuations and make informed investment decisions
    with MKT.JS, the go-to solution for automated stock predictions.
            """
        )
        st.markdown("[To know More...](https://loaiabdalslam.github.io/mkt-website/)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(tdd_image)
    with text_column:
        st.subheader("Trend of Twitter Dashboard")
        st.write(
            """
The Trend of Twitter Dashboard is a dynamic and intuitive tool designed to provide users with real-time insights into
 the trending topics and discussions on Twitter. This powerful dashboard utilizes advanced algorithms to track and display
  the most popular hashtags, keywords, and conversations on the Twitter platform. Users can stay informed about the latest trends,
   breaking news, and viral discussions, making it an invaluable resource for marketers, social media managers, and individuals 
   seeking to understand the pulse of social media. With its visually engaging interface and customizable features, 
   the Trend of Twitter Dashboard offers a comprehensive overview of Twitter trends, enabling users to stay ahead of the curve
    in the fast-paced world of online discourse.
            """
        )
        st.markdown("[To know More...](https://loaiabdalslam.github.io/mkt-website/)")




with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(vgg_image)
    with text_column:
        st.subheader("Brain Tumor MRI Classification | VGG16")
        st.write(
     """
     The main purpose of this project was to build a CNN model that would classify if subject has a tumor or not base on MRI scan. 
     I used the VGG-16, Inception v3 , xception model architecture and weights to train the model for this binary problem.
            """
        )
        st.markdown("[To know More...](https://www.kaggle.com/code/loaiabdalslam/brain-tumor-mri-classification-vgg16#1.-Project-Overview-and-Objectives)")




