import streamlit as st
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(
    page_title="Haiti Culture Connection",
    page_icon="🇭🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Language Dictionary ----------
LANGUAGES = {
    "English": "en",
    "Français": "fr",
    "Español": "es"
}

# Translation dictionary for all UI text
TEXTS = {
    # Sidebar
    "nav_title": {
        "en": "🌍 Explore Haiti",
        "fr": "🌍 Explorez Haïti",
        "es": "🌍 Explora Haití"
    },
    "nav_home": {"en": "🏠 Home", "fr": "🏠 Accueil", "es": "🏠 Inicio"},
    "nav_history": {"en": "📜 History", "fr": "📜 Histoire", "es": "📜 Historia"},
    "nav_music": {"en": "🎵 Music", "fr": "🎵 Musique", "es": "🎵 Música"},
    "nav_art": {"en": "🎨 Art", "fr": "🎨 Art", "es": "🎨 Arte"},
    "nav_cuisine": {"en": "🍲 Cuisine", "fr": "🍲 Cuisine", "es": "🍲 Cocina"},
    "nav_language": {"en": "🗣️ Language", "fr": "🗣️ Langue", "es": "🗣️ Idioma"},
    "nav_festivals": {"en": "🎉 Festivals", "fr": "🎉 Festivals", "es": "🎉 Festivales"},
    "nav_media": {"en": "📺 Media", "fr": "📺 Médias", "es": "📺 Medios"},
    "upload_logo": {"en": "📤 Upload Logo", "fr": "📤 Télécharger le logo", "es": "📤 Subir logo"},
    "upload_success": {"en": "✅ Logo uploaded successfully!", "fr": "✅ Logo téléchargé avec succès !", "es": "✅ ¡Logo subido con éxito!"},
    "footer_copyright": {
        "en": "© 2026 Haiti Culture Connection | Built with ❤️ in Haiti",
        "fr": "© 2026 Haiti Culture Connection | Construit avec ❤️ en Haïti",
        "es": "© 2026 Haiti Culture Connection | Hecho con ❤️ en Haití"
    },
    "footer_tagline": {
        "en": "Celebrating the rich culture, history, and people of Haiti.",
        "fr": "Célébrer la riche culture, l'histoire et le peuple d'Haïti.",
        "es": "Celebrando la rica cultura, historia y pueblo de Haití."
    },
    "footer_hashtags": "#HaitiCulture #Haiti #Culture #History #Music #Art #Cuisine #Language #Festivals #HaitianPride #GlobalInternetpy",
    # Main titles
    "main_title": {
        "en": "🇭🇹 Haiti Culture Connection",
        "fr": "🇭🇹 Connexion Culturelle Haïtienne",
        "es": "🇭🇹 Conexión Cultural Haitiana"
    },
    "sub_title": {
        "en": "✨ Celebrating the Heart and Soul of Haiti ✨",
        "fr": "✨ Célébrer le cœur et l'âme d'Haïti ✨",
        "es": "✨ Celebrando el corazón y el alma de Haití ✨"
    },
    # Home page
    "home_title": {
        "en": "🏠 Welcome to Haiti Culture Connection",
        "fr": "🏠 Bienvenue à Haiti Culture Connection",
        "es": "🏠 Bienvenido a Haiti Culture Connection"
    },
    "home_intro": {
        "en": "Haiti is a nation with a vibrant and resilient culture, shaped by a unique blend of African, French, and Caribbean influences. From the rhythmic beats of Compas and Rara to the vibrant colors of Haitian art, every aspect of Haitian culture tells a story of strength, creativity, and community.",
        "fr": "Haïti est une nation avec une culture vibrante et résiliente, façonnée par un mélange unique d'influences africaines, françaises et caribéennes. Des rythmes entraînants du Compas et du Rara aux couleurs vives de l'art haïtien, chaque aspect de la culture haïtienne raconte une histoire de force, de créativité et de communauté.",
        "es": "Haití es una nación con una cultura vibrante y resiliente, moldeada por una mezcla única de influencias africanas, francesas y caribeñas. Desde los ritmos contagiosos del Compas y el Rara hasta los colores vibrantes del arte haitiano, cada aspecto de la cultura haitiana cuenta una historia de fuerza, creatividad y comunidad."
    },
    "home_explore": {
        "en": "Explore our sections to learn about:",
        "fr": "Explorez nos sections pour en savoir plus :",
        "es": "Explora nuestras secciones para aprender sobre:"
    },
    "home_facts": {
        "en": "🇭🇹 Quick Facts",
        "fr": "🇭🇹 Faits rapides",
        "es": "🇭🇹 Datos rápidos"
    },
    "home_capital": {"en": "Capital:", "fr": "Capitale:", "es": "Capital:"},
    "home_population": {"en": "Population:", "fr": "Population:", "es": "Población:"},
    "home_languages": {"en": "Languages:", "fr": "Langues:", "es": "Idiomas:"},
    "home_currency": {"en": "Currency:", "fr": "Monnaie:", "es": "Moneda:"},
    "home_independence": {"en": "Independence:", "fr": "Indépendance:", "es": "Independencia:"},
    # History
    "history_title": {"en": "📜 Haitian History", "fr": "📜 Histoire Haïtienne", "es": "📜 Historia Haitiana"},
    "history_intro": {
        "en": "Haiti's history is one of resilience and triumph. On January 1, 1804, Haiti became the first independent Black republic in the world, following a successful slave revolt led by Toussaint Louverture and Jean-Jacques Dessalines.",
        "fr": "L'histoire d'Haïti est celle de la résilience et du triomphe. Le 1er janvier 1804, Haïti est devenue la première république noire indépendante au monde, suite à une révolte d'esclaves réussie menée par Toussaint Louverture et Jean-Jacques Dessalines.",
        "es": "La historia de Haití es de resiliencia y triunfo. El 1 de enero de 1804, Haití se convirtió en la primera república negra independiente del mundo, tras una exitosa revuelta de esclavos liderada por Toussaint Louverture y Jean-Jacques Dessalines."
    },
    "history_more": {
        "en": "The Haitian Revolution (1791-1804) was the only successful slave uprising in history, leading to the abolition of slavery and the establishment of a free nation. Today, Haiti stands as a symbol of freedom, resistance, and hope for oppressed people worldwide.",
        "fr": "La Révolution haïtienne (1791-1804) a été la seule révolte d'esclaves réussie de l'histoire, menant à l'abolition de l'esclavage et à l'établissement d'une nation libre. Aujourd'hui, Haïti est un symbole de liberté, de résistance et d'espoir pour les peuples opprimés du monde entier.",
        "es": "La Revolución Haitiana (1791-1804) fue la única rebelión de esclavos exitosa de la historia, que llevó a la abolición de la esclavitud y al establecimiento de una nación libre. Hoy, Haití es un símbolo de libertad, resistencia y esperanza para los pueblos oprimidos de todo el mundo."
    },
    "history_sites": {
        "en": "Key Historical Sites:",
        "fr": "Sites historiques clés :",
        "es": "Sitios históricos clave:"
    },
    "history_site1": "• The Citadelle Laferrière – A UNESCO World Heritage Site",
    "history_site2": "• Sans-Souci Palace – Symbol of Haitian royalty",
    "history_site3": "• The Cathedral of Port-au-Prince – Rich architectural history",
    # Music
    "music_title": {"en": "🎵 Haitian Music", "fr": "🎵 Musique Haïtienne", "es": "🎵 Música Haitiana"},
    "music_intro": {
        "en": "Haitian music is a vibrant fusion of African rhythms, French melodies, and Caribbean influences. It is the heartbeat of Haitian culture, expressing joy, sorrow, and the resilience of the Haitian people.",
        "fr": "La musique haïtienne est une fusion vibrante de rythmes africains, de mélodies françaises et d'influences caribéennes. C'est le cœur battant de la culture haïtienne, exprimant la joie, la tristesse et la résilience du peuple haïtien.",
        "es": "La música haitiana es una fusión vibrante de ritmos africanos, melodías francesas e influencias caribeñas. Es el latido de la cultura haitiana, expresando alegría, tristeza y la resiliencia del pueblo haitiano."
    },
    "music_compas": {"en": "🎵 Compas (Konpa)", "fr": "🎵 Compas (Konpa)", "es": "🎵 Compas (Konpa)"},
    "music_compas_desc": {
        "en": "The most popular modern genre in Haiti. Created by Nemours Jean-Baptiste in the 1950s, Compas is a smooth, danceable rhythm that blends jazz, Latin, and Caribbean sounds.",
        "fr": "Le genre moderne le plus populaire en Haïti. Créé par Nemours Jean-Baptiste dans les années 1950, le Compas est un rythme doux et dansant qui mêle jazz, sons latins et caribéens.",
        "es": "El género moderno más popular en Haití. Creado por Nemours Jean-Baptiste en la década de 1950, el Compas es un ritmo suave y bailable que mezcla jazz, sonidos latinos y caribeños."
    },
    "music_artists": {"en": "Famous Artists:", "fr": "Artistes célèbres :", "es": "Artistas famosos:"},
    "music_rara": {"en": "🥁 Rara", "fr": "🥁 Rara", "es": "🥁 Rara"},
    "music_rara_desc": {
        "en": "A traditional Afro-Haitian genre performed during Carnival and Lent. Rara features bamboo trumpets (vaksen), drums, and call-and-response vocals.",
        "fr": "Un genre afro-haïtien traditionnel joué pendant le Carnaval et le Carême. Le Rara présente des trompettes en bambou (vaksen), des tambours et des chants en appel-réponse.",
        "es": "Un género afro-haitiano tradicional interpretado durante el Carnaval y la Cuaresma. El Rara presenta trompetas de bambú (vaksen), tambores y voces de llamada y respuesta."
    },
    "music_meringue": {"en": "🎸 Meringue", "fr": "🎸 Meringue", "es": "🎸 Meringue"},
    "music_meringue_desc": {
        "en": "A traditional Haitian dance music that predates Compas. It features a slower, more romantic rhythm and is often performed at formal events and ceremonies.",
        "fr": "Une musique de danse traditionnelle haïtienne qui précède le Compas. Elle présente un rythme plus lent, plus romantique et est souvent jouée lors d'événements formels et de cérémonies.",
        "es": "Una música de baile tradicional haitiana que precede al Compas. Presenta un ritmo más lento y romántico y a menudo se interpreta en eventos formales y ceremonias."
    },
    "music_vodou": {"en": "🎶 Vodou Rhythms", "fr": "🎶 Rythmes Vodou", "es": "🎶 Ritmos Vodú"},
    "music_vodou_desc": {
        "en": "Traditional ceremonial music played during Vodou ceremonies, featuring drums, bells, and chanting. These rhythms are deeply spiritual and connect practitioners to their ancestors.",
        "fr": "Musique cérémonielle traditionnelle jouée lors des cérémonies Vodou, avec tambours, cloches et chants. Ces rythmes sont profondément spirituels et relient les pratiquants à leurs ancêtres.",
        "es": "Música ceremonial tradicional tocada durante las ceremonias del Vodú, con tambores, campanas y cánticos. Estos ritmos son profundamente espirituales y conectan a los practicantes con sus antepasados."
    },
    # Art
    "art_title": {"en": "🎨 Haitian Art", "fr": "🎨 Art Haïtien", "es": "🎨 Arte Haitiano"},
    "art_intro": {
        "en": "Haitian art is known for its vibrant colors, bold patterns, and powerful storytelling. From the bustling streets of Port-au-Prince to the rural villages, art is everywhere in Haiti.",
        "fr": "L'art haïtien est connu pour ses couleurs vives, ses motifs audacieux et sa narration puissante. Des rues animées de Port-au-Prince aux villages ruraux, l'art est partout en Haïti.",
        "es": "El arte haitiano es conocido por sus colores vibrantes, patrones audaces y narración poderosa. Desde las bulliciosas calles de Puerto Príncipe hasta los pueblos rurales, el arte está en todas partes en Haití."
    },
    "art_naive": {"en": "🖼️ Naïve Art", "fr": "🖼️ Art Naïf", "es": "🖼️ Arte Naïf"},
    "art_naive_desc": {
        "en": "Haiti is famous for its naïve (or primitive) art, characterized by bright colors, flat perspectives, and scenes of daily life. The Centre d'Art in Port-au-Prince is a hub for this style.",
        "fr": "Haïti est célèbre pour son art naïf (ou primitif), caractérisé par des couleurs vives, des perspectives plates et des scènes de la vie quotidienne. Le Centre d'Art de Port-au-Prince est un lieu incontournable pour ce style.",
        "es": "Haití es famoso por su arte naïf (o primitivo), caracterizado por colores brillantes, perspectivas planas y escenas de la vida cotidiana. El Centre d'Art en Puerto Príncipe es un centro para este estilo."
    },
    "art_sculpture": {"en": "🗿 Sculpture", "fr": "🗿 Sculpture", "es": "🗿 Escultura"},
    "art_sculpture_desc": {
        "en": "Haitian sculptors create works from wood, stone, and metal. Many sculptures depict Haitian heroes, Vodou spirits, and everyday life. The iron market in Port-au-Prince is a great place to see this art form.",
        "fr": "Les sculpteurs haïtiens créent des œuvres à partir de bois, de pierre et de métal. De nombreuses sculptures représentent des héros haïtiens, des esprits Vodou et la vie quotidienne. Le marché de fer de Port-au-Prince est un excellent endroit pour découvrir cette forme d'art.",
        "es": "Los escultores haitianos crean obras a partir de madera, piedra y metal. Muchas esculturas representan héroes haitianos, espíritus del Vodú y la vida cotidiana. El mercado de hierro de Puerto Príncipe es un gran lugar para ver esta forma de arte."
    },
    "art_vodou_flags": {"en": "🎭 Vodou Flags", "fr": "🎭 Drapeaux Vodou", "es": "🎭 Banderas Vodú"},
    "art_vodou_flags_desc": {
        "en": "Ceremonial flags (drapo) made from sequins and beads are used in Vodou ceremonies. These intricate, colorful flags depict spirits and are works of art in their own right.",
        "fr": "Des drapeaux cérémoniels (drapo) en paillettes et perles sont utilisés lors des cérémonies Vodou. Ces drapeaux complexes et colorés représentent des esprits et sont des œuvres d'art à part entière.",
        "es": "Banderas ceremoniales (drapo) hechas de lentejuelas y cuentas se utilizan en las ceremonias del Vodú. Estas banderas intrincadas y coloridas representan espíritus y son obras de arte en sí mismas."
    },
    # Cuisine
    "cuisine_title": {"en": "🍲 Haitian Cuisine", "fr": "🍲 Cuisine Haïtienne", "es": "🍲 Cocina Haitiana"},
    "cuisine_intro": {
        "en": "Haitian cuisine is a delicious blend of African, French, and Caribbean influences. It's known for its bold flavors, fresh ingredients, and the love with which it is prepared.",
        "fr": "La cuisine haïtienne est un délicieux mélange d'influences africaines, françaises et caribéennes. Elle est connue pour ses saveurs audacieuses, ses ingrédients frais et l'amour avec lequel elle est préparée.",
        "es": "La cocina haitiana es una deliciosa mezcla de influencias africanas, francesas y caribeñas. Es conocida por sus sabores audaces, ingredientes frescos y el amor con el que se prepara."
    },
    "cuisine_griot": {"en": "🍛 Griot", "fr": "🍛 Griot", "es": "🍛 Griot"},
    "cuisine_griot_desc": {
        "en": "The national dish of Haiti! Griot is fried pork shoulder marinated in citrus and spices, served with pikliz (spicy pickled vegetables) and plantains.",
        "fr": "Le plat national d'Haïti ! Le Griot est une épaule de porc frite marinée dans des agrumes et des épices, servie avec du pikliz (légumes marinés épicés) et des plantains.",
        "es": "¡El plato nacional de Haití! El Griot es hombro de cerdo frito marinado en cítricos y especias, servido con pikliz (verduras en escabeche picantes) y plátanos."
    },
    "cuisine_soup": {"en": "🍲 Soup Joumou", "fr": "🍲 Soup Joumou", "es": "🍲 Sopa Joumou"},
    "cuisine_soup_desc": {
        "en": "A traditional pumpkin soup served on New Year's Day to celebrate Haiti's independence from France. It's a symbol of freedom and unity for all Haitians.",
        "fr": "Une soupe de citrouille traditionnelle servie le jour de l'An pour célébrer l'indépendance d'Haïti de la France. C'est un symbole de liberté et d'unité pour tous les Haïtiens.",
        "es": "Una sopa de calabaza tradicional que se sirve el día de Año Nuevo para celebrar la independencia de Haití de Francia. Es un símbolo de libertad y unidad para todos los haitianos."
    },
    "cuisine_poulet": {"en": "🍗 Poulet Creole", "fr": "🍗 Poulet Créole", "es": "🍗 Poulet Criollo"},
    "cuisine_poulet_desc": {
        "en": "Chicken cooked with tomatoes, peppers, onions, and a blend of Caribbean spices. Served with rice and beans or plantains.",
        "fr": "Poulet cuit avec des tomates, des poivrons, des oignons et un mélange d'épices caribéennes. Servi avec du riz et des haricots ou des plantains.",
        "es": "Pollo cocinado con tomates, pimientos, cebollas y una mezcla de especias caribeñas. Servido con arroz y frijoles o plátanos."
    },
    "cuisine_acassan": {"en": "🍹 Acassan", "fr": "🍹 Acassan", "es": "🍹 Acassan"},
    "cuisine_acassan_desc": {
        "en": "A refreshing drink made from cornmeal, milk, vanilla, and spices. It's a popular breakfast beverage that has been enjoyed in Haiti for generations.",
        "fr": "Une boisson rafraîchissante à base de farine de maïs, de lait, de vanille et d'épices. C'est une boisson de petit-déjeuner populaire qui est appréciée en Haïti depuis des générations.",
        "es": "Una bebida refrescante hecha de harina de maíz, leche, vainilla y especias. Es una bebida de desayuno popular que se ha disfrutado en Haití durante generaciones."
    },
    # Language
    "lang_title": {"en": "🗣️ Haitian Language", "fr": "🗣️ Langue Haïtienne", "es": "🗣️ Idioma Haitiano"},
    "lang_intro": {
        "en": "Haiti is one of the few nations in the world with two official languages: French and Haitian Creole (Kreyòl). Each language tells a story of Haiti's past and present.",
        "fr": "Haïti est l'une des rares nations au monde à avoir deux langues officielles : le français et le créole haïtien (Kreyòl). Chaque langue raconte une histoire du passé et du présent d'Haïti.",
        "es": "Haití es una de las pocas naciones del mundo con dos idiomas oficiales: el francés y el criollo haitiano (Kreyòl). Cada idioma cuenta una historia del pasado y presente de Haití."
    },
    "lang_french": {"en": "🇫🇷 French", "fr": "🇫🇷 Français", "es": "🇫🇷 Francés"},
    "lang_french_desc": {
        "en": "French is the language of government, education, and media in Haiti. It was inherited from the French colonial period and remains a language of prestige and opportunity.",
        "fr": "Le français est la langue du gouvernement, de l'éducation et des médias en Haïti. Il a été hérité de la période coloniale française et reste une langue de prestige et d'opportunité.",
        "es": "El francés es el idioma del gobierno, la educación y los medios de comunicación en Haití. Se heredó del período colonial francés y sigue siendo un idioma de prestigio y oportunidad."
    },
    "lang_french_example": {"en": "Example:", "fr": "Exemple :", "es": "Ejemplo:"},
    "lang_creole": {"en": "🇭🇹 Haitian Creole (Kreyòl)", "fr": "🇭🇹 Créole haïtien (Kreyòl)", "es": "🇭🇹 Criollo haitiano (Kreyòl)"},
    "lang_creole_desc": {
        "en": "Haitian Creole is the language of the people. It evolved from French with influences from African languages, Spanish, and Taino. It became an official language in 1987.",
        "fr": "Le créole haïtien est la langue du peuple. Il a évolué à partir du français avec des influences des langues africaines, de l'espagnol et du taïno. Il est devenu langue officielle en 1987.",
        "es": "El criollo haitiano es el idioma del pueblo. Evolucionó del francés con influencias de lenguas africanas, español y taíno. Se convirtió en idioma oficial en 1987."
    },
    "lang_phrases_title": {"en": "🗣️ Common Phrases in Haitian Creole", "fr": "🗣️ Phrases courantes en créole haïtien", "es": "🗣️ Frases comunes en criollo haitiano"},
    "lang_phrase1": {"en": "Mèsi - Thank you", "fr": "Mèsi - Merci", "es": "Mèsi - Gracias"},
    "lang_phrase2": {"en": "Wi - Yes", "fr": "Wi - Oui", "es": "Wi - Sí"},
    "lang_phrase3": {"en": "Non - No", "fr": "Non - Non", "es": "Non - No"},
    "lang_phrase4": {"en": "Bonswa - Good evening", "fr": "Bonswa - Bonsoir", "es": "Bonswa - Buenas noches"},
    "lang_phrase5": {"en": "Orevwa - Goodbye", "fr": "Orevwa - Au revoir", "es": "Orevwa - Adiós"},
    "lang_phrase6": {"en": "Souple - Please", "fr": "Souple - S'il vous plaît", "es": "Souple - Por favor"},
    # Festivals
    "fest_title": {"en": "🎉 Haitian Festivals", "fr": "🎉 Festivals Haïtiens", "es": "🎉 Festivales Haitianos"},
    "fest_intro": {
        "en": "Festivals in Haiti are vibrant, colorful, and full of life. They are a time for communities to come together, celebrate their faith, and express their culture.",
        "fr": "Les festivals en Haïti sont vibrants, colorés et pleins de vie. Ils sont un moment pour les communautés de se rassembler, de célébrer leur foi et d'exprimer leur culture.",
        "es": "Los festivales en Haití son vibrantes, coloridos y llenos de vida. Son un momento para que las comunidades se unan, celebren su fe y expresen su cultura."
    },
    "fest_carnival": {"en": "🎭 Carnival (Kanaval)", "fr": "🎭 Carnaval (Kanaval)", "es": "🎭 Carnaval (Kanaval)"},
    "fest_carnival_desc": {
        "en": "Haiti's Carnival is one of the most vibrant in the Caribbean. It takes place in February or March and features elaborate costumes, music, dance, and parades.",
        "fr": "Le Carnaval d'Haïti est l'un des plus vibrants des Caraïbes. Il a lieu en février ou mars et présente des costumes élaborés, de la musique, de la danse et des défilés.",
        "es": "El Carnaval de Haití es uno de los más vibrantes del Caribe. Se celebra en febrero o marzo y presenta disfraces elaborados, música, baile y desfiles."
    },
    "fest_carnival_cities": {"en": "Key Cities:", "fr": "Villes clés :", "es": "Ciudades clave:"},
    "fest_rara": {"en": "💃 Rara Festival", "fr": "💃 Festival Rara", "es": "💃 Festival Rara"},
    "fest_rara_desc": {
        "en": "A Lenten festival that blends African and Catholic traditions. Rara processions feature bands playing bamboo trumpets and drums, with dancers and singers.",
        "fr": "Un festival de Carême qui mêle traditions africaines et catholiques. Les processions de Rara sont accompagnées de fanfares jouant des trompettes en bambou et des tambours, avec des danseurs et des chanteurs.",
        "es": "Un festival de Cuaresma que combina tradiciones africanas y católicas. Las procesiones de Rara cuentan con bandas que tocan trompetas de bambú y tambores, con bailarines y cantantes."
    },
    "fest_christmas": {"en": "🎄 Christmas (Nwèl)", "fr": "🎄 Noël (Nwèl)", "es": "🎄 Navidad (Nwèl)"},
    "fest_christmas_desc": {
        "en": "Christmas in Haiti is a time of joy and celebration. Families attend midnight mass, gather for feasts, and celebrate with music and dancing. Traditional foods like soup joumou are served.",
        "fr": "Noël en Haïti est un moment de joie et de célébration. Les familles assistent à la messe de minuit, se réunissent pour des festins et célèbrent avec de la musique et de la danse. Des plats traditionnels comme la soupe joumou sont servis.",
        "es": "La Navidad en Haití es un momento de alegría y celebración. Las familias asisten a la misa de medianoche, se reúnen para festines y celebran con música y baile. Se sirven platos tradicionales como la sopa joumou."
    },
    "fest_independence": {"en": "🗽 Independence Day (January 1)", "fr": "🗽 Jour de l'Indépendance (1er janvier)", "es": "🗽 Día de la Independencia (1 de enero)"},
    "fest_independence_desc": {
        "en": "Haiti celebrates its independence from France on January 1st. It is a day of national pride, featuring parades, speeches, and the traditional soup joumou.",
        "fr": "Haïti célèbre son indépendance de la France le 1er janvier. C'est une journée de fierté nationale, avec des défilés, des discours et la traditionnelle soupe joumou.",
        "es": "Haití celebra su independencia de Francia el 1 de enero. Es un día de orgullo nacional, con desfiles, discursos y la tradicional sopa joumou."
    },
    # Media section
    "media_title": {"en": "📺 Media Gallery", "fr": "📺 Galerie Médias", "es": "📺 Galería de Medios"},
    "media_subtitle": {"en": "Add YouTube or Dropbox links to share with the community", "fr": "Ajoutez des liens YouTube ou Dropbox à partager avec la communauté", "es": "Agrega enlaces de YouTube o Dropbox para compartir con la comunidad"},
    "media_link_label": {"en": "Media Link (YouTube or Dropbox)", "fr": "Lien média (YouTube ou Dropbox)", "es": "Enlace de medios (YouTube o Dropbox)"},
    "media_caption_label": {"en": "Caption", "fr": "Légende", "es": "Leyenda"},
    "media_add_button": {"en": "➕ Add Media", "fr": "➕ Ajouter un média", "es": "➕ Agregar medio"},
    "media_empty": {"en": "No media added yet. Use the form above to add a link.", "fr": "Aucun média ajouté pour l'instant. Utilisez le formulaire ci-dessus pour ajouter un lien.", "es": "No se han agregado medios aún. Use el formulario anterior para agregar un enlace."},
    "media_remove": {"en": "❌ Remove", "fr": "❌ Supprimer", "es": "❌ Eliminar"},
    "media_youtube": {"en": "YouTube Video", "fr": "Vidéo YouTube", "es": "Video de YouTube"},
    "media_dropbox": {"en": "Dropbox Link", "fr": "Lien Dropbox", "es": "Enlace de Dropbox"},
}

# ---------- Helper function to get text ----------
def get_text(key, lang):
    return TEXTS[key].get(lang, TEXTS[key]["en"])

# ---------- Initialize session state ----------
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'
if 'media_items' not in st.session_state:
    st.session_state.media_items = []
if 'logo' not in st.session_state:
    st.session_state.logo = None

# ---------- Language selection ----------
def set_language():
    st.session_state.lang = LANGUAGES[st.session_state.lang_selector]

# ---------- Sidebar ----------
with st.sidebar:
    # Language selector
    lang_choice = st.selectbox(
        "🌐 Language / Langue / Idioma",
        ["English", "Français", "Español"],
        index=["English", "Français", "Español"].index(
            [k for k, v in LANGUAGES.items() if v == st.session_state.lang][0]
        ),
        key="lang_selector",
        on_change=set_language
    )
    
    lang = st.session_state.lang  # current language code
    
    st.markdown(f"### {get_text('nav_title', lang)}")
    
    nav_items = [
        get_text('nav_home', lang),
        get_text('nav_history', lang),
        get_text('nav_music', lang),
        get_text('nav_art', lang),
        get_text('nav_cuisine', lang),
        get_text('nav_language', lang),
        get_text('nav_festivals', lang),
        get_text('nav_media', lang)
    ]
    
    selected_display = st.radio(
        "Navigate",
        nav_items,
        index=0,
        label_visibility="collapsed"
    )
    
    # Map display name back to key
    nav_map = {
        get_text('nav_home', lang): "Home",
        get_text('nav_history', lang): "History",
        get_text('nav_music', lang): "Music",
        get_text('nav_art', lang): "Art",
        get_text('nav_cuisine', lang): "Cuisine",
        get_text('nav_language', lang): "Language",
        get_text('nav_festivals', lang): "Festivals",
        get_text('nav_media', lang): "Media"
    }
    selected = nav_map[selected_display]
    
    st.markdown("---")
    st.markdown(f"### {get_text('upload_logo', lang)}")
    uploaded_logo = st.file_uploader("", type=["png", "jpg", "jpeg", "svg"])
    
    if uploaded_logo is not None:
        st.session_state.logo = uploaded_logo
        st.success(get_text('upload_success', lang))
    
    st.markdown("---")
    st.caption("🇭🇹 Haiti Culture Connection")
    st.caption("v1.0 | Built with ❤️")

# ---------- Main Content ----------

# Display logo if uploaded
if st.session_state.logo is not None:
    try:
        logo = Image.open(st.session_state.logo)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo, use_column_width=True)
    except Exception as e:
        st.error(f"Error displaying logo: {e}")

