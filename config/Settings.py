import os
class Settings:
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Dev
    #host='localhost'
    #database='practical5'
    #user='root'
    #password='SuzanneLee1012'

    #Production
    host=os.environ['HOST']
    database=os.environ['DATABASE']
    user=os.environ['USER']
    password=os.environ['PASSWORD']