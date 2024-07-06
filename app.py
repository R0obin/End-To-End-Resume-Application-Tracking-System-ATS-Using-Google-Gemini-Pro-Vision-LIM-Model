from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import pdf2image
import io
import os 
from PIL import Image
import base64
import google.generativeai as genai

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Generative AI response
def get_genai_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Function to convert PDF to images
def pdf_to_images(upload_file):
    poppler_path = r'poppler-24.02.0/Library/bin'
    images = pdf2image.convert_from_bytes(upload_file.read(), poppler_path=poppler_path)
    return images

# Function to setup PDF input
def input_pdf_setup(upload_file):
    if upload_file is not None:
        images = pdf_to_images(upload_file)
        first_page = images[0]

        # Converting first page into bytes
        img_bytes_arr = io.BytesIO()
        first_page.save(img_bytes_arr, format="JPEG")
        img_bytes_arr = img_bytes_arr.getvalue()

        pdf_part = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_bytes_arr).decode()  # Encode to base64
            }
        ]
        return pdf_part
    else:
        raise FileNotFoundError("Please Upload the File")

# Streamlit setup
st.set_page_config(page_title="ATS Resume Builder",
                   page_icon="💻",
                   layout= "centered"
                   )
st.header(" 📰 ATS Checking System")
input_text = st.text_area("Job Description", key='input')
upload_file = st.file_uploader("Upload your Resume(PDF)...", type=['pdf'])

if upload_file is not None:
    st.write("PDF Uploaded Successfully")

submit_1 = st.button("Tell Me About Resume")
submit_2 = st.button("How Much Percentage Match")

imput_prompt_1 = """
You are a tech-savvy HR professional tasked with analyzing the applicant's background against the job description for this role. Please provide a comprehensive assessment of whether the candidate's qualifications meet the requirements of the position. In your evaluation, highlight the strengths and weaknesses of the applicant in relation to the specified criteria. Consider factors such as relevant experience, educational background, technical skills, and any other qualifications mentioned in the job description. Your assessment should be thorough and objective, aiming to identify both areas where the candidate excels and areas where they may fall short. This evaluation will help in making an informed decision about the candidate's suitability for the role.
"""
imput_prompt_2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit_1:
    if upload_file is not None: 
        pdf_content = input_pdf_setup(upload_file)
        response = get_genai_response(input_text, pdf_content, imput_prompt_1)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Upload the Resume")
elif submit_2:
    if upload_file is not None: 
        pdf_content = input_pdf_setup(upload_file)
        response = get_genai_response(input_text, pdf_content, imput_prompt_2)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Upload the Resume")

footer = """
---
This Application helps you in your Resume Review with help of 🤖 GEMINI AI [LLM]
"""

st.markdown(footer, unsafe_allow_html=True)