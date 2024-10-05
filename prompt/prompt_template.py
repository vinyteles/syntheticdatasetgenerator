generate_type_template = """
    Você é um classificador de documentos jurídicos, que responde apenas a classificação do documento sem nenhuma informação adicional. 
    Dado um documento, você analisa dois aspectos do documento:
     Tipo: Se o documento é do tipo "base", do tipo "revoga" ou do tipo "altera". 
     Doc_referencia: Se ele for "revoga" ou "altera", responda de maneira direta qual o número do documento que ele altera, se não pule a Etapa 2.
    
    Os tipos são descritos a seguir:
    base: documento que não revoga nem altera outro documento.
    altera: documento que altera outro documento.
    revoga: um documento que revoga outro documento.
    
    Dado o documento, retorne a saída no seguinte formato de tupla:
    (Tipo, Doc_referencia)
    
    NÃO COLOQUE NENHUMA PALAVRA ADICIONAL NA RESPOSTA, APENAS A TUPLA.
    
    ###### Documento: {text}
    ###### Resposta: 
    """

global_question_template = """
Você é um gerador de perguntas para um mecanismo de busca. Dado um conjunto de documentos, gere uma pergunta genérica em que aquele
documento seja a resposta.

### 

Exemplo:
Documento: RESOLVE deliberar que nenhum Conselheiro Relator autorizará a devolução de novos processos à origem, a pedido, se o órgão estiver com inadimplência de prazo junto a esta Corte, ficando ainda determinado que o atendimento aos adimplentes se dará exclusivamente através da Secretaria Geral deste Tribunal, que controlará rigorosamente o prazo estipulado.
Pergunta: Se o orgão estiver com inadimplência, o que os Conselheiros Relatores devem fazer?

####
Documento: {text}
Resposta: 
"""

answer_template = """
Você é um analista jurídico. Dado uma pergunta e um documento jurídico que auxilia a responder a pergunta, responda a pergunta.

Pergunta: {question}
Documento: {document}
Resposta: 

"""

summary_template = """
<|begin_of_text|>

    <|start_header_id|>system<|end_header_id|>
     Por favor, analise o seguinte texto jurídico e forneca um resumo conciso que destaque os principais pontos e argumentos.
O resumo deve ser claro e objetivo e conter apenas informações mais relevantes.
    <|eot_id|>

    <|start_header_id|>user<|end_header_id|>
    Documento: {text}
    Resumo: 
    <|eot_id|>"""