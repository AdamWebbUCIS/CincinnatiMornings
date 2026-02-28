import streamlit as st
from datetime import datetime, timedelta
import random

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Cincinnati Mornings",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────
# MOCK DATA
# ──────────────────────────────────────────────
CATEGORIES = ["Local", "Sports", "Food & Drink", "Culture", "Business", "Opinion"]

HERO_ARTICLE = {
    "category": "Local",
    "title": "Cincinnati's Riverfront Revival: A $2 Billion Vision Takes Shape",
    "excerpt": "The Queen City's most ambitious development project in decades is transforming the banks of the Ohio River into a world-class waterfront destination. Here's everything you need to know about what's coming.",
    "author": "Sarah Mitchell",
    "date": (datetime.now() - timedelta(hours=3)).strftime("%B %d, %Y"),
    "read_time": "8 min read",
    "image": "https://images.unsplash.com/photo-1569878698889-7bffa1896872?w=1200&q=80",
}

LATEST_ARTICLES = [
    {
        "category": "Business",
        "title": "Three Cincinnati Startups Just Landed $50M in New Funding",
        "excerpt": "The Queen City's tech scene continues to heat up as venture capital flows into local AI and biotech companies.",
        "author": "James Chen",
        "date": "2 hours ago",
        "read_time": "5 min read",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&q=80",
    },
    {
        "category": "Food & Drink",
        "title": "The Ultimate Guide to Cincinnati's New Restaurant Openings This Spring",
        "excerpt": "From OTR to Hyde Park, here are the 12 most exciting restaurants opening their doors in 2026.",
        "author": "Maria Torres",
        "date": "4 hours ago",
        "read_time": "6 min read",
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&q=80",
    },
    {
        "category": "Sports",
        "title": "Bengals Draft Preview: Top Prospects Cincinnati Should Target",
        "excerpt": "With the NFL Draft approaching, we break down the players who could make the biggest impact at Paul Brown Stadium.",
        "author": "Derek Wells",
        "date": "5 hours ago",
        "read_time": "7 min read",
        "image": "https://images.unsplash.com/photo-1566577739112-5180d4bf9390?w=600&q=80",
    },
    {
        "category": "Culture",
        "title": "Inside the Cincinnati Art Museum's Stunning New Contemporary Wing",
        "excerpt": "A first look at the $35 million expansion that's putting Cincinnati on the national art map.",
        "author": "Lena Park",
        "date": "6 hours ago",
        "read_time": "4 min read",
        "image": "https://images.unsplash.com/photo-1544967082-d9d25d867d66?w=600&q=80",
    },
    {
        "category": "Local",
        "title": "New Streetcar Expansion Route Approved by City Council",
        "excerpt": "The connector will link the Banks to UC's campus, with construction starting this fall.",
        "author": "Tom Richards",
        "date": "7 hours ago",
        "read_time": "3 min read",
        "image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&q=80",
    },
    {
        "category": "Business",
        "title": "Why Remote Workers Are Flocking to Cincinnati's Co-Working Spaces",
        "excerpt": "Affordable living and a booming downtown scene make the Queen City a top pick for digital nomads.",
        "author": "Rachel Kim",
        "date": "8 hours ago",
        "read_time": "5 min read",
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80",
    },
]

EDITORS_PICKS = [
    {
        "category": "Opinion",
        "title": "Cincinnati Deserves a World-Class Public Transit System. Here's How We Get There.",
        "excerpt": "It's time to stop thinking small and start building the transportation infrastructure our growing city demands.",
        "author": "Editorial Board",
        "date": "Yesterday",
        "read_time": "10 min read",
        "image": "https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=600&q=80",
    },
    {
        "category": "Culture",
        "title": "The Hidden History of Cincinnati's Underground Brewery Tunnels",
        "excerpt": "Beneath the streets of Over-the-Rhine lies a forgotten network of 19th-century lagering cellars.",
        "author": "Michael Brandt",
        "date": "2 days ago",
        "read_time": "12 min read",
        "image": "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=600&q=80",
    },
    {
        "category": "Food & Drink",
        "title": "We Tried Every Skyline Chili Location and Ranked Them All",
        "excerpt": "Is your go-to Skyline actually the best? Our completely unscientific but passionate ranking.",
        "author": "Maria Torres",
        "date": "3 days ago",
        "read_time": "8 min read",
        "image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&q=80",
    },
]

