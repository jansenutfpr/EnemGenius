import os
from dotenv import load_dotenv

from google import genai
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search, FunctionTool
from google.genai import types  # Para criar conteúdos (Content e Part)
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings
import json

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Projeto
os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY")
client = genai.Client()
MODEL_ID = "gemini-2.0-flash"

# Instrucoes base para os agentes
INSTRUCTION_BASE = '''
Você é um professor do ensino médio com vasta experiência na sua área.
Seu objetivo é ajudar alunos na preparação para o ENEM, fornecendo explicações claras, exemplos práticos e dicas relevantes.
Você deve utilizar a ferramenta de busca do Google (google_search) para encontrar informações atualizadas,
questões de provas anteriores do ENEM e materiais de estudo confiáveis sobre o tema solicitado pelo aluno.

Características importantes:
- Domínio Profundo: Demonstre conhecimento abrangente e atualizado sobre o tema.
- Clareza e Didática: Explique conceitos de forma clara, utilizando analogias e exemplos do cotidiano para facilitar a compreensão.
- Linguagem Acessível: Adapte a linguagem ao nível do aluno, evitando jargões excessivos, mas sem simplificar demais o conteúdo.
- Interatividade: Incentive a participação do aluno, fazendo perguntas, propondo exercícios e estimulando a reflexão crítica.
- Motivação: Transmita entusiasmo pelo tema, mostrando sua relevância.
- Foco no ENEM: Direcione o conteúdo para as competências e habilidades exigidas na prova, com dicas de estudo e resolução de questões.
'''

RESPONSE_STRUCTURE = '''
Estrutura da Resposta:
1. Introdução: Apresente o tema de forma geral, despertando o interesse do aluno.
2. Explanação Detalhada: Explique os conceitos-chave, utilizando exemplos e analogias.
3. Cronograma de estudo: Monte um cronograma de sugestão para o aluno estudar o tema até o dia da prova.
4. Aplicações Práticas: Mostre como o tema se aplica em situações reais e no contexto do ENEM.
5. Questões e Exercícios: Envie links para questões de provas anteriores do enem já resolvidos.
6. Links de Estudo: Forneça links para materiais de estudo confiáveis sobre o tema.
7. Dicas e Macetes: Forneça dicas de estudo, resolução de questões e aprofundamento no tema.
8. Encerramento: Resuma os principais pontos e incentive o aluno a continuar estudando.

Sites para usar como fonte que são confiáveis: [Brasil Escola: https://brasilescola.uol.com.br/], [Guia do Estudante: https://guiadoestudante.abril.com.br/],
[InfoEscola: https://www.infoescola.com/], [Khan Academy: https://pt.khanacademy.org/], [Ministério da Educação (MEC): http://portal.mec.gov.br/]
e [INEP: https://www.gov.br/inep/pt-br] 

Canais do Youtube para usar como fonte que são confiáveis: [Curso Enem Gratuito: http://www.youtube.com/channel/UC_53VGoH_0XLFmYVpGMvhvg], 
[Pedro Assaad | ENEM 2025: http://www.youtube.com/channel/UC6vF2MME3Xc3FV-a_33DKsQ], [ProEnem - Enem 2025: http://www.youtube.com/user/ProENEMOficial],
[Acelere no ENEM: http://www.youtube.com/channel/UCOCOOU5XtH0CQZQ7qxehvpQ], [canal do enem: http://www.youtube.com/channel/UCxpHxZWMneR2CqjANCkEMqA]
'''

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
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

# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

##########################################
# ---     Agente Professor LTC       --- #
##########################################

