from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import FileResponse
from .. import schemas, oauth2
from .scrape_modules.linkedindp import get_profile_pic
import os
from starlette.background import BackgroundTask


router = APIRouter(
    prefix="/linkedin",
    tags=["Linkedin"]
)


def remove_file(path: str) -> None:
    os.unlink(path)


@router.post("/dp")
async def get_linkedin_dp(username: schemas.Linkedin, current_user: int = Depends(oauth2.get_current_user)):
    # print(username.username)
    success = get_profile_pic(username.username)
    if success:
        filePath = f"./{username.username}.jpg"
        # print(filePath)
        # print(os.getcwd())
        # response = FileResponse(filePath)
        task = BackgroundTask(remove_file, path=filePath)
        return FileResponse(filePath, background=task)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Download error. Try again later.")

# /Volumes/My Personal Disk/FASTAPI/ashmita-majee-9146a227a.jpg
