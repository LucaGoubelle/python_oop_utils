""" list utils class """

class ListUtils:
    """ list utils class """
    def __init__(self): pass

    def generate_empty_list(self, size:int, value=None) -> list:
        """ generate empty list """
        return [value for _ in range(size)]
    
    def generate_empty_square_matrix(self, size:int, value=None) -> list:
        """ generate empty square matrix """
        return [[value for _ in range(size)] for _ in range(size)]

    def reverse_list(self, list_target:list) -> list:
        """ reverse list """
        return list_target[::-1]
    
    def rotate_elements_left(self, list_target:list, nb_rotate:int) -> list:
        """  rotate elements to left by number of elements """
        list_final:list = list_target[nb_rotate:] + list_target[:nb_rotate]
        return list_final
    
    def rotate_elements_right(self, list_target:list, nb_rotate:int) -> list:
        """  rotate elements to right by number of elements """
        list_final:list = list_target[-nb_rotate:] + list_target[:-nb_rotate]
        return list_final
    
    def to_string(self, lst:list, delimiter:str) -> str:
        """ list to string """
        return delimiter.join(str(elem) for elem in lst)