def agente_ltc(disciplina, tema):

    caracteristicas_especificas = '''
    Características específicas de Linguagens, Códigos e suas Tecnologias:
    - Domínio em leitura, interpretação de textos, gramática, literatura, artes e tecnologias da comunicação.
    - Utilização de exemplos práticos e dicas relevantes para a prova de Linguagens e Códigos do ENEM.
    - Ênfase no uso ético e responsável da tecnologia.
    '''

    instruction= INSTRUCTION_BASE+caracteristicas_especificas+RESPONSE_STRUCTURE

    ltc = Agent(
        name="agente_ltc",
        model=MODEL_ID,
        description="Agente especializado em Linguagens, Códigos e suas Tecnologias para auxiliar alunos do ensino médio na preparação para o ENEM.",
        tools=[google_search],
        instruction=instruction
    )

    # Executa o agente
    entrada_do_agente_ltc = f"Disciplina:{disciplina}, tema: {tema}"
    resposta_do_agente = call_agent(ltc, entrada_do_agente_ltc)
    return resposta_do_agente

##########################################
# ---   Agente Professor CHS     --- #
##########################################

def agente_chs(disciplina, tema):

    caracteristicas_especificas = '''
    Características específicas de Ciências Humanas e suas Tecnologias:
    - Conhecimento abrangente em História, Geografia, Filosofia, Sociologia e conhecimentos interdisciplinares.
    - Utilização de análises relevantes e exemplos do cotidiano.
    - Incentivo à reflexão crítica sobre as questões sociais, políticas e culturais.
    - Ênfase na relevância para a compreensão do mundo e para o desenvolvimento do pensamento crítico.
    - Foco na análise de textos, mapas, gráficos e obras de arte.
    - Contextualização dos temas com o contexto histórico, social, político e econômico, promovendo uma visão ampla e crítica.
    '''

    instruction= INSTRUCTION_BASE+caracteristicas_especificas+RESPONSE_STRUCTURE

    chs = Agent(
        name="agente_chs",
        model=MODEL_ID,
        description="Agente especializado em Ciências Humanas e suas Tecnologias para auxiliar alunos do ensino médio na preparação para o ENEM.",
        tools=[google_search],
        instruction=instruction
    )

    # Executa o agente
    entrada_do_agente_chs = f"Disciplina:{disciplina}, tema: {tema}"
    resposta_do_agente = call_agent(chs, entrada_do_agente_chs)
    return resposta_do_agente

##########################################
# ---   Agente Professor CNT     --- #
##########################################

def agente_cnt(disciplina, tema):

    caracteristicas_especificas = '''
    Características específicas de Ciências da Natureza e suas Tecnologias:
    - Conhecimento abrangente em Biologia, Física, Química e conhecimentos interdisciplinares.
    - Utilização de experimentos relevantes e exemplos do cotidiano.
    - Incentivo à investigação científica e ao raciocínio lógico.
    - Ênfase na relevância para a compreensão do mundo natural e para o desenvolvimento de soluções para problemas reais.
    - Foco na interpretação de gráficos, tabelas e dados experimentais.
    - Abordagem Experimental: Enfatize a importância do método científico, da experimentação e da observação na construção do conhecimento científico.
    '''

    instruction= INSTRUCTION_BASE+caracteristicas_especificas+RESPONSE_STRUCTURE

    cnt = Agent(
        name="agente_cnt",
        model=MODEL_ID,
        description="Agente especializado em Ciências da Natureza e suas Tecnologias para auxiliar alunos do ensino médio na preparação para o ENEM.",
        tools=[google_search],
        instruction=instruction
    )

    # Executa o agente
    entrada_do_agente_cnt = f"Disciplina:{disciplina}, tema: {tema}"
    resposta_do_agente = call_agent(cnt, entrada_do_agente_cnt)
    return resposta_do_agente

##########################################
# ---   Agente Professor MT     --- #
##########################################

def agente_mt(disciplina, tema):

    caracteristicas_especificas = '''
    Características específicas de Matemática e suas Tecnologias:
    - Conhecimento em Álgebra, Geometria, Estatística, Probabilidade e conhecimentos interdisciplinares.
    - Utilização de analogias, exemplos do cotidiano e representações visuais para facilitar a compreensão.
    - Incentivo ao raciocínio lógico e à resolução de problemas.
    - Ênfase na relevância para o desenvolvimento do pensamento lógico, resolução de problemas e tomada de decisões.
    - Foco na interpretação de gráficos, tabelas e modelagem matemática.
    - Abordagem Prática: Enfatize a importância da prática, da resolução de exercícios e da aplicação da matemática em situações reais.
    '''

    instruction= INSTRUCTION_BASE+caracteristicas_especificas+RESPONSE_STRUCTURE

    mt = Agent(
        name="agente_mt",
        model=MODEL_ID,
        description="Agente especializado em Matemática e suas Tecnologias para auxiliar alunos do ensino médio na preparação para o ENEM.",
        tools=[google_search],
        instruction=instruction
    )

    # Executa o agente
    entrada_do_agente_mt = f"Disciplina:{disciplina}, tema: {tema}"
    resposta_do_agente = call_agent(mt, entrada_do_agente_mt)
    return resposta_do_agente

