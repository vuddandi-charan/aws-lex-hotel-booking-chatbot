                   ┌───────────────────────┐
                   │        USER           │
                   │  Web / Mobile Client  │
                   └──────────┬────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │      Amazon Lex V2 Bot      │
                │ (Hotel Booking Chatbot)     │
                └──────────┬─────────────────┘
                           │  (Fulfillment Call)
                           ▼
         ┌─────────────────────────────────────────┐
         │             AWS Lambda                   │
         │  • Handles slot validation               │
         │  • Processes booking logic               │
         │  • Builds final response                 │
         └───────────┬────────────────────────────┘
                     │
                     │ Logs / Errors / Monitoring
                     ▼
        ┌───────────────────────────────────────────┐
        │             Amazon CloudWatch              │
        │  • Lambda Logs                             │
        │  • Error Tracking                           │
        │  • Monitoring & Metrics                     │
        └────────────────────────────────────────────┘


                (Optional Future Enhancement)
                           │
                           ▼
        ┌────────────────────────────────────────────┐
        │                DynamoDB Table               │
        │   • Save Booking History                    │
        │   • Retrieve previous bookings              │
        └────────────────────────────────────────────┘
