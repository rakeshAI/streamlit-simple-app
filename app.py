import streamlit as st

#Header
st.title("streamlit tutorial")
st.header("This is a header")
st.subheader("This is a subheader")

#Text
st.text("Hello Streamlit")

#Markdown
st.markdown("### This is Markdown")


#Error/colorful
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error")

st.exception("NameError('name three not defined')")


#Get Info about python
st.help(range)

#writing text
st.write("Text with write")

st.write(range(10))


