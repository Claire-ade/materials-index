import streamlit as st

st.set_page_config(page_title="Index des polymères", layout="centered")
st.title("🔍 Recherche d'acronymes de polymères")

# Champ de saisie
acronyme = st.text_input("Entrez un acronyme de polymère (ex : PET, PVC, PMMA)").upper()

# Dictionary of polymer acronyms
polymer_data = {
    "PBT": {
        "nom": "Polybutylène téréphtalate",
        "formule": "(C12H12O4)n"
    },
    "PMMA": {
        "nom": "Polyméthacrylate de méthyle",
        "formule": "(C5O2H8)n"
    },
    "PTFE": {
        "nom": "Polytétrafluoroéthylène (Téflon)",
        "formule": "(C2F4)n"
    },
    "CA": {
        "nom": "Acétate de cellulose",
        "formule": "variable"
    },
    "PVC": {
        "nom": "Polychlorure de vinyle",
        "formule": "(C2H3Cl)n"
    },
    "PET": {
        "nom": "Polyéthylène téréphtalate",
        "formule": "(C10H8O4)n"
    },
    "PE": {
        "nom": "Polyéthylène",
        "formule": "(C2H4)n"
    },
    "PP": {
        "nom": "Polypropylène",
        "formule": "(C3H6)n"
    },
    "PS": {
        "nom": "Polystyrène",
        "formule": "(C8H8)n"
    }
    # Tu peux ajouter les autres ici…
}

# Input field
acronym = st.text_input("Enter a polymer acronym (e.g. ABS, PTFE):").upper()

# Affichage des résultats
if acronym:
    if acronym in polymer_data:
        st.subheader("Nom complet")
        st.write(polymer_data[acronym]["nom"])

        st.subheader("Formule chimique")
        st.latex(polymer_data[acronym]["formule"])
    else:
        st.error("Acronyme non trouvé. Essayez un autre.")
