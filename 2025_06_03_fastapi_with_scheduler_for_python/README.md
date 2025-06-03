# README

Story:

+ Suppose we are building a SaaS tool for AI generated whatsapp sales messages
+ Every user receives a daily quota of AI tokens, at the start of each day, the quota is refilled
+ The quota is used to limit the amount of AI chatbot usage
+ The AI takes the chat history into account to personalize the offer messages

Blog post structure:

+ Introduction
+ How to setup the scheduler for fastapi?
+ How to enable the scheduler via the lifetime hook?
  + Every 60 seconds health check
  + Every 24:00 fill up daily user AI tokens
+ How to trigger scheduling via API?
  + Endpoint for send an offer to a single whatsapp contact
  + Endpoint for sending an offer to a whatsapp group with multiple contacts
    + The Endpoint has the delay parameter in minutes and a repetition count
+ Why not the fastapi inbuilt background task?
+ Summary
