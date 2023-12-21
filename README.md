# CC Repository - Destinology (Team CH2-PS397)

Member of Cloud Computing 
| Member | Student ID | University |
|:------:|:----------:|:----------:|
| Dhiya Risalah Ghaida | C002BSX3682 | Bandung Institute of Technology |
| Kofifan Hertza Haribowo | C002BSY3540 | Bandung Institute of Technology |

## About Our API
Our API designed using **FastAPI** for its efficiency and ease of maintenance. We've chosen **OAuth2** as our security framework for its robustness in handling authorization in a secure manner. This module utilizes token bearer authentication, a method where access tokens are pivotal in validating and managing user sessions.

## User Authentication 
 A key component of our authentication process is the integration with Firebase Authentication. This integration leverages Firebase's advanced features to handle user credentials securely, including the management of sensitive data like password hashing. This authentication system is part of a broader set of services provided by our API, ensuring both security and functionality for various application needs. Here is the detail of users's the stored data on firestore database.
 
 - User Data
     - Created time (number)
	 - Email (string)
     - User name (string)
     - Full name (string)
 
### Endpoints
Here are the authentication endpoints used by Destinology:

 - **'/auth/signup'**
- **'/auth/signin'**

## User Data

### Endpoints
- **'/users/me'**

- **'/users/update'**

- **'/users/delete'**

## Models
## Itinerary Planner 

### Endpoints
- **'/models/itinerary'**

- **'/models/itinerary-generate'**

## Landmark Prediction 
- **'/models/landmark'**

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