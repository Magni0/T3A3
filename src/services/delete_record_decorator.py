from main import db
from functools import wraps

# used to fix ORM DetachedInstanceError
def delete_record_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        s = db.session()
        s.expire_on_commit = False

        return func(*args, **kwargs)
    
    return wrapper