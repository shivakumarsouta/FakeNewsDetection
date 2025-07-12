## 📰 Fake News Detection App

**Detect whether a news article is Real or Fake using Machine Learning.**
A lightweight web app built with Streamlit, using an SVM classifier and TF-IDF vectorization trained on labeled news data.

---

## Live 🌐

Hosted [here](https://fakenewsdetector.streamlit.app)
## 🚀 Features

* **Real‑Time Prediction** - Classify news articles instantly with pre-trained ML models.
* **Simple UI** - User-friendly, no-code interface using Streamlit.
* **Editable Model Files** - Easily swap or retrain the vectorizer and classifier with your dataset.
* **Local or Cloud Deployment** - Run it on your machine or host using Streamlit Cloud.

---

## 🏗️ Architecture

```text
User Input: News Article Text
↓
TF-IDF Vectorizer (Pre-trained)
↓
SVM Classifier (Pre-trained)
↓
Prediction: Real or Fake
↓
Streamlit UI (Display Result)
```

---

## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/shivkumars005/FakeNewsDetection.git
cd FakeNewsDetection

# 2. (Optional) Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure model files are present
Place vectorizer.pkl and classifier.pkl in the project directory.

# 5. Run the app
streamlit run app.py
```

---

## 🧪 Usage Guide

1. Open the web app at [FakeNewsDetector](https://fakenewsdetector.streamlit.app).
2. Paste or type in the news article content.
3. Click the **Check** button.
4. The app will display whether the news is **REAL** or **FAKE**.
---

## 🌟 Tech Stack

| Component        | Tech                  |
| ---------------- | --------------------- |
| Machine Learning | SVM Classifier        |
| Vectorization    | TF-IDF (Scikit-learn) |
| UI               | Streamlit             |

---

## 🧩 Customization Options

* **Model Replacement** → Train with your own dataset, swap in new `.pkl` files.
* **UI Styling** → Customized using Streamlit.
* **Deployment** → Host using Streamlit Community Cloud.

---

## 🙋‍♂️ Contact

[GitHub](https://github.com/shivkumars005) | [LinkedIn](https://linkedin.com/in/shivakumarsouta) | [Mail](shivakumarsouta18@gmail.com) | [Portfolio](https://shivakumarsouta-portfolio.vercel.app)
---