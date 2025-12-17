from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from demo import runnable
from typing import List

app = FastAPI(
    title="GZX",
    version="1.0",
    description="干中学"
)



# 添加一下跨域访问  localhost:5173可以访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def redirect_root_to_docs() -> RedirectResponse:
    return RedirectResponse("/docs")






# Edit this to add the chain you want to add
add_routes(
    app,
    runnable,
    path="/gzx",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)