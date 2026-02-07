import streamlit as st
import time

# Python equivalent of STATIC_POETRIES from constants.ts
STATIC_POETRIES_PY = [
    {
        'id': '1',
        'lines': [
            'نہ تھا کچھ تو خدا تھا، کچھ نہ ہوتا تو خدا ہوتا',
            'ڈبویا مجھ کو ہونے نے، نہ ہوتا میں تو کیا ہوتا',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '2',
        'lines': [
            'یہ کہاں کی دوستی ہے کہ بنے ہیں دوست ناصح',
            'کوئی چارہ ساز ہوتا، کوئی غم گسار ہوتا',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '3',
        'lines': [
            'بڑے شوق سے سن رہا تھا زمانہ ہم ہی سو گئے داستاں کہتے کہتے',
            'بس اتنا ہی یاد ہے کہ ہر لفظ کے ساتھ آنسو نکلتے تھے',
        ],
        'poet': 'میر تقی میر',
    },
    {
        'id': '4',
        'lines': [
            'ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے',
            'بہت نکلے مرے ارمان لیکن پھر بھی کم نکلے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '5',
        'lines': [
            'تجھ سے بچھڑ کر میں نے دیکھا، ہر رنگ میں رُلائی دنیا',
            'تیرے بعد مجھے سکھ کی کوئی، آس نہ دی اے پیارے دنیا',
        ],
        'poet': 'احمد فراز',
    },
    {
        'id': '6',
        'lines': [
            'زندگی اپنی جب اس شکل سے گزری غالبؔ',
            'ہم بھی کیا یاد کریں گے کہ خدا رکھتے تھے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '7',
        'lines': [
            'ہر ایک بات پہ کہتے ہو تم کہ تو کیا ہے',
            'تمہیں کہو کہ یہ اندازِ گفتگو کیا ہے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '8',
        'lines': [
            'عشق پر زور نہیں ہے یہ وہ آتش غالب',
            'کہ لگائے نہ لگے اور بجھائے نہ بنے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '9',
        'lines': [
            'یہ عشق نہیں آساں بس اتنا سمجھ لیجیئے',
            'اک آگ کا دریا ہے اور ڈوب کے جانا ہے',
        ],
        'poet': 'علامہ اقبال',
    },
    {
        'id': '10',
        'lines': [
            'آیا ہی تھا خیال کہ آنکھوں میں آ بسے',
            'اب تک تو یہ گمان تھا، میرے دل میں ہے کوئی',
        ],
        'poet': 'فیض احمد فیض',
    },
    {
        'id': '11',
        'lines': [
            'جب سے تو نے مجھے دیوانہ بنا رکھا ہے',
            'سنگ ہر شخص نے ہاتھوں میں اٹھا رکھا ہے',
        ],
        'poet': 'ساحر لدھیانوی',
    },
    {
        'id': '12',
        'lines': [
            'بہت مشکل ہے با ذوق رہنا',
            'جہاں بس بے ذوق لوگ رہتے ہیں',
        ],
        'poet': 'پروین شاکر',
    },
    {
        'id': '13',
        'lines': [
            'تم جو بدلے تو زمانے نے بدل ڈالا مجھے',
            'ورنہ میں تو ترے لفظوں کی امانت تھا کبھی',
        ],
        'poet': 'جون ایلیا',
    },
    {
        'id': '14',
        'lines': [
            'دل کو بہلانے کی تدبیریں بہت تھیں لیکن',
            'اس کے ہاتھوں سے جو ٹوٹا ہے وہ پیمانہ نہیں',
        ],
        'poet': 'ناصر کاظمی',
    },
    {
        'id': '15',
        'lines': [
            'لوگ ہر موڑ پہ رک رک کے سنبھلتے کیوں ہیں',
            'اتنا ڈرتے ہیں تو پھر گھر سے نکلتے کیوں ہیں',
        ],
        'poet': 'کیفی اعظمی',
    },
    {
        'id': '16',
        'lines': [
            'مدت ہوئی ہے یار کو مہماں کیے ہوئے',
            'جوشِ قدح سے بزم چراغاں کیے ہوئے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '17',
        'lines': [
            'اک ذرا سی بات پر برسوں کے یارانے گئے',
            'لیکن اتنا تو ہوا کچھ لوگ پہچانے گئے',
        ],
        'poet': 'احمد فراز',
    },
    {
        'id': '18',
        'lines': [
            'ہم تو فنا ہو گئے ان کی آنکھیں دیکھ کر غالب',
            'نہ جانے وہ آئینہ کیسے دیکھتے ہوں گے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '19',
        'lines': [
            'جلا ہے جسم جہاں دل بھی جل گیا ہوگا',
            'کریدتے ہو جو اب راکھ جستجو کیا ہے',
        ],
        'poet': 'مرزا غالب',
    },
    {
        'id': '20',
        'lines': [
            'ہم نے ہر سانس پہ لکھی تھی تمہاری چاہت',
            'تم نے ہر بات پہ لکھا ہے جدائی میری',
        ],
        'poet': 'پروین شاکر',
    },
    {
        'id': '21',
        'lines': [
            'کب تک رہے گی یونہی دل کی یہ بے چینی',
            'اے کاش کوئی آ کے مجھے پیار کر لے',
        ],
        'poet': 'حبیب جالب',
    },
    {
        'id': '22',
        'lines': [
            'شامِ فراق اب نہ پوچھئے، آئی اور آ کے ٹل گئی',
            'دل تھام کر ہر ایک کی، آنکھیں بھری اور چل گئی',
        ],
        'poet': 'فیض احمد فیض',
    },
    {
        'id': '23',
        'lines': [
            'کیا غم ہے جو ہر سو یہ بکھرے ہیں پرانے لوگ',
            'اک نئے عزم کے ساتھ پھر سے سجانے لوگ',
        ],
        'poet': 'جون ایلیا',
    },
    {
        'id': '24',
        'lines': [
            'مجھ سے پہلی سی محبت مری محبوب نہ مانگ',
            'میں نے سمجھا تھا کہ تو ہے تو درخشاں ہے حیات',
        ],
        'poet': 'فیض احمد فیض',
    },
    {
        'id': '25',
        'lines': [
            'یاد ماضی عذاب ہے یا رب',
            'چھین لے مجھ سے حافظہ میرا',
        ],
        'poet': 'اختر شیرانی',
    },
    {
        'id': '26',
        'lines': [
            'زندگی بھر کا حساب بس اتنا ہی رہا',
            'اُس کو چاہا اُس نے چاہا کسی اور کو',
        ],
        'poet': 'نامعلوم',
    },
    {
        'id': '27',
        'lines': [
            'کون کہتا ہے کہ موت آئی تو مر جاؤں گا',
            'میں تو دریا ہوں سمندر میں اتر جاؤں گا',
        ],
        'poet': 'عابد علی عابد',
    },
    {
        'id': '28',
        'lines': [
            'کیا کہا عشق جاودانی ہے',
            'ایک کمزور کی کہانی ہے',
        ],
        'poet': 'احمد ندیم قاسمی',
    },
    {
        'id': '29',
        'lines': [
            'کچھ اس طرح سے گزاری ہے زندگی میں نے',
            'کہ جیسے سچ کا گناہ ہو سرِ عام مجھ پر',
        ],
        'poet': 'افتخار عارف',
    },
    {
        'id': '30',
        'lines': [
            'یوں تو ہر شام امیدوں میں گزر جاتی ہے',
            'آج کچھ بات ہے جو شام پہ رونا آیا',
        ],
        'poet': 'پروین شاکر',
    },
]

POETRIES_PER_PAGE = 5

st.set_page_config(layout="centered")

# Custom CSS for dark theme and Urdu font (similar to React app)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;500;600;700&display=swap');
    
    body {
        font-family: 'Noto Nastaliq Urdu', 'Nastaliq Urdu', 'Pak Nastaleeq', 'Urdu Typesetting', 'Arial Unicode MS', 'serif';
        background-color: #000; /* Black background */
        color: #fff; /* White text */
        direction: rtl; /* Right-to-left for Urdu */
        text-align: right;
    }
    
    /* Streamlit's main app container */
    .stApp {
        background-color: #000;
        color: #fff;
        font-family: 'Noto Nastaliq Urdu', sans-serif;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Noto Nastaliq Urdu', sans-serif;
        color: #fff;
        text-align: center;
    }
    
    /* Text elements */
    p, div, span, li, a, label {
        font-family: 'Noto Nastaliq Urdu', sans-serif;
        color: #fff;
    }
    
    /* Specific styling for poetry cards */
    .poetry-card {
        background-color: #1a1a1a; /* Darker gray for cards */
        border-radius: 1rem; /* Rounded corners */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); /* Subtle shadow */
        padding: 2rem;
        margin-bottom: 1.5rem;
        text-align: center;
        border: 1px solid #333; /* Darker border */
        transition: all 0.3s ease;
    }
    .poetry-card:hover {
        border-color: #555;
    }
    .poetry-line {
        font-size: 1.875rem; /* text-3xl */
        line-height: 1.75; /* leading-loose */
        font-weight: 500; /* font-medium */
        margin: 0.5rem 0;
    }
    .poetry-poet {
        font-size: 1.25rem; /* text-xl */
        color: #aaa; /* Lighter gray for poet name */
        margin-top: 1rem;
    }
    .copy-button {
        background-color: #2563eb; /* Blue-600 */
        color: white;
        font-weight: 600; /* font-semibold */
        padding: 0.625rem 1.25rem; /* px-5 py-2 */
        border-radius: 0.5rem; /* rounded-lg */
        margin-top: 1.5rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .copy-button:hover {
        background-color: #1d4ed8; /* Blue-700 */
    }
    .copy-button.copied {
        background-color: #16a34a; /* Green-600 */
    }
    .copy-button.copied:hover {
        background-color: #15803d; /* Green-700 */
    }
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-family: 'Noto Nastaliq Urdu', sans-serif;
        font-size: 1.25rem;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 0.75rem;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
    }
    .stButton > button:active {
        background-color: #1e40af;
    }
    /* Adjust Streamlit's native elements for dark theme */
    .stMarkdown, .stText {
        color: #fff;
    }
    .footer-text {
        color: #6b7280; /* gray-500 */
        font-size: 0.875rem; /* text-sm */
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #333;
    }
    .loading-message, .end-of-poetry-message, .no-poetry-found-message {
        font-size: 1.5rem; /* text-2xl */
        color: #a0a0a0; /* gray-400 */
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    .end-of-poetry-message {
        font-size: 1.25rem; /* text-xl */
        color: #6b7280; /* gray-500 */
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state variables
if 'poetries_displayed' not in st.session_state:
    st.session_state.poetries_displayed = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0 # Use 0 so initial load correctly fetches page 1
if 'has_more' not in st.session_state:
    st.session_state.has_more = True
if 'loading' not in st.session_state:
    st.session_state.loading = False


def load_poetries_page(page, limit):
    """Simulates fetching a page of poetries with a delay."""
    # st.session_state.loading = True # Set loading state
    time.sleep(0.7)  # Simulate network delay
    start_index = (page - 1) * limit
    end_index = start_index + limit
    data = STATIC_POETRIES_PY[start_index:end_index]
    has_more = end_index < len(STATIC_POETRIES_PY)
    # st.session_state.loading = False # Clear loading state
    return data, has_more


def append_poetries():
    """Callback for the 'Load More' button."""
    st.session_state.loading = True
    st.session_state.current_page += 1
    new_poetries, new_has_more = load_poetries_page(st.session_state.current_page, POETRIES_PER_PAGE)
    
    # Filter out duplicates if any (important for re-runs and retries)
    existing_ids = {p['id'] for p in st.session_state.poetries_displayed}
    unique_new_poetries = [p for p in new_poetries if p['id'] not in existing_ids]

    st.session_state.poetries_displayed.extend(unique_new_poetries)
    st.session_state.has_more = new_has_more
    st.session_state.loading = False
    st.rerun() # Force a rerun to update the UI


# --- Header ---
st.markdown("""
<header class="w-full text-center py-6 sm:py-8 md:py-10">
    <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-2 leading-tight">
        اردو شاعری
    </h1>
    <p class="text-xl sm:text-2xl text-gray-300">
        انتخابِ بہترین دو سطر شاعری
    </p>
</header>
""", unsafe_allow_html=True)

# --- Initial Load ---
if not st.session_state.poetries_displayed and st.session_state.current_page == 0:
    with st.spinner("لوڈنگ شاعری..."):
        st.session_state.loading = True
        st.session_state.current_page = 1 # Start from page 1
        initial_poetries, initial_has_more = load_poetries_page(st.session_state.current_page, POETRIES_PER_PAGE)
        st.session_state.poetries_displayed.extend(initial_poetries)
        st.session_state.has_more = initial_has_more
        st.session_state.loading = False
        st.rerun() # Force rerun after initial load to display content

# --- Display Poetries ---
if st.session_state.poetries_displayed:
    for poetry in st.session_state.poetries_displayed:
        lines_html = "".join([f"<p class='poetry-line'>{line}</p>" for line in poetry['lines']])
        poet_html = f"<p class='poetry-poet'>— {poetry['poet']}</p>" if poetry.get('poet') else ""

        # Using a unique key for the button to manage its state (e.g., copied text)
        copy_button_id = f"copy-btn-{poetry['id']}"
        if st.button("کاپی کریں (Copy)", key=copy_button_id):
            st.code(f"{poetry['lines'][0]}\n{poetry['lines'][1]}", language="text", display_as_code=False)
            st.toast("کاپی ہو گیا! (Copied!)", icon="✅")

        st.markdown(f"""
        <div class="poetry-card">
            <div class="poetry-text">
                {lines_html}
            </div>
            {poet_html}
            <button class="copy-button" onclick="navigator.clipboard.writeText(`{'\\n'.join(poetry['lines'])}`); alert('کاپی ہو گیا! (Copied!)');">
                کاپی کریں (Copy)
            </button>
        </div>
        """, unsafe_allow_html=True)
else:
    if not st.session_state.loading and not st.session_state.has_more:
        st.markdown("<p class='no-poetry-found-message'>کوئی شاعری نہیں ملی۔ (No poetry found.)</p>", unsafe_allow_html=True)


# --- Load More / End of List ---
if st.session_state.has_more:
    if st.session_state.loading:
        st.markdown("<p class='loading-message'>لوڈنگ مزید شاعری...</p>", unsafe_allow_html=True)
        st.spinner("") # Show default spinner if needed, but text is more friendly
    else:
        st.button("مزید شاعری لوڈ کریں (Load More Poetry)", on_click=append_poetries)
elif not st.session_state.loading and st.session_state.poetries_displayed:
    st.markdown("<p class='end-of-poetry-message'>تمام شاعری ختم ہو گئی (End of all poetry).</p>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(f"""
<footer class="footer-text">
    <p>© {time.strftime("%Y")} اردو شاعری Hub. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
