import streamlit as st

st.set_page_config(page_title="Structure moléculaire", layout="centered")
st.set_page_config(page_title="Index des polymères", layout="centered")

# Supprimer l'encadré rouge par défaut sur le champ de saisie
st.markdown("""
    <style>
    div[data-testid="stTextInput"] > div > input {
        border: 1px solid #ccc !important;
        border-radius: 5px;
    }

    div[data-testid="stTextInput"] > div > input:focus {
        border: 1px solid #ccc !important;
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Recherche d'acronymes de polymères")

# Dictionnaire complet des acronymes
polymer_data = {
  "ABS": {"nom": "Acrylonitrile Butadiène Styrène", "formule": r"(C_8H_8 \cdot C_4H_6 \cdot C_3H_3N)_n"},
    "PTFE": {"nom": "Polytétrafluoroéthylène (Téflon)", "formule": r"(C_2F_4)_n"},
    "PBT": {"nom": "Polybutylène téréphtalate", "formule": r"(C_{12}H_{12}O_4)_n"},
    "PMMA": {"nom": "Polyméthacrylate de méthyle", "formule": r"(C_5O_2H_8)_n"},
    "CA": {"nom": "Acétate de cellulose", "formule": "variable"},
    "CAB": {"nom": "Acétobutyrate de cellulose", "formule": "variable"},
    "CAP": {"nom": "Acétoproprionate de cellulose", "formule": "variable"},
    "CN": {"nom": "Nitrate de cellulose (celluloïd)", "formule": "variable"},
    "CP": {"nom": "Propionate de cellulose", "formule": "variable"},
    "CTA": {"nom": "Triacétate de cellulose", "formule": "variable"},
    "EC": {"nom": "Ethylcellulose", "formule": "variable"},
    "MC": {"nom": "Méthylcellulose", "formule": "variable"},
    "PVAC": {"nom": "Polyacétate de vinyle", "formule": r"(C_4H_6O_2)_n"},
    "PVAL": {"nom": "Polyalcool vinylique", "formule": r"(C_2H_4O)_n"},
    "PVB": {"nom": "Polybutyral de vinyle", "formule": "variable"},
    "PVC/VAC": {"nom": "Copolymère PVC/VAC", "formule": "variable"},
    "PVFM": {"nom": "Polyformal de vinyle", "formule": "variable"},
    "A/MMA": {"nom": "Copolymère acrylonitrile/méthacrylate de méthyle", "formule": "variable"},
    "MBS": {"nom": "Copolymère méthacrylate de méthyle/acrylonitrile/styrène", "formule": "variable"},
    "NBR": {"nom": "Copolymère acrylonitrile/butadiène", "formule": "variable"},
    "PAN": {"nom": "Polyacrylonitrile", "formule": r"(C_3H_3N)_n"},
    "SAN": {"nom": "Copolymère styrène/acrylonitrile", "formule": "variable"},
    "PA6-3T": {"nom": "Polyamide semi-aromatique (Trogamid)", "formule": "variable"},
    "PAA": {"nom": "Polyarylamides (Ixef)", "formule": "variable"},
    "PPA": {"nom": "Polyphtalamides (Amodel)", "formule": "variable"},
    "PC": {"nom": "Polycarbonate", "formule": r"(C_{16}H_{14}O_3)_n", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Polycarbonate_PC.png/330px-Polycarbonate_PC.png"},
    "PVC": {"nom": "Polychlorure de vinyle", "formule": r"(C_2H_3Cl)_n"},
    "PVC/A": {"nom": "Copolymère chlorure de vinyle/acrylate", "formule": "variable"},
    "PVC/ABS": {"nom": "Mélange PVC/ABS", "formule": "variable"},
    "PVC/AC": {"nom": "Copolymère chlorure de vinyle/acétate de vinyle", "formule": "variable"},
    "PVCC": {"nom": "Polychlorure de vinyle surchloré", "formule": "variable"},
    "PVC/E": {"nom": "Mélange PVC/polyéthylène chloré", "formule": "variable"},
    "PVDC": {"nom": "Polychlorure de vinylidène", "formule": r"(C_2H_2Cl_2)_n"},
    "VC/P": {"nom": "Copolymère chlorure de vinyle/propylène", "formule": "variable"},
    "PET": {"nom": "Polyéthylène téréphtalate", "formule": r"(C_{10}H_{8}O_{4})_n"},
    "PAI": {"nom": "Polyamide-imide (Torlon)", "formule": r"[-CO-C_6H_4-CO-NH-C_6H_4-NH-]_n"},
    "PAR": {"nom": "Polytéréphtalate de bisphénol A", "formule": r"[-C(CH_3)_2-C_6H_4-C_6H_4-COO-]_n"},
    "PEEK": {"nom": "Polyétheréthercétone", "formule": r"[-C_6H_4-O-C_6H_4-O-C_6H_4-CO-]_n"},
    "PEI": {"nom": "Polyétherimide", "formule": r"[-C_6H_4-O-C_6H_4-CO-NH-C_6H_4-NH-CO-]_n"},
    "PEK": {"nom": "Polyéthercétone", "formule": r"[-C_6H_4-O-C_6H_4-CO-]_n"},
    "PES": {"nom": "Polyéther sulfone", "formule": r"[-C_6H_4-SO_2-C_6H_4-O-]_n"},
    "PI": {"nom": "Polypyromellitimide (Kapton)", "formule": r"[-C_6H_2(CO)_2-NH-C_6H_4-NH-]_n"},
    "PPE": {"nom": "Polyphénylène éther", "formule": r"[-C_6H_4-O-]_n"},
    "PPS": {"nom": "Polysulfure de phénylène", "formule": r"[-C_6H_4-S-]_n"},
    "PSU": {"nom": "Polysulfone", "formule": r"[-C_6H_4-SO_2-C_6H_4-O-]_n"},
    "TPI": {"nom": "Polyimide thermoplastique", "formule": r"[-C_6H_4-N(CO)-C_6H_4-CO-]_n"},
    "ETFE": {"nom": "Copolymère éthylène-tétrafluoroéthylène", "formule": r"[-CH_2-CH_2-CH_2-CF_4-]_n"},
    "FEP": {"nom": "Poly(éthylène-propylène) perfluoré", "formule": "variable"},
    "PCTFE": {"nom": "Polychlorotrifluoroéthylène", "formule": "variable"},
      "PVDF": {"nom": "Polyfluorure de vinylidène", "formule": r"(C_{2}H_{2}F_{2})_n"},
    "PE": {"nom": "Polyéthylène", "formule": r"(C_{2}H_{4})_n"},
    "PP": {"nom": "Polypropylène", "formule": r"(C_{3}H_{6})_n"},
    "PP-C": {"nom": "Polypropylène copolymère", "formule": "variable"},
    "PP-H": {"nom": "Polypropylène homopolymère", "formule": "variable"},
    "P-IB": {"nom": "Polyisobutylène", "formule": r"(C_{4}H_{8})_n"},
    "P-MP": {"nom": "Polyméthylpentène", "formule": "variable"},
    "PE UHMW": {"nom": "Polyéthylène ultra-haute masse molaire", "formule": "variable"},
    "POM": {"nom": "Polyoxyméthylène", "formule": r"(CH_{2}O)_n"},
    "PESU": {"nom": "Polyéthersulfone", "formule": "variable"},
    "PPSU": {"nom": "Polyphénylsulfone", "formule": "variable"},
    "PUR": {"nom": "Polyuréthanne", "formule": "variable"},
    "TDI": {"nom": "Toluène diisocyanate", "formule": r"C_{9}H_{6}N_{2}O_{2}"},
    "MDI": {"nom": "Méthylène-bis 4 phénylisocyanate", "formule": r"C_{15}H_{10}N_{2}O_{2}"},
    "MDA": {"nom": "Méthylène dianiline", "formule": r"C_{13}H_{14}N_{2}"},
    "MOCA": {"nom": "Méthylène bis orthochloroaniline", "formule": r"C_{13}H_{12}Cl_{2}N_{2}"},
    "ASA": {"nom": "Acrylonitrile styrène acrylate", "formule": "variable"},
    "mSMA": {"nom": "Polystyrène-anhydride maléique modifié", "formule": "variable"},
    "PC/ABS": {"nom": "Alliage polycarbonate/ABS", "formule": "variable"},
    "PS": {"nom": "Polystyrène", "formule": r"(C_{8}H_{8})_n"},
    "PS/PE": {"nom": "Mélange polystyrène/polyéthylène", "formule": "variable"},
    "PS/PP": {"nom": "Mélange polystyrène/polypropylène", "formule": "variable"},
    "PS/PPE": {"nom": "Alliage polystyrène/polyphénylène éther (Noryl)", "formule": "variable"},
    "PSE": {"nom": "Polystyrène expansible", "formule": "variable"},
    "SB": {"nom": "Polystyrène-choc", "formule": "variable"},
    "MBS": {"nom": "Terpolymère méthacrylate, butadiène, styrène", "formule": "variable"},
    "TPE": {"nom": "Elastomère thermoplastique", "formule": "variable"},
    "NR": {"nom": "Caoutchouc naturel (de 'natural rubber') ou Poly(isoprène)", "formule": r"CH_{2}C(CH_{3})CHCH_{2}", "image_url": "https://new.societechimiquedefrance.fr/wp-content/uploads/2019/12/arton318-1.png"},
    "SBR": {"nom": "Caoutchouc styrène-butadiène", "formule": r"C_{6}H_{5}CHCH_{2}(C_{4}H_{6})_{n}"},
      
    # Tu peux ajouter les autres ici…
}

# Champ de saisie
acronym = st.text_input("Entrez un acronyme de polymère (ex : PET, PVC, PMMA)").upper()
# Appliquer encadrement vert uniquement si reconnu
if acronym and acronym in polymer_data:
    st.markdown("""
        <style>
        div[data-testid="stTextInputRootElement"] > div > input {
            border: 2px solid #28a745;
            border-radius: 5px;
        }
        div[data-testid="stTextInputRootElement"] > div > input:focus {
            border: 2px solid #28a745;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

# Affichage des résultats
if acronym:
    if acronym in polymer_data:
        st.subheader("Nom complet")
        st.write(polymer_data[acronym]["nom"])
        st.subheader("Formule chimique")
        st.latex(polymer_data[acronym]["formule"])
        if "image_url" in polymer_data[acronym]:
            st.image(
            polymer_data[acronym]["image_url"],
            caption=f"Structure de {polymer_data[acronym]['nom']}",
            use_column_width=True
    )
    else:
        st.error("Acronyme non trouvé. Essayez un autre.")
