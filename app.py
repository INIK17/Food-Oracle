import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Food Oracle",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ------------------------------
   Main Background
------------------------------ */

.stApp {
    background: linear-gradient(135deg, #fffaf7 0%, #fff4ee 100%);
}

/* Remove default top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* ------------------------------
   Main Title
------------------------------ */

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: #f4511e;
    margin-bottom: 5px;
    letter-spacing: -1px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #666666;
    margin-bottom: 35px;
}

/* ------------------------------
   Hero Section
------------------------------ */

.hero {
    background: linear-gradient(135deg, #ff6533, #ff4b16);
    padding: 35px 40px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 15px 35px rgba(255, 81, 30, 0.22);
}

.hero h2 {
    font-size: 30px;
    margin-bottom: 12px;
    color: white;
}

.hero p {
    font-size: 17px;
    line-height: 1.6;
    color: white;
}

/* ------------------------------
   Info Cards
------------------------------ */

.info-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    min-height: 165px;
    border: 1px solid #eeeeee;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.info-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(255,81,27,0.18);
}

.info-card .card-icon {
    font-size: 38px;
    margin-bottom: 10px;
    opacity: 1;
}

.info-card h3 {
    margin: 5px 0 8px 0;
    color: #ff511e;
    font-size: 20px;
}

.info-card p {
    color: #666666;
    font-size: 14px;
    margin: 0;
}

/* ------------------------------
   Section Heading
------------------------------ */

.delivery-heading {
    margin-top: 35px;
    margin-bottom: 25px;
    padding: 16px 22px;
    background: linear-gradient(90deg, #fff0e9, #ffffff);
    border-left: 6px solid #ff511e;
    border-radius: 12px;
    color: #292b35;
    font-size: 27px;
    font-weight: 700;
}

/* ------------------------------
   Labels
------------------------------ */

label {
    font-weight: 600 !important;
    color: #444444 !important;
}

/* ------------------------------
   Input Styling
------------------------------ */

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

div[data-testid="stNumberInput"] {
    border-radius: 10px;
}

/* ------------------------------
   Button
------------------------------ */

div.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 700;
    background: #ff511e;
    color: white;
    border: none;
    box-shadow: 0 8px 20px rgba(255,81,30,0.20);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: #e84315;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(255,81,30,0.30);
}

/* ------------------------------
   Prediction Result
------------------------------ */

