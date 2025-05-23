# Dados iniciais para gerar a pontuação
pontuacao = {
    "Sanguíneo": 0,
    "Colérico": 0,
    "Melancólico": 0,
    "Fleumático": 0
}

mapeamento = {
    "a": "Melancólico",
    "b": "Sanguíneo",
    "c": "Colérico",
    "d": "Fleumático"
}

# Lista de perguntas
perguntas = [
    {
        "pergunta": "Como você se sente ao participar de atividades em grupo?",
        "alternativas": {
            "a": "Fico mais confortável com tarefas individuais.",  # Melancólico
            "b": "Gosto de conversar e me divertir durante as atividades.",  # Sanguíneo
            "c": "Me sinto motivado a liderar ou tomar decisões.",  # Colérico
            "d": "Prefiro observar e colaborar de forma discreta."  # Fleumático
        }
    },
    {
        "pergunta": "Quando precisa começar uma nova tarefa, você:",
        "alternativas": {
            "a": "Analisa bem antes de dar o primeiro passo.",  # Melancólico
            "b": "Começa com entusiasmo, mesmo sem ter todos os detalhes.",  # Sanguíneo
            "c": "Toma a frente e inicia o trabalho imediatamente.",  # Colérico
            "d": "Espera instruções claras e começa com calma."  # Fleumático
        }
    },
    {
        "pergunta": "Quando você entra em uma nova turma na faculdade, sua reação mais comum é:",
        "alternativas": {
            "a": "Espero que o ambiente se acalme e só interajo se for necessário.",  # Melancólico
            "b": "Já puxo papo com alguém, adoro conhecer gente nova!",  # Sanguíneo
            "c": "Observo quem pode ser útil em trabalhos e começo a me aproximar estrategicamente.",  # Colérico
            "d": "Fico mais na minha, levo um tempo para me sentir à vontade."  # Fleumático
        }
    },
    {
        "pergunta": "Você está sobrecarregado com prazos e provas. Sua reação:",
        "alternativas": {
            "a": "Sente o peso das cobranças e fica ansioso com medo de não dar conta.",  # Melancólico
            "b": "Tenta relaxar vendo algo ou saindo com amigos, mesmo sabendo que deveria estudar.",  # Sanguíneo
            "c": "Organiza sua agenda e encara tudo com intensidade. Nada vai te parar.",  # Colérico
            "d": "Faz o possível, mas sem desespero. Acha que tudo se resolve com paciência."  # Fleumático
        }
    },
    {
        "pergunta": "Quando há uma discussão no grupo de estudos, você tende a:",
        "alternativas": {
            "a": "Fica desconfortável e evita se envolver, mas pensa muito sobre aquilo depois.",  # Melancólico
            "b": "Intervém tentando descontrair e mudar o assunto.",  # Sanguíneo
            "c": "Toma uma posição firme e tenta resolver de forma direta.",  # Colérico
            "d": "Escuta todos os lados e sugere um meio-termo para acalmar a situação."  # Fleumático
        }
    },
    {
        "pergunta": "Em uma apresentação de trabalho, você:",
        "alternativas": {
            "a": "Fica nervoso e ensaia bastante para se sentir seguro.",  # Melancólico
            "b": "Gosta de falar, se expressa com entusiasmo e até faz piadas.",  # Sanguíneo
            "c": "Usa a oportunidade para se destacar e impressionar.",  # Colérico
            "d": "Prefere falar por último ou deixar que outros apresentem."  # Fleumático
        }
    },
    {
        "pergunta": "Quando o professor é rude ao corrigir sua dúvida ou trabalho, você:",
        "alternativas": {
            "a": "Leva para o lado pessoal e fica remoendo a situação por dias.",  # Melancólico
            "b": "Fica indignado, comenta com os colegas, mas depois esquece o assunto.",  # Sanguíneo
            "c": "Responde na hora ou guarda aquilo como motivação para se superar.",  # Colérico
            "d": "Tenta entender o lado do professor e evita confrontos."  # Fleumático
        }
    },
    {
        "pergunta": "Quando pensa sobre seu futuro na carreira, você:",
        "alternativas": {
            "a": "Se preocupa com as incertezas e prefere caminhos mais seguros.",  # Melancólico
            "b": "Tem muitas ideias, mas nem sempre foca em uma só.",  # Sanguíneo
            "c": "Já tem metas claras e faz de tudo para atingi-las.",  # Colérico
            "d": "Vai deixando rolar e toma decisões com calma, conforme as coisas se mostram."  # Fleumático
        }
    },
    {
        "pergunta": "Em relação a mudanças inesperadas no conteúdo ou formato das aulas, você:",
        "alternativas": {
            "a": "Fica desconfortável, pois precisa de previsibilidade.",  # Melancólico
            "b": "Gosta, pois traz novidade.",  # Sanguíneo
            "c": "Se adapta rapidamente e assume o controle.",  # Colérico
            "d": "Aceita, mas prefere que não seja com frequência."  # Fleumático
        }
    },
    {
        "pergunta": "Quando você está em aula, o que mais chama sua atenção?",
        "alternativas": {
            "a": "A organização e a clareza do conteúdo.",  # Melancólico
            "b": "A dinâmica e o envolvimento com os colegas.",  # Sanguíneo
            "c": "Os desafios e a chance de se destacar.",  # Colérico
            "d": "Os detalhes e a profundidade dos temas abordados."  # Fleumático
        }
    },
    {
        "pergunta": "Quando um colega erra durante uma apresentação, você normalmente:",
        "alternativas": {
            "a": "Fica nervoso só de pensar que poderia ser você.",  # Melancólico
            "b": "Ri, mas depois tenta animá-lo.",  # Sanguíneo
            "c": "Corrige ou orienta na hora se puder.",  # Colérico
            "d": "Pensa em como pode ajudar sem chamar atenção."  # Fleumático
        }
    },
    {
        "pergunta": "Quando está em um projeto longo, você:",
        "alternativas": {
            "a": "Revisa tudo com cuidado para garantir perfeição.",  # Melancólico
            "b": "Se motiva com novidades no meio do caminho.",  # Sanguíneo
            "c": "Fica focado em alcançar os resultados.",  # Colérico
            "d": "Prefere manter o ritmo constante até o final."  # Fleumático
        }
    },
    {
        "pergunta": "Em um evento ou aula mais movimentada, você:",
        "alternativas": {
            "a": "Se sente sobrecarregado e prefere ambientes calmos.",  # Melancólico
            "b": "Interage, conversa e se diverte.",  # Sanguíneo
            "c": "Lidera ou organiza a atividade.",  # Colérico
            "d": "Observa, participa discretamente."  # Fleumático
        }
    },
    {
        "pergunta": "Como você se sente em atividades com prazos curtos e pressão?",
        "alternativas": {
            "a": "Fica estressado e teme não conseguir fazer perfeito.",  # Melancólico
            "b": "Se atrapalha um pouco, mas dá um jeito.",  # Sanguíneo
            "c": "Se motiva com o desafio e entrega rápido.",  # Colérico
            "d": "Trabalha bem, desde que tudo esteja organizado."  # Fleumático
        }
    },
    {
        "pergunta": "Um professor tem uma didática confusa e as aulas não fazem sentido. Você:",
        "alternativas": {
            "a": "Fica frustrado e tenta aprender tudo sozinho, mesmo que isso te desgaste.",  # Melancólico
            "b": "Reclama com os colegas e até ri da situação, tentando levar na esportiva.",  # Sanguíneo
            "c": "Vai direto falar com o professor ou coordenação para exigir uma solução.",  # Colérico
            "d": "Tolera a situação com paciência e evita conflitos, mesmo achando injusto."  # Fleumático
        }
    },
    {
        "pergunta": "Quando você estuda por conta porque não entendeu nada da aula, você:",
        "alternativas": {
            "a": "Sente que nunca está suficientemente preparado e fica inseguro para a prova.",  # Melancólico
            "b": "Procura um colega para estudar junto ou assistir um vídeo no YouTube, mas se distrai fácil.",  # Sanguíneo
            "c": "Cria seu próprio cronograma e vai atrás de outros materiais para dominar o conteúdo.",  # Colérico
            "d": "Estuda no seu ritmo, com tranquilidade, mesmo que o aprendizado leve mais tempo."  # Fleumático
        }
    },
    {
        "pergunta": "Como você se sente ao ser chamado para responder uma pergunta na frente da turma?",
        "alternativas": {
            "a": "Fico nervoso e penso muito no que vou dizer.",  # Melancólico
            "b": "Fico animado e respondo com naturalidade.",  # Sanguíneo
            "c": "Respondo com firmeza e gosto de mostrar que sei.",  # Colérico
            "d": "Respondo com calma, mesmo que não saiba tudo."  # Fleumático
        }
    },
    {
        "pergunta": "Ao receber uma nota abaixo da esperada, sua reação mais comum é:",
        "alternativas": {
            "a": "Fico frustrado e reflito onde errei.",  # Melancólico
            "b": "Levo na esportiva e digo que vou melhorar da próxima.",  # Sanguíneo
            "c": "Me irrito, mas uso isso como motivação para superar.",  # Colérico
            "d": "Aceito com tranquilidade e sigo em frente."  # Fleumático
        }
    },
    {
        "pergunta": "Quando o semestre começa, você costuma:",
        "alternativas": {
            "a": "Criar um plano de estudos detalhado desde o início.",  # Melancólico
            "b": "Se animar com as aulas e os colegas.",  # Sanguíneo
            "c": "Ficar motivado a se destacar em tudo.",  # Colérico
            "d": "Seguir o ritmo das aulas com calma e consistência."  # Fleumático
        }
    },
    {
        "pergunta": "Durante aulas longas, você geralmente:",
        "alternativas": {
            "a": "Sente cansaço mental, mesmo prestando atenção.",  # Melancólico
            "b": "Se concentra bem e mantém o foco até o fim.",  # Sanguíneo
            "c": "Se distrai com facilidade, mas tenta manter a atenção.",  # Colérico
            "d": "Mantém-se calmo e acompanha o conteúdo no seu tempo."  # Fleumático
        }
    }
]


