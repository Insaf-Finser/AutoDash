from __future__ import annotations

import re


class SemanticDetector:
    """
    Detects the semantic meaning of a column.

    Returns values like:
    - identifier
    - measure
    - category
    - date
    - boolean
    - email
    - phone
    - url
    - location
    - currency
    - percentage
    - text
    """

    IDENTIFIER_KEYWORDS = {
        "id",
        "uuid",
        "guid",
        "key",
        "code",
        "number",
        "no",
        "index",
    }

    DATE_KEYWORDS = {
        "date",
        "time",
        "created",
        "updated",
        "modified",
        "deadline",
        "timestamp",
        "dob",
        "birth",
        "joined",
        "start",
        "end",
    }

    MEASURE_KEYWORDS = {
        "amount",
        "price",
        "cost",
        "profit",
        "loss",
        "sales",
        "revenue",
        "income",
        "expense",
        "budget",
        "salary",
        "bonus",
        "quantity",
        "qty",
        "count",
        "total",
        "sum",
        "average",
        "avg",
        "score",
        "rating",
        "reward",
        "points",
        "distance",
        "duration",
        "age",
        "weight",
        "height",
        "size",
        "bytes",
    }

    CATEGORY_KEYWORDS = {
        "country",
        "city",
        "state",
        "province",
        "region",
        "department",
        "division",
        "team",
        "category",
        "group",
        "segment",
        "status",
        "priority",
        "level",
        "gender",
        "role",
        "type",
    }

    PERSON_KEYWORDS = {
        "customer",
        "client",
        "employee",
        "student",
        "teacher",
        "manager",
        "owner",
        "person",
        "user",
        "vendor",
        "supplier",
        "company",
        "organization",
        "organisation",
        "name",
        "title",
    }

    EMAIL_KEYWORDS = {
        "email",
        "mail",
    }

    PHONE_KEYWORDS = {
        "phone",
        "mobile",
        "telephone",
        "contact",
    }

    URL_KEYWORDS = {
        "url",
        "website",
        "link",
        "uri",
    }

    LOCATION_KEYWORDS = {
        "latitude",
        "longitude",
        "lat",
        "lng",
        "lon",
        "zip",
        "zipcode",
        "postal",
        "postcode",
        "address",
    }

    CURRENCY_KEYWORDS = {
        "currency",
    }

    PERCENTAGE_KEYWORDS = {
        "percent",
        "percentage",
        "ratio",
    }

    def detect(
        self,
        column_name: str,
        physical_type: str,
    ) -> str:

        name = column_name.lower().strip()

        tokens = set(re.findall(r"[a-z0-9]+", name))

        # ----------------------------------------------------
        # 1. Boolean
        # ----------------------------------------------------

        if physical_type == "boolean":
            return "boolean"

        # ----------------------------------------------------
        # 2. Date
        # ----------------------------------------------------

        if physical_type in {"date", "datetime"}:
            return "date"

        if any(keyword in name for keyword in self.DATE_KEYWORDS):
            return "date"

        # ----------------------------------------------------
        # 3. Identifier
        # ----------------------------------------------------

        if (
            name.endswith("id")
            or name.endswith("_id")
            or name.endswith("uuid")
            or name.endswith("guid")
            or name.endswith("code")
        ):
            return "identifier"

        if tokens & self.IDENTIFIER_KEYWORDS:
            return "identifier"

        # ----------------------------------------------------
        # 4. Email
        # ----------------------------------------------------

        if tokens & self.EMAIL_KEYWORDS:
            return "email"

        # ----------------------------------------------------
        # 5. Phone
        # ----------------------------------------------------

        if tokens & self.PHONE_KEYWORDS:
            return "phone"

        # ----------------------------------------------------
        # 6. URL
        # ----------------------------------------------------

        if tokens & self.URL_KEYWORDS:
            return "url"

        # ----------------------------------------------------
        # 7. Location
        # ----------------------------------------------------

        if tokens & self.LOCATION_KEYWORDS:
            return "location"

        # ----------------------------------------------------
        # 8. Currency
        # ----------------------------------------------------

        if tokens & self.CURRENCY_KEYWORDS:
            return "currency"

        # ----------------------------------------------------
        # 9. Percentage
        # ----------------------------------------------------

        if tokens & self.PERCENTAGE_KEYWORDS:
            return "percentage"

        # ----------------------------------------------------
        # 10. Category
        # ----------------------------------------------------

        if tokens & self.CATEGORY_KEYWORDS:
            return "category"

        # ----------------------------------------------------
        # 11. Person
        # ----------------------------------------------------

        if tokens & self.PERSON_KEYWORDS:
            return "person"

        # ----------------------------------------------------
        # 12. Measures
        # ----------------------------------------------------

        if tokens & self.MEASURE_KEYWORDS:
            return "measure"

        if physical_type in {"integer", "float"}:
            return "measure"

        # ----------------------------------------------------
        # 13. Default
        # ----------------------------------------------------

        return "text"