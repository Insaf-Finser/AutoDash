from enum import Enum

class WorkbookStatus(str,Enum):

    UPLOADED = "uploaded"

    VALIDATING = "validating"

    PROCESSING = "processing"

    READY = "ready"

    FAILED = "failed"

    ARCHIVED = "archived"