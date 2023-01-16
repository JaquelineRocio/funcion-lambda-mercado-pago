import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
   
    payment_response = sdk.payment().create(event)
    payment = payment_response["response"]
    
    status =payment["status"]
    
    
    if status != 400:
        id =payment["id"]
        status_detail =payment["status_detail"]
        date_approved=payment["date_approved"]
        payer = payment["payer"]
        payment_method_id= payment["payment_method_id"]
        payment_type_id= payment["payment_type_id"]
        refunds= payment["refunds"]
        body={
            'status': status,
            'id': id,
            'status_detail': status_detail,
            "date_approved":date_approved,
            "payer": payer,
            "payment_method_id":payment_method_id,
            "payment_type_id": payment_type_id,
            "refunds": refunds
        }
    else:
        body = json.dumps(payment)
        
    return {
        "statusCode": 200,
        "body":body ,
    }