import uvicorn

# from fastapi import FastAPI
from fastapi_offline import FastAPIOffline
from tasks.from_dirs.router import router as from_dirs_router
from tasks.last_operations.router import router as last_operations_router

from tasks.router import router as tasks_router
from tasks.to_dirs.router import router as to_dirs_router
from tasks.copy_extensions.router import router as copy_operations_router

# app = FastAPI()
app = FastAPIOffline()

app.include_router(tasks_router)
app.include_router(from_dirs_router)
app.include_router(to_dirs_router)
app.include_router(last_operations_router)
app.include_router(copy_operations_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
