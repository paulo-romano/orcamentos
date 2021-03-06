from random import choice
from django.db import IntegrityError
from orcamentos.core.models import Contract, Proposal, Customer

REPEAT = Proposal.objects.filter(status='a')

for i in REPEAT:
    proposal = Proposal.objects.get(pk=i.pk)
    contractor = Customer.objects.get(pk=proposal.work.customer.pk)
    try:
        Contract.objects.create(
            proposal=proposal,
            contractor=contractor,
            is_canceled=choice((True, False)))
    except IntegrityError:
        print('Registro existente.')
