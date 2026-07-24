from typing import Optional
from pydantic import BaseModel, Field


class DealerResponse(BaseModel):
    """
    Dealer Response Model

    Used when returning dealer information
    from the API.
    """

    id: Optional[int] = Field(
        default=None,
        description="Unique dealer ID"
    )

    name: str = Field(
        ...,
        example="Green Agro Center",
        description="Dealer Name"
    )

    district: str = Field(
        ...,
        example="Nashik",
        description="Dealer District"
    )

    pincode: str = Field(
        ...,
        example="422101",
        description="Dealer Pincode"
    )

    phone: str = Field(
        ...,
        example="9876543210",
        description="Dealer Contact Number"
    )

    latitude: float = Field(
        ...,
        example=19.9975,
        description="Latitude"
    )

    longitude: float = Field(
        ...,
        example=73.7898,
        description="Longitude"
    )

    distance: Optional[float] = Field(
        default=None,
        example=2.4,
        description="Distance from user in KM"
    )

    class Config:
        from_attributes = True


class SearchResponse(BaseModel):
    """
    Wrapper Response

    Useful if later you want to return
    metadata like total records.
    """

    success: bool = True

    total_results: int

    dealers: list[DealerResponse]


class ErrorResponse(BaseModel):
    """
    Standard Error Response
    """

    success: bool = False

    message: str

    error: Optional[str] = None


class HealthResponse(BaseModel):
    """
    Health Check Response
    """

    status: str

    application: str

    version: str