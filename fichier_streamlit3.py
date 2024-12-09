import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format


lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',

'password': 'utilisateurMDP',

'email': 'utilisateur@gmail.com',

'failed_login_attemps': 0,

'logged_in': False,

'role': 'utilisateur'},

'root': {'name': 'root',

'password': 'rootMDP',

'email': 'admin@gmail.com',

'failed_login_attemps': 0,

'logged_in': False,

'role': 'administrateur'}}}

# je stocke dans une variable la class Authenticate, qui contient les données de compte:
authenticator = Authenticate(lesDonneesDesComptes,

"cookie name",

"cookie key",

30,

)

# Utiliser la méthode login pour afficher le formulaire de connexion (username & password) et vérifier les informations d'identification de l'utilisateur:
authenticator.login()

#gestion des infos en fonction des utilisateurs:
# ici je declare deux acceuils, 1 pour l'accueil du site, 1 pour l'album photos
def accueil():
    st.title('Bienvenu.e.s sur ma page!')
def accueil_photos():
    st.title("Bienvenu.e.s sur l'album photo de mon chien")

if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write("Bienvenu.e utilisateur")
        selection = option_menu(
            menu_title= 'Menu',
            options= ['Accueil', 'Photos'],
            icons= ['house', 'camera'],
            menu_icon= 'cast'
                    )
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")

    if selection == "Accueil":
        accueil()                                       # j'appelle la fonction accueil prédéfinie en amont
        st.image('photo.jpg')
    elif selection == "Photos":
        accueil_photos()                                # j'appelle la fonction accueil_photos prédéfinie en amont
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image('photo1.jpg')
            st.write("quand il me demande quelque chose")
        with col2:
            st.image('photo2.jpg')
            st.write('quand il était petit')
        with col3:
            st.image('photo3.jpg')
            st.write("c'est vraiment le plus BEAU!")
        # Le bouton de déconnexion
if st.session_state["authentication_status"] is False:
    st.error("Le nom d'utilisateur ou le mot de passe est/sont incorrect(s)")
if st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis') 

