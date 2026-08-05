import streamlit as st
from PIL import Image
import os

# ---------- Page Config ----------
st.set_page_config(
    page_title="Haiti Culture Connection",
    page_icon="🇭🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS with Haitian Colors ----------
st.markdown("""
    <style>
    /* Main background - dark blue */
    .stApp {
        background: #0a1628 !important;
    }
    
    /* Sidebar - matching dark blue */
    .stSidebar,
    .stSidebar .sidebar-content,
    section[data-testid="stSidebar"] {
        background: #0d1f3c !important;
    }
    
    .stSidebar .stMarkdown,
    .stSidebar .stCaption,
    .stSidebar .stButton button {
        color: #ffffff !important;
    }
    
    /* Main title - Haitian colors */
    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #00209f, #d21034, #00209f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        padding: 20px 0;
        text-shadow: 0 0 60px rgba(0, 32, 159, 0.3);
        animation: glow 3s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(210, 16, 52, 0.2)); }
        50% { filter: drop-shadow(0 0 40px rgba(0, 32, 159, 0.4)); }
    }
    
    .sub-title {
        color: #ffcc00;
        font-size: 1.2rem;
        text-align: center;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    
    /* Section headers */
    .section-title {
        color: #ffcc00;
        font-size: 2rem;
        font-weight: 700;
        border-bottom: 3px solid #d21034;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    
    .section-subtitle {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 10px;
    }
    
    /* Cards */
    .culture-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        transition: 0.3s;
        backdrop-filter: blur(10px);
    }
    .culture-card:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: #d21034;
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(210, 16, 52, 0.15);
    }
    .culture-card h3 {
        color: #ffcc00;
        margin-bottom: 10px;
    }
    .culture-card p {
        color: #dddddd;
        line-height: 1.6;
    }
    
    /* Sidebar navigation */
    .nav-item {
        color: #ffffff !important;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
        transition: 0.3s;
        text-decoration: none;
        display: block;
        font-weight: 500;
    }
    .nav-item:hover {
        background: rgba(210, 16, 52, 0.2);
        color: #ffcc00 !important;
    }
    
    /* Logo container */
    .logo-container {
        text-align: center;
        padding: 20px 0;
    }
    .logo-container img {
        max-width: 200px;
        border-radius: 15px;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 30px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        margin-top: 40px;
        color: #888888;
        font-size: 0.9rem;
    }
    .footer .heart {
        color: #d21034;
    }
    
    /* Video container */
    .video-container {
        border-radius: 15px;
        overflow: hidden;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    /* Image styling */
    .stImage {
        border-radius: 15px;
        overflow: hidden;
    }
    
    /* Text colors */
    .white-text {
        color: #ffffff !important;
    }
    .gold-text {
        color: #ffcc00 !important;
    }
    .red-text {
        color: #d21034 !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #00209f, #d21034) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 30px rgba(210, 16, 52, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
with st.sidebar:
    st.markdown("""
    <div class="logo-container">
        <img src="https://via.placeholder.com/200x200/00209f/d21034?text=🇭🇹" alt="Haiti Culture Logo" style="width:150px;border-radius:50%;border:3px solid #ffcc00;">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### 🌍 Explore Haiti")
    
    # Create navigation buttons
    nav_items = [
        "🏠 Home",
        "📜 History",
        "🎵 Music",
        "🎨 Art",
        "🍲 Cuisine",
        "🗣️ Language",
        "🎉 Festivals"
    ]
    
    selected = st.radio(
        "Navigate",
        nav_items,
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Logo upload section
    st.markdown("### 📤 Upload Logo")
    uploaded_logo = st.file_uploader("Upload your logo", type=["png", "jpg", "jpeg", "svg"])
    
    if uploaded_logo is not None:
        # The logo will be displayed in the main content
        st.session_state['logo'] = uploaded_logo
        st.success("✅ Logo uploaded successfully!")
    
    st.markdown("---")
    st.caption("🇭🇹 Haiti Culture Connection")
    st.caption("v1.0 | Built with ❤️")

# ---------- Main Content ----------

# Display logo if uploaded
if 'logo' in st.session_state and st.session_state['logo'] is not None:
    logo = Image.open(st.session_state['logo'])
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo, use_container_width=True)

# Header
st.markdown('<div class="main-title">🇭🇹 Haiti Culture Connection</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">✨ Celebrating the Heart and Soul of Haiti ✨</div>', unsafe_allow_html=True)

# ---------- Page Content ----------
if selected == "🏠 Home":
    st.markdown('<h2 class="section-title">🏠 Welcome to Haiti Culture Connection</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h3>🇭🇹 Discover the Rich Culture of Haiti</h3>
            <p>
                Haiti is a nation with a vibrant and resilient culture, shaped by a unique blend of 
                African, French, and Caribbean influences. From the rhythmic beats of Compas and 
                Rara to the vibrant colors of Haitian art, every aspect of Haitian culture tells a 
                story of strength, creativity, and community.
            </p>
            <p>
                <strong style="color:#ffcc00;">Explore our sections to learn about:</strong><br>
                📜 History – The first independent Black republic<br>
                🎵 Music – The soul of Haiti<br>
                🎨 Art – Vibrant expressions of Haitian life<br>
                🍲 Cuisine – A delicious fusion of flavors<br>
                🗣️ Language – Creole and French<br>
                🎉 Festivals – Celebrations of faith and community
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card" style="text-align:center;">
            <h3>🇭🇹 Quick Facts</h3>
            <p style="font-size:0.95rem;">
                <strong style="color:#ffcc00;">Capital:</strong> Port-au-Prince<br>
                <strong style="color:#ffcc00;">Population:</strong> 11.4 million<br>
                <strong style="color:#ffcc00;">Languages:</strong> French, Haitian Creole<br>
                <strong style="color:#ffcc00;">Currency:</strong> Gourde (HTG)<br>
                <strong style="color:#ffcc00;">Independence:</strong> January 1, 1804
            </p>
            <p style="font-size:1.5rem; margin-top:10px;">
                🇭🇹❤️💙
            </p>
        </div>
        """, unsafe_allow_html=True)

elif selected == "📜 History":
    st.markdown('<h2 class="section-title">📜 Haitian History</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h3>🇭🇹 The First Independent Black Republic</h3>
            <p>
                Haiti's history is one of resilience and triumph. On January 1, 1804, Haiti became 
                the first independent Black republic in the world, following a successful slave 
                revolt led by Toussaint Louverture and Jean-Jacques Dessalines.
            </p>
            <p>
                The Haitian Revolution (1791-1804) was the only successful slave uprising in history, 
                leading to the abolition of slavery and the establishment of a free nation. Today, 
                Haiti stands as a symbol of freedom, resistance, and hope for oppressed people worldwide.
            </p>
            <p>
                <strong style="color:#ffcc00;">Key Historical Sites:</strong><br>
                • The Citadelle Laferrière – A UNESCO World Heritage Site<br>
                • Sans-Souci Palace – Symbol of Haitian royalty<br>
                • The Cathedral of Port-au-Prince – Rich architectural history
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://via.placeholder.com/400x300/00209f/d21034?text=🇭🇹+Haitian+History", use_container_width=True)
        st.caption("📸 The Citadelle Laferrière - A symbol of Haitian freedom")

elif selected == "🎵 Music":
    st.markdown('<h2 class="section-title">🎵 Haitian Music</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h3>🎶 The Rhythm of Haiti</h3>
        <p>
            Haitian music is a vibrant fusion of African rhythms, French melodies, and Caribbean 
            influences. It is the heartbeat of Haitian culture, expressing joy, sorrow, and the 
            resilience of the Haitian people.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h4>🎵 Compas (Konpa)</h4>
            <p>
                The most popular modern genre in Haiti. Created by Nemours Jean-Baptiste in the 1950s, 
                Compas is a smooth, danceable rhythm that blends jazz, Latin, and Caribbean sounds.
            </p>
            <p><strong style="color:#ffcc00;">Famous Artists:</strong> Tabou Combo, Coupé Cloué, Jean Baptiste</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>🥁 Rara</h4>
            <p>
                A traditional Afro-Haitian genre performed during Carnival and Lent. Rara features 
                bamboo trumpets (vaksen), drums, and call-and-response vocals.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card">
            <h4>🎸 Meringue</h4>
            <p>
                A traditional Haitian dance music that predates Compas. It features a slower, more 
                romantic rhythm and is often performed at formal events and ceremonies.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>🎶 Vodou Rhythms</h4>
            <p>
                Traditional ceremonial music played during Vodou ceremonies, featuring drums, bells, 
                and chanting. These rhythms are deeply spiritual and connect practitioners to their ancestors.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Video placeholder
    st.markdown("""
    <div class="culture-card">
        <h4>🎬 Watch: Haitian Music Documentary (Placeholder)</h4>
        <div class="video-container">
            <div style="background:#0d1f3c; padding:60px; text-align:center; color:#888;">
                🎥 YouTube Video Will Appear Here
                <p style="font-size:0.8rem; margin-top:10px;">Replace with actual YouTube embed</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "🎨 Art":
    st.markdown('<h2 class="section-title">🎨 Haitian Art</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h3>🎨 Vibrant Expressions of Haitian Life</h3>
        <p>
            Haitian art is known for its vibrant colors, bold patterns, and powerful storytelling. 
            From the bustling streets of Port-au-Prince to the rural villages, art is everywhere in Haiti.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h4>🖼️ Naïve Art</h4>
            <p>
                Haiti is famous for its naïve (or primitive) art, characterized by bright colors, 
                flat perspectives, and scenes of daily life. The Centre d'Art in Port-au-Prince 
                is a hub for this style.
            </p>
            <p style="font-size:0.8rem; color:#888;">Placeholder image below</p>
            <div style="background:#0d1f3c; padding:30px; text-align:center; color:#888; border-radius:10px;">
                🎨 Image Here
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card">
            <h4>🗿 Sculpture</h4>
            <p>
                Haitian sculptors create works from wood, stone, and metal. Many sculptures depict 
                Haitian heroes, Vodou spirits, and everyday life. The iron market in Port-au-Prince 
                is a great place to see this art form.
            </p>
            <p style="font-size:0.8rem; color:#888;">Placeholder image below</p>
            <div style="background:#0d1f3c; padding:30px; text-align:center; color:#888; border-radius:10px;">
                🗿 Image Here
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="culture-card">
            <h4>🎭 Vodou Flags</h4>
            <p>
                Ceremonial flags (drapo) made from sequins and beads are used in Vodou ceremonies. 
                These intricate, colorful flags depict spirits and are works of art in their own right.
            </p>
            <p style="font-size:0.8rem; color:#888;">Placeholder image below</p>
            <div style="background:#0d1f3c; padding:30px; text-align:center; color:#888; border-radius:10px;">
                🎭 Image Here
            </div>
        </div>
        """, unsafe_allow_html=True)

elif selected == "🍲 Cuisine":
    st.markdown('<h2 class="section-title">🍲 Haitian Cuisine</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h3>🇭🇹 A Delicious Fusion of Flavors</h3>
        <p>
            Haitian cuisine is a delicious blend of African, French, and Caribbean influences. 
            It's known for its bold flavors, fresh ingredients, and the love with which it is prepared.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h4>🍛 Griot</h4>
            <p>
                The national dish of Haiti! Griot is fried pork shoulder marinated in citrus and 
                spices, served with pikliz (spicy pickled vegetables) and plantains.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>🍲 Soup Joumou</h4>
            <p>
                A traditional pumpkin soup served on New Year's Day to celebrate Haiti's independence 
                from France. It's a symbol of freedom and unity for all Haitians.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card">
            <h4>🍗 Poulet Creole</h4>
            <p>
                Chicken cooked with tomatoes, peppers, onions, and a blend of Caribbean spices. 
                Served with rice and beans or plantains.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>🍹 Acassan</h4>
            <p>
                A refreshing drink made from cornmeal, milk, vanilla, and spices. It's a popular 
                breakfast beverage that has been enjoyed in Haiti for generations.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h4>🍽️ Local Dishes to Try (Placeholder Images)</h4>
        <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">
            <div style="background:#0d1f3c; padding:20px; border-radius:10px; text-align:center; color:#888; flex:1; min-width:100px;">
                🍛 Griot
            </div>
            <div style="background:#0d1f3c; padding:20px; border-radius:10px; text-align:center; color:#888; flex:1; min-width:100px;">
                🍲 Soup Joumou
            </div>
            <div style="background:#0d1f3c; padding:20px; border-radius:10px; text-align:center; color:#888; flex:1; min-width:100px;">
                🍗 Poulet Creole
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "🗣️ Language":
    st.markdown('<h2 class="section-title">🗣️ Haitian Language</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h3>🇭🇹 A Rich Linguistic Heritage</h3>
        <p>
            Haiti is one of the few nations in the world with two official languages: French and 
            Haitian Creole (Kreyòl). Each language tells a story of Haiti's past and present.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h4>🇫🇷 French</h4>
            <p>
                French is the language of government, education, and media in Haiti. It was inherited 
                from the French colonial period and remains a language of prestige and opportunity.
            </p>
            <p><strong style="color:#ffcc00;">Example:</strong> "Bonjour, comment allez-vous?"</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card">
            <h4>🇭🇹 Haitian Creole (Kreyòl)</h4>
            <p>
                Haitian Creole is the language of the people. It evolved from French with influences 
                from African languages, Spanish, and Taino. It became an official language in 1987.
            </p>
            <p><strong style="color:#ffcc00;">Example:</strong> "Bonjou, kijan ou ye?"</p>
            <p style="font-size:0.8rem; color:#888;">Hello, how are you?</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h4>🗣️ Common Phrases in Haitian Creole</h4>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; color:#dddddd;">
            <div><strong style="color:#ffcc00;">Mèsi</strong> - Thank you</div>
            <div><strong style="color:#ffcc00;">Wi</strong> - Yes</div>
            <div><strong style="color:#ffcc00;">Non</strong> - No</div>
            <div><strong style="color:#ffcc00;">Bonswa</strong> - Good evening</div>
            <div><strong style="color:#ffcc00;">Orevwa</strong> - Goodbye</div>
            <div><strong style="color:#ffcc00;">Souple</strong> - Please</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "🎉 Festivals":
    st.markdown('<h2 class="section-title">🎉 Haitian Festivals</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h3>🎊 Celebrations of Faith, Culture, and Community</h3>
        <p>
            Festivals in Haiti are vibrant, colorful, and full of life. They are a time for 
            communities to come together, celebrate their faith, and express their culture.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="culture-card">
            <h4>🎭 Carnival (Kanaval)</h4>
            <p>
                Haiti's Carnival is one of the most vibrant in the Caribbean. It takes place in 
                February or March and features elaborate costumes, music, dance, and parades.
            </p>
            <p><strong style="color:#ffcc00;">Key Cities:</strong> Port-au-Prince, Jacmel</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>💃 Rara Festival</h4>
            <p>
                A Lenten festival that blends African and Catholic traditions. Rara processions 
                feature bands playing bamboo trumpets and drums, with dancers and singers.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="culture-card">
            <h4>🎄 Christmas (Nwèl)</h4>
            <p>
                Christmas in Haiti is a time of joy and celebration. Families attend midnight mass, 
                gather for feasts, and celebrate with music and dancing. Traditional foods like 
                soup joumou are served.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="culture-card">
            <h4>🗽 Independence Day (January 1)</h4>
            <p>
                Haiti celebrates its independence from France on January 1st. It is a day of 
                national pride, featuring parades, speeches, and the traditional soup joumou.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="culture-card">
        <h4>🎬 Festival Videos (Placeholder)</h4>
        <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">
            <div style="background:#0d1f3c; padding:40px; border-radius:10px; text-align:center; color:#888; flex:1; min-width:200px;">
                🎥 Carnival 2024
            </div>
            <div style="background:#0d1f3c; padding:40px; border-radius:10px; text-align:center; color:#888; flex:1; min-width:200px;">
                🎥 Rara Performance
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    <p>
        🇭🇹 <strong style="color:#ffcc00;">Haiti Culture Connection</strong> 🇭🇹
    </p>
    <p style="font-size:0.8rem; color:#666;">
        Celebrating the rich culture, history, and people of Haiti.
    </p>
    <p style="font-size:0.7rem; color:#555;">
        © 2026 Haiti Culture Connection | Built with <span class="heart">❤️</span> in Haiti
    </p>
    <p style="font-size:0.7rem; color:#555;">
        📞 (509)-47385663 | 📧 deslandes78@gmail.com
    </p>
    <p style="font-size:0.7rem; color:#555;">
        #HaitiCulture #Haiti #Culture #History #Music #Art #Cuisine #Language #Festivals #HaitianPride #GlobalInternetpy
    </p>
</div>
""", unsafe_allow_html=True)
