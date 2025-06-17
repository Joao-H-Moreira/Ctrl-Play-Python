def recomendar_musica(estado_emocional):
    links = {
        "triste": "https://www.youtube.com/watch?v=XB7CkZ__ajQ",  # Playlist para animar
        "raiva": "https://www.youtube.com/watch?v=fLexgOxsZu0",   # Músicas calmas para relaxar
        "ansiedade": "https://www.youtube.com/watch?v=VZ4WJr9dH1g",  # Sons para meditação
        "feliz": "https://www.youtube.com/watch?v=3GwjfUFyY6M",   # Celebration!
    }
    return links.get(estado_emocional.lower(), "Desculpe, ainda não tenho sugestões para esse sentimento.")

def responder_pergunta(pergunta):
    pergunta = pergunta.lower()

    if "capital do brasil" in pergunta:
        return "A capital do Brasil é Brasília."
    elif "presidente do brasil" in pergunta:
        return "O presidente do Brasil atualmente é o Luiz Inácio Lula da Silva."
    elif "maior estado do brasil" in pergunta:
        return "O maior estado do Brasil em território é o Amazonas."
    elif "obrigado" in pergunta:
        return "De nada! Sempre à disposição. 😊"
    elif "que horas são" in pergunta:
        from datetime import datetime
        return f"Agora são {datetime.now().strftime('%H:%M')}."
    else:
        return "Hmm... ainda estou aprendendo. Pode tentar perguntar de outra forma?"

def iniciar_chat():
    print("🤖 Chatbot: Oi! Como foi seu dia? (responda com: bom, triste, raiva, ansiedade, feliz...)")
    
    while True:
        usuario = input("Você: ").lower()

        if usuario == "sair":
            print("🤖 Chatbot: Até logo! Cuide-se! 💙")
            break

        # Emoções
        if usuario in ["triste", "raiva", "ansiedade", "feliz", "bom"]:
            link = recomendar_musica(usuario)
            print(f"🤖 Chatbot: Entendi que você está se sentindo {usuario}.")
            print(f"Aqui vai uma música que pode ajudar: {link}")
            print("Se quiser conversar mais ou fazer perguntas, estou aqui! 😉")
        # Perguntas gerais
        elif any(p in usuario for p in ["capital", "presidente", "estado", "horas", "obrigado"]):
            resposta = responder_pergunta(usuario)
            print("🤖 Chatbot:", resposta)
        # Caso genérico
        else:
            print("🤖 Chatbot: Não entendi muito bem... você pode me dizer como está se sentindo ou perguntar algo simples sobre o Brasil.")
            print("Ou digite 'sair' para encerrar.")

# Iniciar chatbot
iniciar_chat()
