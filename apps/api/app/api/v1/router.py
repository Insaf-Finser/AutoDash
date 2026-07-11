from fastapi import APIRouter

from app.api.v1.workbooks import router as workbook_router

router = APIRouter(prefix="/v1")

router.include_router(
    workbook_router,
    prefix="/workbooks",
    tags=["Workbooks"],
)