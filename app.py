import streamlit as st
import datetime
import random

# Cache static data
@st.cache_data
def get_city_data():
    return {
        "Paris": {
            "attractions": [
                ("Eiffel Tower", "https://maps.google.com/?q=Eiffel+Tower"),
                ("Louvre Museum", "https://maps.google.com/?q=Louvre+Museum"),
                ("Notre-Dame Cathedral", "https://maps.google.com/?q=Notre-Dame+Cathedral")
            ],
            "food": ["Croissants", "Crepes", "French Onion Soup"]
        },
        "Tokyo": {
            "attractions": [
                ("Tokyo Tower", "https://maps.google.com/?q=Tokyo+Tower"),
                ("Shibuya Crossing", "https://maps.google.com/?q=Shibuya+Crossing"),
                ("Senso-ji Temple", "https://maps.google.com/?q=Senso-ji+Temple")
            ],
            "food": ["Sushi", "Ramen", "Takoyaki"]
        },
        "New York": {
            "attractions": [
                ("Statue of Liberty", "https://maps.google.com/?q=Statue+of+Liberty"),
                ("Central Park", "https://maps.google.com/?q=Central+Park"),
                ("Times Square", "https://maps.google.com/?q=Times+Square")
            ],
            "food": ["Bagels", "Hot Dogs", "New York-style Pizza"]
        },
        "London": {
            "attractions": [
                ("Big Ben", "https://maps.google.com/?q=Big+Ben"),
                ("London Eye", "https://maps.google.com/?q=London+Eye"),
                ("Tower Bridge", "https://maps.google.com/?q=Tower+Bridge")
            ],
            "food": ["Fish and Chips", "Shepherd’s Pie", "English Breakfast"]
        },
        "Rome": {
            "attractions": [
                ("Colosseum", "https://maps.google.com/?q=Colosseum"),
                ("Trevi Fountain", "https://maps.google.com/?q=Trevi+Fountain"),
                ("Pantheon", "https://maps.google.com/?q=Pantheon")
            ],
            "food": ["Pizza", "Pasta", "Gelato"]
        },
        "Barcelona": {
            "attractions": [
                ("Sagrada Familia", "https://maps.google.com/?q=Sagrada+Familia"),
                ("Park Güell", "https://maps.google.com/?q=Park+Güell"),
                ("La Rambla", "https://maps.google.com/?q=La+Rambla")
            ],
            "food": ["Tapas", "Paella", "Churros"]
        },
        "Dubai": {
            "attractions": [
                ("Burj Khalifa", "https://maps.google.com/?q=Burj+Khalifa"),
                ("Dubai Mall", "https://maps.google.com/?q=Dubai+Mall"),
                ("Palm Jumeirah", "https://maps.google.com/?q=Palm+Jumeirah")
            ],
            "food": ["Shawarma", "Harees", "Luqaimat"]
        },
        "Singapore": {
            "attractions": [
                ("Marina Bay Sands", "https://maps.google.com/?q=Marina+Bay+Sands"),
                ("Gardens by the Bay", "https://maps.google.com/?q=Gardens+by+the+Bay"),
                ("Sentosa Island", "https://maps.google.com/?q=Sentosa+Island")
            ],
            "food": ["Laksa", "Chicken Rice", "Chilli Crab"]
        },
        "Istanbul": {
            "attractions": [
                ("Hagia Sophia", "https://maps.google.com/?q=Hagia+Sophia"),
                ("Blue Mosque", "https://maps.google.com/?q=Blue+Mosque"),
                ("Grand Bazaar", "https://maps.google.com/?q=Grand+Bazaar")
            ],
            "food": ["Kebab", "Baklava", "Turkish Delight"]
        },
        "Bangkok": {
            "attractions": [
                ("Grand Palace", "https://maps.google.com/?q=Grand+Palace"),
                ("Wat Arun", "https://maps.google.com/?q=Wat+Arun"),
                ("Chatuchak Market", "https://maps.google.com/?q=Chatuchak+Market")
            ],
            "food": ["Pad Thai", "Tom Yum", "Mango Sticky Rice"]
        }
    }

budgets = {
    "Low 💸": "Use public transport, explore free attractions, try local street food.",
    "Medium 💼": "Mix of paid and free attractions, mid-range restaurants.",
    "Luxury 💎": "Private tours, fine dining, premium experiences."
}

# UI
st.set_page_config(page_title="TripWise", layout="centered")
st.title("🌍 TripWise – Your Personalized Travel Planner")

st.markdown("Plan your dream trip in seconds! Choose your destination, travel dates, and budget – we'll do the rest. ✈️")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=100)
st.sidebar.header("📋 Trip Details")
city_data = get_city_data()
city = st.sidebar.selectbox("🌆 Select City", list(city_data.keys()))
start_date = st.sidebar.date_input("📅 Start Date", datetime.date.today())
end_date = st.sidebar.date_input("📅 End Date", datetime.date.today() + datetime.timedelta(days=2))
budget = st.sidebar.selectbox("💰 Budget Type", list(budgets.keys()))

trip_days = (end_date - start_date).days + 1
if trip_days <= 0:
    st.error("⚠ Please select a valid date range.")
else:
    if st.sidebar.button("🎒 Generate Itinerary"):
        with st.spinner("✏️ Planning your itinerary..."):
            attractions = city_data[city]["attractions"]
            foods = city_data[city]["food"]

            st.success("📝 Here's your personalized plan!")
            st.subheader(f"📌 {trip_days}-Day Plan for {city}")
            st.markdown(f"**Budget**: *{budget}* – _{budgets[budget]}_")
            st.markdown("---")

            for day in range(1, trip_days + 1):
                place = random.choice(attractions)
                food = random.choice(foods)
                st.markdown(f"### 🗓 Day {day}")
                st.markdown(f"- 📍 *Visit:* [{place[0]}]({place[1]})")
                st.markdown(f"- 🍽️ *Try:* {food}")
                st.markdown("---")

