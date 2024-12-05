import re
from validate_docbr import CPF

def invalid_name(name) -> bool:
    return not name.isalpha()

def invalid_cpf(cpf_number) -> bool:
    cpf = CPF()
    return not cpf.validate(cpf_number)

def invalid_phone_number(phone_number) -> bool:
    pattern = '^[\d]{2}\s[\d]{5}-[\d]{4}$'
    return not re.findall(pattern, phone_number)