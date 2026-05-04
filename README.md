# AI Resume Builder & ATS Optimizer

A Streamlit-based application that helps users upload resumes, view extracted content, estimate an ATS score, improve resume wording using an LLM, and export the improved resume as a `.docx` file.

## Features

- Upload resumes in **PDF** or **DOCX** format.
- Parse and display original resume text.
- Predict an estimated ATS score using a local scikit-learn model.
- Enhance resume language and ATS optimization with Gemini.
- Download the improved resume as `enhanced_resume.docx`.

## Project Structure

```text
AI-Resume-Builder/
├── app.py                     # Streamlit UI entrypoint
├── config.py                  # Environment loading and API key config
├── requirements.txt           # Python dependencies
├── check_models.py            # Utility script to list available Gemini models
├── models/
│   └── ats_model.pkl          # Serialized ATS model
└── modules/
    ├── parser.py              # PDF/DOCX resume parsing
    ├── ats_model.py           # ATS model train/load/predict logic
    ├── generator.py           # DOCX generation for improved resume
    ├── similarity.py          # (placeholder / future use)
    └── enhancer_gemini.py     # Gemini-based resume enhancement
```

## Tech Stack

- **Frontend/UI**: Streamlit
- **Parsing**: PyMuPDF (`fitz`), `python-docx`
- **ML Scoring**: scikit-learn (RandomForestRegressor)
- **LLM Enhancement**: Google Gemini (`google-generativeai`)
- **Output**: `python-docx`

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd AI-Resume-Builder
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .venv\Scripts\activate    # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Running the App

Start Streamlit:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## How It Works

1. User uploads a PDF or DOCX resume.
2. `modules/parser.py` extracts the text.
3. `modules/ats_model.py` predicts an ATS score (currently using sample numeric features in the app flow).
4. LLM enhancer rewrites and optimizes resume content.
5. `modules/generator.py` writes the enhanced result to `enhanced_resume.docx`.

## Notes

- The ATS model is trained on small sample data for demonstration and bootstrapped automatically if `models/ats_model.pkl` is missing.
- Ensure your API key is valid before using enhancement features.
- `app.py` currently imports `modules.enhancer_openai`; if this module is not present, switch import/use to `modules.enhancer_gemini` (or add the OpenAI enhancer module).

## Future Improvements

- Extract real ATS features directly from parsed resume text.
- Add job-description matching and similarity scoring.
- Support section-aware resume formatting in generated output.
- Add test suite and CI pipeline.
