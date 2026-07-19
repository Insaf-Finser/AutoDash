from __future__ import annotations

import re


class SemanticDetector:
    """
    Rule-based semantic detector.

    Returns one of:

    - identifier
    - measure
    - category
    - date
    - boolean
    - person
    - email
    - phone
    - url
    - location
    - currency
    - percentage
    - text
    """

    # --------------------------------------------------
    # Identifier
    # --------------------------------------------------

    IDENTIFIER_KEYWORDS = {
        "id",
        "uuid",
        "guid",
        "key",
        "code",
        "number",
        "no",
        "index",
        "identifier",
    }

    # --------------------------------------------------
    # Date
    # --------------------------------------------------

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
        "year",
        "month",
        "day",
    }

    # --------------------------------------------------
    # Measure
    # --------------------------------------------------

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
        "speed",
        "temperature",
        "volume",
        "length",
        "width",
        "depth",
        "consumption",
        "emission",
        "co2",
        "fuel",
        "mpg",
        "engine",
    }

    # --------------------------------------------------
    # Category
    # --------------------------------------------------

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
        "class",
        "make",
        "brand",
        "model",
        "vehicle",
        "fueltype",
        "transmission",
    }

    # --------------------------------------------------
    # Person
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    EMAIL_KEYWORDS = {
        "email",
        "mail",
    }

    # --------------------------------------------------
    # Phone
    # --------------------------------------------------

    PHONE_KEYWORDS = {
        "phone",
        "mobile",
        "telephone",
        "contact",
    }

    # --------------------------------------------------
    # URL
    # --------------------------------------------------

    URL_KEYWORDS = {
        "url",
        "website",
        "link",
        "uri",
    }

    # --------------------------------------------------
    # Location
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Currency
    # --------------------------------------------------

    CURRENCY_KEYWORDS = {
        "currency",
    }

    # --------------------------------------------------
    # Percentage
    # --------------------------------------------------

    PERCENTAGE_KEYWORDS = {
        "percent",
        "percentage",
        "ratio",
    }

    def detect(
        self,
        column_name: str,
        physical_type: str,
        unique_count: int,
        row_count: int,
        sample_values: list[str],
    ) -> tuple[str, float]:
        """
        Detect the semantic type of a column.
        """

        # ---------------------------------------------
        # Normalize column name
        # ---------------------------------------------

        normalized = re.sub(
            r"([a-z])([A-Z])",
            r"\1 \2",
            column_name,
        )

        normalized = (
            normalized.replace("_", " ")
            .replace("-", " ")
            .lower()
            .strip()
        )

        tokens = set(
            re.findall(
                r"[a-z0-9]+",
                normalized,
            )
        )

        unique_ratio = unique_count / max(row_count, 1)

        # ---------------------------------------------
        # Initialize scores
        # ---------------------------------------------

        scores = {
            "identifier": 0,
            "measure": 0,
            "category": 0,
            "date": 0,
            "boolean": 0,
            "person": 0,
            "email": 0,
            "phone": 0,
            "url": 0,
            "location": 0,
            "currency": 0,
            "percentage": 0,
        }

        # ---------------------------------------------
        # Apply scoring
        # ---------------------------------------------

        self._score_physical_type(
            scores,
            physical_type,
        )

        self._score_keywords(
            scores,
            normalized,
            tokens,
        )

        self._score_statistics(
            scores,
            tokens,
            physical_type,
            unique_ratio,
        )

        self._score_sample_values(
            scores,
            sample_values,
        )

        # ---------------------------------------------
        # Final decision
        # ---------------------------------------------

        best_type = max(
            scores,
            key=scores.get,
        )

        if scores[best_type] == 0:
            return "text", 1.0

        total = sum(scores.values())

        confidence = round(
            scores[best_type] / total,
            2,
        )

        print(f"\n{column_name}")
        print(scores)
        print(best_type)

        return best_type, confidence

    def _score_physical_type(
        self,
        scores: dict[str, int],
        physical_type: str,
    ) -> None:
        """
        Score based on the physical data type.
        """

        if physical_type == "boolean":
            scores["boolean"] += 100
            return

        if physical_type in {"date", "datetime"}:
            scores["date"] += 100
            return

        if physical_type in {"integer", "float"}:
            scores["measure"] += 30
    
    def _score_keywords(
        self,
        scores: dict[str, int],
        normalized: str,
        tokens: set[str],
    ) -> None:
        """
        Score using column name keywords.
        """

        # -----------------------------
        # Identifier
        # -----------------------------

        if (
            normalized.endswith(" id")
            or normalized.endswith("_id")
            or normalized.endswith(" uuid")
            or normalized.endswith(" guid")
            or normalized.endswith(" code")
        ):
            scores["identifier"] += 60

        if tokens & self.IDENTIFIER_KEYWORDS:
            scores["identifier"] += 40

        # -----------------------------
        # Date
        # -----------------------------

        if tokens & self.DATE_KEYWORDS:
            scores["date"] += 40

        # -----------------------------
        # Measure
        # -----------------------------

        if tokens & self.MEASURE_KEYWORDS:
            scores["measure"] += 40

        # -----------------------------
        # Category
        # -----------------------------

        if tokens & self.CATEGORY_KEYWORDS:
            scores["category"] += 40

        # -----------------------------
        # Person
        # -----------------------------

        if tokens & self.PERSON_KEYWORDS:
            scores["person"] += 40

        # -----------------------------
        # Email
        # -----------------------------

        if tokens & self.EMAIL_KEYWORDS:
            scores["email"] += 100

        # -----------------------------
        # Phone
        # -----------------------------

        if tokens & self.PHONE_KEYWORDS:
            scores["phone"] += 100

        # -----------------------------
        # URL
        # -----------------------------

        if tokens & self.URL_KEYWORDS:
            scores["url"] += 100

        # -----------------------------
        # Location
        # -----------------------------

        if tokens & self.LOCATION_KEYWORDS:
            scores["location"] += 100

        # -----------------------------
        # Currency
        # -----------------------------

        if tokens & self.CURRENCY_KEYWORDS:
            scores["currency"] += 100

        # -----------------------------
        # Percentage
        # -----------------------------

        if tokens & self.PERCENTAGE_KEYWORDS:
            scores["percentage"] += 100
    
    def _score_statistics(
        self,
        scores: dict[str, int],
        tokens: set[str],
        physical_type: str,
        unique_ratio: float,
    ) -> None:
        """
        Score using statistical properties of the column.
        """

        # -----------------------------------------
        # Likely identifier
        # -----------------------------------------

        if unique_ratio > 0.95:
            scores["identifier"] += 30

        # -----------------------------------------
        # String columns with few unique values
        # are usually categories.
        # -----------------------------------------

        if (
            physical_type == "string"
            and unique_ratio < 0.10
        ):
            scores["category"] += 40

        # -----------------------------------------
        # Numeric columns with many unique values
        # are usually measures.
        # -----------------------------------------

        if (
            physical_type in {"integer", "float"}
            and unique_ratio > 0.20
        ):
            scores["measure"] += 20

        # -----------------------------------------
        # Numeric columns with very few unique values
        # are often categories.
        # Example:
        # Rating (1-5)
        # Priority (1-3)
        # Status (0/1)
        # -----------------------------------------

        if (
            physical_type in {"integer", "float"}
            and unique_ratio < 0.05
        ):
            scores["category"] += 15

        # -----------------------------------------
        # Years are categories, not measures.
        # -----------------------------------------

        if (
            "year" in tokens
            and physical_type == "integer"
            and unique_ratio < 0.05
        ):
            scores["category"] += 50

        # -----------------------------------------
        # IDs should never become measures.
        # -----------------------------------------

        if (
            scores["identifier"] > 0
            and scores["measure"] > 0
        ):
            scores["identifier"] += 20

        # -----------------------------------------
        # Category names usually aren't persons.
        # -----------------------------------------

        if (
            scores["category"] > 0
            and scores["person"] > 0
        ):
            scores["category"] += 10

    def _score_sample_values(
        self,
        scores: dict[str, int],
        sample_values: list[str],
    ) -> None:
        """
        Score semantic types using actual sample values.
        """

        if not sample_values:
            return

        values = [
            str(value).strip().lower()
            for value in sample_values
            if str(value).strip()
        ]

        if not values:
            return

        # -----------------------------------------
        # Email
        # -----------------------------------------

        email_count = sum(
            1
            for value in values
            if re.match(
                r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
                value,
            )
        )

        if email_count >= len(values) * 0.6:
            scores["email"] += 100

        # -----------------------------------------
        # URL
        # -----------------------------------------

        url_count = sum(
            1
            for value in values
            if value.startswith("http://")
            or value.startswith("https://")
            or value.startswith("www.")
        )

        if url_count >= len(values) * 0.6:
            scores["url"] += 100

        # -----------------------------------------
        # Phone
        # -----------------------------------------

        phone_count = sum(
            1
            for value in values
            if re.match(
                r"^\+?[0-9 ()-]{7,}$",
                value,
            )
        )

        if phone_count >= len(values) * 0.6:
            scores["phone"] += 100

        # -----------------------------------------
        # Boolean
        # -----------------------------------------

        boolean_values = {
            "true",
            "false",
            "yes",
            "no",
            "0",
            "1",
        }

        if all(value in boolean_values for value in values):
            scores["boolean"] += 80

        # -----------------------------------------
        # ISO Date
        # -----------------------------------------

        date_count = sum(
            1
            for value in values
            if re.match(
                r"^\d{4}-\d{2}-\d{2}$",
                value,
            )
        )

        if date_count >= len(values) * 0.6:
            scores["date"] += 80

        # -----------------------------------------
        # Currency
        # -----------------------------------------

        currency_count = sum(
            1
            for value in values
            if value.startswith("$")
            or value.startswith("€")
            or value.startswith("£")
            or value.startswith("₹")
            or value.startswith("aed")
            or value.startswith("usd")
        )

        if currency_count >= len(values) * 0.6:
            scores["currency"] += 80

        # -----------------------------------------
        # Percentage
        # -----------------------------------------

        percentage_count = sum(
            1
            for value in values
            if value.endswith("%")
        )

        if percentage_count >= len(values) * 0.6:
            scores["percentage"] += 80

        # -----------------------------------------
        # Latitude / Longitude
        # -----------------------------------------

        numeric_values = []

        # -----------------------------------------
        # Small repeated string set
        # Usually indicates a category
        # -----------------------------------------

        unique = len(set(values))

        if (
            unique <= 20
            and unique < len(values)
        ):
            scores["category"] += 20

    def _score_keywords(
        self,
        scores: dict[str, int],
        normalized: str,
        tokens: set[str],
    ) -> None:
        """
        Score semantic types using weighted keywords.
        """

        keyword_weights = {
            "identifier": {
                "id": 60,
                "uuid": 60,
                "guid": 60,
                "code": 40,
                "key": 40,
                "identifier": 50,
            },
            "measure": {
                "amount": 50,
                "price": 50,
                "cost": 50,
                "sales": 60,
                "revenue": 60,
                "profit": 60,
                "income": 60,
                "expense": 60,
                "score": 40,
                "rating": 40,
                "count": 30,
                "quantity": 40,
                "total": 30,
                "average": 30,
                "avg": 30,
                "weight": 40,
                "height": 40,
                "size": 30,
                "distance": 40,
                "duration": 40,
                "fuel": 30,
                "consumption": 60,
                "co2": 60,
                "emission": 60,
                "engine": 20,
                "mpg": 60,
            },
            "category": {
                "country": 40,
                "city": 20,
                "state": 20,
                "province": 20,
                "region": 20,
                "department": 40,
                "category": 40,
                "segment": 30,
                "status": 30,
                "priority": 30,
                "gender": 30,
                "role": 30,
                "type": 30,
                "class": 40,
                "vehicle": 20,
                "make": 50,
                "brand": 50,
                "model": 20,
                "transmission": 40,
                "fueltype": 40,
            },
            "person": {
                "customer": 40,
                "employee": 40,
                "student": 40,
                "teacher": 40,
                "manager": 40,
                "owner": 40,
                "vendor": 40,
                "supplier": 40,
                "user": 40,
                "company": 20,
                "organization": 20,
                "name": 20,
            },
            "date": {
                "date": 50,
                "time": 40,
                "created": 40,
                "updated": 40,
                "timestamp": 50,
                "year": 50,
                "month": 40,
                "day": 40,
            },
            "email": {
                "email": 100,
                "mail": 80,
            },
            "phone": {
                "phone": 100,
                "mobile": 100,
                "telephone": 100,
            },
            "url": {
                "url": 100,
                "website": 100,
                "link": 80,
            },
            "location": {
                "address": 80,
                "latitude": 80,
                "longitude": 80,
                "lat": 60,
                "lng": 60,
                "zip": 60,
                "postal": 60,
            },
            "currency": {
                "currency": 100,
            },
            "percentage": {
                "percent": 100,
                "percentage": 100,
                "ratio": 40,
            },
        }

        if (
            normalized.endswith(" id")
            or normalized.endswith("_id")
            or normalized.endswith(" uuid")
            or normalized.endswith(" guid")
        ):
            scores["identifier"] += 60

        for token in tokens:
            for semantic_type, mapping in keyword_weights.items():
                scores[semantic_type] += mapping.get(token, 0)

        