FEED_ARTICLES = [
    {"category": "Local", "title": "Findlay Market Vendors Report Record Spring Sales", "author": "Sarah Mitchell", "date": "9 hours ago"},
    {"category": "Sports", "title": "FC Cincinnati Announces International Friendly Against Bayern Munich", "author": "Derek Wells", "date": "10 hours ago"},
    {"category": "Business", "title": "Procter & Gamble Unveils Sustainability Campus at Downtown HQ", "author": "James Chen", "date": "11 hours ago"},
    {"category": "Culture", "title": "Music Hall Renovation Uncovers 140-Year-Old Time Capsule", "author": "Lena Park", "date": "12 hours ago"},
    {"category": "Food & Drink", "title": "The Definitive Map of Cincinnati's Best Breakfast Spots", "author": "Maria Torres", "date": "13 hours ago"},
    {"category": "Local", "title": "Washington Park Farmers Market Opens for the Season This Weekend", "author": "Tom Richards", "date": "14 hours ago"},
    {"category": "Opinion", "title": "It's Time to Rethink How We Fund Cincinnati Public Schools", "author": "Editorial Board", "date": "15 hours ago"},
    {"category": "Sports", "title": "Reds Pitching Rotation Looks Dominant in Spring Training", "author": "Derek Wells", "date": "16 hours ago"},
    {"category": "Business", "title": "Cincinnati Named Top 10 City for Young Entrepreneurs", "author": "Rachel Kim", "date": "17 hours ago"},
    {"category": "Culture", "title": "Blink 2026: What to Expect From This Year's Light Festival", "author": "Lena Park", "date": "18 hours ago"},
]

CATEGORY_COLORS = {
    "Local": "#E4002B",
    "Sports": "#FF6B35",
    "Food & Drink": "#FFB81C",
    "Culture": "#A855F7",
    "Business": "#3B82F6",
    "Opinion": "#10B981",
}


