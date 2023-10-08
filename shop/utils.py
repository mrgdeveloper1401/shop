from kavenegar import *


def send_otp_code(email, code):
    try:
        api = KavenegarAPI('78663065366A5A513878732F572B5665734F315A6769436A6D4132584C6A36744733376D793755687675383D', timeout=20)
        params = {
            'sender': '',#optional
            'receptor': '',#multiple mobile number, split by comma
            'message': f'accept account with code {code}',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)