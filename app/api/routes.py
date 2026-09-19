from fastapi import APIRouter

router = APIRouter()


@router.post("/customer-analysis")
def customer_analysis(customer: str):
    return {
        "customer": customer,
        "message": "Customer analysis endpoint is working"
    }