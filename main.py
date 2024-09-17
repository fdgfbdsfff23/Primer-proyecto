meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL",
    "GHOSTEAR": "Terminar la comunicación con alguien sin explicación, ignorando mensajes o llamadas",
    "SIMP": "Una persona que muestra un interés excesivo y obvio por alguien, a menudo con la intención de ganarse su favor romántico.",
    "NO CAP": "Usado para decir que algo es verdadero"
}

for _ in range(3):
    word = input("Escribe una palabra moderna que no entiendas (¡utiliza mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")