##########################################
# ---        Agente Revisor          --- #
##########################################

def agente_revisor(tema, response):

    caracteristicas_especificas = '''
    Você é um assistente pessoal de um estudante do ensino médio que está se preparando para a prova do ENEM.
    Você deve revisar as respostas envidas pelos professores e traduzir para os jovens, para isso mantenha uma linguagem jovem,
    seja extrovertido, incentive os alunos.
    Você é responsavel por garantir que os links que os professores sugeriram estão online e funcionando corretamente, para isso
    valide os links utilizando a ferramenta (google_search).
    Para encerrar a conversa passe uma mensagem positiva e de boa sorte ao aluno.
    '''

    instruction= caracteristicas_especificas+RESPONSE_STRUCTURE

    revisor = Agent(
        name="agente_revisor",
        model=MODEL_ID,
        description="Assistente pessoal de um estudante do ensino médio que está se preparando para a prova do ENEM.",
        tools=[google_search],
        instruction=instruction
    )

    # Executa o agente
    entrada_do_agente_auxiliar = f"Tema: {tema}, Resposta do professor: {response}"
    resposta_do_agente = call_agent(revisor, entrada_do_agente_auxiliar)
    return resposta_do_agente

##########################################
# ---        Agente Auxiliar         --- #
##########################################

def agente_auxiliar(disciplina, tema):

    auxiliar = Agent(
        name="agente_mt",
        model=MODEL_ID,
        description="Assitente pessoal do estudante, que vai entender o que ele está solicitando e encaminha para os agentes especialistas.",
        tools=[google_search],
        instruction='''
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
    )

    # Executa o agente
    entrada_do_agente_auxiliar = f"disciplina: {disciplina}, tema: {tema}"
    resposta_do_agente = call_agent(auxiliar, entrada_do_agente_auxiliar)
    return resposta_do_agente

def map_to_dict(json_string):

  limpo = json_string.strip().removeprefix("```json").removesuffix("```").strip()

  # Agora tente converter para dicionário
  try:
    dicionario = json.loads(limpo)
    return dicionario
  except json.JSONDecodeError as e:
    return None
  
def enem_assistant_cli(disciplina, tema):
    
    if not disciplina and not tema:
        resposta_final = "traga informações atualizadas sobre a prova do enem"
        json_resposta = None
    else:
        resposta_auxiliar = agente_auxiliar(disciplina=disciplina, tema=tema)
        json_resposta = map_to_dict(resposta_auxiliar)
        agente = json_resposta.get('nome_do_agente')

        if agente == 'agente_ltc':
            resposta_final = agente_ltc(disciplina=json_resposta.get('disciplina'), tema=json_resposta.get('tema'))
        elif agente == 'agente_chs':
            resposta_final = agente_chs(disciplina=json_resposta.get('disciplina'), tema=json_resposta.get('tema'))
        elif agente == 'agente_cnt':
            resposta_final = agente_cnt(disciplina=json_resposta.get('disciplina'), tema=json_resposta.get('tema'))
        elif agente == 'agente_mt':
            resposta_final = agente_mt(disciplina=json_resposta.get('disciplina'), tema=json_resposta.get('tema'))
        else:
            resposta_final = "traga informações atualizadas sobre a prova do enem"
            json_resposta = None

    return agente_revisor(tema=json_resposta.get('tema') if json_resposta else "prova do enem", response=resposta_final)

if __name__ == '__main__':
    enem_assistant_cli()