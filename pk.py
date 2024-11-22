import streamlit as st
import numpy as np

def Tran_OC(VO, IO, WO):
    """
    Calculates the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements.

    Args:
        VO: Open circuit voltage (V)
        IO: Open circuit current (A)
        WO: Open circuit power (W)

    Returns:
        A tuple containing R0 and X0
    """

    NPF = WO / (VO * IO)
    I = IO * np.sqrt(1 - NPF**2)
    Iw = IO * NPF
    R0 = VO / Iw
    X0 = VO / I

    return R0, X0

def main():
    st.title("2205A21031-PS7")
    st.write("Calculate the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements")

    # Create two columns for input and output
    col1, col2 = st.columns(2)

    # Input fields in the left column
    with col1:
        VO = st.number_input("Enter Open Circuit Voltage (V)", value=100.0)
        IO = st.number_input("Enter Open Circuit Current (A)", value=100.0)  # Set IO to 100
        WO = st.number_input("Enter Open Circuit Power (W)", value=100.0)

    # Compute button and output in the right column
    with col2:
        if st.button("Compute"):
            # Calculate R0 and X0
            R0, X0 = Tran_OC(VO, IO, WO)

            # Display results
            st.write("R0 =", round(R0, 2), "ohms")
            st.write("X0 =", round(X0, 2), "ohms")

if __name__ == "__main__":
    main()