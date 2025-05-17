import json
import re

def converter_para_dict(json_string):

    limpo = json_string.strip()
    if limpo.startswith("```json"):
        limpo = limpo[len("```json"):].strip()
    if limpo.endswith("```"):
        limpo = limpo[:-3].strip()
    
    limpo_corrigido = re.sub(r"(?<!\\)'", '"', limpo)
    
    try:
        return json.loads(limpo_corrigido)
    except json.JSONDecodeError as e:
        print("error converte: ", e)
        return None
