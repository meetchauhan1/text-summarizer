# 📝 Text Summarizer

A Streamlit-based web application that generates concise summaries from large blocks of text or uploaded documents. The app supports both plain text and PDF files, offering multiple output formats for the summaries.

## ✨ Features

- **Text Input**: Paste or type your text directly into the application
- **File Upload**: Supports both `.txt` and `.pdf` files
- **Multiple Output Formats**:
  - Plain Text
  - Bullet Points
  - Numbered List
- **Adjustable Summary Length**: Control the length of your summary using a percentage slider
- **Real-time Word Count**: Track the length of your input text
- **Downloadable Summaries**: Save your summaries as text files
- **Responsive Design**: Works on both desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Docker and Docker Compose

### Installation with Python

#### Method 1: Using pip (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/meetchauhan1/text-summarizer.git
   cd text-summarizer
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   # source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

#### Method 2: Using Docker

1. Make sure you have Docker installed and running on your system.
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Build the Docker image:
   ```bash
   docker build -t text-summarizer .
   ```

4. Run the container:
   ```bash
   docker run -p 8501:8501 text-summarizer
   ```
   Or with Docker Compose:
   ```bash
   docker-compose up
   ```
# After container starts, access the app in your browser at:
# http://localhost:8501
5. The application will be available at `http://localhost:8501`

##### Additional Docker Options:

- To run in detached mode (in background):
  ```bash
  docker run -d -p 8501:8501 --name my-summarizer text-summarizer
  ```

- To view logs:
  ```bash
  docker logs -f my-summarizer
  ```

- To stop the container:
  ```bash
  docker stop my-summarizer
  docker rm my-summarizer  # To remove the container after stopping
  ```

### Installation

See the installation methods above for both Python and Docker setups.

## 🛠️ Usage

1. **Input Text**:
   - Type or paste your text in the text area
   - OR upload a `.txt` or `.pdf` file using the file uploader

2. **Adjust Settings**:
   - Use the slider to set your desired summary length (10-100% of original text)
   - Select your preferred output format

3. **Generate Summary**:
   - Click the "Summarize" button to generate your summary
   - Download the summary using the download button

## 📦 Dependencies

- streamlit
- pdfplumber (for PDF processing)
- spacy (for text processing)

## 🌐 Live Demo


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Color scheme inspired by modern web design trends

---
