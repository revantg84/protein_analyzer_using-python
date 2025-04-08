import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

# Dictionary of amino acid molecular weights
MOLECULAR_WEIGHTS = {
    'A': 71.08, 'R': 156.19, 'N': 114.11, 'D': 115.09, 'C': 103.15,
    'E': 129.12, 'Q': 128.14, 'G': 57.05, 'H': 137.14, 'I': 113.16,
    'L': 113.16, 'K': 128.18, 'M': 131.20, 'F': 147.18, 'P': 97.12,
    'S': 87.08, 'T': 101.11, 'W': 186.22, 'Y': 163.18, 'V': 99.13
}

# Hydrophobic amino acids (for simplicity)
HYDROPHOBIC_AA = {'A', 'V', 'I', 'L', 'M', 'F', 'W', 'Y'}


def analyze_protein_sequence(sequence):
    sequence = sequence.upper()
    if not all(aa in MOLECULAR_WEIGHTS for aa in sequence):
        return None, "Invalid characters found in the sequence."

    analysis = {}
    analysis['Length'] = len(sequence)

    # Amino acid composition
    aa_counts = Counter(sequence)
    analysis['Amino Acid Composition'] = dict(aa_counts)

    # Molecular weight
    total_weight = sum(MOLECULAR_WEIGHTS[aa] for aa in sequence)
    analysis['Molecular Weight'] = round(total_weight, 2)

    # Hydrophobic ratio
    hydrophobic_count = sum(1 for aa in sequence if aa in HYDROPHOBIC_AA)
    hydrophobic_ratio = hydrophobic_count / len(sequence) * 100
    analysis['Hydrophobic Ratio (%)'] = round(hydrophobic_ratio, 2)

    return analysis, None


def plot_composition(composition):
    labels = composition.keys()
    values = composition.values()

    fig, ax = plt.subplots()
    ax.bar(labels, values, color='skyblue')
    ax.set_title('Amino Acid Composition')
    ax.set_xlabel('Amino Acid')
    ax.set_ylabel('Count')
    st.pyplot(fig)


# Streamlit UI
st.set_page_config(page_title="Protein Analyzer", layout="centered")
st.title("🔬 Protein Sequence Analyzer")

st.markdown("Enter a protein sequence to analyze its properties.")

sequence_input = st.text_input("Enter Protein Sequence:", max_chars=1000)

if sequence_input:
    results, error = analyze_protein_sequence(sequence_input)

    if error:
        st.error(error)
    else:
        st.success("✅ Analysis Complete")
        st.write("### Results:")
        st.write(results)

        st.write("### Amino Acid Composition Graph:")
        plot_composition(results['Amino Acid Composition'])

        st.markdown("---")
        st.caption("Made with ❤️ using Streamlit")
