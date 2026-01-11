import streamlit as st
import pandas as pd
from openai import OpenAI
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Intelligent Restaurant Food Service System: A Decision centric Smart Approach",
    layout="wide"
)

st.title("🍽️ Intelligent Restaurant Food Service System")
st.subheader("A Decision-Centric Smart Approach using Agentic Generative AI")
st.caption("FutureEats | Multi-Agent AI for Food & Hospitality Intelligence")

# =====================================================
# OPENAI CONFIG
# =====================================================
if "OPENAI_API_KEY" not in st.secrets:
    st.error("⚠️ OpenAI API Key missing in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# =====================================================
# MULTILINGUAL SUPPORT
# =====================================================
language = st.selectbox(
    "🌍 Select Output Language",
    ["English", "Hindi", "Marathi", "Spanish", "French"]
)

LANG_INSTRUCTION = {
    "English": "Respond in English.",
    "Hindi": "Respond in simple Hindi.",
    "Marathi": "Respond in simple Marathi.",
    "Spanish": "Respond in Spanish.",
    "French": "Respond in French."
}

# =====================================================
# LEADERBOARD STATE
# =====================================================
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {
        "Chef Innovation": 0,
        "Waste Reduction": 0,
        "Marketing Creativity": 0,
        "Event Excellence": 0,
        "Visual Appeal": 0
    }

def add_score(category, points):
    st.session_state.leaderboard[category] += points

# =====================================================
# AGENT-BASED AI ENGINE
# =====================================================
def agentic_ai(agent_role, task_prompt):
    prompt = f"""
    You are acting as the following specialized AI agent:
    ROLE: {agent_role}

    TASK:
    {task_prompt}

    OUTPUT RULES:
    - Be strategic, practical, and decision-focused
    - Think like an industry expert
    - {LANG_INSTRUCTION[language]}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.75,
        max_tokens=1100
    )
    return response.choices[0].message.content.strip()

# =====================================================
# DATASET – EAT FIT (31 DAYS)
# =====================================================
menu_df = pd.DataFrame({
    "Day": list(range(1, 32)),
    "Dish Name": ["Quinoa Power Bowl", "Herb Chicken", "Vegan Buddha Bowl", "Paneer Stir Fry", "Oats Smoothie"] * 7,
    "Category": ["Main", "Main", "Main", "Main", "Breakfast"] * 7,
    "Diet": ["Vegan", "High-Protein", "Vegan", "Vegetarian", "Gluten-Free"] * 7,
    "Feedback": ["Excellent", "Very Good", "Good", "Excellent", "Good"] * 7
})

# =====================================================
# FEATURE 1 – CHEF RECIPE AGENT
# =====================================================
st.header("👨‍🍳 Feature 1: AI Recipe Innovation Agent")

ingredients = st.text_input("Available Ingredients")
seasonal = st.text_input("Seasonal / Local Produce")

if st.button("🍳 Generate Intelligent Recipes"):
    output = agentic_ai(
        "Culinary Innovation Agent",
        f"""
        Ingredients: {ingredients}
        Seasonal Produce: {seasonal}

        Generate:
        1. Three signature-level recipe ideas
        2. Nutritional positioning
        3. Commercial viability
        4. Brand differentiation logic
        """
    )
    add_score("Chef Innovation", 10)
    st.write(output)

st.dataframe(menu_df)

# =====================================================
# FEATURE 2 – SUSTAINABILITY AGENT
# =====================================================
st.header("♻️ Feature 2: Leftover Optimization Agent")

leftovers = st.text_input("Leftover Raw Ingredients")

if st.button("🌱 Optimize Leftovers"):
    output = agentic_ai(
        "Sustainability & Waste Reduction Agent",
        f"""
        Leftover Ingredients: {leftovers}

        Provide:
        - Next-day menu reuse
        - Zero-waste strategy
        - Shelf-life & safety guidance
        - Estimated waste reduction %
        """
    )
    add_score("Waste Reduction", 8)
    st.write(output)

# =====================================================
# FEATURE 3 – MARKETING AGENT
# =====================================================
st.header("📢 Feature 3: Promotion Strategy Agent")

promo_type = st.selectbox(
    "Promotion Objective",
    ["Discount", "BOGO", "Health Campaign", "Festival Theme"]
)

if st.button("🎯 Generate Promotion"):
    output = agentic_ai(
        "Restaurant Marketing Strategy Agent",
        f"""
        Promotion Type: {promo_type}

        Generate:
        - Campaign idea
        - Psychological trigger
        - Social media caption
        - Expected business impact
        """
    )
    add_score("Marketing Creativity", 7)
    st.write(output)

# =====================================================
# FEATURE 4 – EVENT PLANNING AGENT
# =====================================================
st.header("🎉 Feature 4: Event Planning Agent")

event_type = st.selectbox(
    "Event Type",
    ["Birthday", "Corporate Event", "Family Night", "Wellness Brunch"]
)
guests = st.number_input("Number of Guests", 10, 300, 50)

if st.button("📅 Plan Event"):
    output = agentic_ai(
        "Event Operations & Experience Agent",
        f"""
        Event Type: {event_type}
        Guests: {guests}

        Provide:
        - Seating plan
        - Menu strategy
        - Theme & decor
        - Staff workflow
        - Guest engagement ideas
        """
    )
    add_score("Event Excellence", 9)
    st.write(output)

# =====================================================
# FEATURE 5 – VISUAL MENU AGENT
# =====================================================
st.header("📸 Feature 5: Visual Menu Personalization Agent")

uploaded_image = st.file_uploader("Upload Dish Image", type=["jpg", "png", "jpeg"])
diet_pref = st.selectbox(
    "Diet Preference",
    ["Vegan", "Vegetarian", "Gluten-Free", "Keto", "High-Protein"]
)

if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, width=250)

    if st.button("🍽️ Personalize Menu"):
        output = agentic_ai(
            "Visual Intelligence & Menu Personalization Agent",
            f"""
            Customer Diet Preference: {diet_pref}

            Generate:
            - Dish inference
            - Healthy alternatives
            - Ingredient substitutions
            - Cross-sell suggestions
            """
        )
        add_score("Visual Appeal", 6)
        st.write(output)

# =====================================================
# LEADERBOARD DASHBOARD
# =====================================================
st.header("🏆 Gamification & Performance Leaderboard")

leaderboard_df = pd.DataFrame.from_dict(
    st.session_state.leaderboard,
    orient="index",
    columns=["Score"]
)

st.dataframe(leaderboard_df)

st.success(
    "🎮 This leaderboard drives behavioral change by rewarding innovation, "
    "sustainability, creativity, and customer experience."
)

# =====================================================
# FOOTER
# =====================================================
st.write("---")
st.write("🚀 Powered by OpenAI GPT-4o-mini | Agent-Based Generative AI System")
st.caption("Academic-grade | Decision-Centric | Industry-Ready")
