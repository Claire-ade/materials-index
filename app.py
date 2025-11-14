import streamlit as st

# Set up the page
st.set_page_config(page_title="Polymer Acronym Index", layout="centered")
st.title("🔍 Polymer Acronym Lookup")

# Dictionary of polymer acronyms
polymer_data = {
    "ABS": {
        "name": "Acrylonitrile Butadiene Styrene",
        "formula": "(C8H8·C4H6·C3H3N)n"
    },
    "PTFE": {
        "name": "Polytetrafluoroethylene",
        "formula": "(C2F4)n"
    },
    "PVC": {
        "name": "Polyvinyl Chloride",
        "formula": "(C2H3Cl)n"
    },
    "PET": {
        "name": "Polyethylene Terephthalate",
        "formula": "(C10H8O4)n"
    },
    "PMMA": {
        "name": "Polymethyl Methacrylate",
        "formula": "(C5O2H8)n"
    }
}

# Input field
acronym = st.text_input("Enter a polymer acronym (e.g. ABS, PTFE):").upper()

# Display results
if acronym:
    if acronym in polymer_data:
        st.subheader("Full Name")
        st.write(polymer_data[acronym]["name"])

        st.subheader("Chemical Formula")
        st.latex(polymer_data[acronym]["formula"])
    else:
        st.error("Acronym not found. Try another one.")
