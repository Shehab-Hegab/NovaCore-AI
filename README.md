# 🟣 NovaCore AI | Enterprise AutoML Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> **The Bridge Between Raw Data and Actionable Intelligence.**
>
> NovaCore AI is a high-performance, no-code Machine Learning dashboard designed for analysts and decision-makers. Built with a "Cyberpunk FinTech" aesthetic, it transforms Excel/CSV files into predictive models without writing a single line of code.

---

## 📸 Interface Preview

*(You should take screenshots of your app and put them in a folder named 'screenshots' in your repo, then link them here. For now, use this placeholder)*

| **Data Ingestion** | **Model Engine** |
|:---:|:---:|
| <img src="https://via.placeholder.com/400x200/0E1117/8B5CF6?text=Data+Ingestion" alt="Data Ingestion"> | <img src="https://via.placeholder.com/400x200/0E1117/00C9FF?text=Model+Training" alt="Model Engine"> |

---

## ✨ Key Features

### 📂 1. Universal Data Ingestion
*   **Drag & Drop:** Support for `.csv` and `.xlsx` (Excel) files.
*   **Auto-Detection:** Instantly analyzes schema, detecting numeric vs. categorical columns.
*   **Smart Preview:** Financial-terminal style data viewing.

### 📊 2. Interactive Analytics Studio (EDA)
*   **Dynamic Plotting:** Generate Scatter, Line, Bar, 3D, and Violin plots on the fly.
*   **Correlation Heatmaps:** Visualize relationships between variables instantly.
*   **Dark Mode Visuals:** All charts are rendered in `plotly_dark` to match the cyberpunk UI.

### 🧹 3. Intelligent Data Refinery
*   **One-Click Clean:** Automated pipeline to:
    *   Impute missing numeric values (Median).
    *   Impute missing categorical values (Mode).
    *   Remove duplicate entries.
*   **Quality Metrics:** Real-time feedback on data health before and after cleaning.

### 🧠 4. AutoML Engine
*   **Algorithm Selection:** Choose between Random Forest, Gradient Boosting, or Logistic Regression.
*   **Problem Detection:** Automatically switches between **Regression** (predicting numbers) and **Classification** (predicting categories).
*   **Performance Metrics:** Real-time Confusion Matrix, ROC Curves, RMSE, and R² scores.
*   **Feature Importance:** Visual ranking of which factors drive your predictions.

### 🔮 5. Prediction Simulator
*   **What-If Analysis:** Manually input hypothetical data points to see how the model reacts.
*   **Confidence Scores:** View probability distributions for every prediction.

---

## 🛠️ Tech Stack

*   **Core:** Python 3.9+
*   **Frontend:** Streamlit (Custom CSS)
*   **Data Processing:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn
*   **Visualization:** Plotly Express / Graph Objects

---

## 🚀 Installation & Local Run

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/novacore-ai.git
    cd novacore-ai
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Dashboard**
    ```bash
    streamlit run app.py
    ```

4.  **Access the App**
    Open your browser to `http://localhost:8501`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
    <p>Built with ❤️ by [Your Name]</p>
</div>
