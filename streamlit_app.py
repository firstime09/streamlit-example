import streamlit as st
from demo_leafDiseases import ST_DEMO_LEAF
from demo_phishingLink import ST_DEMO_PHISHING
from streamlit.logger import get_logger

def main():
  st.set_page_config(page_title="| Home", page_icon="👋")
  st.write("# Summary")
  #st.sidebar.success("Select a demo above.")
  st.markdown(
        """
        I am a computer science lecturer at Universitas Bunda Mulia (UBM) with 5+ years of
        experience in teaching and research. The research topics I cover include Optimization,
        Image Processing, Expert Systems, Machine Learning, and Artificial Intelligence.
        The conclusions of all of my research are published in internationally accredited
        journals, national journals, or conferences and hope to be feedback for review,
        replicated, or applied in an organization. Some demo systems that have been created
        can be **viewed on the sidebar 👈**
        
        ### Whare you can find me?
        - in my publication [Google scholar](https://scholar.google.com/citations?user=LxbIO5sAAAAJ)
        - in my code documentation [Github](https://github.com/firstime09)
        - in my social media [LinkedIn](https://id.linkedin.com/in/felliks-feiters-tampinongkol-100084174)
        
        ### Under Maintenance    
        """
        )
  
  # with st.sidebar.selectbox(
  #   "My Prototipe list",
  #   ("---My List---","Leaf Disease", "Phishing link"))

  with st.sidebar:
    st.header('My Prototipe List')
    api_options = ('Leaf Diseases Detection', 'Phishing Link Detection')
    select_api = st.selectbox(label='Choose what you want to try:',
                              options=api_options)
  page_option = (list(ST_DEMO_LEAF.keys())
                 if select_api == 'Leaf Diseases Detection'
                 else list(ST_DEMO_PHISHING.keys()))
  selected_page = st.selectbox(options=page_option)

  demo = (ST_DEMO_PHISHING[selected_page]
          if select_api == 'Phishing Link Detection'
          else ST_DEMO_LEAF[selected_page])
  demo()

if __name__ == "__main__":
  main()