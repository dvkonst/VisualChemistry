from handlers import *

class Molecule:
    """Класс молекула

    Содержит информацию об одной молекуле, дублирует кусок SDF
    """
    
    header_list = []
    counts_line = []
    atom_block_list = []
    bond_block_list = []
    associated_data_dict = {}

    def get_atom_count(self):
        """Возвращает количество атомов в молекуле
        """
        return self.counts_line[0]
    def get_bond_count(self):
        """Возвращает количество связей в молекуле
        """
        return self.counts_line[1]

def extract_molecule_by_string(input_string):
    """Преобразует кусок sdf в класс Molecule

    Возвращает экземпляр класса
    """
    string_lines_list = input_string.splitlines()

    header_list = string_lines_list[:3]

    counts_line_string = string_lines_list[3].split() 
    counts_line = {int(value) for value in counts_line_string[:-1]}
    # последняя ячейка - текст 'V2000'
    counts_line.append(counts_line_string[-1])

    OutputMolecule = Molecule()
    OutputMolecule.header_list = header_list
    OutputMolecule.counts_line = counts_line

    atom_count = OutputMolecule.get_atom_count()
    atom_block_string_list = string_lines_list[4 : 4 + atom_count].split()
'''    atom_block = []
    for i in range(atom_count):
        for j in range(len(atom_block_string_list[i]):
            value = atom_block_string_list[i][j]
            try:
                value = float(value)
                atom_block[i][j] = value
            except:
                atom_block[i][j] = value
                continue   
'''
