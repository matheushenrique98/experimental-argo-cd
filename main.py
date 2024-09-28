from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse



app = FastAPI()


@app.get("/health")
async def health_check():
    return JSONResponse(
        content="Server is running",
        status_code=status.HTTP_200_OK,
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
