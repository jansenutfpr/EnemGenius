<p align="center">
  <img src="https://github.com/taiaraujo/EnemGenius/blob/main/img/logo-eg-final.png" alt="EnemGenius Logo" width="200"> 
  <h3 align="center">Preparação Inteligente e Divertida para o Enem! 🧞‍♂️📚</h3>
</p>

<p align="center">
  Planejamento, dicas e macetes para o Enem? <b>Temos!</b> Sistema de Multi Agentes Expecialistas em todas as Áreas? <b>Temos também!</b> 
  <b> EnemGenius é seu companheiro de jornada rumo ao sucesso acadêmico. 🎯</b>
</p>

----

<p align="center">
  <a href="https://taia-araujo.gitbook.io/enemgenius/">
    <img src="https://img.shields.io/badge/Documenta%C3%A7%C3%A3o%20(GitBook)-blue?style=for-the-badge" alt="Documentação (GitBook)">
  </a>
  &nbsp;
  <a href="https://enemgenius-uwavzs9ha5zvg46teys76y.streamlit.app/">
    <img src="https://img.shields.io/badge/Acesse%20o%20App%20Online-success?style=for-the-badge" alt="Acesse o App Online">
  </a>
  &nbsp;
  <a href="https://colab.research.google.com/github/taiaraujo/EnemGenius/blob/main/prototipo/EnemGenius_Prototipo.ipynb">
    <img src="https://img.shields.io/badge/Prot%C3%B3tipo%20(Google%20Colab)-orange?style=for-the-badge" alt="Protótipo (Google Colab)">
  </a>
  &nbsp;
  <a href="https://taia-araujo.gitbook.io/enemgenius/parte-tecnica/manual-do-usuario">
    <img src="https://img.shields.io/badge/Rodar%20Local%20(Passo%20a%20passo)-brightgreen?style=for-the-badge" alt="Rodar Local (Passo a passo)">
  </a>
</p>

----

### O Que É o EnemGenius? 🧠💡

O EnemGenius é um projeto incrível feito pra ajudar estudantes do ensino médio a se prepararem para o ENEM com a ajuda de professores inteligentes, divertidos e especialistas — todos powered by inteligência artificial! 🤖📘

### Por Que Criamos o EnemGenius? 🤔

Este projeto nasceu da Imersão Alura! 🧑‍💻👩‍💻 A ideia é criar algo que realmente fizesse a diferença na vida dos estudantes, tornando a preparação para o Enem mais organizada e menos estressante. Pois estamos falando de uma longa jornada, e o EnemGenius está aqui para ser seu guia! 🗺️

### O Problema Que Resolvemos 🎯

Preparar para o Enem é um desafio ENORME!  Muitos estudantes se sentem perdidos com a quantidade de conteúdo, a falta de organização e o estresse da prova. O EnemGenius veio para:

* **Organizar seus estudos:** Cronogramas personalizados e planos de estudo que cabem na sua rotina. 📅
* **Dar aquele empurrãozinho:** Dicas, macetes e motivação para você não desanimar. 🚀
* **Simplificar o complexo:** Conteúdo didático e fácil de entender, sem enrolação. 🤓

----

### Como o EnemGenius Funciona? ⚙️

<p align="center">
  <img src="https://github.com/taiaraujo/EnemGenius/blob/main/img/fluxoEnemGenius.png" alt="EnemGenius Fluxo" width="900">
</p>

Você irá interagir com o EnemGenius pelo front-end do projeto. Ele é uma tela onde solicita que você forneça informações sobre a disciplina e o tema que você deseja estudar.! 🧞‍♀️✨

