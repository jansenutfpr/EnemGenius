from agentes import (agente_auxiliar, agente_chs, agente_cnt, agente_ltc, agente_mt, agente_revisor)
from utils import converter_para_dict

def executar_enem_assistant(disciplina, tema):

    if not disciplina and not tema:
        resposta_exp = "traga informações atualizadas sobre a prova do enem"
        tema = "prova enem"
        print("entrou no not disciplina and not tema")
    else:
        resposta_aux = agente_auxiliar(disciplina, tema)
        dict_pedido = converter_para_dict(resposta_aux)

        if not dict_pedido:
            resposta_exp = "traga informações atualizadas sobre a prova do enem"
            tema = "prova enem"
            print("entrou no not dict_pedido")
            print(resposta_aux)
            print("dict_pedido", dict_pedido)
        else:
            agente_nome = dict_pedido.get("nome_do_agente")
            disciplina = dict_pedido.get("disciplina")
            tema = dict_pedido.get("tema")

            agentes = {
                "agente_ltc": agente_ltc,
                "agente_chs": agente_chs,
                "agente_cnt": agente_cnt,
                "agente_mt": agente_mt
            }

            funcao_agente = agentes.get(agente_nome)
            if funcao_agente:
                resposta_exp = funcao_agente(disciplina, tema)
            else:
                resposta_exp = "traga informações atualizadas sobre a prova do enem"
                print("entrou no else onde não encontrou a funcao_agente")
        
    return agente_revisor(tema, resposta_exp)