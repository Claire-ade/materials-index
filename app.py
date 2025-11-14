import streamlit as st

st.set_page_config(page_title="Index des polymères", layout="centered")
st.title("🔍 Recherche d'acronymes de polymères")

# Dictionnaire complet des acronymes
polymer_data = {
    "ABS": {"nom": "Acrylonitrile Butadiène Styrène", "formule": "(C8H8·C4H6·C3H3N)n"},
    "PTFE": {"nom": "Polytétrafluoroéthylène (Téflon)", "formule": "(C2F4)n"},
    "PBT": {"nom": "Polybutylène téréphtalate", "formule": "(C12H12O4)n"},
    "PMMA": {"nom": "Polyméthacrylate de méthyle", "formule": "(C5O2H8)n"},
    "CA": {"nom": "Acétate de cellulose", "formule": "variable"},
    "CAB": {"nom": "Acétobutyrate de cellulose", "formule": "variable"},
    "CAP": {"nom": "Acétoproprionate de cellulose", "formule": "variable"},
    "CN": {"nom": "Nitrate de cellulose (celluloïd)", "formule": "variable"},
    "CP": {"nom": "Propionate de cellulose", "formule": "variable"},
    "CTA": {"nom": "Triacétate de cellulose", "formule": "variable"},
    "EC": {"nom": "Ethylcellulose", "formule": "variable"},
    "MC": {"nom": "Méthylcellulose", "formule": "variable"},
    "PVAC": {"nom": "Polyacétate de vinyle", "formule": "(C4H6O2)n"},
    "PVAL": {"nom": "Polyalcool vinylique", "formule": "(C2H4O)n"},
    "PVB": {"nom": "Polybutyral de vinyle", "formule": "variable"},
    "PVC/VAC": {"nom": "Copolymère PVC/VAC", "formule": "variable"},
    "PVFM": {"nom": "Polyformal de vinyle", "formule": "variable"},
    "A/MMA": {"nom": "Copolymère acrylonitrile/méthacrylate de méthyle", "formule": "variable"},
    "MBS": {"nom": "Copolymère méthacrylate de méthyle/acrylonitrile/styrène", "formule": "variable"},
    "NBR": {"nom": "Copolymère acrylonitrile/butadiène", "formule": "variable"},
    "PAN": {"nom": "Polyacrylonitrile", "formule": "(C3H3N)n"},
    "SAN": {"nom": "Copolymère styrène/acrylonitrile", "formule": "variable"},
    "PA6-3T": {"nom": "Polyamide semi-aromatique (Trogamid)", "formule": "variable"},
    "PAA": {"nom": "Polyarylamides (Ixef)", "formule": "variable"},
    "PPA": {"nom": "Polyphtalamides (Amodel)", "formule": "variable"},
    "PC": {"nom": "Polycarbonate", "formule": "(C16H14O3)n"},
    "PVC": {"nom": "Polychlorure de vinyle", "formule": "(C2H3Cl)n"},
    "PVC/A": {"nom": "Copolymère chlorure de vinyle/acrylate", "formule": "variable"},
    "PVC/ABS": {"nom": "Mélange PVC/ABS", "formule": "variable"},
    "PVC/AC": {"nom": "Copolymère chlorure de vinyle/acétate de vinyle", "formule": "variable"},
    "PVCC": {"nom": "Polychlorure de vinyle surchloré", "formule": "variable"},
    "PVC/E": {"nom": "Mélange PVC/polyéthylène chloré", "formule": "variable"},
    "PVDC": {"nom": "Polychlorure de vinylidène", "formule": "(C2H2Cl2)n"},
    "VC/P": {"nom": "Copolymère chlorure de vinyle/propylène", "formule": "variable"},
    "PET": {"nom": "Polyéthylène téréphtalate", "formule": "(C10H8O4)n"},
    "PAI": {"nom": "Polyamide-imide (Torlon)", "formule": "variable"},
    "PAR": {"nom": "Polytéréphtalate de bisphénol A", "formule": "variable"},
    "PEEK": {"nom": "Polyétheréthercétone", "formule": "variable"},
    "PEI": {"nom": "Polyétherimide", "formule": "variable"},
    "PEK": {"nom": "Polyéthercétone", "formule": "variable"},
    "PES": {"nom": "Polyéther sulfone", "formule": "variable"},
    "PI": {"nom": "Polypyromellitimide (Kapton)", "formule": "variable"},
    "PPE": {"nom": "Polyphénylène éther", "formule": "variable"},
    "PPS": {"nom": "Polysulfure de phénylène", "formule": "variable"},
    "PSU": {"nom": "Polysulfone", "formule": "variable"},
    "TPI": {"nom": "Polyimide thermoplastique", "formule": "variable"},
    "ETFE": {"nom": "Copolymère éthylène-tétrafluoroéthylène", "formule": "variable"},
    "FEP": {"nom": "Poly(éthylène-propylène) perfluoré", "formule": "variable"},
    "PCTFE": {"nom": "Polychlorotrifluoroéthylène", "formule": "variable"},
    "PVDF": {"nom": "Polyfluorure de vinylidène", "formule": "(C2H2F2)n"},
    "PE": {"nom": "Polyéthylène", "formule": "(C2H4)n"},
    "PP": {"nom": "Polypropylène", "formule": "(C3H6)n"},
    "PP-C": {"nom": "Polypropylène copolymère", "formule": "variable"},
    "PP-H": {"nom": "Polypropylène homopolymère", "formule": "variable"},
    "P-IB": {"nom": "Polyisobutylène", "formule": "(C4H8)n"},
    "P-MP": {"nom": "Polyméthylpentène", "formule": "variable"},
    "PE UHMW": {"nom": "Polyéthylène ultra-haute masse molaire", "formule": "variable"},
    "POM": {"nom": "Polyoxyméthylène", "formule": "(CH2O)n"},
    "PESU": {"nom": "Polyéthersulfone", "formule": "variable"},
    "PPSU": {"nom": "Polyphénylsulfone", "formule": "variable"},
    "PUR": {"nom": "Polyuréthanne", "formule": "variable"},
    "TDI": {"nom": "Toluène diisocyanate", "formule": "C9H6N2O2"},
    "MDI": {"nom": "Méthylène-bis 4 phénylisocyanate", "formule": "C15H10N2O2"},
    "MDA": {"nom": "Méthylène dianiline", "formule": "C13H14N2"},
    "MOCA": {"nom": "Méthylène bis orthochloroaniline", "formule": "C13H12Cl2N2"},
    "ASA": {"nom": "Acrylonitrile styrène acrylate", "formule": "variable"},
    "mSMA": {"nom": "Polystyrène-anhydride maléique modifié", "formule": "variable"},
    "PC/ABS": {"nom": "Alliage polycarbonate/ABS", "formule": "variable"},
    "PS": {"nom": "Polystyrène", "formule": "(C8H8)n"},
    "PS/PE": {"nom": "Mélange polystyrène/polyéthylène", "formule": "variable"},
    "PS/PP": {"nom": "Mélange polystyrène/polypropylène", "formule": "variable"},
    "PS/PPE": {"nom": "Alliage polystyrène/polyphénylène éther (Noryl)", "formule": "variable"},
    "PSE": {"nom": "Polystyrène expansible", "formule": "variable"},
    "SB": {"nom": "Polystyrène-choc", "formule": "variable"},
    "MBS": {"nom": "Terpolymère méthacrylate, butadiène, styrène", "formule": "variable"}
      
    # Tu peux ajouter les autres ici…
}

# Champ de saisie
acronym = st.text_input("Entrez un acronyme de polymère (ex : PET, PVC, PMMA)").upper()

# Détection et couleur dynamique
is_known = acronym in polymer_data if acronym else None

# Couleur dynamique
if is_known is not None:
    color = "#28a745" if is_known else "#dc3545"  # vert ou rouge
    st.markdown(f"""
        <style>
        div[data-testid="stTextInput"] > div > input {{
            border: 2px solid {color};
            border-radius: 5px;
        }}
        </style>
    """, unsafe_allow_html=True)

# Affichage des résultats
if acronym:
    if acronym in polymer_data:
        st.subheader("Nom complet")
        st.write(polymer_data[acronym]["nom"])

        st.subheader("Formule chimique")
        st.latex(polymer_data[acronym]["formule"])
    else:
        st.error("Acronyme non trouvé. Essayez un autre.")
