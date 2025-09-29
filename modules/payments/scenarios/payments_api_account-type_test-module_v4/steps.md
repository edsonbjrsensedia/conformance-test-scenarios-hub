# Steps - 002-agendar-5-pagamentos-d+1

1. POST /recurring-payments (5x) com data D+1 usando o `consentId`
2. Validar 201 e guardar `paymentIds`
3. GET /recurring-payments/{paymentId} até `status = SCHD`
