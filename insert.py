import bdProdutos

v = bdProdutos.Produto()
v.titulo = 'Telefone 2'
v.preco = 10
v.avaliacao = 'S'

bdProdutos.session.add(v) # Vou inserir no banco o objeto v
bdProdutos.session.commit() # Comita a transação

