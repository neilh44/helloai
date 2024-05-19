import streamlit as st
import backend  # Import the backend module

def main():
    st.title("Streamlit App with Backend")

    # Get user input using Streamlit components
    user_input = st.text_input("Enter your message:")

    # Process user input using a function from the backend module
    if st.button("Process"):
        response = backend.process_input(user_input)
        st.write("Response:", response)

if __name__ == "__main__":
    main()
  
