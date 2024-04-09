This folder contains 2 files:
- dotOcean-test.crt
- dotOcean-test.key

These files are used to use HTTPS with the webhooks.
HTTPS is used to ensure that the data being sent from NetBox to EDA is encrypted.  
This was implemented to prevent data leakage (due to MITM attacks) and to ensure the data integrity of the data being sent.  

I still have to implement the usage of a pre-shared secret (HMAC) to ensure the integrity of the data being sent.  
This secret can then be set in the NetBox webhook configuration, and the EDA rulebook. It then ensures that the data being sent is not tampered with.  