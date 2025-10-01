# Steps

**PATCH Payments happy path test that will require the tester to revoke the scheduled Payment on the Financial Instituion application, leading the scheduled payment to have a cancelation object set as DETENTORA**

- 1 - Create consent with request payload with both the  schedule.single.date field set as D+1
- 2 - Call the POST Consents endpoints
- 3 - Expects 201 - Validate response
- 4 - Redirects the user to authorize the created consent
- 5 - Call GET Consent
- 6 - Expects 200 - Validate if status is ""AUTHORISED"" and validate response
- 7 - Call the POST Payments Endpoint
- 8 - Expects 201 - Validate Response
- 9 - Poll the Get Payments endpoint with the PaymentID Created while payment status is RCVD or ACCP
- 10 - Expect Payment Scheduled to be reached (SCHD) - Validate Response
- 11 - Poll the Get Payments endpoint with the PaymentID Created while payment status is SCHD for up to 10 minutes - Wait for the payment to reach a CANC state
- 12  - Expect 200 - Make Sure cancellation.cancelledFrom is set as ""DETENTORA"". Make Sure cancellation.reason is set as "CANCELADO_AGENDAMENTO" - Validate Response