# var para controlar o índice da pergunta atual
indice_pergunta = 0

# função que calcula o temperamento vencedor
def responder(alternativa):
    global indice_pergunta

    # atualizando a pontuação
    temperamento = mapeamento[alternativa]
    pontuacao[temperamento] += 1

    # avançando o índice
    indice_pergunta += 1

    if indice_pergunta < len(perguntas):
        # mostra a prox pergunta enquanto houver mais perguntas
        return perguntas[indice_pergunta]
    else:
        # calcula o resultado final ao chegar na última pergunta
        vencedor = max(pontuacao, key=pontuacao.get)
    
        # Mensagens personalizadas
        if vencedor == "Melancólico":
            mensagem = "Você é uma pessoa reflexiva, detalhista e dedicada. Seu senso de responsabilidade e busca pela perfeição são admiráveis. Lembre-se de ser gentil consigo mesmo e não se cobrar tanto. O mundo precisa da sua sensibilidade e profundidade!"
            
        elif vencedor == "Colérico":
            mensagem = "Você tem uma mente determinada, foco em resultados e muita energia para liderar e fazer acontecer. Sua proatividade é inspiradora! Só tome cuidado para não atropelar seus próprios limites — descansar também faz parte da vitória."
            
        elif vencedor == "Sanguíneo":
            mensagem = "Você é extrovertido, entusiasmado e cheio de energia! Sua facilidade em fazer amigos e contagiar os outros com seu bom humor é incrível. Continue espalhando alegria, mas não se esqueça de cuidar dos seus próprios projetos e focar quando for preciso."
            
        elif vencedor == "Fleumático":
            mensagem = "Você é calmo, diplomático e uma pessoa de paz. Seu jeito tranquilo traz equilíbrio por onde passa. Sua empatia e paciência são valiosas. Não se esqueça: sua voz também importa, e suas ideias merecem ser ouvidas."
            
        else:
            mensagem = "Não conseguimos determinar seu temperamento. Tente refazer o teste!"

        # Mostrando o resultado
        return f"Seu temperamento predominante é: {vencedor}\n\n{mensagem}"


# Loop para experimentar execução manual
print("\n--- Quiz dos Temperamentos ---\n")
pergunta_atual = perguntas[indice_pergunta]

while True:
    print(f"\n{pergunta_atual['pergunta']}")
    for letra, texto in pergunta_atual['alternativas'].items():
        print(f"{letra}) {texto}")

    resposta = input("\nDigite sua resposta (a, b, c ou d): ")

    resultado = responder(resposta)

    if isinstance(resultado, str):
        print("\n--- Resultado Final ---")
        print(resultado)
        break
    else:
        pergunta_atual = resultado