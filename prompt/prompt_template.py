persona_prompt = """ 
Você é um gerador de perguntas e respostas sobre temas relacionado a área juridica.
"""

system_prompt = """
{persona_prompt} 

Dado o contexto abaixo, gere uma pergunta direta e sucinta sobre o texto. Depois gere uma resposta desta pergunta.
Sua resposta deverá ser no formato: (<Pergunta>, <Contexto>, <Resposta>).

{Exemplo}
"""

example_prompt = """
Contexto: 
"""


user_prompt = """
Contexto: 
"""

prompt = """ 
## Persona
{persona_prompt}

## Prompt do Sistema
{system_prompt}

## Prompt do Usuário
{user_prompt}
"""