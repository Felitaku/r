meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ta":"termina con algo o deja de hacerlo o no te pases en joda",
            "XD":"en risa",
            "vo":"llamar la atencion de alguien para referirte a esa persona"}
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        significado = input("ingresa el significado de la palabra")
        meme_dict[word]=significado
