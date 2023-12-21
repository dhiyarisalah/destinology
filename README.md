# CC Repository - Destinology (Team CH2-PS397)

Member of Cloud Computing 
| Member | Student ID | University |
|:------:|:----------:|:----------:|
| Dhiya Risalah Ghaida | C002BSX3682 | Bandung Institute of Technology |
| Kofifan Hertza Haribowo | C002BSY3540 | Bandung Institute of Technology |

## About Our API
Our API designed using **FastAPI** for its efficiency and ease of maintenance. We've chosen **OAuth2** as our security framework for its robustness in handling authorization in a secure manner. This module utilizes token bearer authentication, a method where access tokens are pivotal in validating and managing user sessions.

## User Authentication 
 A key component of our authentication process is the integration with Firebase Authentication. This integration leverages Firebase's advanced features to handle user credentials securely, including the management of sensitive data like password hashing. This authentication system is part of a broader set of services provided by our API, ensuring both security and functionality for various application needs. Here is the detail of users's the stored data on firestore database:
 
 - User Data
     - Created time (number): records the timestamp when the user account was created.
	 - Email (string): Stores the user's email address.
     - User name (string): Contains the user's chosen username.
     - Full name (string): Holds the full name of the user.
 
### Endpoints
- **'/auth/signup'**
Register a new user with email and password, storing user data in Firestore.

- **'/auth/signin'**
Authenticate an existing user, providing access via token-based session management.

## User Data Management
User Data Management is a crucial facet of our API, designed to provide users with complete control over their personal information. This system allows users to securely access, update, and delete their personal data, including details such as their full name, username, email address, and the time their account was created. With a focus on privacy and security, this module ensures that all user information is handled with confidentiality and integrity that providing a trustworthy environment for managing personal data.

### Endpoints
- **'/users/me'**
Retrieve the current user's profile data.

- **'/users/update'**
Update existing user profile information.

- **'/users/delete'**
Delete a user's account and associated data.


## Models
## Itinerary Planner 
The Itinerary Planner is an innovative feature of our API, designed to simplify and enhance the travel planning experience. It offers users the ability to create their travel itineraries with ease. This planner not only assists in organizing trips but also includes functionality for automatic itinerary generation based on user preferences such as city, duration, and price. The Itinerary Planner is an indispensable tool for travelers seeking a hassle-free and personalized way to plan their journeys.

### Endpoints
- **'/models/itinerary'**
Automatically generate a travel itinerary based on user preferences.

- **'/models/itinerary-generate'**
Regenerating parts of a travel itinerary that do not align with the user's preferences

## Landmark Prediction 
Landmark Prediction is an advanced feature of our API that leverages image recognition to identify and provide detailed information about landmarks. This tool is designed for users who wish to learn more about specific landmarks or explore their surroundings through images. By analyzing input from the user, it offers insightful and accurate information about various landmarks, enhancing the user's understanding and experience of different cultural and historical sites.

### Endpoints
- **'/models/landmark'**
Predict and provide details about landmarks in images or descriptions.

## Others   
- **'/auth/logout'**
Deleting the user's session token

## Deployment
**are deployed on Google Cloud Platform Compute Engine.**
Here is the detailed specification of  the compute engine used for deployment.

| Item | Specification |
|:-----:|:------------:|
| Type | Instance |
| Zone | asia-southeast2-a |
| Machine type | e2-medium |
| CPU Platform | Intel Broadwell |
| Architecture | x86/64 |
| Boot Disk | debian-11-bullseye |

## Run the API in GCP Compute Engine
To set up the environment required by the APIs and AI-Model that will be deployed, follow this step.

 1. Create a VM Instance with the exact specification above
 2. Create a firewall to enable tcp in port:8000
 3. Run this code
```
! sudo apt update
```
```
! sudo apt install git
```
```
! sudo apt-get install python3-pip
```
```
! git clone https://github.com/dhiyarisalah/destinology.git
```
```
! cd destinology
```
```
! pip3 install -r requirements.txt
```
4. After that run this code to start the server
```
! python3 main-api.py
```
5. Or this code to keep the program running
```
! nohup python3 main-api.py &
```

Thank you :)