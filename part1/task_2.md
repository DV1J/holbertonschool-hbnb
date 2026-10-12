User Registration :-

sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (Register User/ user details)
API->>BusinessLogic: Validate(user data) and Process Request
BusinessLogic->>Database: check if User is already in Database
Note over BusinessLogic: User in Database
Database-->>BusinessLogic: User already in Database
BusinessLogic-->>API: Return Reponse
API-->>User: Return Error(Account already exists)
Note over BusinessLogic: User not in Database
Database-->>BusinessLogic: User not in Database
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Created / Error

Place Creation:-

sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (User enters Place details)
API->>BusinessLogic: Validate(Place data) and Process Request
BusinessLogic->>Database: check if User is already in Database
Note over BusinessLogic: User not in Database
Database-->>BusinessLogic: User not Registered
BusinessLogic-->>API: Return Reponse
API-->>User: Please Register your account
Note over BusinessLogic: User in Database
Database-->>BusinessLogic: User in Database
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Place Created

Review Submission:-

sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call(User Submits Review for a place)
API->>BusinessLogic: Validate(Review data) and Process Request
BusinessLogic->>Database: Checks for User and Place Data in database
Note over BusinessLogic: User not in Database
Database-->>BusinessLogic:User not in Database
BusinessLogic-->>API: Return Response
API-->>User: Please Register your account to leave a Review
Note over BusinessLogic: Place not in Database
Database-->>BusinessLogic: Place not found
BusinessLogic-->>API: Return Response
API-->>User: Return: Plcae not found
Note over BusinessLogic: User and Place in Database
Database-->>BusinessLogic: User and Place in Database
BusinessLogic->>Database: Save Review
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Review Created

Fetching a lish of places:-

sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call(User Enters Criteria they are looking for)
API->>BusinessLogic: Validate(Criteria data) and Process Request
BusinessLogic->>Database: Checks for places that matches the criteria in database
Note over BusinessLogic: No place found in Database
Database-->>BusinessLogic:No place found in Database
BusinessLogic-->>API: Return Response
API-->>User: No Place found
Note over BusinessLogic: Found Place that matches in Database
Database-->>BusinessLogic: Found places that matchs criteria
BusinessLogic-->>API: Return Response
API-->>User: Return: List of Places