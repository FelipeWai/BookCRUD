from firebase_admin import firestore
from conn import firebase_admin
db = firestore.client()



from validations import create_validation
from exceptions import LivroAlreadyExists
def AddBook(nome_livro, nome_autor, ano_publicacao, nome_editora):

    create_validation(nome_livro, nome_autor, ano_publicacao, nome_editora)

    nome_livro = nome_livro.lower()

    livro_exists = db.collection('livros').where(field_path='nome_livro', op_string='==', value=nome_livro).limit(1).get()
    if livro_exists:
        raise LivroAlreadyExists("Um livro com esse nome já foi cadastrado!")

    db.collection('livros').add({
        'nome_livro': nome_livro,
        'nome_autor': nome_autor,
        'ano_publicacao': ano_publicacao,
        'nome_editora': nome_editora,
    })

from validations import SearchValidation
def SearchBook(nome_livro):

    nome_livro = nome_livro.lower()

    SearchValidation(nome_livro)

    query = db.collection('livros').where(field_path='nome_livro', op_string='==', value=nome_livro).limit(1).get()

    if query:
        dados = query[0].to_dict()
        return dados
    else:
        return None
    

def UpdateBook(nome_livro, nome_autor, ano_publicacao, nome_editora):

    create_validation(nome_livro, nome_autor, ano_publicacao, nome_editora)

    query = db.collection('livros').where(field_path='nome_livro', op_string='==', value=nome_livro).limit(1).get()

    if query:
        livro_ref = query[0].reference
        try:
            livro_ref.update({
                'nome_autor': nome_autor,
                'ano_publicacao': ano_publicacao,
                'nome_editora': nome_editora,
            })
            return True
        except:
            raise Exception("Erro ao atualizar livro")
    else:
        return None

def DeleteBook(nome_livro):

    SearchValidation(nome_livro)

    query = db.collection('livros').where(field_path='nome_livro', op_string='==', value=nome_livro).limit(1).get()

    if query:
        livro_ref = query[0].reference
        try:
            livro_ref.delete()
        except Exception as e:
            raise Exception("Erro ao excluir livro:", str(e))
    else:
        return None