# ──────────────────────────────────────────────
# CUSTOM CSS
# ──────────────────────────────────────────────
def inject_css():
    st.markdown(
        """
    <style>
    /* ── Import Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&display=swap');

    /* ── Global Dark Theme ── */
    .stApp {
        background-color: #0D0D1A !important;
        color: #E8E8ED !important;
    }
    .stApp > header { background-color: transparent !important; }
    [data-testid="stSidebar"] { display: none !important; }

    /* Hide default Streamlit header/footer */
    #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 1280px !important;
    }

    /* ── Typography ── */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        color: #FFFFFF !important;
    }
    p, span, div, a, li {
        font-family: 'Inter', sans-serif !important;
    }

    /* ── Top Navigation Bar ── */
    .nav-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 32px;
    }
    .nav-logo {
        font-family: 'Outfit', sans-serif;
        font-size: 28px;
        font-weight: 900;
        background: linear-gradient(135deg, #E4002B, #FFB81C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    .nav-logo span {
        font-family: 'Outfit', sans-serif !important;
        background: linear-gradient(135deg, #E4002B, #FFB81C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .nav-links {
        display: flex;
        gap: 28px;
    }
    .nav-links a {
        color: #9CA3AF !important;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        transition: color 0.2s ease;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .nav-links a:hover { color: #FFB81C !important; }

    /* ── Category Badge ── */
    .category-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #FFFFFF;
        margin-bottom: 8px;
    }

    /* ── Hero Section ── */
    .hero-card {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 48px;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hero-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 60px rgba(228, 0, 43, 0.15);
    }
    .hero-card img {
        width: 100%;
        height: 480px;
        object-fit: cover;
        display: block;
    }
    .hero-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 48px 40px;
        background: linear-gradient(transparent, rgba(13,13,26,0.95));
    }
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: 36px;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.2;
        margin-bottom: 12px;
    }
    .hero-excerpt {
        font-size: 16px;
        color: #C5C5D0;
        line-height: 1.6;
        margin-bottom: 16px;
        max-width: 700px;
    }
    .hero-meta {
        font-size: 13px;
        color: #9CA3AF;
    }
    .hero-meta span {
        color: #FFB81C;
        font-weight: 600;
    }

    /* ── Section Headers ── */
    .section-header {
        font-family: 'Outfit', sans-serif;
        font-size: 24px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 24px;
        padding-bottom: 12px;
        border-bottom: 3px solid;
        border-image: linear-gradient(90deg, #E4002B, #FFB81C) 1;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .section-header-full {
        width: 100%;
        margin-top: 56px;
    }

    /* ── Article Card ── */
    .article-card {
        background: linear-gradient(145deg, #14142B, #1A1A35);
        border-radius: 16px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        height: 100%;
        border: 1px solid rgba(255,255,255,0.04);
    }
    .article-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 48px rgba(228, 0, 43, 0.12);
    }
    .article-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }
    .article-card-body {
        padding: 20px;
    }
    .article-card-title {
        font-family: 'Outfit', sans-serif;
        font-size: 18px;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.3;
        margin-bottom: 8px;
    }
    .article-card-excerpt {
        font-size: 14px;
        color: #9CA3AF;
        line-height: 1.5;
        margin-bottom: 12px;
    }
    .article-card-meta {
        font-size: 12px;
        color: #6B7280;
    }
    .article-card-meta span {
        color: #FFB81C;
        font-weight: 600;
    }

    /* ── Editor's Pick Card (large) ── */
    .pick-card-lg {
        background: linear-gradient(145deg, #14142B, #1A1A35);
        border-radius: 16px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        border: 1px solid rgba(255,255,255,0.04);
        height: 100%;
    }
    .pick-card-lg:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 48px rgba(228, 0, 43, 0.12);
    }
    .pick-card-lg img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        display: block;
    }
    .pick-card-lg .article-card-body { padding: 24px; }
    .pick-card-lg .article-card-title { font-size: 22px; }

    /* ── Editor's Pick Card (small) ── */
    .pick-card-sm {
        background: linear-gradient(145deg, #14142B, #1A1A35);
        border-radius: 16px;
        overflow: hidden;
        display: flex;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        border: 1px solid rgba(255,255,255,0.04);
        margin-bottom: 16px;
    }
    .pick-card-sm:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 36px rgba(228, 0, 43, 0.10);
    }
    .pick-card-sm img {
        width: 160px;
        min-height: 140px;
        object-fit: cover;
        display: block;
        flex-shrink: 0;
    }
    .pick-card-sm .article-card-body { padding: 16px; }
    .pick-card-sm .article-card-title { font-size: 15px; }

    /* ── Newsletter CTA ── */
    .newsletter-cta {
        background: linear-gradient(135deg, #E4002B 0%, #1A1A2E 50%, #FFB81C 100%);
        border-radius: 20px;
        padding: 56px 48px;
        text-align: center;
        margin: 56px 0;
        position: relative;
        overflow: hidden;
    }
    .newsletter-cta::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,184,28,0.08) 0%, transparent 60%);
        animation: pulse-glow 4s ease-in-out infinite;
    }
    @keyframes pulse-glow {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 1; }
    }
    .newsletter-cta h2 {
        font-family: 'Outfit', sans-serif;
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 12px;
        position: relative;
    }
    .newsletter-cta p {
        font-size: 16px;
        color: #D1D5DB;
        margin-bottom: 28px;
        position: relative;
    }
    .newsletter-input-row {
        display: flex;
        justify-content: center;
        gap: 12px;
        position: relative;
        flex-wrap: wrap;
    }
    .newsletter-input {
        padding: 14px 24px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255,255,255,0.08);
        color: #FFFFFF;
        font-size: 15px;
        width: 320px;
        outline: none;
        font-family: 'Inter', sans-serif;
        backdrop-filter: blur(10px);
    }
    .newsletter-input::placeholder { color: #9CA3AF; }
    .newsletter-btn {
        padding: 14px 32px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #FFB81C, #E4002B);
        color: #FFFFFF;
        font-size: 15px;
        font-weight: 700;
        cursor: pointer;
        font-family: 'Inter', sans-serif;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .newsletter-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(228, 0, 43, 0.4);
    }

    /* ── Feed / List Items ── */
    .feed-item {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        transition: background 0.2s ease;
        cursor: pointer;
    }
    .feed-item:hover {
        background: rgba(255,255,255,0.02);
        border-radius: 8px;
        padding-left: 12px;
    }
    .feed-number {
        font-family: 'Outfit', sans-serif;
        font-size: 32px;
        font-weight: 900;
        color: rgba(228, 0, 43, 0.25);
        min-width: 48px;
        text-align: center;
    }
    .feed-content {}
    .feed-title {
        font-family: 'Outfit', sans-serif;
        font-size: 17px;
        font-weight: 600;
        color: #E8E8ED;
        margin-bottom: 4px;
        line-height: 1.3;
    }
    .feed-meta {
        font-size: 12px;
        color: #6B7280;
    }
    .feed-meta span {
        font-weight: 600;
    }

    /* ── Footer ── */
    .footer {
        border-top: 1px solid rgba(255,255,255,0.06);
        padding: 48px 0 24px;
        margin-top: 56px;
    }
    .footer-logo {
        font-family: 'Outfit', sans-serif;
        font-size: 22px;
        font-weight: 800;
        background: linear-gradient(135deg, #E4002B, #FFB81C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .footer-tagline {
        font-size: 14px;
        color: #6B7280;
        margin-bottom: 24px;
    }
    .footer-links {
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
        margin-bottom: 24px;
    }
    .footer-links a {
        color: #9CA3AF !important;
        text-decoration: none;
        font-size: 13px;
        font-weight: 500;
        transition: color 0.2s;
    }
    .footer-links a:hover { color: #FFB81C !important; }
    .footer-copy {
        font-size: 12px;
        color: #4B5563;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.04);
    }

    /* ── Hide Streamlit column gaps ── */
    [data-testid="column"] {
        padding: 0 8px !important;
    }

    /* ── Divider style override ── */
    hr {
        border-color: rgba(255,255,255,0.06) !important;
        margin: 8px 0 !important;
    }

    /* ── Scrollbar styling ── */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0D0D1A;
    }
    ::-webkit-scrollbar-thumb {
        background: #2A2A45;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #3A3A55;
    }

    /* ── Animate on load ── */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .animate-in {
        animation: fadeInUp 0.6s ease-out forwards;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# COMPONENT HELPERS
# ──────────────────────────────────────────────
def render_nav():
    st.markdown(
        """
    <div class="nav-bar animate-in">
        <div class="nav-logo">☀️ <span>Cincinnati Mornings</span></div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Local</a>
            <a href="#">Sports</a>
            <a href="#">Food & Drink</a>
            <a href="#">Culture</a>
            <a href="#">Business</a>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_hero():
    a = HERO_ARTICLE
    cat_color = CATEGORY_COLORS.get(a["category"], "#E4002B")
    st.markdown(
        f"""
    <div class="hero-card animate-in">
        <img src="{a['image']}" alt="{a['title']}" />
        <div class="hero-overlay">
            <div class="category-badge" style="background:{cat_color};">{a['category']}</div>
            <div class="hero-title">{a['title']}</div>
            <div class="hero-excerpt">{a['excerpt']}</div>
            <div class="hero-meta">
                By <span>{a['author']}</span> &nbsp;·&nbsp; {a['date']} &nbsp;·&nbsp; {a['read_time']}
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_article_card(article):
    cat_color = CATEGORY_COLORS.get(article["category"], "#E4002B")
    return f"""
    <div class="article-card">
        <img src="{article['image']}" alt="{article['title']}" />
        <div class="article-card-body">
            <div class="category-badge" style="background:{cat_color};">{article['category']}</div>
            <div class="article-card-title">{article['title']}</div>
            <div class="article-card-excerpt">{article['excerpt']}</div>
            <div class="article-card-meta">
                By <span>{article['author']}</span> &nbsp;·&nbsp; {article['date']}
            </div>
        </div>
    </div>
    """


def render_latest_section():
    st.markdown(
        '<div class="section-header-full"><div class="section-header">The Latest</div></div>',
        unsafe_allow_html=True,
    )
    # First row — 3 cards
    cols = st.columns(3)
    for i, col in enumerate(cols):
        if i < len(LATEST_ARTICLES):
            with col:
                st.markdown(
                    f'<div class="animate-in" style="animation-delay:{i*0.1}s">{render_article_card(LATEST_ARTICLES[i])}</div>',
                    unsafe_allow_html=True,
                )

    st.markdown("<br>", unsafe_allow_html=True)

    # Second row — 3 cards
    cols2 = st.columns(3)
    for i, col in enumerate(cols2):
        idx = i + 3
        if idx < len(LATEST_ARTICLES):
            with col:
                st.markdown(
                    f'<div class="animate-in" style="animation-delay:{(i+3)*0.1}s">{render_article_card(LATEST_ARTICLES[idx])}</div>',
                    unsafe_allow_html=True,
                )


def render_editors_picks():
    st.markdown(
        '<div class="section-header-full"><div class="section-header">Editor\'s Picks</div></div>',
        unsafe_allow_html=True,
    )

    col_left, col_right = st.columns([3, 2])

    with col_left:
        a = EDITORS_PICKS[0]
        cat_color = CATEGORY_COLORS.get(a["category"], "#E4002B")
        st.markdown(
            f"""
        <div class="pick-card-lg animate-in">
            <img src="{a['image']}" alt="{a['title']}" />
            <div class="article-card-body">
                <div class="category-badge" style="background:{cat_color};">{a['category']}</div>
                <div class="article-card-title">{a['title']}</div>
                <div class="article-card-excerpt">{a['excerpt']}</div>
                <div class="article-card-meta">
                    By <span>{a['author']}</span> &nbsp;·&nbsp; {a['date']} &nbsp;·&nbsp; {a['read_time']}
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_right:
        for idx, a in enumerate(EDITORS_PICKS[1:]):
            cat_color = CATEGORY_COLORS.get(a["category"], "#E4002B")
            st.markdown(
                f"""
            <div class="pick-card-sm animate-in" style="animation-delay:{(idx+1)*0.15}s">
                <img src="{a['image']}" alt="{a['title']}" />
                <div class="article-card-body">
                    <div class="category-badge" style="background:{cat_color};">{a['category']}</div>
                    <div class="article-card-title">{a['title']}</div>
                    <div class="article-card-meta">
                        By <span>{a['author']}</span> &nbsp;·&nbsp; {a['date']}
                    </div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )


def render_newsletter_cta():
    st.markdown(
        """
    <div class="newsletter-cta animate-in">
        <h2>☕ Start your morning smarter</h2>
        <p>Get Cincinnati's most important stories delivered to your inbox every weekday morning. Free, forever.</p>
        <div class="newsletter-input-row">
            <input type="email" class="newsletter-input" placeholder="Enter your email address" />
            <button class="newsletter-btn">Subscribe</button>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_feed():
    st.markdown(
        '<div class="section-header-full"><div class="section-header">The Feed</div></div>',
        unsafe_allow_html=True,
    )
    for i, article in enumerate(FEED_ARTICLES):
        cat_color = CATEGORY_COLORS.get(article["category"], "#E4002B")
        st.markdown(
            f"""
        <div class="feed-item animate-in" style="animation-delay:{i*0.05}s">
            <div class="feed-number">{str(i+1).zfill(2)}</div>
            <div class="feed-content">
                <div style="margin-bottom:4px;">
                    <span class="category-badge" style="background:{cat_color};font-size:10px;padding:3px 8px;">{article['category']}</span>
                </div>
                <div class="feed-title">{article['title']}</div>
                <div class="feed-meta">
                    By <span style="color:#FFB81C">{article['author']}</span> &nbsp;·&nbsp; {article['date']}
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )


def render_footer():
    st.markdown(
        """
    <div class="footer animate-in">
        <div class="footer-logo">☀️ Cincinnati Mornings</div>
        <div class="footer-tagline">Your daily briefing on the Queen City. Brewed fresh every morning.</div>
        <div class="footer-links">
            <a href="#">Home</a>
            <a href="#">Local</a>
            <a href="#">Sports</a>
            <a href="#">Food & Drink</a>
            <a href="#">Culture</a>
            <a href="#">Business</a>
            <a href="#">Opinion</a>
            <a href="#">About</a>
            <a href="#">Advertise</a>
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
        </div>
        <div class="footer-copy">
            &copy; 2026 Cincinnati Mornings. All rights reserved. Made with ☕ in the Queen City.
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# MAIN APP
# ──────────────────────────────────────────────
def main():
    inject_css()
    render_nav()
    render_hero()
    render_latest_section()
    render_editors_picks()
    render_newsletter_cta()
    render_feed()
    render_footer()


if __name__ == "__main__":
    main()
