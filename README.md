# ATS Tracking System

An ATS (Applicant Tracking System) checking app built with Streamlit, Google Gemini Pro Vision API, and various Python libraries to analyze resumes against job descriptions.

## Features

- **Upload PDF Resumes**: Upload a resume in PDF format.
- **Job Description Analysis**: Paste a job description for the role you are hiring for.
- **Resume Assessment**: Get a comprehensive assessment of the resume against the job description.
- **Percentage Match**: Determine the percentage match between the resume and the job description.
- **Highlight Missing Keywords**: Identify keywords or skills missing from the resume.

## Technologies Used

- **Streamlit**: Web application framework for creating the app interface.
- **pdf2image**: Library for converting PDF documents to images.
- **Pillow**: Python Imaging Library for image processing.
- **Google Generative AI (Gemini Pro Vision API)**: For generating content and analyzing the resume.
- **Base64**: Encoding binary data for API requests.
- **dotenv**: Loading environment variables from a `.env` file.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/R0obin/End-To-End-Resume-Application-Tracking-System-ATS-Using-Google-Gemini-Pro-Vision-LIM-Model.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd End-To-End-Resume-Application-Tracking-System-ATS-Using-Google-Gemini-Pro-Vision-LIM-Model
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv atsenv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        atsenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source atsenv/bin/activate
        ```

5. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Install Poppler**:
    - On Windows: Download Poppler from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) and add the `bin` folder to your PATH environment variable.

7. **Create a `.env` file** and add your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and navigate to `http://localhost:8501`.

3. **Upload a resume PDF** and **paste the job description** in the provided text area.

4. **Click on the buttons** to get a detailed assessment or percentage match.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**: 
    ```sh
    git checkout -b my-feature-branch
    ```
3. **Make your changes and commit them**:
    ```sh
    git commit -m "Add some feature"
    ```
4. **Push to the branch**:
    ```sh
    git push origin my-feature-branch
    ```
5. **Create a Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow](https://python-pillow.org/)
- [Google Generative AI](https://cloud.google.com/generative-ai)
