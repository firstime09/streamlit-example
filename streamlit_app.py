import streamlit as st
import inspect
import textwrap

from demo_leafDiseases import ST_DEMO_LEAF
from demo_phishingLink import ST_DEMO_PHISHING


def main():
    st.title("Streamlit ECharts Demo")

    with st.sidebar:
        st.header("Configuration")
        api_options = ('Leaf Diseases Detection', 'Phishing Link Detection')
        selected_api = st.selectbox(
            label="Choose your preferred API:",
            options=api_options,
        )

        page_options = (
            list(ST_DEMO_PHISHING.keys())
            if selected_api == 'Phishing Link Detection'
            else list(ST_DEMO_LEAF.keys())
        )
        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )
        demo, url = (
            ST_DEMO_LEAF[selected_page]
            if selected_api == 'Leaf Diseases Detection'
            else ST_DEMO_PHISHING[selected_page]
        )

        if selected_api == "Leaf Diseases Detection":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "Phishing Link Detection":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    demo()

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )