import streamlit as st

st.title("Profil Penulis")

# CSS Custom
st.markdown("""
    <style>
    .profile-card {
        background-color: #183B4E; 
        padding: 20px;
        border-radius: 15px;
        text-align: center; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin: 10px;
        color: white;
    }
    .circle-img {
        width: 180px;   
        height: 180px;  
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #183B54;
        margin-bottom: 15px;
    }
    a {
        color: #FFD54F;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="profile-card">
            <img src="https://tse3.mm.bing.net/th/id/OIP.1o-tp6Wjn5nr6Vp6k6KWZwHaHH?rs=1&pid=ImgDetMain&o=7&rm=3"
                class="circle-img">

            Ilma Fitriyani
            NRP: 5003221063
            Program Studi: S-1 Statistika ITS

            E-mail: ilmafitri906@gmail.com
            LinkedIn: ilmafitriyani
            Instagram: ilmafitriyani
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
         <div class="profile-card">
            <img src="https://tse3.mm.bing.net/th/id/OIP.1o-tp6Wjn5nr6Vp6k6KWZwHaHH?rs=1&pid=ImgDetMain&o=7&rm=3"
                class="circle-img">

            Cika Rahmannia Febrianti
            NRP: 5003221081
            Program Studi: S-1 Statistika ITS
            
            E-mail: cikarahmanniaa@gmail.com
            LinkedIn: cikarahmanniaf
            Instagram: @cikarhma
        </div>
        """,
        unsafe_allow_html=True  
    )