1.  **Informe a disciplina:** O campo não é obrigatório, mas ajuda os nossos agentes nas buscas de suas respostas.
2.  **Informe o tema:** Aqui você pode enviar um tema amplo como `era vargas`, uma pergunta, um tema bem especifico, ou não enviar nada. Os agentes vão sempre buscar a melhor resposta em todos os cenários. **MAS ATENÇÃO** quando mais específico o tema, melhor a resposta ☺️.
3.  **O agente auxiliar:** Ele recebe a sua resposta, entende o que o aluno está pedido, ou seja identifica a disciplina e para qual agente deve encaminhar, caso o aluno não tenha passado nenhuma informação, o agente auxiliar pede ao agente redator formular um resposta explicando os detalhes da prova em si.
4.  **Os agente professor:** São especialistas em suas áreas, temos um professor para cada área abordada no Enem - Ciências Humanas e suas Tecnologias, Ciências da Natureza e suas Tecnologias, Linguagens, Códigos e suas Tecnologias, e Matemática e suas Tecnologias. Esses agentes vão oferecer a resposta mais completa e recheada de dicas para os alunos.
5.  **Os agente revisor:** Ele traduz para uma linguagem simples e divertida a resposta do professor, além de pedir para o **agente validador** verificar se os links encaminhados estão funcionando corretamente.
6.  **Resposta do Enem Genius:** Ela sempre vem bem estrutura, com uma introdução, um explicação detalhada, sugestão de cronograma de estudos, dicas macetes e link! Todo o arcenal para você ficar prepardo(a) 🥳

----

### Demonstração de uso

Para uma demonstração mais detalhada da aplicação, você pode assistir ao vídeo no YouTube:

<div align="center">
<a href="https://www.youtube.com/watch?v=GvZxxS05dgo">
<img src="https://github.com/taiaraujo/EnemGenius/blob/main/img/tela-eg.jpg" alt="Demonstração em Vídeo" width="900" />
</a>
</div>

----

### O EnemGenius e suas versões 🛠️

* **Protótipo no Google Colab:** Foi aqui que tudo começou!  Nosso laboratório de ideias e testes. 🧪
    <a href="caminho/para/o/seu/prototipo.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

* **App Online (Streamlit):** A versão que você pode acessar de qualquer lugar!  Fácil, prático e pronto para te ajudar. 💻📱
    <a href="https://enemgenius-uwavzs9ha5zvg46teys76y.streamlit.app/">Acesse aqui!</a>

* **Código Local:** Para os mais curiosos e para quem quer personalizar ainda mais a ferramenta!  Baixe e explore! 📂

----

### Tecnologias Utilizadas 💻

* **Google Cloud Vertex AI:**
    * `google-genai`: Para acessar os modelos de IA do Google Gemini.
    * `google-cloud-aiplatform`: Para criar e gerenciar os agentes de IA.
* **Python:** Versão 3.10 ou superior
* **Streamlit:** Para a interface do usuário.

----

### Passo a passo para rodar localmente

-   Você precisa ter o Python 3 instalado na sua máquina.
-   Instale as bibliotecas do `requirements.txt`:

    ```bash
    pip3 install -r requirements.txt
    ```
-   Obtenha uma chave de API do Google e adicione-a ao seu projeto.
-   Execução do código: O front-end do projeto utiliza a biblioteca Streamlit, e é ela que iniciamos para rodar o projeto.

    ```bash
    python3 streamlit run interface.py
    ```
----

### Próximos Passos 🚀

O EnemGenius está só começando!  Nossas ideias para o futuro incluem:

* **Simulados personalizados:** Para você testar seus conhecimentos e ver onde precisa melhorar. 📝
* **Comunidade de estudos:** Um espaço para trocar ideias, tirar dúvidas e motivar uns aos outros. 🤝
* **Integração com outras ferramentas:** Para tornar sua preparação ainda mais completa. 🔗
---- 

### Contribua! 💖

Quer fazer parte dessa jornada?  Sua contribuição é muito bem-vinda!  Seja com ideias, código ou divulgação, vamos juntos transformar a preparação para o Enem!

----

### Agradecimentos 🙏

Agradeço à Alura e à Imersão por proporcionar essa experiência incrível! E um agradecimento especial a minha sobrinha Ana Victória (que vai fazer enem esse ano👏) e a todos os estudantes que me inspiram a criar o EnemGenius.
