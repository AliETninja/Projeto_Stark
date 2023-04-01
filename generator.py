import random
import pprint
import json
import starkbank


class People:
    _data = json.load(open('nomes.json', encoding='iso-8859-1'))
    _nomes = _data['nomes']
    _sobre_nomes = _data['sobre_nomes']

    @staticmethod
    def cpf():
        numbs = str(random.randint(111111111, 999999999))
        # criando o primeiro digito
        x = 10
        value = 0
        for i in numbs:
            value += x * int(i)
            x -= 1

        value = value % 11

        if value < 2:
            digit_1 = 0
        else:
            digit_1 = 11 - (value % 11)

        # criando o segundo digito
        numbss = numbs + str(digit_1)

        x = 11
        value = 0
        for i in numbss:
            value += x * int(i)
            x -= 1

        value = value % 11

        if value < 2:
            digit_2 = 0
        else:
            digit_2 = 11 - (value % 11)


        # separando em grupos de 3 "[xxx, xxx, xxx]"
        cpf = [numbs[x * 3: (3 * x) + 3] for x in range(3)]

        cpf = ".".join(cpf)
        return f'{cpf}-{digit_1}{digit_2}'

    @staticmethod
    def nome():
        return f"{random.choice(People._nomes).encode('iso-8859-1').decode('utf-8')} {random.choice(People._sobre_nomes).encode('iso-8859-1').decode('utf-8')}"

class Invoices:

    @staticmethod
    def create_invoices():
        invoices_int = random.randint(8, 12)
        invoices = list()
        for i in range(invoices_int):
            invoices.append(starkbank.Invoice(
                amount=random.randint(1, 10000),
                name=People.nome(),
                tax_id=People.cpf()
            ))

        return invoices

class Transfer:

    @staticmethod
    def transaction(amount):
        return starkbank.Transfer(
                amount=int(amount),
                tax_id="20.018.183/0001-80",
                name="Stark Bank S.A.",
                bank_code="20018183",
                branch_code="0001",
                account_number="6341320293482496",
                account_type="payment"
            )


if __name__ == '__main__':

    pessoa = {
        "nome": People.nome(),
        "cpf": People.cpf()
    }

    pprint.pprint(pessoa)