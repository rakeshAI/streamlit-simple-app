import streamlit as st

#NLP pkgs
import spacy
from textblob import TextBlob



def text_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	
	tokens = [token.text for token in docx]
	allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
	return allData

def entity_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	tokens = [token.text  for token in docx]
	entities = [(entity.text,entity.label_) for entity in docx.ents]
	allData = ['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

 

#pkgs

def main():
	""" NLP APP with Streamlit"""
	st.title("NLPiffy with Streamlit")
	st.subheader("Natural Language Processing on the Go")

	# Tokenization
	if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize yout text")
		message = st.text_area("Enter your text","Tokenize here")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)


	# Named Entity
	if st.checkbox("Show Named Entities"):
		st.subheader("Extract Entities From your Text")
		message = st.text_area("Enter your text","Entity here")
		if st.button("Extract"):
			nlp_result = entity_analyzer(message)
			st.json(nlp_result)

	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Sentiment of your text")
		message = st.text_area("Enter your text","Analyze here")
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)
	# Text summarization
	if st.checkbox("Show Text Summerization"):
		st.subheader("Summarize your text")
		message = st.text_area("Enter your text","summarize here")
		summary_options = st.selectbox("Choice Your Summerizer",("gensim","sumy"))
		if st.button("Summarize"):
			if summary_options == 'gensim':
				st.text("Using Gensim..")




if __name__ == '__main__':
	main()