# Header
st.markdown(f'<div class="main-title">{get_text("main_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-title">{get_text("sub_title", lang)}</div>', unsafe_allow_html=True)

# ---------- Page Content ----------
if selected == "Home":
    st.markdown(f'<h2 class="section-title">{get_text("home_title", lang)}</h2>', unsafe_allow_html=True)
    
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

elif selected == "History":
    st.markdown(f'<h2 class="section-title">{get_text("history_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Music":
    st.markdown(f'<h2 class="section-title">{get_text("music_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Art":
    st.markdown(f'<h2 class="section-title">{get_text("art_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Cuisine":
    st.markdown(f'<h2 class="section-title">{get_text("cuisine_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Language":
    st.markdown(f'<h2 class="section-title">{get_text("lang_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Festivals":
    st.markdown(f'<h2 class="section-title">{get_text("fest_title", lang)}</h2>', unsafe_allow_html=True)
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

elif selected == "Media":
    st.markdown(f'<h2 class="section-title">{get_text("media_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="culture-card">
        <h3>📺 {get_text("media_title", lang)}</h3>
        <p>{get_text("media_subtitle", lang)}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Form to add media
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            link = st.text_input(get_text("media_link_label", lang), key="media_link")
        with col2:
            caption = st.text_input(get_text("media_caption_label", lang), key="media_caption")
        
        if st.button(get_text("media_add_button", lang), use_container_width=True):
            if link.strip():
                st.session_state.media_items.append({"link": link.strip(), "caption": caption.strip()})
                st.success("✅ Media added!")
                st.rerun()
            else:
                st.warning("Please enter a link.")
    
    # Display media items
    if st.session_state.media_items:
        for idx, item in enumerate(st.session_state.media_items):
            with st.container():
                st.markdown(f"**{item['caption'] if item['caption'] else get_text('media_youtube', lang)}**")
                # Detect if it's a YouTube link
                if "youtube.com" in item['link'] or "youtu.be" in item['link']:
                    # Try to extract video ID
                    import re
                    vid_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:[&?]|$)", item['link'])
                    if vid_match:
                        vid = vid_match.group(1)
                        st.markdown(f'<iframe width="100%" height="315" src="https://www.youtube.com/embed/{vid}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>', unsafe_allow_html=True)
                else:
                    # Dropbox or other - just show link
                    st.markdown(f'<a href="{item["link"]}" target="_blank">{item["link"]}</a>', unsafe_allow_html=True)
                
                if st.button(f"{get_text('media_remove', lang)} {idx}", key=f"remove_{idx}"):
                    del st.session_state.media_items[idx]
                    st.rerun()
                st.markdown("---")
    else:
        st.info(get_text("media_empty", lang))

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
