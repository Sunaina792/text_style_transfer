
# Text Style Transfer

## Overview

This project is a **Text Style Transfer web application** that transforms input text into different linguistic styles while preserving its original meaning. The application enables users to convert standard or informal text into **Gen Z slang** or **formal, professional language** through an intuitive web interface.

The system leverages **pre-trained transformer-based models** from Hugging Face and also includes experimentation with **custom-trained RNN and LSTM models on a proprietary dataset**, providing a comparative study of traditional and modern NLP approaches.

---

## 🚀 Features

* **Gen Z Slang Conversion**
  Converts plain text into modern Gen Z–style language with slang and emojis.

* **Formal Style Conversion**
  Transforms informal text into clear, professional, and formal language.

* **Interactive Web Interface**
  Built using **Gradio**, offering real-time text transformation with example inputs.

* **AI-Powered Models**
  Utilizes transformer-based models for accurate and context-aware style transfer.

* **Flexible Deployment**
  Can be run locally or deployed to cloud platforms.

---
## Demo

### To Gen Z Slang
![To Gen Z](to_genz.png)


### To Formal Language
![To Formal](formal.png)

---
## 📋 Requirements

* Python 3.8 or higher
* Virtual environment (recommended)

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Sunaina792/text_style_transfer.git
cd text_style_transfer
```

Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### Running the Application

1. Activate the virtual environment (if not already active).
2. Start the application:

```bash
python app.py
```

3. Open your browser and navigate to the local URL provided (typically `http://127.0.0.1:7860`).

---

### Using the Interface

* Enter text into the input field.
* Select the target writing style: **Gen Z** or **Formal**.
* Click **Transform** or choose from the provided examples.
* View the transformed output instantly.

---

## 📝 Examples

**Input:**
`Hello, how are you?`

* **Gen Z:** `For fun, how are you? 😎`
* **Formal:** `Hello, how are you doing?`

**Input:**
`What's up?`

* **Gen Z:** `What's popping? 🔥`
* **Formal:** `How are you?`


---

### Custom RNN and LSTM Models

In addition to transformer models, this project includes:

* **RNN and LSTM architectures trained from scratch**
* Training performed on a **custom-curated dataset** for text style transfer
* Implementations and experiments documented in Jupyter notebooks

These models were developed to compare traditional sequence-based approaches with transformer-based methods.

---


## 🤖 Models Used

### Transformer-Based Models

* **Gen Z Slang Model:** `jusshini/genz_slang_model`
  A fine-tuned T5 model for generating Gen Z–style slang.

* **Formal Style Model:** `rajistics/informal_formal_style_transfer`
  A T5 model trained to convert informal text into formal language.

Models are automatically downloaded from Hugging Face during the first run.


## 📁 Project Structure

```
text_style_transfer/
├── app.py                 # Main Gradio application
├── models/
│   ├── genz_model.py      # Gen Z style transfer logic
│   └── formal_model.py    # Formal style transfer logic
├── notebooks/
│   ├── normal_to_genz.ipynb     # RNN/LSTM and transformer experiments
│   └── normal_to_formal.ipynb   # Formal style training experiments
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🔧 Customization

* **Model Configuration:**
  Modify `models/genz_model.py` or `models/formal_model.py` to change models or inference parameters.

* **UI Customization:**
  Update `app.py` to adjust the Gradio layout, themes, or examples.

* **Training:**
  Use the notebooks to train or fine-tune models on your own dataset.

---

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch

   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes

   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch and open a pull request

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 👩‍💻 Author

**Sunaina**



