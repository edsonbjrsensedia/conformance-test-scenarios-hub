# Steps

Ensure that the tested institution accepts a DCM request to remove the webhook notification endpoint. This test also ensures that a webhook is retried after a failure message is sent.
For this test the institution will need to register on it’s software statement a webhook under the following format - https://web.conformance.directory.openbankingbrasil.org.br/test-mtls/a/&lt;alias&gt;

1 • Obtain a SSA from the Directory
2 • Ensure that on the SSA the attribute software_api_webhook_uris contains the URI https://web.conformance.directory.openbankingbrasil.org.br/test-mtls/a/&lt;alias&gt;, where the alias is to be obtained from the field alias on the test configuration
4 • Call the Registration Endpoint, also sending the field ""webhook_uris"":[“https://web.conformance.directory.openbankingbrasil.org.br/test-mtls/a/&lt;alias&gt;”]
5 • Expect a 201 - Validate Response
6 • Set the test to wait for X seconds, where X is the time in seconds provided on the test configuration for the attribute webhookWaitTime. If no time is provided, X is defaulted to 600 seconds
7 • Calls POST Consents Endpoint with localInstrument set as DICT
8 • Expects 201 - Validate Response
9 • Redirects the user to authorize the created consent
10 • Call GET Consent
11 • Expects 200 - Validate if status is ""AUTHORISED""
12 • Calls the POST Payments with localInstrument as DICT
13 • Expects 201 - Validate response
14 • Set the payments webhook notification endpoint to be equal to https://web.conformance.directory.openbankingbrasil.org.br/test-mtls/a/&lt;alias&gt;/open-banking/webhook/v1/payments/v4/pix/payments/{paymentId} where the alias is to be obtained from the field alias on the test configuration
15 • Set the payments webhook notification endpoint to be equal to https://web.conformance.directory.openbankingbrasil.org.br/test-mtls/a/&lt;alias&gt;/open-banking/webhook/v1/payments/v4/consents/{consentsId} where the alias is to be obtained from the field alias on the test configuration
16 • Expect an incoming message, for at most 60 seconds,which must be mtls protected, to be received on the webhook endpoint set for this test
17 • Return a 503 - Validate the contents of the incoming message, including the presence of the x-webhook-interaction-id header and that the timestamp value is within  now and the start of the test
18 • Expect an incoming message, for at most 60 seconds, which must be mtls protected, to be received on the webhook endpoint set for this test
19 • Return a 202 - Validate the contents of the incoming message, including the presence of the x-webhook-interaction-id header and that the timestamp value is within  now and the start of the test
20 • Call the Get Payments endpoint with the PaymentID 
21 • Expects status returned to be (ACSC) - Validate Response
22 • Call the PUT Registration Endpoint without sending the field ""webhook_uris""
23 • Set the test to wait for X seconds, where X is the time in seconds provided on the test configuration for the attribute webhookWaitTime. If no time is provided, X is defaulted to 600 seconds
24 • Calls POST Consents Endpoint with localInstrument set as DICT
25 • Expects 201 - Validate Response
26 • Redirects the user to authorize the created consent
27 • Call GET Consent
28 • Expects 200 - Validate if status is ""AUTHORISED""
29 • Calls the POST Payments with localInstrument as DICT
30 • Expects 201 - Validate response
31 • Validate that no webhook is called on the payments webhook endpoints 
32 • Call the Delete Registration Endpoint
33 • Expect a 204 - No Content
