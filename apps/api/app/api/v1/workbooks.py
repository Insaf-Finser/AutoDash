from fastapi import APIRouter,Depends,File,UploadFile
from app.schemas.status import StatusResponse

from app.database.session import get_db
from app.repositories.workbook_repository import WorkbookRepository
from app.schemas import WorkbookResponse
from app.services.storage import get_storage_service
from app.services.workbook_service import WorkbookService


router = APIRouter()


@router.get("/",response_model = StatusResponse)
async def list_workbooks():
    return StatusResponse(
        message="Workbook API working !"
    )

@router.post(
    "/upload",
    response_model=WorkbookResponse,
)
async def upload_workbook(
    file: UploadFile = File(...),
    db=Depends(get_db),
):

    repository = WorkbookRepository(db)

    storage = get_storage_service()

    service = WorkbookService(
        repository,
        storage,
    )

    workbook = await service.upload_workbook(
        filename=file.filename,
        content_type=file.content_type,
        data=await file.read(),
    )

    return WorkbookResponse.model_validate(
        workbook,
    )