.result-box {
    background: linear-gradient(135deg, #ff511e, #ff7a45);
    padding: 35px;
    border-radius: 22px;
    text-align: center;
    color: white;
    margin-top: 30px;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(255,81,30,0.25);
}

.result-box h2 {
    font-size: 24px;
    margin-bottom: 8px;
    color: white;
}

.result-box .time {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

/* ------------------------------
   Footer
------------------------------ */

.footer {
    text-align: center;
    color: #888888;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #eeeeee;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("food_oracle_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error("❌ Model could not be loaded.")
    st.code(str(e))
    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🍔 Food Oracle</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Food Delivery Time Prediction</div>',
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
<h2>🔮 Predict Your Delivery Time</h2>
<p>Enter the delivery and order details below. Our Machine Learning model will estimate the expected delivery time using multiple real-world factors.</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# PROJECT HIGHLIGHTS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="card-icon">🧠</div>
        <h3>Machine Learning</h3>
        <p>Random Forest based prediction model</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="card-icon">⚡</div>
        <h3>Fast Prediction</h3>
        <p>Instant delivery time estimation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="card-icon">🎯</div>
        <h3>Smart Estimation</h3>
        <p>Multiple delivery factors considered</p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# DELIVERY INFORMATION
# =========================================================

st.markdown(
    '<div class="delivery-heading">📋 Delivery Information</div>',
    unsafe_allow_html=True
)


# =========================================================
# ROW 1
# =========================================================

col1, col2 = st.columns(2)

with col1:
    weather = st.selectbox(
        "Weather",
        ["Clear", "Rainy", "Foggy", "Snowy", "Stormy"]
    )

with col2:
    order_hour = st.number_input(
        "Order Hour",
        min_value=0.0,
        max_value=23.0,
        value=10.0,
        step=1.0
    )


# =========================================================
# ROW 2
# =========================================================

col1, col2 = st.columns(2)

with col1:
    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Bike", "Scooter", "Car"]
    )

with col2:
    is_weekend = st.number_input(
        "Is Weekend",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=1.0
    )


# =========================================================
# ROW 3
# =========================================================

col1, col2 = st.columns(2)

with col1:
    restaurant_load = st.selectbox(
        "Restaurant Load",
        ["Low", "Medium", "High"]
    )

with col2:
    is_festival = st.number_input(
        "Is Festival",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=1.0
    )


# =========================================================
# ROW 4
# =========================================================

col1, col2 = st.columns(2)

with col1:
    delivery_distance = st.selectbox(
        "Delivery Distance Category",
        ["Short", "Medium", "Long"]
    )

with col2:
    rider_experience = st.number_input(
        "Rider Experience (Years)",
        min_value=0.0,
        max_value=20.0,
        value=3.0,
        step=1.0
    )


# =========================================================
# ROW 5
# =========================================================

col1, col2 = st.columns(2)

with col1:
    traffic_level = st.selectbox(
        "Traffic Level",
        ["Low", "Medium", "High"]
    )

with col2:
    rider_rating = st.number_input(
        "Rider Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )


# =========================================================
# ROW 6
# =========================================================

col1, col2 = st.columns(2)

with col1:
    delivery_priority = st.selectbox(
        "Delivery Priority",
        ["Low", "Medium", "High"]
    )

with col2:
    restaurant_rating = st.number_input(
        "Restaurant Rating",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )


# =========================================================
# ROW 7
# =========================================================

col1, col2 = st.columns(2)

with col1:
    order_items = st.number_input(
        "Order Items",
        min_value=1.0,
        max_value=30.0,
        value=2.0,
        step=1.0
    )

with col2:
    preparation_time = st.number_input(
        "Preparation Time (Min)",
        min_value=1.0,
        max_value=120.0,
        value=15.0,
        step=1.0
    )


# =========================================================
# ROW 8
# =========================================================

col1, col2 = st.columns(2)

with col1:
    road_distance = st.number_input(
        "Road Distance (km)",
        min_value=0.1,
        max_value=100.0,
        value=5.0,
        step=0.5
    )

with col2:
    number_signals = st.number_input(
        "Number of Signals",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=1.0
    )


# =========================================================
# ROW 9
# =========================================================

col1, col2 = st.columns(2)

with col1:
    average_speed = st.number_input(
        "Average Speed (kmph)",
        min_value=1.0,
        max_value=100.0,
        value=10.0,
        step=1.0
    )

with col2:
    st.write("")


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔮 Predict Delivery Time"
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    input_data = pd.DataFrame([{
        "Weather": weather,
        "Vehicle_Type": vehicle_type,
        "Restaurant_Load": restaurant_load,
        "Delivery_Distance_Category": delivery_distance,
        "Traffic_Level": traffic_level,
        "Delivery_Priority": delivery_priority,
        "Order_Hour": order_hour,
        "Is_Weekend": is_weekend,
        "Is_Festival": is_festival,
        "Rider_Experience_Years": rider_experience,
        "Rider_Rating": rider_rating,
        "Restaurant_Rating": restaurant_rating,
        "Order_Items": order_items,
        "Preparation_Time_Min": preparation_time,
        "Road_Distance_km": road_distance,
        "Number_of_Signals": number_signals,
        "Average_Speed_kmph": average_speed
    }])

    try:

        prediction = model.predict(input_data)[0]

        prediction = float(prediction)

        # Prevent negative delivery time
        prediction = max(0, prediction)

        st.markdown(f"""
<div class="result-box">

<h2>🎯 Estimated Delivery Time</h2>

<div class="time">
{prediction:.1f} <span>minutes</span>
</div>

<div class="result-status">
🚴 Your order is expected to arrive soon
</div>

<p>
🤖 Prediction generated using the Random Forest Machine Learning model,
based on traffic, distance, rider, restaurant and order details.
</p>

</div>
""", unsafe_allow_html=True)

            # Additional information
        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-icon">⏱️</div>
                <div class="result-label">Estimated Time</div>
                <div class="result-value">{prediction:.1f} min</div>
            </div>
            """, unsafe_allow_html=True)

        with result_col2:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-icon">📍</div>
                <div class="result-label">Road Distance</div>
                <div class="result-value">{road_distance:.1f} km</div>
            </div>
            """, unsafe_allow_html=True)

        with result_col3:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-icon">🚦</div>
                <div class="result-label">Average Speed</div>
                <div class="result-value">{average_speed:.1f} km/h</div>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:

        st.error("❌ Prediction failed.")

        st.code(str(e))

        st.info(
            "Please check that the input values match "
            "the categories used while training the model."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    🍔 Food Oracle &nbsp; | &nbsp;
    AI-Powered Food Delivery Prediction
    <br><br>
    Built with Python • Streamlit • Scikit-Learn
</div>
""", unsafe_allow_html=True)