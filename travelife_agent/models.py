# test_agent/models.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union

class DomainError(BaseModel):
  error_type: str
  error_message: str
  
class SuggestDestinationsInput(BaseModel):
  destination: str = Field(..., description="User's destination interest (e.g., Hanoi, Da Nang, etc.)")
  
class TourDetailInput(BaseModel):
  tour_id: str = Field(..., description='Id of the tour that user request to get')

class DestinationSuggestions(BaseModel):
  interest: str
  destinations: dict

class GiveTourDetailInfomation(BaseModel):
  tour_infomation: dict
  
class SuggestDestinationsResponse(BaseModel):
  status: Literal["success", "error"]
  data: Optional[DestinationSuggestions] = None
  error: Optional[DomainError] = None

class GiveTourDetailInfomationResponse(BaseModel):
  status: Literal["success", "error"]
  data: Optional[GiveTourDetailInfomation] = None
  error: Optional[DomainError] = None
