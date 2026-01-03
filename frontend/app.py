import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Drone Intelligence System",
    layout="wide"
)

st.title("🚁 Drone Intelligence System")

tab1, tab2, tab3, tab4 = st.tabs([
    "Ask Drone AI",
    "ROI Calculator",
    "Flight Time Estimator",
    "DGCA Compliance Check"
])

# ---------------- CHAT (RAG) ----------------
with tab1:
    st.subheader("Ask drone-related questions")
    question = st.text_input("Enter your question")

    if st.button("Ask"):
        try:
            res = requests.post(
                f"{API_URL}/chat",
                json={"question": question},
                timeout=10
            )

            if res.status_code != 200:
                st.error(f"API Error: {res.text}")
            else:
                data = res.json()
                st.success(data.get("answer", "No answer returned"))

                if data.get("source"):
                    st.caption(f"Source: {data['source']}")

        except Exception as e:
            st.error(f"Error contacting API: {e}")


# ---------------- ROI CALCULATOR ----------------
with tab2:
    acres = st.number_input("Farm size (acres)", min_value=1, step=1)

    if st.button("Calculate ROI"):
        try:
            res = requests.post(
                f"{API_URL}/roi",
                json={"farm_size_acres": acres}
            )

            st.success(res.json()["result"])

        except Exception as e:
            st.error(f"Error: {e}")



# ---------------- FLIGHT TIME ESTIMATOR ----------------
with tab3:
    st.subheader("Drone Flight Time Estimator (Engineering Model)")

    battery_percent = st.slider("Battery Percentage (%)", 0, 100, 70)
    battery_capacity = st.number_input(
        "Battery Capacity (Ah)", min_value=1.0, value=10.0, step=0.5
    )
    motors = st.number_input(
        "Number of Motors", min_value=1, value=4, step=1
    )
    motor_current = st.number_input(
        "Motor Current per Motor (A)", min_value=1.0, value=8.0, step=0.5
    )

    if st.button("Estimate Flight Time"):
        res = requests.post(
            f"{API_URL}/flight-time",
            json={
                "battery_percent": battery_percent,
                "battery_capacity_ah": battery_capacity,
                "motors": motors,
                "motor_current_a": motor_current
            }
        )

        st.success(res.json()["result"])

# ---------------- DGCA COMPLIANCE CHECK ----------------
with tab4:
    st.subheader("DGCA Drone Compliance Checker")

    weight = st.number_input("Drone Weight (kg)", min_value=0.1, step=0.1)
    zone = st.selectbox("Airspace Zone", ["green", "yellow", "red"])

    if st.button("Check Compliance"):
        try:
            res = requests.post(
                f"{API_URL}/compliance",
                json={
                    "drone_weight_kg": weight,
                    "zone": zone
                },
                timeout=10
            )

            if res.status_code != 200:
                st.error(f"API Error: {res.text}")
            else:
                data = res.json()
                st.success(data["result"])

        except Exception as e:
            st.error(f"Error: {e}")
