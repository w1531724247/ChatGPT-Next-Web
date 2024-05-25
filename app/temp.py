import requests
import json 

def list_all_model_ids(url: str):
  response = requests.get(url)
  if response.status_code == 200:
    models = response.json()
    return [model['id'] for model in models["data"]]
  else:
    raise Exception(f"Failed to get models. Status code: {response.status_code}")

if __name__ == "__main__":
    model_ids = list_all_model_ids('https://openrouter.ai/api/v1/models')
    mode_list = []
    for md_info in model_ids:
       md_name = md_info.split('/')[1]
       mode_list.append(md_name)
    print(json.dumps(mode_list))