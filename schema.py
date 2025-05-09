from pydantic import BaseModel, EmailStr, constr


class RegisterSchema(BaseModel):
    user: constr(min_length=6, max_length=18)
    email: EmailStr
    password: constr(min_length=8)


class LoginSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
