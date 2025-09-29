# Steps

1. POST /recurring-consents (`schedule.daily.startDate = D+1`, `quantity = 5`)
2. Validar 201 e extrair `consentId`
3. Autorização do consent
4. GET Consent e validar `status = AUTHORIZED`
