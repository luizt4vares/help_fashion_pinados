import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
def consolidar_bases(*args, # objeto que recebe ids, caso vc queira determinar as abas
         path:str="", # localização da sua credencial
         id:str
         ):
    gs=gspread.oauth(credentials_filename=path)
    
    df_return = pd.DataFrame(columns=['count_items','validation','item_id','horário'])
    planilha = gs.open_by_key(id)
    sheets = planilha.worksheets()
    for aba in sheets:
        print(aba.title)
        dados = aba.get_all_values()
        df = pd.DataFrame(dados[1:],columns=dados[0])
        df_return=pd.concat([df_return,df])
    return df_return

    