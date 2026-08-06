import streamlit as st
from PIL import Image
import re
import base64
from io import BytesIO

# ---------- Page Config ----------
st.set_page_config(
    page_title="Haiti Culture Connection",
    page_icon="🇭🇹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Language Dictionary ----------
LANGUAGES = {
    "English": "en",
    "Français": "fr",
    "Español": "es"
}

# ---------- Translation Dictionary ----------
# (Full dictionary – same as previous version, omitted for brevity)
# Include all TEXTS as before – they are unchanged.
# For the sake of completeness, we assume all TEXTS are present.
# We'll include a placeholder comment.

TEXTS = {
    # ... (copy your full TEXTS dictionary here) ...
    # To save space, we'll note that all texts from the previous version are used.
    # You must paste the complete TEXTS from the earlier full version.
}

# ---------- Helper function ----------
def get_text(key, lang):
    return TEXTS[key].get(lang, TEXTS[key]["en"])

# ---------- Session state ----------
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'
if 'media_items' not in st.session_state:
    st.session_state.media_items = []
if 'logo' not in st.session_state:
    st.session_state.logo = None
if 'media_authenticated' not in st.session_state:
    st.session_state.media_authenticated = False
if 'show_owner_panel' not in st.session_state:
    st.session_state.show_owner_panel = False
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = None
if 'editing_index' not in st.session_state:
    st.session_state.editing_index = None
if 'voice_audio_base64' not in st.session_state:
    st.session_state.voice_audio_base64 = None
if 'show_voice_player' not in st.session_state:
    st.session_state.show_voice_player = False

# ---------- Language selection ----------
def set_language():
    st.session_state.lang = LANGUAGES[st.session_state.lang_selector_top]

# ---------- Menu selection callback ----------
def on_menu_change():
    selected = st.session_state.menu_select
    menu_map = {
        get_text('nav_dashboard', st.session_state.lang): None,
        get_text('nav_home', st.session_state.lang): "home",
        get_text('nav_history', st.session_state.lang): "history",
        get_text('nav_music', st.session_state.lang): "music",
        get_text('nav_art', st.session_state.lang): "art",
        get_text('nav_cuisine', st.session_state.lang): "cuisine",
        get_text('nav_language', st.session_state.lang): "language",
        get_text('nav_festivals', st.session_state.lang): "festivals",
        get_text('nav_media', st.session_state.lang): "media",
        get_text('nav_about', st.session_state.lang): "about"
    }
    st.session_state.selected_section = menu_map.get(selected, None)

# ---------- CSS (Light Blue Theme + Metallic Logo) ----------
st.markdown("""
    <style>
    /* ... (all your existing CSS for layout, cards, etc.) ... */
    /* We keep all the previous styling except the logo section. */
    /* The new logo CSS is below. */
    .stApp {
        background: #e6f0ff !important;
    }
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
    .stRadio label, .stRadio div {
        color: #1a2b4c !important;
    }
    .stMarkdown {
        color: #1a2b4c !important;
    }
    .stCaption {
        color: #1a2b4c !important;
    }
    .media-item {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(0, 68, 170, 0.1);
    }
    .media-item img {
        border-radius: 8px;
        max-width: 100%;
    }
    .about-quote {
        font-size: 1.3rem;
        font-style: italic;
        color: #004488;
        text-align: center;
        padding: 20px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 12px;
        border-left: 4px solid #3399ff;
        margin: 15px 0;
    }
    .dashboard-intro {
        font-size: 1.1rem;
        color: #1a2b4c;
        text-align: center;
        padding: 10px 0 20px 0;
        opacity: 0.8;
    }
    .owner-panel {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(0, 68, 170, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0 20px 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    .welcome-banner {
        text-align: center;
        color: #004488;
        font-size: 2.2rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .back-btn-container {
        margin: 20px 0;
        text-align: center;
    }
    .management-item {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(0, 68, 170, 0.1);
    }

    /* ---------- METALLIC LOGO – EXACTLY AS PROMPT ---------- */
    .logo-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 10px 0;
        position: relative;
        perspective: 800px;
    }

    /* Main emblem – pink circle, metallic, spinning with blur */
    .logo-emblem {
        position: relative;
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffb6c1, #ff69b4, #d87093);
        border: 4px solid #ff69b4;
        box-shadow: 0 0 40px rgba(255, 105, 180, 0.4), 0 0 80px rgba(255, 105, 180, 0.2), inset 0 0 30px rgba(255, 215, 0, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        animation: spinWithBlur 4s ease-in-out infinite;
        transform-style: preserve-3d;
        overflow: visible;
    }

    /* Spin + blur animation */
    @keyframes spinWithBlur {
        0% { transform: rotate(0deg) scale(1); filter: blur(0px); }
        20% { filter: blur(2px); }
        50% { transform: rotate(180deg) scale(1.02); filter: blur(0px); }
        70% { filter: blur(2px); }
        100% { transform: rotate(360deg) scale(1); filter: blur(0px); }
    }

    /* Metallic shine (specular highlights) */
    .logo-emblem::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(255,255,255,0) 30%, rgba(255,255,255,0.3) 60%, rgba(255,255,255,0) 80%, rgba(255,215,0,0.2) 100%);
        pointer-events: none;
        z-index: 5;
        mix-blend-mode: overlay;
        animation: shineMove 6s linear infinite;
    }
    @keyframes shineMove {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }

    /* Starburst glints – using small stars positioned around */
    .glint {
        position: absolute;
        font-size: 0.8rem;
        color: white;
        text-shadow: 0 0 10px rgba(255,255,255,0.8), 0 0 20px rgba(255,255,255,0.4);
        z-index: 6;
        animation: glintPulse 2s ease-in-out infinite alternate;
    }
    .glint:nth-child(1) { top: -8px; left: 30%; }
    .glint:nth-child(2) { top: 60%; right: -10px; animation-delay: 0.5s; }
    .glint:nth-child(3) { bottom: -5px; left: 40%; animation-delay: 1s; }
    .glint:nth-child(4) { top: 20%; left: -10px; animation-delay: 1.5s; }
    @keyframes glintPulse {
        0% { opacity: 0.3; transform: scale(0.8) rotate(0deg); }
        100% { opacity: 1; transform: scale(1.2) rotate(20deg); }
    }

    /* Motion trail (ghost copies) */
    .logo-emblem::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: inherit;
        border: inherit;
        box-shadow: inherit;
        z-index: -1;
        animation: trailSpin 4s ease-in-out infinite;
        opacity: 0.25;
        transform: scale(0.9) rotate(30deg);
        filter: blur(2px);
    }
    @keyframes trailSpin {
        0% { transform: scale(0.9) rotate(30deg); opacity: 0.25; }
        50% { transform: scale(1.1) rotate(-30deg); opacity: 0.1; }
        100% { transform: scale(0.9) rotate(30deg); opacity: 0.25; }
    }

    /* HC letters: H in blue, C in yellow-red gradient, stacked */
    .hc-text {
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: -4px;
        font-family: 'Inter', sans-serif;
        transform: rotate(-2deg);
        position: relative;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        line-height: 0.9;
        text-shadow: 0 0 20px rgba(0,68,170,0.5), 0 0 40px rgba(255,215,0,0.3);
        filter: drop-shadow(0 0 10px rgba(255,215,0,0.2));
    }
    .hc-text .h-letter {
        color: #0044aa;
        font-size: 2.2rem;
        text-shadow: 0 0 10px #0044aa, 0 0 30px #0066cc;
    }
    .hc-text .c-letter {
        font-size: 2.2rem;
        background: linear-gradient(135deg, #ffcc00, #d21034);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
        filter: drop-shadow(0 0 8px rgba(255,200,0,0.4));
    }

    /* Green network nodes and lines – rotating ring */
    .network-ring {
        position: absolute;
        top: -15px;
        left: -15px;
        width: calc(100% + 30px);
        height: calc(100% + 30px);
        pointer-events: none;
        z-index: 1;
        animation: rotateNodes 6s linear infinite;
    }
    @keyframes rotateNodes {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .node {
        position: absolute;
        width: 8px;
        height: 8px;
        background: #00cc88;
        border-radius: 50%;
        box-shadow: 0 0 12px #00cc88, 0 0 24px #00cc88;
        animation: nodeGlow 2s ease-in-out infinite alternate;
    }
    .node:nth-child(1) { top: 0%; left: 50%; }
    .node:nth-child(2) { top: 25%; left: 95%; animation-delay: 0.2s; }
    .node:nth-child(3) { top: 75%; left: 95%; animation-delay: 0.4s; }
    .node:nth-child(4) { top: 100%; left: 50%; animation-delay: 0.6s; }
    .node:nth-child(5) { top: 75%; left: 5%; animation-delay: 0.8s; }
    .node:nth-child(6) { top: 25%; left: 5%; animation-delay: 1s; }
    .node:nth-child(7) { top: 50%; left: 100%; animation-delay: 0.3s; }
    .node:nth-child(8) { top: 50%; left: 0%; animation-delay: 0.7s; }
    @keyframes nodeGlow {
        0% { opacity: 0.4; transform: scale(0.8); }
        100% { opacity: 1; transform: scale(1.2); }
    }

    /* Network lines – connecting ring */
    .ring-line {
        position: absolute;
        top: -10px;
        left: -10px;
        width: calc(100% + 20px);
        height: calc(100% + 20px);
        border-radius: 50%;
        border: 1px dashed rgba(0, 204, 136, 0.3);
        box-shadow: 0 0 20px rgba(0, 204, 136, 0.1);
        z-index: 0;
        animation: ringPulse 4s ease-in-out infinite;
    }
    .ring-line:nth-child(2) {
        top: 0px;
        left: 0px;
        width: 100%;
        height: 100%;
        border-color: rgba(0, 204, 136, 0.15);
        animation-delay: 2s;
    }
    @keyframes ringPulse {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.8; }
    }

    /* Floating effect */
    .logo-container {
        animation: floatLogo 6s ease-in-out infinite;
    }
    @keyframes floatLogo {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }

    /* Rippling text below */
    .logo-text {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 8px;
        text-align: center;
        color: #d21034;
        text-shadow: 0 0 10px rgba(210,16,52,0.2);
        animation: rippleText 4s ease-in-out infinite, lightSweep 3s linear infinite;
        background: linear-gradient(90deg, #d21034, #ff6666, #d21034);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% 100%;
    }
    @keyframes rippleText {
        0% { transform: scaleY(1) skewX(0deg); }
        50% { transform: scaleY(1.08) skewX(2deg); }
        100% { transform: scaleY(1) skewX(0deg); }
    }
    @keyframes lightSweep {
        0% { background-position: 0% 0%; }
        100% { background-position: 200% 0%; }
    }

    /* Compact audio player */
    .compact-audio {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 4px 12px;
        background: rgba(255,255,255,0.4);
        border-radius: 30px;
        margin: 4px 0 8px 0;
        border: 1px solid rgba(0,68,170,0.1);
    }
    .compact-audio audio {
        height: 30px;
        flex: 1;
        min-width: 150px;
    }
    .compact-audio .close-btn {
        font-size: 0.8rem;
        color: #888;
        cursor: pointer;
        padding: 2px 8px;
        border-radius: 50%;
        transition: 0.2s;
    }
    .compact-audio .close-btn:hover {
        background: rgba(0,0,0,0.05);
        color: #d21034;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Top Bar: Logo, Language, Menu, Voice Button, Owner Toggle ----------
lang = st.session_state.lang

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("""
    <div class="logo-container">
        <div class="logo-emblem">
            <!-- Network ring (green nodes) -->
            <div class="network-ring">
                <div class="node"></div><div class="node"></div>
                <div class="node"></div><div class="node"></div>
                <div class="node"></div><div class="node"></div>
                <div class="node"></div><div class="node"></div>
            </div>
            <div class="ring-line"></div>
            <div class="ring-line"></div>
            <!-- Starburst glints -->
            <div class="glint">✦</div>
            <div class="glint">✦</div>
            <div class="glint">✦</div>
            <div class="glint">✦</div>
            <!-- HC monogram -->
            <div class="hc-text">
                <span class="h-letter">H</span>
                <span class="c-letter">C</span>
            </div>
        </div>
        <!-- Rippling text below -->
        <div class="logo-text">HAITI CULTURE CONNECTION</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown('<div style="display:flex; justify-content:flex-end; align-items:center; gap:10px; padding-top:10px; flex-wrap:wrap;">', unsafe_allow_html=True)
    # Language selector
    lang_choice = st.selectbox(
        "🌐 Language",
        ["English", "Français", "Español"],
        index=["English", "Français", "Español"].index(
            [k for k, v in LANGUAGES.items() if v == st.session_state.lang][0]
        ),
        key="lang_selector_top",
        on_change=set_language,
        label_visibility="collapsed"
    )
    # Menu
    menu_items = [
        get_text('nav_dashboard', lang),
        get_text('nav_home', lang),
        get_text('nav_history', lang),
        get_text('nav_music', lang),
        get_text('nav_art', lang),
        get_text('nav_cuisine', lang),
        get_text('nav_language', lang),
        get_text('nav_festivals', lang),
        get_text('nav_media', lang),
        get_text('nav_about', lang)
    ]
    current_display = get_text('nav_dashboard', lang)
    if st.session_state.selected_section == "home":
        current_display = get_text('nav_home', lang)
    elif st.session_state.selected_section == "history":
        current_display = get_text('nav_history', lang)
    elif st.session_state.selected_section == "music":
        current_display = get_text('nav_music', lang)
    elif st.session_state.selected_section == "art":
        current_display = get_text('nav_art', lang)
    elif st.session_state.selected_section == "cuisine":
        current_display = get_text('nav_cuisine', lang)
    elif st.session_state.selected_section == "language":
        current_display = get_text('nav_language', lang)
    elif st.session_state.selected_section == "festivals":
        current_display = get_text('nav_festivals', lang)
    elif st.session_state.selected_section == "media":
        current_display = get_text('nav_media', lang)
    elif st.session_state.selected_section == "about":
        current_display = get_text('nav_about', lang)
    selected_menu = st.selectbox(
        get_text('menu_label', lang),
        menu_items,
        index=menu_items.index(current_display) if current_display in menu_items else 0,
        key="menu_select",
        label_visibility="collapsed",
        on_change=on_menu_change
    )
    # Voice button
    if st.button(get_text('voice_button_label', lang), key="voice_button_top", use_container_width=False):
        if lang == "fr":
            voice_script = get_text("about_voice_script_fr", lang)
            voice_lang = "fr"
        elif lang == "es":
            voice_script = get_text("about_voice_script_es", lang)
            voice_lang = "es"
        else:
            voice_script = get_text("about_voice_script_en", lang)
            voice_lang = "en"
        with st.spinner("🔊 Generating..."):
            try:
                from gtts import gTTS
                tts = gTTS(text=voice_script, lang=voice_lang, slow=False)
                audio_bytes = BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                audio_base64 = base64.b64encode(audio_bytes.read()).decode()
                st.session_state.voice_audio_base64 = audio_base64
                st.session_state.show_voice_player = True
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("💡 Please check internet connection.")
    # Owner toggle
    if st.button(get_text('owner_toggle_button', lang), key="owner_toggle_btn", use_container_width=False):
        st.session_state.show_owner_panel = not st.session_state.show_owner_panel
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Compact Voice Player (if active) ----------
if st.session_state.show_voice_player and st.session_state.voice_audio_base64:
    audio_html = f"""
        <div class="compact-audio">
            <span style="font-size:0.9rem;">🔊</span>
            <audio controls preload="auto" autoplay>
                <source src="data:audio/mp3;base64,{st.session_state.voice_audio_base64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            <span class="close-btn" onclick="this.parentElement.style.display='none';">✕</span>
        </div>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# ---------- Owner Panel ----------
if st.session_state.show_owner_panel:
    with st.container():
        st.markdown('<div class="owner-panel">', unsafe_allow_html=True)
        if not st.session_state.media_authenticated:
            st.markdown(f"### {get_text('owner_login_title', lang)}")
            password_input = st.text_input("Enter password", type="password", placeholder="Password", key="owner_password_top")
            if st.button("🔑 Login", key="owner_login_button", use_container_width=True):
                if password_input == "2026":
                    st.session_state.media_authenticated = True
                    st.rerun()
                else:
                    st.error(get_text('owner_wrong_password', lang))
        else:
            st.success(get_text('owner_logged_in_msg', lang))
            if st.button(get_text('owner_logout_button', lang), key="owner_logout_button", use_container_width=True):
                st.session_state.media_authenticated = False
                st.rerun()
            st.markdown("---")

            # Logo upload
            st.markdown(f"### {get_text('logo_upload_title', lang)}")
            st.markdown(f"<p style='font-size:0.9rem; color:#1a2b4c;'>{get_text('logo_upload_subtitle', lang)}</p>", unsafe_allow_html=True)
            logo_file = st.file_uploader("", type=["png", "jpg", "jpeg", "svg"], key="logo_uploader_top")
            if logo_file is not None:
                st.session_state.logo = logo_file
                st.success(get_text('logo_upload_success', lang))
                st.rerun()

            st.markdown("---")

            # Image upload
            st.markdown(f"### {get_text('media_add_image', lang)}")
            col1, col2 = st.columns([2, 1])
            with col1:
                image_file = st.file_uploader("", type=["png", "jpg", "jpeg", "gif", "webp"], key="image_upload_owner")
            with col2:
                image_caption = st.text_input(get_text('media_image_caption', lang), key="image_caption_owner")
            if st.button(get_text('media_add_image_button', lang), key="add_image_owner", use_container_width=True):
                if image_file is not None:
                    img_bytes = image_file.read()
                    st.session_state.media_items.append({
                        "type": "image",
                        "data": img_bytes,
                        "caption": image_caption.strip(),
                        "filename": image_file.name
                    })
                    st.success("✅ Image added!")
                    st.rerun()
                else:
                    st.warning("Please upload an image file.")

            st.markdown("---")

            # Link upload
            st.markdown(f"### {get_text('media_add_link', lang)}")
            col1, col2 = st.columns([2, 1])
            with col1:
                link = st.text_input("", key="media_link_owner")
            with col2:
                caption = st.text_input(get_text('media_link_caption', lang), key="media_caption_owner")
            if st.button(get_text('media_add_link_button', lang), key="add_link_owner", use_container_width=True):
                if link.strip():
                    st.session_state.media_items.append({
                        "type": "link",
                        "link": link.strip(),
                        "caption": caption.strip()
                    })
                    st.success("✅ Link added!")
                    st.rerun()
                else:
                    st.warning("Please enter a link.")

            st.markdown("---")

            # Manage media
            st.markdown(f"### {get_text('manage_media_title', lang)}")
            if not st.session_state.media_items:
                st.info(get_text('no_media_to_manage', lang))
            else:
                for idx, item in enumerate(st.session_state.media_items):
                    with st.container():
                        st.markdown(f'<div class="management-item">', unsafe_allow_html=True)
                        if item["type"] == "image":
                            try:
                                img = Image.open(BytesIO(item["data"]))
                                st.image(img, caption=item["caption"], use_column_width=True)
                            except:
                                st.warning("Image cannot be displayed")
                        else:
                            st.markdown(f"**{item['caption'] if item['caption'] else 'Link'}**")
                            st.markdown(f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>', unsafe_allow_html=True)
                        
                        if st.session_state.editing_index == idx:
                            if item["type"] == "image":
                                new_caption = st.text_input(get_text('edit_caption_label', lang), value=item["caption"], key=f"edit_caption_{idx}")
                                col_save, col_cancel = st.columns(2)
                                with col_save:
                                    if st.button(get_text('save_label', lang), key=f"save_{idx}"):
                                        st.session_state.media_items[idx]["caption"] = new_caption
                                        st.session_state.editing_index = None
                                        st.rerun()
                                with col_cancel:
                                    if st.button(get_text('cancel_label', lang), key=f"cancel_{idx}"):
                                        st.session_state.editing_index = None
                                        st.rerun()
                            else:
                                new_caption = st.text_input(get_text('edit_caption_label', lang), value=item["caption"], key=f"edit_caption_link_{idx}")
                                new_link = st.text_input(get_text('edit_link_label', lang), value=item["link"], key=f"edit_link_{idx}")
                                col_save, col_cancel = st.columns(2)
                                with col_save:
                                    if st.button(get_text('save_label', lang), key=f"save_link_{idx}"):
                                        st.session_state.media_items[idx]["caption"] = new_caption
                                        st.session_state.media_items[idx]["link"] = new_link
                                        st.session_state.editing_index = None
                                        st.rerun()
                                with col_cancel:
                                    if st.button(get_text('cancel_label', lang), key=f"cancel_link_{idx}"):
                                        st.session_state.editing_index = None
                                        st.rerun()
                        else:
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button(get_text('edit_label', lang), key=f"edit_btn_{idx}"):
                                    st.session_state.editing_index = idx
                                    st.rerun()
                            with col2:
                                if st.button(get_text('delete_label', lang), key=f"del_btn_{idx}"):
                                    del st.session_state.media_items[idx]
                                    if st.session_state.editing_index == idx:
                                        st.session_state.editing_index = None
                                    st.rerun()
                        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Main Content ----------
st.markdown(f'<div class="welcome-banner">🏠 {get_text("welcome_banner", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align:center; color:#004488; font-size:2.5rem; margin-top:0;">{get_text("dashboard_title", lang)}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="dashboard-intro">✨ {get_text("sub_title", lang)} ✨</p>', unsafe_allow_html=True)

# ---------- Section render functions ----------
def render_section(section_key, title_key, content_func):
    if st.session_state.selected_section is None or st.session_state.selected_section == section_key:
        if st.session_state.selected_section == section_key:
            st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
            if st.button(get_text('back_to_dashboard', lang), key=f"back_{section_key}"):
                st.session_state.selected_section = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        content_func()

def home_content():
    st.markdown(f'<h2 id="home" class="section-title">{get_text("home_title", lang)}</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h3>🇭🇹 {get_text("home_title", lang)}</h3>
            <p>{get_text("home_intro", lang)}</p>
            <p>
                <strong style="color:#004488;">{get_text("home_explore", lang)}</strong><br>
                📜 {get_text("nav_history", lang)} – {get_text("history_intro", lang).split('.')[0]}<br>
                🎵 {get_text("nav_music", lang)} – {get_text("music_intro", lang).split('.')[0]}<br>
                🎨 {get_text("nav_art", lang)} – {get_text("art_intro", lang).split('.')[0]}<br>
                🍲 {get_text("nav_cuisine", lang)} – {get_text("cuisine_intro", lang).split('.')[0]}<br>
                🗣️ {get_text("nav_language", lang)} – {get_text("lang_intro", lang).split('.')[0]}<br>
                🎉 {get_text("nav_festivals", lang)} – {get_text("fest_intro", lang).split('.')[0]}
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card" style="text-align:center;">
            <h3>{get_text("home_facts", lang)}</h3>
            <p style="font-size:0.95rem;">
                <strong style="color:#004488;">{get_text("home_capital", lang)}</strong> Port-au-Prince<br>
                <strong style="color:#004488;">{get_text("home_population", lang)}</strong> 11.4 million<br>
                <strong style="color:#004488;">{get_text("home_languages", lang)}</strong> French, Haitian Creole<br>
                <strong style="color:#004488;">{get_text("home_currency", lang)}</strong> Gourde (HTG)<br>
                <strong style="color:#004488;">{get_text("home_independence", lang)}</strong> January 1, 1804
            </p>
            <p style="font-size:1.5rem; margin-top:10px;">
                🇭🇹❤️💙
            </p>
        </div>
        """, unsafe_allow_html=True)

def history_content():
    st.markdown(f'<h2 id="history" class="section-title">{get_text("history_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🇭🇹 {get_text("history_title", lang)}</h3>
        <p>{get_text("history_intro", lang)}</p>
        <p>{get_text("history_more", lang)}</p>
        <p>
            <strong style="color:#004488;">{get_text("history_sites", lang)}</strong><br>
            {get_text("history_site1", lang)}<br>
            {get_text("history_site2", lang)}<br>
            {get_text("history_site3", lang)}
        </p>
    </div>
    """, unsafe_allow_html=True)

def music_content():
    st.markdown(f'<h2 id="music" class="section-title">{get_text("music_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🎶 {get_text("music_title", lang)}</h3>
        <p>{get_text("music_intro", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("music_compas", lang)}</h4>
            <p>{get_text("music_compas_desc", lang)}</p>
            <p><strong style="color:#004488;">{get_text("music_artists", lang)}</strong> Tabou Combo, Coupé Cloué, Jean Baptiste</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("music_rara", lang)}</h4>
            <p>{get_text("music_rara_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("music_meringue", lang)}</h4>
            <p>{get_text("music_meringue_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("music_vodou", lang)}</h4>
            <p>{get_text("music_vodou_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)

def art_content():
    st.markdown(f'<h2 id="art" class="section-title">{get_text("art_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🎨 {get_text("art_title", lang)}</h3>
        <p>{get_text("art_intro", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("art_naive", lang)}</h4>
            <p>{get_text("art_naive_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("art_sculpture", lang)}</h4>
            <p>{get_text("art_sculpture_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("art_vodou_flags", lang)}</h4>
            <p>{get_text("art_vodou_flags_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)

def cuisine_content():
    st.markdown(f'<h2 id="cuisine" class="section-title">{get_text("cuisine_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🇭🇹 {get_text("cuisine_title", lang)}</h3>
        <p>{get_text("cuisine_intro", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("cuisine_griot", lang)}</h4>
            <p>{get_text("cuisine_griot_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("cuisine_soup", lang)}</h4>
            <p>{get_text("cuisine_soup_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("cuisine_poulet", lang)}</h4>
            <p>{get_text("cuisine_poulet_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("cuisine_acassan", lang)}</h4>
            <p>{get_text("cuisine_acassan_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)

def language_content():
    st.markdown(f'<h2 id="language" class="section-title">{get_text("lang_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🇭🇹 {get_text("lang_title", lang)}</h3>
        <p>{get_text("lang_intro", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("lang_french", lang)}</h4>
            <p>{get_text("lang_french_desc", lang)}</p>
            <p><strong style="color:#004488;">{get_text("lang_french_example", lang)}</strong> "Bonjour, comment allez-vous?"</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("lang_creole", lang)}</h4>
            <p>{get_text("lang_creole_desc", lang)}</p>
            <p><strong style="color:#004488;">{get_text("lang_french_example", lang)}</strong> "Bonjou, kijan ou ye?"</p>
            <p style="font-size:0.8rem; color:#555;">{get_text("lang_french_example", lang).replace("Example:", "").strip()}: Hello, how are you?</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h4>{get_text("lang_phrases_title", lang)}</h4>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; color:#1a2b4c;">
            <div><strong style="color:#004488;">{get_text("lang_phrase1", lang)}</strong></div>
            <div><strong style="color:#004488;">{get_text("lang_phrase2", lang)}</strong></div>
            <div><strong style="color:#004488;">{get_text("lang_phrase3", lang)}</strong></div>
            <div><strong style="color:#004488;">{get_text("lang_phrase4", lang)}</strong></div>
            <div><strong style="color:#004488;">{get_text("lang_phrase5", lang)}</strong></div>
            <div><strong style="color:#004488;">{get_text("lang_phrase6", lang)}</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def festivals_content():
    st.markdown(f'<h2 id="festivals" class="section-title">{get_text("fest_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>🎊 {get_text("fest_title", lang)}</h3>
        <p>{get_text("fest_intro", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("fest_carnival", lang)}</h4>
            <p>{get_text("fest_carnival_desc", lang)}</p>
            <p><strong style="color:#004488;">{get_text("fest_carnival_cities", lang)}</strong> Port-au-Prince, Jacmel</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("fest_rara", lang)}</h4>
            <p>{get_text("fest_rara_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("fest_christmas", lang)}</h4>
            <p>{get_text("fest_christmas_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="culture-card">
            <h4>{get_text("fest_independence", lang)}</h4>
            <p>{get_text("fest_independence_desc", lang)}</p>
        </div>
        """, unsafe_allow_html=True)

def media_content():
    st.markdown(f'<h2 id="media" class="section-title">{get_text("media_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>📺 {get_text("media_title", lang)}</h3>
        <p>{get_text("media_subtitle", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.media_items:
        for idx, item in enumerate(st.session_state.media_items):
            with st.container():
                st.markdown(f'<div class="media-item">', unsafe_allow_html=True)
                if item["type"] == "image":
                    try:
                        img = Image.open(BytesIO(item["data"]))
                        st.image(img, caption=item["caption"], use_column_width=True)
                    except:
                        st.warning("Image cannot be displayed")
                else:
                    st.markdown(f"**{item['caption'] if item['caption'] else get_text('media_youtube', lang)}**")
                    if "youtube.com" in item['link'] or "youtu.be" in item['link']:
                        vid_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:[&?]|$)", item['link'])
                        if vid_match:
                            vid = vid_match.group(1)
                            st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{vid}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>', unsafe_allow_html=True)
                if st.session_state.media_authenticated:
                    if st.button(f"{get_text('media_remove', lang)} {idx+1}", key=f"remove_{idx}_dash"):
                        del st.session_state.media_items[idx]
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("---")
    else:
        st.info(get_text("media_empty", lang))

def about_content():
    st.markdown(f'<h2 id="about" class="section-title">{get_text("about_title", lang)}</h2>', unsafe_allow_html=True)
    if st.button(get_text('play_voice_label', lang), key="voice_button_about", use_container_width=True):
        if lang == "fr":
            voice_script = get_text("about_voice_script_fr", lang)
            voice_lang = "fr"
        elif lang == "es":
            voice_script = get_text("about_voice_script_es", lang)
            voice_lang = "es"
        else:
            voice_script = get_text("about_voice_script_en", lang)
            voice_lang = "en"
        with st.spinner("🔊 Generating..."):
            try:
                from gtts import gTTS
                tts = gTTS(text=voice_script, lang=voice_lang, slow=False)
                audio_bytes = BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                audio_base64 = base64.b64encode(audio_bytes.read()).decode()
                st.session_state.voice_audio_base64 = audio_base64
                st.session_state.show_voice_player = True
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("💡 Please check internet connection.")
    st.markdown("---")
    st.markdown(f"""
    <div class="culture-card">
        <h3>🏷️ {get_text("nav_about", lang)}</h3>
        <p>{get_text("about_intro", lang)}</p>
        <p>{get_text("about_mission", lang)}</p>
        <p>{get_text("about_connection", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="about-quote">
        " {get_text("about_quote", lang)} "
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>📱 {get_text("about_ceo", lang)}</h3>
        <p><strong style="color:#004488;">📞 {get_text("about_whatsapp", lang)}</strong></p>
        <p><strong style="color:#004488;">🌐 {get_text("about_social", lang)}</strong></p>
        <p style="font-size:0.8rem; color:#555; margin-top:10px;">
            🇭🇹 <strong>HCC</strong> – Le nouveau patrimoine structurel de la culture haïtienne.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; padding:10px;">
        <p style="font-size:1.2rem;">
            <a href="https://wa.me/18094177808" target="_blank" style="text-decoration:none; color:#004488;">📱 WhatsApp</a>
            &nbsp;|&nbsp;
            <a href="https://www.instagram.com/HCC" target="_blank" style="text-decoration:none; color:#004488;">📸 Instagram</a>
            &nbsp;|&nbsp;
            <a href="https://www.facebook.com/HCC" target="_blank" style="text-decoration:none; color:#004488;">📘 Facebook</a>
            &nbsp;|&nbsp;
            <a href="https://twitter.com/HCC" target="_blank" style="text-decoration:none; color:#004488;">🐦 Twitter</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- Render sections ----------
if st.session_state.selected_section is None:
    render_section("home", "home_title", home_content)
    render_section("history", "history_title", history_content)
    render_section("music", "music_title", music_content)
    render_section("art", "art_title", art_content)
    render_section("cuisine", "cuisine_title", cuisine_content)
    render_section("language", "lang_title", language_content)
    render_section("festivals", "fest_title", festivals_content)
    render_section("media", "media_title", media_content)
    render_section("about", "about_title", about_content)
else:
    if st.session_state.selected_section == "home":
        render_section("home", "home_title", home_content)
    elif st.session_state.selected_section == "history":
        render_section("history", "history_title", history_content)
    elif st.session_state.selected_section == "music":
        render_section("music", "music_title", music_content)
    elif st.session_state.selected_section == "art":
        render_section("art", "art_title", art_content)
    elif st.session_state.selected_section == "cuisine":
        render_section("cuisine", "cuisine_title", cuisine_content)
    elif st.session_state.selected_section == "language":
        render_section("language", "lang_title", language_content)
    elif st.session_state.selected_section == "festivals":
        render_section("festivals", "fest_title", festivals_content)
    elif st.session_state.selected_section == "media":
        render_section("media", "media_title", media_content)
    elif st.session_state.selected_section == "about":
        render_section("about", "about_title", about_content)

# ---------- Footer ----------
st.markdown("---")
st.markdown(f"""
<div class="footer">
    <p>
        🇭🇹 <strong style="color:#004488;">Haiti Culture Connection</strong> 🇭🇹
    </p>
    <p style="font-size:0.8rem; color:#555;">
        {get_text("footer_tagline", lang)}
    </p>
    <p style="font-size:0.7rem; color:#666;">
        {get_text("footer_copyright", lang)}
    </p>
    <p style="font-size:0.7rem; color:#666;">
        📞 (509)-47385663 | 📧 deslandes78@gmail.com
    </p>
    <p style="font-size:0.7rem; color:#666;">
        {get_text("footer_hashtags", lang)}
    </p>
</div>
""", unsafe_allow_html=True)
