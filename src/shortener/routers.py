from fastapi import APIRouter, Depends, HTTPException
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from .schemas import ShortenLinkRequest, ShortenLinkRespone
from .repositories import ShortLinkRepository
from .services import ShortLinkService
from .exceptions import CodeExistsError, RedirectError

from src.core.database import get_db
from src.core.generic_response import success_response

shortener_router = APIRouter()


@shortener_router.post("/api/short-links")
async def shorten_link(
    request: Request, request_body: ShortenLinkRequest, db: Session = Depends(get_db)
):
    repo = ShortLinkRepository(db=db)

    try:
        short_link_obj = ShortLinkService(repo).create_short_link(
            **request_body.model_dump()
        )
    except CodeExistsError as e:
        raise HTTPException(400, str(e))

    short_url = str(
        request.url_for("redirect_to_original_link", code=short_link_obj.code)
    )
    return success_response(data=ShortenLinkRespone(short_url=short_url, code=short_link_obj.code))


@shortener_router.get("/s/{code}")
async def redirect_to_original_link(code: str, db: Session = Depends(get_db)):
    repo = ShortLinkRepository(db=db)
    short_link_service = ShortLinkService(repo)

    try:
        short_link_obj = short_link_service.get_by_code(code)
        short_link_service.incr_visitor_count_by_code(
            short_link_obj.code, visitor_count=short_link_obj.visitor_count
        )
    except RedirectError as e:
        raise HTTPException(404, str(e))

    return RedirectResponse(short_link_obj.original_link)
