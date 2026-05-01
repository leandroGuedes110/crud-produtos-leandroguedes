from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos", response_model=list[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.get_produtos(db)

@app.get("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.get_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos", response_model=schemas.ProdutoResponse, status_code=201)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.create_produto(db, produto)

@app.put("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def atualizar_produto(produto_id: int, dados: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    produto = crud.update_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.patch("/produtos/{produto_id}", response_model=schemas.ProdutoResponse)
def atualizar_parcial(produto_id: int, dados: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    produto = crud.patch_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.delete_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"msg": "Produto deletado com sucesso"}
