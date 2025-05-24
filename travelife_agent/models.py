# test_agent/models.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union

class SuggestDestinationsInput(BaseModel):
  destination: str = Field(..., description="User's destination interest (e.g., Hanoi, Da Nang, etc.)")

class DestinationSuggestions(BaseModel):
  interest: str
  destinations: dict

class DomainError(BaseModel):
  error_type: str
  error_message: str

class SuggestDestinationsResponse(BaseModel):
  status: Literal["success", "error"]
  data: Optional[DestinationSuggestions] = None
  error: Optional[DomainError] = None

class BookTourInput(BaseModel):
  destination: str = Field(..., description="Destination the user wants to book a tour for")
  date: str = Field(..., description="Date in ISO format (YYYY-MM-DD)")

class TourBookingConfirmation(BaseModel):
  destination: str
  date: str
  status: str

class FAQInput(BaseModel):
  question: str = Field(..., description="Frequently asked question about travel or booking")

class FAQAnswer(BaseModel):
  question: str
  answer: str
  
