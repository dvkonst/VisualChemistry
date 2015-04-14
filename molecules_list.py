from molecule import *

class MoleculesList:
    """Список молекул
    """
    
    mol_list = []
    name = ''
    

def extract_molecules_list_from_sdf(file):
    """Преобразует sdf в класс MoleculeList

    Возвращет экземпляр класса 'Cписок молекул' по sdf. В случае ошибки возвращает None.
    """
    file_as_sring = file.read()
    molecules_count = file_as_string.count('$$$$')
    if molecules_count != 0:
        OutputClass = MoleculeList()
        string_list = file_as_string_list.split('$$$$', molecules_count)
        
        
        return OutputClass
    else:
        return None
