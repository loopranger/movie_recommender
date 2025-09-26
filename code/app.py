# %%

import streamlit as st
from helper_funcs import get_movies_from_plot

st.set_page_config(page_title="Movie Info Finder", layout="centered")
st.title("Movie Info Finder")

st.write("Beschreibe die Handlung des Films:")
plot = st.text_area("Handlung eingeben", height=150)

if st.button("Suche Film"):
	if plot.strip():
		with st.spinner("Suche läuft..."):
			result = get_movies_from_plot(plot)
		if "error" in result:
			st.error(f"Fehler: {result['error']}")
		elif result["total_movies"] == 0:
			st.warning("Keine Filme gefunden.")
		else:
			for movie in result["movies"]:
				st.subheader(movie["title"])
				st.markdown(f"**Jahr:** {movie['release_year']}")
				st.markdown(f"**Regisseur:** {movie['director']}")
				st.markdown(f"**Hauptcharaktere:** {movie['main_characters']}")
				st.markdown("---")
	else:
		st.info("Bitte gib eine Handlung ein.")
