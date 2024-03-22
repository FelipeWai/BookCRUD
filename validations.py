from exceptions import EmpityFieldsError, AnoNotIntError

def create_validation(nome_livro, nome_autor, ano_publicacao, nome_editora):
    if not all([nome_livro, nome_autor, ano_publicacao, nome_editora]):
        raise EmpityFieldsError("Todos os campos devem ser preenchidos")
    
    try:
        int_ano_publi = int(ano_publicacao)
    except ValueError:
        raise AnoNotIntError("O ano deve ser um numero inteiro")
    

def SearchValidation(nome_livro):
    if not nome_livro:
        raise EmpityFieldsError("O campo do nome do livro é obrigatório")
    
    