from analyzer.text_analyzer import(
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    longest_word,
    longest_sentences,
    longest_paragraph
)

text = """
Hola Mundo. Este texto es para analizar un programa de analisis de texto.

En este texto habra al menos 5 oraciones.

Un ejemplo de oracion es: las comillas se usan para delimitar el texto.
"""

print("Palabras: ", count_words(text))
print("Caracteres: ", count_characters(text))
print("Parrafos: ", count_paragraphs(text))
print("Oraciones: ", count_sentences(text))
print("Palabra mas larga: ",longest_word(text))
print("Oracion mas larga: ",longest_sentences(text))
print("Parrafo mas largo: ",longest_paragraph(text))