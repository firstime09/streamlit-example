import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def app():
    st.title('Leaf Diseases Detection')
    st.markdown(
        """
            In this case, we build the Machine Learning Model using two types
            of leaf diseases which are spot and blight. Details from the code
            and methods can be read in my publication list on Google Scholar
            about `Leaf Diseases Segmentation`.
        """)

    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,
                                                        random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)