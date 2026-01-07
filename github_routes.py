from fastapi import APIRouter, HTTPException
from validator import validate_username, validate_repo

router = APIRouter(prefix="/github")

@router.get("/validate-user/{username}")
async def validate_user(username: str):
    try:
        return {"valid": await validate_username(username)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/validate-repo")
async def validate_repository(owner: str, repo: str):
    try:
        data = await validate_repo(owner, repo)
        return {"repo": data["full_name"], "private": data["private"]}
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))