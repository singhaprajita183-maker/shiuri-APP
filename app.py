import streamlit as st
import time

st.set_page_config(page_title="Shiori (栞)", page_icon="📚", layout="wide")

# Custom Dark Theme CSS Injection
st.markdown("""
    <style>
    .stApp { background-color: #07090E; color: white; }
    .stButton>button { background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%); color: white; border-radius: 8px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Top Bar
col_logo, col_search, col_pts = st.columns([1, 2, 1])
with col_logo:
    st.title("栞 Shiori")
with col_search:
    st.text_input("Search", placeholder="Search books, authors, ISBN...", label_visibility="collapsed")
with col_pts:
    st.metric(label="Your Impact Points", value="🌱 1,250 pts")

# Navigation Tabs
tabs = st.tabs(["📚 Feed", "📷 AI Vision Scanner", "🔄 Smart Exchange", "🛡️ Trust & Safety", "🌱 ESG Dashboard"])

# TAB 1: FEED
with tabs[0]:
    st.subheader("Learn. Share. Grow. Together.")
    st.caption("Buy, Sell, Donate or Swap educational materials in your community.")
    
    col1, col2, col3, col4 = st.columns(4)
    books = [
        ("NCERT Physics", "Class 11", "₹280", "Aarav S."),
        ("Mathematics", "Class 12", "₹320", "Diya S."),
        ("Organic Chem", "Class 12", "₹350", "Rohan D."),
        ("Indian Polity", "UPSC", "₹180", "Meera I.")
    ]
    
    for i, col in enumerate([col1, col2, col3, col4]):
        title, cls, price, seller = books[i]
        with col:
            st.container(border=True).markdown(f"""
                ### {title}
                **{cls}**  
                Seller: {seller}  
                #### {price}
            """)
            st.button(f"Buy #{i+1}")

# TAB 2: SCANNER
with tabs[1]:
    st.subheader("📷 AI Vision Scanner")
    st.write("Scan book cover or ISBN barcode to extract details.")
    
    if st.button("Simulate AI Camera Scan"):
        with st.spinner("AI analyzing book cover..."):
            time.sleep(1)
            st.success("✓ Scan Complete!")
            st.json({
                "Title": "HC Verma — Concepts of Physics Vol 1",
                "Author": "H.C. Verma",
                "Board": "CBSE / JEE Prep",
                "Est. Resale Price": "₹320 - ₹420"
            })

# TAB 3: EXCHANGE
with tabs[2]:
    st.subheader("🔄 Smart Exchange Engine")
    col_have, col_want = st.columns(2)
    with col_have:
        have = st.text_input("YOU HAVE", "Mathematics Class 12 - NCERT")
    with col_want:
        want = st.text_input("YOU WANT", "Physics Part 1 Class 11 - NCERT")
        
    if st.button("Find Graph Matches"):
        st.info("Searching Student Graph... 3 Direct Matches Found in Laxmi Nagar!")

# TAB 4: SAFETY
with tabs[3]:
    st.subheader("🛡️ Trust & Safety Hub")
    st.write("- 🎓 **Verified Student Profiles** via School Email")
    st.write("- 🔒 **Privacy by Design** (Location approximate only)")
    st.write("- 💬 **Secure In-App Chat**")

# TAB 5: ESG DASHBOARD
with tabs[4]:
    st.subheader("🌱 Your Personal Impact Dashboard")
    m1, m2, m3 = st.columns(3)
    m1.metric("Impact Points", "1,250")
    m2.metric("Books Reused", "42")
    m3.metric("CO2e Avoided", "98.4 kg")
