from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.tools import google_search
from config import MODEL_ID, INSTRUCTION_BASE, RESPONSE_STRUCTURE

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def executar_agente(agent: Agent, message_text: str) -> str:
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

def criar_agente_professor(nome, descricao, caracteristicas):
    instruction = INSTRUCTION_BASE + caracteristicas + RESPONSE_STRUCTURE
    return Agent(
        name=nome,
        model=MODEL_ID,
        description=descricao,
        tools=[google_search],
        instruction=instruction
    )

def agente_ltc(disciplina, tema):
    caracteristicas = """
    Características específicas de Linguagens, Códigos e suas Tecnologias:
    - Domínio em leitura, interpretação de textos, gramática, literatura, artes e tecnologias da comunicação.
    - Utilização de exemplos práticos e dicas relevantes para a prova de Linguagens e Códigos do ENEM.
    - Ênfase no uso ético e responsável da tecnologia."""

    agente = criar_agente_professor(
        nome="agente_ltc",
        descricao="Agente especializado em Linguagens, Códigos e suas Tecnologias",
        caracteristicas=caracteristicas
    )
    return executar_agente(agente, f"Disciplina:{disciplina}, tema: {tema}")

def agente_chs(disciplina, tema):
    caracteristicas = """
    Características específicas de Ciências Humanas e suas Tecnologias:
    - Conhecimento abrangente em História, Geografia, Filosofia, Sociologia e conhecimentos interdisciplinares.
    - Utilização de análises relevantes e exemplos do cotidiano.
    - Incentivo à reflexão crítica sobre as questões sociais, políticas e culturais.
    - Ênfase na relevância para a compreensão do mundo e para o desenvolvimento do pensamento crítico.
    - Foco na análise de textos, mapas, gráficos e obras de arte.
    - Contextualização dos temas com o contexto histórico, social, político e econômico, promovendo uma visão ampla e crítica.
    """

    agente = criar_agente_professor(
        nome="agente_chs",
        descricao="Agente especializado em Ciências Humanas",
        caracteristicas=caracteristicas
    )
    return executar_agente(agente, f"Disciplina:{disciplina}, tema: {tema}")

def agente_cnt(disciplina, tema):
    caracteristicas = """
    Características específicas de Ciências da Natureza e suas Tecnologias:
    - Conhecimento abrangente em Biologia, Física, Química e conhecimentos interdisciplinares.
    - Utilização de experimentos relevantes e exemplos do cotidiano.
    - Incentivo à investigação científica e ao raciocínio lógico.
    - Ênfase na relevância para a compreensão do mundo natural e para o desenvolvimento de soluções para problemas reais.
    - Foco na interpretação de gráficos, tabelas e dados experimentais.
    - Abordagem Experimental: Enfatize a importância do método científico, da experimentação e da observação na construção do conhecimento científico.
    """

    agente = criar_agente_professor(
        nome="agente_cnt",
        descricao="Agente especializado em Ciências da Natureza",
        caracteristicas=caracteristicas
    )
    return executar_agente(agente, f"Disciplina:{disciplina}, tema: {tema}")

def agente_mt(disciplina, tema):
    caracteristicas = """
    Características específicas de Matemática e suas Tecnologias:
    - Conhecimento em Álgebra, Geometria, Estatística, Probabilidade e conhecimentos interdisciplinares.
    - Utilização de analogias, exemplos do cotidiano e representações visuais para facilitar a compreensão.
    - Incentivo ao raciocínio lógico e à resolução de problemas.
    - Ênfase na relevância para o desenvolvimento do pensamento lógico, resolução de problemas e tomada de decisões.
    - Foco na interpretação de gráficos, tabelas e modelagem matemática.
    - Abordagem Prática: Enfatize a importância da prática, da resolução de exercícios e da aplicação da matemática em situações reais.
    """

    agente = criar_agente_professor(
        nome="agente_mt",
        descricao="Agente especializado em Matemática",
        caracteristicas=caracteristicas
    )
    return executar_agente(agente, f"Disciplina:{disciplina}, tema: {tema}")


