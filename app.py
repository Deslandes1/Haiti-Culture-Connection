import streamlit as st
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(
    page_title="Haiti Culture Connection",
    page_icon="🇭🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS (Light Blue Theme) ----------
st.markdown("""
    <style>
    /* Main background - light blue */
    .stApp {
        background: #e6f0ff !important;
    }
    
    /* Sidebar - light blue, slightly darker for contrast */
    .stSidebar,
    .stSidebar .sidebar-content,
    section[data-testid="stSidebar"] {
        background: #d4e4f7 !important;
    }
    
    .stSidebar .stMarkdown,
    .stSidebar .stCaption,
    .stSidebar .stButton button {
        color: #1a2b4c !important;
    }
    
    /* Main title - blue gradient */
    .main-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #0044aa, #0066cc, #3399ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        padding: 20px 0;
        text-shadow: 0 0 60px rgba(0, 68, 170, 0.2);
        animation: glow 3s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 68, 170, 0.15)); }
        50% { filter: drop-shadow(0 0 40px rgba(0, 68, 170, 0.3)); }
    }
    
    .sub-title {
        color: #004488;
        font-size: 1.2rem;
        text-align: center;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    
    /* Section headers */
    .section-title {
        color: #004488;
        font-size: 2rem;
        font-weight: 700;
        border-bottom: 3px solid #3399ff;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    
    .culture-card {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(0, 68, 170, 0.1);
        transition: 0.3s;
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    .culture-card:hover {
        background: rgba(255, 255, 255, 0.8);
        border-color: #3399ff;
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 68, 170, 0.15);
    }
    .culture-card h3 {
        color: #003366;
        margin-bottom: 10px;
    }
    .culture-card h4 {
        color: #004488;
        margin-bottom: 8px;
    }
    .culture-card p {
        color: #1a2b4c;
        line-height: 1.6;
    }
    
    /* Sidebar navigation */
    .nav-item {
        color: #1a2b4c !important;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
        transition: 0.3s;
        text-decoration: none;
        display: block;
        font-weight: 500;
    }
    .nav-item:hover {
        background: rgba(0, 68, 170, 0.1);
        color: #003366 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 30px 0;
        border-top: 1px solid rgba(0, 68, 170, 0.1);
        margin-top: 40px;
        color: #555;
        font-size: 0.9rem;
    }
    .footer .heart {
        color: #d21034;
    }
    
    .video-container {
        border-radius: 15px;
        overflow: hidden;
        margin: 15px 0;
        border: 1px solid rgba(0, 68, 170, 0.1);
    }
    
    .white-text {
        color: #ffffff !important;
    }
    .gold-text {
        color: #ffcc00 !important;
    }
    .red-text {
        color: #d21034 !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #0066cc, #3399ff) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }
    .stButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 30px rgba(0, 68, 170, 0.3) !important;
    }
    
    /* Adjust text colors for contrast */
    .stRadio label, .stRadio div {
        color: #1a2b4c !important;
    }
    .stMarkdown {
        color: #1a2b4c !important;
    }
    .stCaption {
        color: #1a2b4c !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
with st.sidebar:
    # Removed logo placeholder
    
    st.markdown("### 🌍 Explore Haiti")
    
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
    st.markdown("### 📤 Upload Logo")
    uploaded_logo = st.file_uploader("Upload your logo", type=["png", "jpg", "jpeg", "svg"])
    
    if uploaded_logo is not None:
        st.session_state['logo'] = uploaded_logo
        st.success("✅ Logo uploaded successfully!")
    
    st.markdown("---")
    st.caption("🇭🇹 Haiti Culture Connection")
    st.caption("v1.0 | Built with ❤️")

# ---------- Main Content ----------

# Display logo if uploaded
if 'logo' in st.session_state and st.session_state['logo'] is not None:
    try:
        logo = Image.open(st.session_state['logo'])
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo, use_column_width=True)
    except Exception as e:
        st.error(f"Error displaying logo: {e}")
        st.info("Please upload a valid image file (PNG, JPG, JPEG, or SVG).")

# Header
st.markdown('<div class="main-title">🇭🇹 Haiti Culture Connection</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">✨ Celebrating the Heart and Soul of Haiti ✨</div>', unsafe_allow_html=True)

# ---------- Page Content ----------
if selected == "🏠 Home":
    st.markdown('<h2 class="section-title">🏠 Welcome to Haiti Culture Connection</h2>', unsafe_allow_html=True)
    
    # Logo design prompt (expandable)
    with st.expander("🎨 View Logo Design Prompt (Click to expand)", expanded=False):
        st.markdown("""
        <div style="background:rgba(255,255,255,0.5); padding:20px; border-radius:10px; color:#1a2b4c; font-size:0.95rem; line-height:1.8;">
            <p><strong style="color:#004488;">Logo Description:</strong></p>
            <p>
            A high-resolution, cinematic close-up of the "Haiti Culture Connection" logo from image_0.png, 
            rendered as a polished metallic and enamel emblem. The central 3D-beveled 'HC' monogram 
            (blue 'H' and yellow/red 'C') and the enclosing red circle are finished in high-gloss materials, 
            catching intense, brilliant specular highlights. The green network nodes and their connecting 
            lines are transformed into delicate, glowing fiber-optic elements. The entire green network 
            node structure rotates slowly and smoothly around the central 'HC' monogram, with motion blur 
            on the nodes indicating movement. Subtle light trails and bokeh particles follow the path of 
            the rotating nodes. The text "HAITI CULTURE CONNECTION" below the emblem is sharply defined 
            and softly underlit. The background is a clean, soft-focus gradient of deep blue to purple, 
            with a subtle, pulsing digital grid pattern. The overall scene is bathed in a warm, brilliant, 
            and dynamic light, making the entire logo shine brightly. The view is slightly dynamic, with 
            depth of field.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
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
                <strong style="color:#004488;">Explore our sections to learn about:</strong><br>
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
                <strong style="color:#004488;">Capital:</strong> Port-au-Prince<br>
                <strong style="color:#004488;">Population:</strong> 11.4 million<br>
                <strong style="color:#004488;">Languages:</strong> French, Haitian Creole<br>
                <strong style="color:#004488;">Currency:</strong> Gourde (HTG)<br>
                <strong style="color:#004488;">Independence:</strong> January 1, 1804
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
                <strong style="color:#004488;">Key Historical Sites:</strong><br>
                • The Citadelle Laferrière – A UNESCO World Heritage Site<br>
                • Sans-Souci Palace – Symbol of Haitian royalty<br>
                • The Cathedral of Port-au-Prince – Rich architectural history
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/400x300/0066cc/ffffff?text=🇭🇹+Haitian+History", use_column_width=True)
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
            <p><strong style="color:#004488;">Famous Artists:</strong> Tabou Combo, Coupé Cloué, Jean Baptiste</p>
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
    st.markdown("""
    <div class="culture-card">
        <h4>🎬 Watch: Haitian Music Documentary (Placeholder)</h4>
        <div class="video-container">
            <div style="background:#d4e4f7; padding:60px; text-align:center; color:#555;">
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
            <div style="background:#d4e4f7; padding:30px; text-align:center; color:#555; border-radius:10px;">
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
            <div style="background:#d4e4f7; padding:30px; text-align:center; color:#555; border-radius:10px;">
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
            <div style="background:#d4e4f7; padding:30px; text-align:center; color:#555; border-radius:10px;">
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
            <div style="background:#d4e4f7; padding:20px; border-radius:10px; text-align:center; color:#555; flex:1; min-width:100px;">
                🍛 Griot
            </div>
            <div style="background:#d4e4f7; padding:20px; border-radius:10px; text-align:center; color:#555; flex:1; min-width:100px;">
                🍲 Soup Joumou
            </div>
            <div style="background:#d4e4f7; padding:20px; border-radius:10px; text-align:center; color:#555; flex:1; min-width:100px;">
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
            <p><strong style="color:#004488;">Example:</strong> "Bonjour, comment allez-vous?"</p>
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
            <p><strong style="color:#004488;">Example:</strong> "Bonjou, kijan ou ye?"</p>
            <p style="font-size:0.8rem; color:#555;">Hello, how are you?</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div class="culture-card">
        <h4>🗣️ Common Phrases in Haitian Creole</h4>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; color:#1a2b4c;">
            <div><strong style="color:#004488;">Mèsi</strong> - Thank you</div>
            <div><strong style="color:#004488;">Wi</strong> - Yes</div>
            <div><strong style="color:#004488;">Non</strong> - No</div>
            <div><strong style="color:#004488;">Bonswa</strong> - Good evening</div>
            <div><strong style="color:#004488;">Orevwa</strong> - Goodbye</div>
            <div><strong style="color:#004488;">Souple</strong> - Please</div>
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
            <p><strong style="color:#004488;">Key Cities:</strong> Port-au-Prince, Jacmel</p>
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
            <div style="background:#d4e4f7; padding:40px; border-radius:10px; text-align:center; color:#555; flex:1; min-width:200px;">
                🎥 Carnival 2024
            </div>
            <div style="background:#d4e4f7; padding:40px; border-radius:10px; text-align:center; color:#555; flex:1; min-width:200px;">
                🎥 Rara Performance
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    <p>
        🇭🇹 <strong style="color:#004488;">Haiti Culture Connection</strong> 🇭🇹
    </p>
    <p style="font-size:0.8rem; color:#555;">
        Celebrating the rich culture, history, and people of Haiti.
    </p>
    <p style="font-size:0.7rem; color:#666;">
        © 2026 Haiti Culture Connection | Built with <span class="heart">❤️</span> in Haiti
    </p>
    <p style="font-size:0.7rem; color:#666;">
        📞 (509)-47385663 | 📧 deslandes78@gmail.com
    </p>
    <p style="font-size:0.7rem; color:#666;">
        #HaitiCulture #Haiti #Culture #History #Music #Art #Cuisine #Language #Festivals #HaitianPride #GlobalInternetpy
    </p>
</div>
""", unsafe_allow_html=True)
