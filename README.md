# 🟣 NovaCore AI | Enterprise AutoML Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> **The Bridge Between Raw Data and Actionable Intelligence.**
>
> NovaCore AI is a high-performance, no-code Machine Learning dashboard designed for analysts and decision-makers. Built with a "Cyberpunk FinTech" aesthetic, it transforms Excel/CSV files into predictive models without writing a single line of code.

---

## 📸 Interface Preview


<img width="1848" height="938" alt="image" src="https://github.com/user-attachments/assets/20a8499b-bbd7-4449-8cd6-e246df4fab3f" />
<img width="1872" height="907" alt="image" src="https://github.com/user-attachments/assets/1193f89d-d8c3-4cd9-9ff6-f48921aff7cf" />

<img width="1847" height="934" alt="image" src="https://github.com/user-attachments/assets/8dc9449e-e69b-4890-8422-71103548c4c1" />
<img width="1855" height="932" alt="image" src="https://github.com/user-attachments/assets/b956c57b-ba3e-4ecd-9a77-81ff6a8ec78d" />
<img width="1848" height="933" alt="image" src="https://github.com/user-attachments/assets/c5a78b7f-074b-4b44-a5d2-36946f88addf" />

<img width="1856" height="933" alt="image" src="https://github.com/user-attachments/assets/d12b095d-6589-4551-8d45-b20f0e82601d" />
<img width="1507" height="792" alt="image" src="https://github.com/user-attachments/assets/6814fa67-8fd5-45d1-8ab5-fa234fce4efe" />
<img width="1856" height="941" alt="image" src="https://github.com/user-attachments/assets/99775174-5a08-4f0a-af5e-4a55768d6722" />
<img width="1852" height="938" alt="image" src="https://github.com/user-attachments/assets/abd4199c-4c15-417f-b073-6fa0ac1584ca" />
<img width="1552" height="507" alt="image" src="https://github.com/user-attachments/assets/f9a79277-963b-4d37-818d-35d10379980c" />
<img width="1852" height="927" alt="image" src="https://github.com/user-attachments/assets/0da3836a-60b5-4238-82d8-c42fc55a0d90" />


<img width="1852" height="991" alt="image" src="https://github.com/user-attachments/assets/14c10b93-4a44-4bb8-ad42-e71dfa77fef3" />

<img width="1561" height="928" alt="image" src="https://github.com/user-attachments/assets/f7a83394-f088-411f-b1f3-36e89359bae8" />

<img width="1450" height="937" alt="image" src="https://github.com/user-attachments/assets/0565bfc6-7c0f-4777-9c04-09fc01d81a1e" />
<img width="1498" height="541" alt="image" src="https://github.com/user-attachments/assets/851c6169-5555-4b86-b781-fb77679ca959" />
<img width="1845" height="939" alt="image" src="https://github.com/user-attachments/assets/80e761fa-8eba-466e-bdb4-1f42e3c7cdc0" />



<img width="1405" height="901" alt="image" src="https://github.com/user-attachments/assets/fe835794-478e-44d9-bc7e-63d78b160605" />


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
