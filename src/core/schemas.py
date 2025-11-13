from typing import Literal
from pydantic import BaseModel, Field


class DatasetSchema(BaseModel):
    age: int = Field(
        ..., description="Age of the individual in years", ge=0, alias="Age"
    )
    annual_income: float = Field(
        ..., description="Annual income in USD", ge=0, alias="AnnualIncome"
    )
    gender: Literal["Male", "Female"] = Field(
        ..., description="Gender of the individual", alias="Gender"
    )
    membership_duration: int = Field(
        ...,
        description="Duration of membership in years",
        ge=0,
        alias="MembershipDuration",
    )
    Location: Literal["Urban", "Rural", "Suburban"] = Field(
        ..., description="Location type of the individual", alias="Location"
    )
