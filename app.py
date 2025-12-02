"""
🚀 High-End AutoML Dashboard - Cyberpunk FinTech Edition
Built with Streamlit | Theme: Deep Navy, Pure Black, Neon Purple
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score, classification_report,
    mean_absolute_error, mean_squared_error, r2_score
)
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════
# 🎨 CUSTOM CSS INJECTION - CYBERPUNK FINTECH THEME
# ═══════════════════════════════════════════════════════════════════════════

def inject_custom_css():
    """Inject premium cyberpunk-themed CSS"""
    st.markdown("""
    <style>
    /* ═══ GLOBAL THEME ═══ */
    .stApp {
        background: linear-gradient(135deg, #0E1117 0%, #1a1f2e 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #161B22 0%, #0E1117 100%);
        border-right: 2px solid #8B5CF6;
    }
    
    /* ═══ GLOWING BUTTONS ═══ */
    .stButton > button {
        background: linear-gradient(135deg, #8B5CF6 0%, #00C9FF 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px 0 rgba(139, 92, 246, 0.4);
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 25px 0 rgba(139, 92, 246, 0.8);
        transform: translateY(-2px);
    }
    
    /* ═══ INPUT FIELDS ═══ */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #1a1f2e;
        color: #FAFAFA;
        border-radius: 10px;
        border: 1px solid #8B5CF6;
        padding: 0.5rem;
    }
    
    /* ═══ DATAFRAME TERMINAL STYLE ═══ */
    .dataframe {
        background-color: #0E1117;
        color: #00FF41;
        border: 2px solid #8B5CF6;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, #8B5CF6 0%, #00C9FF 100%);
        color: white;
        font-weight: bold;
        padding: 12px;
    }
    
    .dataframe tbody tr:hover {
        background-color: #1a1f2e;
    }
    
    /* ═══ METRICS CARDS ═══ */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #00C9FF;
        font-weight: bold;
    }
    
    [data-testid="stMetricLabel"] {
        color: #8B5CF6;
        font-weight: 600;
    }
    
    /* ═══ HEADERS ═══ */
    h1, h2, h3 {
        color: #FAFAFA;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
    }
    
    /* ═══ FILE UPLOADER ═══ */
    [data-testid="stFileUploader"] {
        background-color: #1a1f2e;
        border: 2px dashed #8B5CF6;
        border-radius: 10px;
        padding: 2rem;
    }
    
    /* ═══ SLIDER ═══ */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #8B5CF6 0%, #00C9FF 100%);
    }
    
    /* ═══ CUSTOM CARD STYLING ═══ */
    .custom-card {
        background: linear-gradient(135deg, #1a1f2e 0%, #161B22 100%);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid #8B5CF6;
        box-shadow: 0 8px 32px 0 rgba(139, 92, 246, 0.2);
        margin-bottom: 1rem;
    }
    
    /* ═══ GLOW TEXT ═══ */
    .glow-text {
        color: #00C9FF;
        text-shadow: 0 0 10px #00C9FF, 0 0 20px #00C9FF, 0 0 30px #00C9FF;
        font-weight: bold;
    }
    
    /* ═══ WARNING/INFO BOXES ═══ */
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #8B5CF6;
    }
    
    /* ═══ TABS ═══ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #1a1f2e;
        border-radius: 10px;
        color: #FAFAFA;
        padding: 10px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #8B5CF6 0%, #00C9FF 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 SESSION STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

def init_session_state():
    """Initialize session state variables"""
    if 'df' not in st.session_state:
        st.session_state.df = None
    if 'cleaned_df' not in st.session_state:
        st.session_state.cleaned_df = None
    if 'model' not in st.session_state:
        st.session_state.model = None
    if 'X_train' not in st.session_state:
        st.session_state.X_train = None
    if 'X_test' not in st.session_state:
        st.session_state.X_test = None
    if 'y_train' not in st.session_state:
        st.session_state.y_train = None
    if 'y_test' not in st.session_state:
        st.session_state.y_test = None
    if 'feature_names' not in st.session_state:
        st.session_state.feature_names = None
    if 'target_name' not in st.session_state:
        st.session_state.target_name = None
    if 'label_encoders' not in st.session_state:
        st.session_state.label_encoders = {}
    if 'is_regression' not in st.session_state:
        st.session_state.is_regression = False
    if 'problem_type' not in st.session_state:
        st.session_state.problem_type = None

# ═══════════════════════════════════════════════════════════════════════════
# 📂 DATA INGESTION MODULE
# ═══════════════════════════════════════════════════════════════════════════

def data_ingestion_page():
    """Data upload and preview section"""
    st.markdown('<h1 class="glow-text">📂 Data Ingestion Portal</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "🚀 Upload your dataset (CSV or Excel)",
        type=['csv', 'xlsx'],
        help="Drag and drop or click to upload"
    )
    
    if uploaded_file is not None:
        try:
            # Read file based on extension
            if uploaded_file.name.endswith('.csv'):
                # Try multiple encodings for CSV files
                encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'utf-16']
                df = None
                successful_encoding = None
                
                for encoding in encodings:
                    try:
                        uploaded_file.seek(0)  # Reset file pointer
                        df = pd.read_csv(uploaded_file, encoding=encoding)
                        successful_encoding = encoding
                        break
                    except (UnicodeDecodeError, UnicodeError):
                        continue
                    except Exception as e:
                        # If it's not an encoding error, break and show the error
                        if df is None:
                            raise e
                        break
                
                if df is None:
                    raise ValueError("Unable to read file with any supported encoding. Please check your file format.")
                
                if successful_encoding and successful_encoding != 'utf-8':
                    st.info(f"📝 File loaded successfully with **{successful_encoding}** encoding")
            else:
                df = pd.read_excel(uploaded_file)
            
            st.session_state.df = df
            st.session_state.cleaned_df = df.copy()
            
            # Success message
            st.success(f"✅ Successfully loaded: **{uploaded_file.name}**")
            
            # Dataset shape metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📊 Total Rows", f"{df.shape[0]:,}")
            with col2:
                st.metric("📋 Total Columns", df.shape[1])
            with col3:
                st.metric("💾 Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            
            st.markdown("---")
            
            # Data Preview
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown("### 🔍 Data Preview (First 10 Rows)")
            st.dataframe(df.head(10), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Column Type Detection
            st.markdown("---")
            st.markdown("### 🧬 Intelligent Column Analysis")
            
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="custom-card">', unsafe_allow_html=True)
                st.markdown("#### 🔢 Numeric Columns")
                if numeric_cols:
                    for col in numeric_cols:
                        st.markdown(f"- `{col}` (Range: {df[col].min():.2f} → {df[col].max():.2f})")
                else:
                    st.info("No numeric columns detected")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="custom-card">', unsafe_allow_html=True)
                st.markdown("#### 🏷️ Categorical Columns")
                if categorical_cols:
                    for col in categorical_cols:
                        unique_count = df[col].nunique()
                        st.markdown(f"- `{col}` ({unique_count} unique values)")
                else:
                    st.info("No categorical columns detected")
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Missing Values Summary
            st.markdown("---")
            missing_data = df.isnull().sum()
            if missing_data.sum() > 0:
                st.warning(f"⚠️ Missing Values Detected: {missing_data.sum()} total")
                missing_df = pd.DataFrame({
                    'Column': missing_data[missing_data > 0].index,
                    'Missing Count': missing_data[missing_data > 0].values,
                    'Percentage': (missing_data[missing_data > 0].values / len(df) * 100).round(2)
                })
                st.dataframe(missing_df, use_container_width=True)
            else:
                st.success("✅ No missing values found!")
                
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
    else:
        # Welcome screen
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("""
        ## 👋 Welcome to the AutoML Dashboard
        
        **Getting Started:**
        1. 📤 Upload your CSV or Excel file using the uploader above
        2. 📊 Explore your data with Advanced EDA
        3. 🧹 Clean your data with one-click automation
        4. 🧠 Train ML models without writing code
        5. 🔮 Make predictions on new data
        
        **Supported File Types:**
        - `.csv` (Comma-Separated Values)
        - `.xlsx` (Microsoft Excel)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# 📊 ADVANCED EDA MODULE
# ═══════════════════════════════════════════════════════════════════════════

def advanced_eda_page():
    """Exploratory Data Analysis with interactive visualizations"""
    st.markdown('<h1 class="glow-text">📊 Advanced Exploratory Data Analysis</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state.df is None:
        st.warning("⚠️ Please upload a dataset first in the Data Ingestion section!")
        return
    
    df = st.session_state.cleaned_df if st.session_state.cleaned_df is not None else st.session_state.df
    
    # Statistical Summary
    st.markdown("### 📈 Statistical Summary")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.dataframe(df.describe(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dynamic Plotting Control Panel
    st.markdown("### 🎨 Interactive Visualization Studio")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        chart_type = st.selectbox(
            "📊 Chart Type",
            ["Scatter", "Line", "Bar", "3D Scatter", "Box", "Violin", "Histogram", "Density Heatmap", "Pie Chart", "Sunburst", "Treemap", "Funnel", "Area", "Bubble"],
            help="Select visualization type"
        )
    
    with col2:
        x_axis = st.selectbox("🔵 X-Axis", df.columns.tolist())
    
    with col3:
        y_axis = st.selectbox("🟢 Y-Axis", df.columns.tolist())
    
    with col4:
        color_col = st.selectbox("🎨 Color (Hue)", [None] + df.columns.tolist())
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate Plot
    try:
        if chart_type == "Scatter":
            fig = px.scatter(
                df, x=x_axis, y=y_axis, color=color_col,
                template="plotly_dark",
                color_continuous_scale="Viridis"
            )
        elif chart_type == "Line":
            fig = px.line(
                df, x=x_axis, y=y_axis, color=color_col,
                template="plotly_dark"
            )
        elif chart_type == "Bar":
            fig = px.bar(
                df, x=x_axis, y=y_axis, color=color_col,
                template="plotly_dark",
                color_continuous_scale="Plasma"
            )
        elif chart_type == "3D Scatter":
            if len(df.columns) >= 3:
                z_axis = st.selectbox("🔴 Z-Axis", df.columns.tolist())
                fig = px.scatter_3d(
                    df, x=x_axis, y=y_axis, z=z_axis, color=color_col,
                    template="plotly_dark"
                )
            else:
                st.error("Need at least 3 columns for 3D plot")
                return
        elif chart_type == "Box":
            fig = px.box(
                df, x=x_axis, y=y_axis, color=color_col,
                template="plotly_dark"
            )
        elif chart_type == "Violin":
            fig = px.violin(df, x=x_axis, y=y_axis, color=color_col, template="plotly_dark")
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_axis, color=color_col, template="plotly_dark", marginal="box")
        elif chart_type == "Density Heatmap":
            fig = px.density_heatmap(df, x=x_axis, y=y_axis, template="plotly_dark", color_continuous_scale="Purples")
        elif chart_type == "Pie Chart":
            fig = px.pie(df, names=x_axis, values=y_axis, template="plotly_dark", color_discrete_sequence=px.colors.sequential.Purp)
        elif chart_type == "Sunburst":
            fig = px.sunburst(df, path=[x_axis], values=y_axis, template="plotly_dark", color_discrete_sequence=px.colors.sequential.Purp)
        elif chart_type == "Treemap":
            fig = px.treemap(df, path=[x_axis], values=y_axis, template="plotly_dark", color_discrete_sequence=px.colors.sequential.Purp)
        elif chart_type == "Funnel":
            fig = px.funnel(df, x=y_axis, y=x_axis, template="plotly_dark")
        elif chart_type == "Area":
            fig = px.area(df, x=x_axis, y=y_axis, color=color_col, template="plotly_dark")
        elif chart_type == "Bubble":
            size_col = st.selectbox("Bubble Size", df.select_dtypes(include=[np.number]).columns.tolist())
            fig = px.scatter(df, x=x_axis, y=y_axis, size=size_col, color=color_col, template="plotly_dark")
        
        # Update layout with cyberpunk theme
        fig.update_layout(
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='#FAFAFA'),
            title=dict(
                text=f"{chart_type} Plot: {y_axis} vs {x_axis}",
                font=dict(size=20, color='#8B5CF6')
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ Error creating plot: {str(e)}")
    
    # Correlation Matrix
    st.markdown("---")
    st.markdown("### 🔥 Correlation Heatmap")
    
    numeric_df = df.select_dtypes(include=[np.number])
    if len(numeric_df.columns) > 1:
        corr_matrix = numeric_df.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='Purples',
            text=corr_matrix.values.round(2),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            template="plotly_dark",
            title="Feature Correlation Matrix",
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='#FAFAFA'),
            width=800,
            height=800
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("ℹ️ Need at least 2 numeric columns for correlation analysis")
    
    # Distribution Analysis
    st.markdown("---")
    st.markdown("### 📊 Distribution Analysis")
    
    selected_col = st.selectbox("Select column for distribution", numeric_df.columns.tolist())
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogram
        fig = px.histogram(
            df, x=selected_col,
            template="plotly_dark",
            color_discrete_sequence=['#8B5CF6']
        )
        fig.update_layout(
            title=f"Distribution of {selected_col}",
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='#FAFAFA')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Box plot
        fig = px.box(
            df, y=selected_col,
            template="plotly_dark",
            color_discrete_sequence=['#00C9FF']
        )
        fig.update_layout(
            title=f"Box Plot of {selected_col}",
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='#FAFAFA')
        )
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# 🧹 SMART DATA CLEANING MODULE
# ═══════════════════════════════════════════════════════════════════════════

def smart_data_cleaning_page():
    """Automated data cleaning with one-click functionality"""
    st.markdown('<h1 class="glow-text">🧹 Smart Data Cleaning Lab</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state.df is None:
        st.warning("⚠️ Please upload a dataset first in the Data Ingestion section!")
        return
    
    df = st.session_state.df.copy()
    
    # Missing Values Analysis
    st.markdown("### 🔍 Missing Values Analysis")
    
    missing_data = df.isnull().sum()
    total_missing = missing_data.sum()
    
    if total_missing > 0:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        
        missing_df = pd.DataFrame({
            'Column': missing_data[missing_data > 0].index,
            'Missing Count': missing_data[missing_data > 0].values,
            'Percentage': (missing_data[missing_data > 0].values / len(df) * 100).round(2)
        })
        
        st.dataframe(missing_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization of missing values
        fig = px.bar(
            missing_df,
            x='Column',
            y='Percentage',
            title='Missing Values by Column (%)',
            template='plotly_dark',
            color='Percentage',
            color_continuous_scale='Reds'
        )
        fig.update_layout(
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='#FAFAFA')
        )
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.success("✅ No missing values detected!")
    
    # Duplicate Analysis
    st.markdown("---")
    st.markdown("### 🔄 Duplicate Rows Analysis")
    
    duplicates = df.duplicated().sum()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Duplicate Rows", duplicates)
    with col2:
        st.metric("Percentage", f"{(duplicates / len(df) * 100):.2f}%")
    
    # One-Click Clean Button
    st.markdown("---")
    st.markdown("### 🚀 Automated Cleaning")
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("""
    **The One-Click Cleaner will:**
    - 🔢 Fill numeric missing values with **Median**
    - 🏷️ Fill categorical missing values with **Mode**
    - 🗑️ Remove duplicate rows
    - ✨ Optimize data types
    """)
    
    if st.button("🧹 ONE-CLICK CLEAN", use_container_width=True):
        with st.spinner("🔄 Cleaning data..."):
            cleaned_df = df.copy()
            
            # Fill numeric columns with median
            numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                if cleaned_df[col].isnull().sum() > 0:
                    cleaned_df[col].fillna(cleaned_df[col].median(), inplace=True)
            
            # Fill categorical columns with mode
            categorical_cols = cleaned_df.select_dtypes(include=['object', 'category']).columns
            for col in categorical_cols:
                if cleaned_df[col].isnull().sum() > 0:
                    mode_value = cleaned_df[col].mode()
                    if len(mode_value) > 0:
                        cleaned_df[col].fillna(mode_value[0], inplace=True)
            
            # Remove duplicates
            original_rows = len(cleaned_df)
            cleaned_df.drop_duplicates(inplace=True)
            removed_duplicates = original_rows - len(cleaned_df)
            
            # Update session state
            st.session_state.cleaned_df = cleaned_df
            
            st.success(f"""
            ✅ **Data Cleaning Complete!**
            - 🗑️ Removed {removed_duplicates} duplicate rows
            - 📊 Final dataset: {len(cleaned_df)} rows × {len(cleaned_df.columns)} columns
            - 💾 Memory optimized: {cleaned_df.memory_usage(deep=True).sum() / 1024:.2f} KB
            """)
            
            # Show before/after comparison
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Original Rows", original_rows)
                st.metric("Original Missing Values", total_missing)
            with col2:
                st.metric("Cleaned Rows", len(cleaned_df))
                st.metric("Remaining Missing Values", cleaned_df.isnull().sum().sum())
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Preview cleaned data
    if st.session_state.cleaned_df is not None:
        st.markdown("---")
        st.markdown("### ✨ Cleaned Data Preview")
        st.dataframe(st.session_state.cleaned_df.head(10), use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# 🧠 MODEL ENGINE MODULE
# ═══════════════════════════════════════════════════════════════════════════

def model_engine_page():
    """Machine Learning model training and evaluation"""
    st.markdown('<h1 class="glow-text">🧠 AI Model Engine</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state.df is None:
        st.warning("⚠️ Please upload a dataset first in the Data Ingestion section!")
        return
    
    df = st.session_state.cleaned_df if st.session_state.cleaned_df is not None else st.session_state.df
    
    # Model Configuration Panel
    st.markdown("### ⚙️ Model Configuration")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        target_column = st.selectbox(
            "🎯 Target Variable (What to Predict)",
            df.columns.tolist(),
            help="Select the column you want to predict"
        )
    
    with col2:
        test_size = st.slider(
            "📊 Test Split %",
            min_value=10,
            max_value=40,
            value=20,
            step=5,
            help="Percentage of data used for testing"
        )
    
    with col3:
        # Determine available models based on problem type
        if st.session_state.get('is_regression', False):
            available_models = ["Random Forest Regressor", "Linear Regression", "Ridge", "Lasso", "Gradient Boosting Regressor", "SVR"]
        else:
            available_models = ["Random Forest", "Logistic Regression", "Gradient Boosting"]
        
        model_type = st.selectbox(
            "🤖 Model Algorithm",
            available_models,
            help="Select the ML algorithm"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Feature selection
    st.markdown("---")
    st.markdown("### 🎯 Feature Selection")
    
    available_features = [col for col in df.columns if col != target_column]
    selected_features = st.multiselect(
        "Select features for training (leave empty to use all)",
        available_features,
        default=available_features
    )
    
    if not selected_features:
        selected_features = available_features
    
    # Train button
    st.markdown("---")
    
    if st.button("🚀 TRAIN MODEL", use_container_width=True):
        try:
            with st.spinner("🔄 Training model... Please wait"):
                # Prepare data
                X = df[selected_features].copy()
                y = df[target_column].copy()
                
                # Handle categorical variables
                label_encoders = {}
                for col in X.select_dtypes(include=['object', 'category']).columns:
                    le = LabelEncoder()
                    X[col] = le.fit_transform(X[col].astype(str))
                    label_encoders[col] = le
                
                # Encode target if categorical
                if y.dtype == 'object' or y.dtype == 'category':
                    target_encoder = LabelEncoder()
                    y = target_encoder.fit_transform(y.astype(str))
                    label_encoders['target'] = target_encoder
                
                # Determine problem type
                unique_targets = len(np.unique(y))
                is_regression = unique_targets > 10 or (y.dtype in ['float64', 'float32'] and unique_targets > 5)
                st.session_state.is_regression = is_regression
                st.session_state.problem_type = "Regression" if is_regression else "Classification"
                
                if is_regression:
                    st.info(f"📊 Detected **Regression** problem ({unique_targets} unique values)")
                else:
                    st.info(f"🎯 Detected **Classification** problem ({unique_targets} classes)")
                
                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size/100, random_state=42
                )
                
                # Train model based on problem type
                if st.session_state.is_regression:
                    # Regression models
                    if model_type == "Random Forest Regressor":
                        model = RandomForestRegressor(n_estimators=100, random_state=42)
                    elif model_type == "Linear Regression":
                        model = LinearRegression()
                    elif model_type == "Ridge":
                        model = Ridge(alpha=1.0, random_state=42)
                    elif model_type == "Lasso":
                        model = Lasso(alpha=1.0, random_state=42)
                    elif model_type == "Gradient Boosting Regressor":
                        model = GradientBoostingRegressor(n_estimators=100, random_state=42)
                    else:  # SVR
                        model = SVR(kernel='rbf')
                else:
                    # Classification models
                    if model_type == "Random Forest":
                        model = RandomForestClassifier(n_estimators=100, random_state=42)
                    elif model_type == "Logistic Regression":
                        model = LogisticRegression(max_iter=1000, random_state=42)
                    else:  # Gradient Boosting
                        model = GradientBoostingClassifier(n_estimators=100, random_state=42)
                
                model.fit(X_train, y_train)
                
                # Store in session state
                st.session_state.model = model
                st.session_state.X_train = X_train
                st.session_state.X_test = X_test
                st.session_state.y_train = y_train
                st.session_state.y_test = y_test
                st.session_state.feature_names = selected_features
                st.session_state.target_name = target_column
                st.session_state.label_encoders = label_encoders
                
                st.success("✅ Model trained successfully!")
        
        except Exception as e:
            st.error(f"❌ Error training model: {str(e)}")
            return
    
    # Model Evaluation (show only if model is trained)
    if st.session_state.model is not None:
        st.markdown("---")
        st.markdown("### 📊 Model Performance")
        
        model = st.session_state.model
        X_test = st.session_state.X_test
        y_test = st.session_state.y_test
        
        # Threshold slider
        threshold = st.slider(
            "🎚️ Probability Threshold (For Binary Classification)",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Adjust classification threshold"
        )
        
        # Predictions and Metrics
        if st.session_state.is_regression:
            # Regression predictions
            y_pred = model.predict(X_test)
            
            # Regression Metrics
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                mae = mean_absolute_error(y_test, y_pred)
                st.metric("📊 MAE", f"{mae:.3f}")
            
            with col2:
                mse = mean_squared_error(y_test, y_pred)
                st.metric("📊 MSE", f"{mse:.3f}")
            
            with col3:
                rmse = np.sqrt(mse)
                st.metric("📊 RMSE", f"{rmse:.3f}")
            
            with col4:
                r2 = r2_score(y_test, y_pred)
                st.metric("📊 R² Score", f"{r2:.3f}")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Prediction vs Actual plot
            st.markdown("---")
            st.markdown("### 📈 Prediction vs Actual")
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=y_test, y=y_pred, mode='markers', name='Predictions', 
                                     marker=dict(color='#8B5CF6', size=8)))
            fig.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()],
                                     mode='lines', name='Perfect Prediction', 
                                     line=dict(color='#00C9FF', dash='dash')))
            
            fig.update_layout(template="plotly_dark", plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
                            font=dict(color='#FAFAFA'), xaxis_title="Actual", yaxis_title="Predicted")
            st.plotly_chart(fig, use_container_width=True)
            
            # Residual plot
            st.markdown("### 📊 Residual Analysis")
            residuals = y_test - y_pred
            fig = px.scatter(x=y_pred, y=residuals, template="plotly_dark",
                           labels={'x': 'Predicted', 'y': 'Residuals'})
            fig.add_hline(y=0, line_dash="dash", line_color="#00C9FF")
            fig.update_layout(plot_bgcolor='#0E1117', paper_bgcolor='#0E1117', font=dict(color='#FAFAFA'))
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            # Classification predictions
            if len(np.unique(y_test)) == 2:
                y_pred_proba = model.predict_proba(X_test)[:, 1]
                y_pred = (y_pred_proba >= threshold).astype(int)
            else:
                y_pred = model.predict(X_test)
            
            # Classification Metrics
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                acc = accuracy_score(y_test, y_pred)
                st.metric("🎯 Accuracy", f"{acc:.3f}")
            
            with col2:
                prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
                st.metric("🎯 Precision", f"{prec:.3f}")
            
            with col3:
                rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
                st.metric("🎯 Recall", f"{rec:.3f}")
            
            with col4:
                f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
                st.metric("🎯 F1-Score", f"{f1:.3f}")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Confusion Matrix (Classification only)
        if not st.session_state.is_regression:
            st.markdown("---")
            st.markdown("### 🔥 Confusion Matrix")
            
            cm = confusion_matrix(y_test, y_pred)
        
            fig = go.Figure(data=go.Heatmap(
                z=cm,
                x=[f"Pred {i}" for i in range(len(cm))],
                y=[f"True {i}" for i in range(len(cm))],
                colorscale='Purples',
                text=cm,
                texttemplate='%{text}',
                textfont={"size": 16},
                colorbar=dict(title="Count")
            ))
            
            fig.update_layout(
                template="plotly_dark",
                title="Confusion Matrix",
                plot_bgcolor='#0E1117',
                paper_bgcolor='#0E1117',
                font=dict(color='#FAFAFA'),
                xaxis_title="Predicted",
                yaxis_title="Actual"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
            # ROC Curve (for binary classification)
            if len(np.unique(y_test)) == 2:
                st.markdown("---")

                st.markdown("### 📈 ROC Curve")

            
                try:
                    y_pred_proba = model.predict_proba(X_test)[:, 1]
                    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
                    auc_score = roc_auc_score(y_test, y_pred_proba)
                    
                    fig = go.Figure()
                    
                    # ROC Curve
                    fig.add_trace(go.Scatter(
                        x=fpr, y=tpr,
                        mode='lines',
                        name=f'ROC Curve (AUC = {auc_score:.3f})',
                        line=dict(color='#8B5CF6', width=3)
                    ))
                    
                    # Diagonal line
                    fig.add_trace(go.Scatter(
                        x=[0, 1], y=[0, 1],
                        mode='lines',
                        name='Random Classifier',
                        line=dict(color='#00C9FF', width=2, dash='dash')
                    ))
                    
                    fig.update_layout(
                        template="plotly_dark",
                        title=f"ROC Curve (AUC = {auc_score:.3f})",
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        font=dict(color='#FAFAFA'),
                        xaxis_title="False Positive Rate",
                        yaxis_title="True Positive Rate"
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                except Exception as e:
                    st.warning(f"Could not generate ROC curve: {str(e)}")
        
        # Feature Importance (for tree-based models)
        if hasattr(model, 'feature_importances_'):
            st.markdown("---")
            st.markdown("### 🌟 Feature Importance")
            
            importance_df = pd.DataFrame({
                'Feature': st.session_state.feature_names,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False)
            
            fig = px.bar(
                importance_df,
                x='Importance',
                y='Feature',
                orientation='h',
                template='plotly_dark',
                color='Importance',
                color_continuous_scale='Purples'
            )
            
            fig.update_layout(
                plot_bgcolor='#0E1117',
                paper_bgcolor='#0E1117',
                font=dict(color='#FAFAFA')
            )
            
            st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# 🔮 PREDICTION SIMULATOR MODULE
# ═══════════════════════════════════════════════════════════════════════════

def prediction_simulator_page():
    """Interactive prediction interface"""
    st.markdown('<h1 class="glow-text">🔮 Prediction Simulator</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state.model is None:
        st.warning("⚠️ Please train a model first in the Model Engine section!")
        return
    
    st.markdown("### 🎯 Input Feature Values")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    # Get original dataframe for reference
    df = st.session_state.cleaned_df if st.session_state.cleaned_df is not None else st.session_state.df
    feature_names = st.session_state.feature_names
    
    # Create input fields dynamically
    input_data = {}
    
    # Organize inputs in columns (2 per row)
    num_features = len(feature_names)
    for i in range(0, num_features, 2):
        cols = st.columns(2)
        
        for j, col in enumerate(cols):
            if i + j < num_features:
                feature = feature_names[i + j]
                
                with col:
                    # Check if feature is numeric or categorical
                    if df[feature].dtype in ['int64', 'float64']:
                        # Numeric input
                        min_val = float(df[feature].min())
                        max_val = float(df[feature].max())
                        mean_val = float(df[feature].mean())
                        
                        input_data[feature] = st.number_input(
                            f"🔢 {feature}",
                            min_value=min_val,
                            max_value=max_val,
                            value=mean_val,
                            help=f"Range: {min_val:.2f} to {max_val:.2f}"
                        )
                    else:
                        # Categorical input
                        unique_values = df[feature].unique().tolist()
                        input_data[feature] = st.selectbox(
                            f"🏷️ {feature}",
                            unique_values,
                            help=f"Select from {len(unique_values)} options"
                        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Predict button
    st.markdown("---")
    
    if st.button("🔮 MAKE PREDICTION", use_container_width=True):
        try:
            # Prepare input
            input_df = pd.DataFrame([input_data])
            
            # Encode categorical features
            label_encoders = st.session_state.label_encoders
            for col in input_df.columns:
                if col in label_encoders and col != 'target':
                    le = label_encoders[col]
                    try:
                        input_df[col] = le.transform(input_df[col].astype(str))
                    except:
                        # Handle unseen categories
                        input_df[col] = 0
            
            # Make prediction
            model = st.session_state.model
            prediction = model.predict(input_df)[0]
            
            # Get probability if available
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(input_df)[0]
                max_proba = proba[prediction]
            else:
                max_proba = None
            
            # Decode prediction if target was encoded
            if 'target' in label_encoders:
                prediction_label = label_encoders['target'].inverse_transform([prediction])[0]
            else:
                prediction_label = prediction
            
            # Display result
            st.markdown("---")
            st.markdown("### 🎊 Prediction Result")
            
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"## 🎯 Predicted: **{prediction_label}**")
            
            with col2:
                if max_proba is not None:
                    st.markdown(f"## 📊 Confidence: **{max_proba * 100:.2f}%**")
            
            # Show probability distribution
            if hasattr(model, 'predict_proba'):
                st.markdown("---")
                st.markdown("#### 📊 Probability Distribution")
                
                # Create bar chart of probabilities
                if 'target' in label_encoders:
                    classes = label_encoders['target'].classes_
                else:
                    classes = [f"Class {i}" for i in range(len(proba))]
                
                prob_df = pd.DataFrame({
                    'Class': classes,
                    'Probability': proba
                })
                
                fig = px.bar(
                    prob_df,
                    x='Class',
                    y='Probability',
                    template='plotly_dark',
                    color='Probability',
                    color_continuous_scale='Purples'
                )
                
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    font=dict(color='#FAFAFA'),
                    yaxis_range=[0, 1]
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main application entry point"""
    
    # Page config
    st.set_page_config(
        page_title="AutoML Dashboard | Cyberpunk Edition",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    init_session_state()
    
    # Inject custom CSS
    inject_custom_css()
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <h1 style='color: #8B5CF6; text-shadow: 0 0 20px #8B5CF6;'>
                🚀 AutoML
            </h1>
            <p style='color: #00C9FF; font-size: 0.9rem;'>
                Cyberpunk FinTech Edition
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation Menu
        page = st.radio(
            "🧭 Navigation",
            [
                "📂 Data Ingestion",
                "📊 Advanced EDA",
                "🧹 Smart Cleaning",
                "🧠 Model Engine",
                "🔮 Prediction Simulator"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Info section
        st.markdown("""
        <div class="custom-card">
            <h4>ℹ️ Quick Stats</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.df is not None:
            df = st.session_state.cleaned_df if st.session_state.cleaned_df is not None else st.session_state.df
            st.metric("Dataset Rows", f"{len(df):,}")
            st.metric("Dataset Columns", len(df.columns))
            if st.session_state.model is not None:
                st.success("✅ Model Trained")
            else:
                st.info("⏳ No Model Yet")
        else:
            st.info("No dataset loaded")
        
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; font-size: 0.8rem; color: #8B5CF6;'>
            Built with ❤️ using Streamlit<br>
            © 2024 AutoML Dashboard
        </div>
        """, unsafe_allow_html=True)
    
    # Route to appropriate page
    if page == "📂 Data Ingestion":
        data_ingestion_page()
    elif page == "📊 Advanced EDA":
        advanced_eda_page()
    elif page == "🧹 Smart Cleaning":
        smart_data_cleaning_page()
    elif page == "🧠 Model Engine":
        model_engine_page()
    elif page == "🔮 Prediction Simulator":
        prediction_simulator_page()

if __name__ == "__main__":
    main()
