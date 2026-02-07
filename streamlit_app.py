import streamlit as st

st.set_page_config(layout="wide")

st.title("Urdu Poetry Hub - Frontend (React) Deployment Note")

st.markdown("""
This `streamlit_app.py` file is included as per your request.
However, it's important to note that the main application developed is a **React frontend application**.

**How to deploy the React application:**
A React application is typically deployed as static files (HTML, CSS, JavaScript) to a web server, a Content Delivery Network (CDN), or a static site hosting service (e.g., Netlify, Vercel, GitHub Pages, Firebase Hosting).

This Streamlit app serves only as a placeholder to acknowledge the request for a Streamlit file.
It does not run the React application directly.
""")

st.subheader("React Application Details")
st.markdown("""
The React application (`index.html`, `index.tsx`, `App.tsx`, etc.) needs to be built and served separately.
1.  **Build:** Run `npm run build` (or `yarn build`) in your React project directory. This generates optimized static files.
2.  **Deploy:** Upload the contents of the `build` folder to your preferred static hosting provider.
""")

st.write("---")
st.info("For the full functionality of the Urdu Poetry Hub, please refer to the generated React application files.")

st.markdown("Feel free to close this Streamlit app and launch the React app.")
