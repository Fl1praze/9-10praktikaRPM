from fastapi import APIRouter,HTTPException
from app.products.schemas import ProductSchemas

from app.products.dao import ProductsDAO

router = APIRouter(prefix='/products',tags=['PRODUCTS'])


@router.get('')
async def get_products():
    result = ProductsDAO.find_all()
    return await result

@router.post('')
async def get_products(data:ProductSchemas):
    await ProductsDAO.add(**data.dict())
    return {"message": "Product add successfully"}

@router.get("/{id}")
async def get_products_by_id(id:int):
    result = ProductsDAO.find_by_id(id)
    return await result

@router.put("/{id}")
async def update_product(id: int, product_data: ProductSchemas):
    existing_product = await ProductsDAO.find_by_id(id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    update_data = product_data.dict(exclude_unset=True)
    await ProductsDAO.update(id, **update_data)
    return {"message": "Product updated successfully"}


@router.delete('/{id}')
async def delete_products(id:int):
    existing_product = await ProductsDAO.find_by_id(id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    await ProductsDAO.delete(id)
    return {"message": "Product deleted successfully"}
