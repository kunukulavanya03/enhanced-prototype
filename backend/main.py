from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Aims_To_Develop_The_Backend_Api_For_An_Enhanced_Prototype,_Leveraging_Fastapi_And_Sqlalchemy_To_Provide_Robust_And_Scalable_Backend_Services. API",
    description="Generated from Impact Analysis specifications",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "endpoints": 1,
        "models": 7
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "this_project_aims_to_develop_the_backend_api_for_an_enhanced_prototype,_leveraging_fastapi_and_sqlalchemy_to_provide_robust_and_scalable_backend_services."}

# Generated API endpoints
@app.put("/30")
def 30(id: int, item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
