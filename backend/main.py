from typing import Dict

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from .crud import FileCRUD, generate_engine, generate_session
from .initialize_database import initialize_database

app = FastAPI()
api_router = APIRouter(prefix="/api")

engine = generate_engine()
initialize_database(engine)

def get_db():
    session = generate_session(engine)
    try:
        yield session
    finally:
        session.close()


@api_router.get("/files")
def get_configurations(session: Session = Depends(get_db)):
    print("Getting all files")
    return FileCRUD.get_files(session)


@api_router.post("/files")
def register_file(file_data: Dict[str, str], session: Session = Depends(get_db)):
    print(f"Creating file: {file_data}")
    FileCRUD.create_file(
        name=file_data.get("name"), path=file_data.get("path"), session=session
    )


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
