# test_agent/tools.py
from pydantic import ValidationError

from travelife_agent.models import (
    SuggestDestinationsInput, DestinationSuggestions, SuggestDestinationsResponse
)
from travelife_agent.API import tour_api


def suggest_destinations(input_data: dict) -> SuggestDestinationsResponse:
    try:
        parsed = SuggestDestinationsInput(**input_data)
        result = tour_api.search_tour(parsed.destination)
        return SuggestDestinationsResponse(
            status="success",
            data=DestinationSuggestions(
                interest=parsed.destination,
                destinations=result
            )
        )
    except ValidationError as ve:
        return SuggestDestinationsResponse(
            status="error",
            error={
                "error_type": "ValidationError",
                "error_message": str(ve)
            }
        )
    except Exception as e:
        return SuggestDestinationsResponse(
            status="error",
            error={
                "error_type": "SearchError",
                "error_message": str(e)
            }
        )



# @adk_tool(
#   name="book_tour",
#   description="Books a tour for a specific destination and date."
# )
# def book_tour(input_data: dict) -> TourBookingConfirmation | DomainError:
#   try:
#     parsed = BookTourInput(**input_data)
#     result = tour_api.book_tour(destination=parsed.destination, date=parsed.date)

#     return TourBookingConfirmation(**result)
#   except ValidationError as ve:
#     return DomainError(
#         error_type="ValidationError",
#         error_message=str(ve)
#     )
#   except Exception as e:
#     return DomainError(
#         error_type="BookingError",
#         error_message=str(e)
#     )


# @adk_tool(
#     name="answer_faq",
#     description="Answers frequently asked questions related to travel, booking, or cancellations."
# )
# def get_faq_answer(input_data: dict) -> FAQAnswer | DomainError:
#   try:
#     parsed = FAQInput(**input_data)
#     answer = tour_api.get_faq_answer(parsed.question)

#     return FAQAnswer(question=parsed.question, answer=answer)
#   except ValidationError as ve:
#     return DomainError(
#         error_type="ValidationError",
#         error_message=str(ve)
#     )
#   except Exception as e:
#     return DomainError(
#         error_type="FAQError",
#         error_message=str(e)
#     )
