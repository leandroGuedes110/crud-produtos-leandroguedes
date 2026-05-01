from sqlalchemy.orm import Session
import models, schemas

def get_produtos(db: Session):
    return db.query(models.Produto).all()

def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def update_produto(db: Session, produto_id: int, dados: schemas.ProdutoCreate):
    produto = get_produto(db, produto_id)
    if produto:
        for key, value in dados.dict().items():
            setattr(produto, key, value)
        db.commit()
        db.refresh(produto)
    return produto

def patch_produto(db: Session, produto_id: int, dados: schemas.ProdutoUpdate):
    produto = get_produto(db, produto_id)
    if produto:
        for key, value in dados.dict(exclude_unset=True).items():
            setattr(produto, key, value)
        db.commit()
        db.refresh(produto)
    return produto

def delete_produto(db: Session, produto_id: int):
    produto = get_produto(db, produto_id)
    if produto:
        db.delete(produto)
        db.commit()
    return produto