def agente_auxiliar(disciplina, tema):
    instruction = '''
    Você é um assistente pessoal do estudante, sua missão é entender ou encaminhar a solicitação do estudante para um dos agentes especialistas, de acordo com a necessidade dele.
    O que significa:
    - caso o aluno informe a disciplina e o tema, você irá identificar o agente correspondente e retorna a resposta, sem muito processamento.
    - caso o aluno informe apenas o tema, você irá identificar a disciplina utilizando a ferramente de pesquisa google_search e o agente que deve ser executado e retorna a resposta.
    - caso o aluno informe apenas a disciplina, você irá identificar o agente e o tema será montar um cronogramada de estudo para a disciplina até o dia da prova.

    Estrutura da Resposta:
    1. você retornará APENAS um objeto, com chave e valor, onde as chaves serão: nome_do_agente, disciplina, tema.
    2. você irá identificar a area de acordo com a disciplina, da seguinte forma:
    - Linguagens, Códigos e suas Tecnologias: [Língua Portuguesa, Literatura, Redação, Língua Estrangeira (Inglês ou Espanhol), Artes, Educação Física, Tecnologias da Informação e Comunicação]
    - Ciências Humanas e suas Tecnologias: [História, Geografia, Filosofia, Sociologia]
    - Ciências da Natureza e suas Tecnologias: [Química, Física, Biologia]
    - Matemática e suas Tecnologias:[Matemática]
    3. você irá identificar qual o agente certo de acordo com a area, da seguite forma:
    - Linguagens, Códigos e suas Tecnologias: agente_ltc
    - Ciências Humanas e suas Tecnologias: agente_chs
    - Ciências da Natureza e suas Tecnologias: agente_cnt
    - Matemática e suas Tecnologias: agente_mt

    Exemplos de resposta:
    - quando o aluno informa apenas disciplina, apenas o tema ou ambos:
    resposata: {"nome_do_agente": "agente_ltc", "disciplina": "literatura", 'tema': "barroco"}
    - quando o aluno informa apenas a disciplina:
    resposata: {"nome_do_agente": "agente_ltc", "disciplina": "literatura", 'tema': 'monte um cronograma de estudos desta discipliana até o dia da prova'}
    '''

    agente = Agent(
        name="agente_auxiliar",
        model=MODEL_ID,
        description="Agente responsável por encaminhar a solicitação ao agente correto",
        tools=[google_search],
        instruction=instruction
    )
    return executar_agente(agente, f"Disciplina:{disciplina}, tema:{tema}")

def agente_revisor(tema, resposta):
    instruction= '''
    Você é um assistente pessoal de um estudante do ensino médio que está se preparando para a prova do ENEM.
    Você deve revisar as respostas envidas pelos professores e traduzir para os jovens, para isso mantenha uma linguagem jovem,
    seja extrovertido, incentive os alunos.
    Você é responsavel por garantir que os links que os professores sugeriram estão online e funcionando corretamente, para isso
    valide os links utilizando a ferramenta (google_search).
    Para encerrar a conversa passe uma mensagem positiva e de boa sorte ao aluno.
    '''

    agente = Agent(
        name="agente_revisor",
        model=MODEL_ID,
        description="Agente responsável por revisar a resposta final",
        tools=[google_search],
        instruction=instruction
    )
    return executar_agente(agente, f"Tema: {tema}, resposta do Professor: {resposta}")


def agente_validador_url(resposta):

    resposta = agente_validador_url(response=resposta)

    caracteristicas_especificas = '''
    Você é um agente especializado em verificar e validar se uma páginas da web está com o conteúdo esperado. 
    Dado uma mensagem para você, sua missão é encontras os links dentro da mensagem, após encontrar o link sua tarefa 
    é acessar a página, ler e tentar resumir conteúdo, caso não consiga fazer o resumo esse link deve ser reescrito com 
    o caminho para a home da página analisada. Ao final você deve manter a resposta de acordo com a Estrutura da Resposta recebida.

    Exemplos:
    url encontrada que não teve o conteúdo entendido: [https://guiadoestudante.abril.com.br/estudar/exercicios/biologia/]
    url substituta: [https://guiadoestudante.abril.com.br/]
    '''

    instruction= caracteristicas_especificas+RESPONSE_STRUCTURE
    agente = Agent(
        name="agente_validador_url",
        model=MODEL_ID,
        description="Agente responsável por revisar a resposta final",
        tools=[google_search],
        instruction=instruction
    )
    return executar_agente(agente, resposta)

