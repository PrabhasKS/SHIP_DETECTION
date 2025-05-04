
## 🚢 Ship Detection Web App

This is a Streamlit-based web application for detecting ships in images using a custom object detection model hosted on [Roboflow](https://roboflow.com/).

### 📂 Repository Structure

```
.
├── main.py           # Streamlit app for ship detection
├── requirements.txt  # Required Python packages
```

---

### 📸 Features

* Upload an image (`.jpg`, `.jpeg`, `.png`)
* Detect ships using Roboflow inference API
* Displays bounding boxes and confidence scores
* Simple, interactive UI using Streamlit

---

### 🚀 Getting Started

#### 1. Clone the repository:

```bash
git clone https://github.com/PrabhasKS/SHIP_DETECTION.git
cd SHIP_DETECTION
```

#### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Run the app:

```bash
streamlit run main.py
```

---

### 🔑 API Setup

This app uses the `inference_sdk` from Roboflow. Ensure your API key and model ID are correctly set in `main.py`:

```python
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="your_api_key_here"
)
```

---

### 🧪 Example

Upload an image like this:

![Example](https://via.placeholder.com/400x200.png?text=Ship+Detection+Sample)

---

### 📌 Requirements

* Python 3.7+
* Streamlit
* Roboflow SDK
* Pillow

---

### 🛠️ Credits

* Built with ❤️ using [Streamlit](https://streamlit.io/)
* Model powered by [Roboflow](https://roboflow.com/)

---

