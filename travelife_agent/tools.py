# test_agent/tools.py
from pydantic import ValidationError

from travelife_agent.models import (
    GiveTourDetailInfomation, GiveTourDetailInfomationResponse, SuggestDestinationsInput, DestinationSuggestions, SuggestDestinationsResponse, TourDetailInput
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

def give_tour_detail_infomation(input_data: dict) -> GiveTourDetailInfomationResponse:
    try:
        print(f"TourDetailInput: {input_data}")
        parsed = TourDetailInput(**input_data)
        print(f"TourDetailInputParsed: #{parsed}")
        print(f"Tour id: #{parsed.tour_id}")
        result = tour_api.get_tour_detail(parsed.tour_id)
        return GiveTourDetailInfomationResponse(
            status="success",
            data=GiveTourDetailInfomation(
                tour_infomation=result
            )
    )
    except ValidationError as ve:
        return GiveTourDetailInfomationResponse(
            status="error",
            error={
                "error_type": "ValidationError",
                "error_message": str(ve)
            }
        )
    except Exception as e:
        return GiveTourDetailInfomationResponse(
            status="error",
            error={
                "error_type": "GiveInfomationError",
                "error_message": str(e)
            }
        )