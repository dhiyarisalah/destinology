# Destinology-CC Repository (# Team CH2-PS397)
Member of Cloud Computing 
| Member | Student ID | University |
|:------:|:----------:|:----------:|
| Dhiya Risalah Ghaida | C002BSX3682 | Bandung Institute of Technology |
| Kofifan Hertza Haribowo | C002BSY3540 | Bandung Institute of Technology |


## User authentication and user data
For the implementation of user authentication features, Destinology use **the Firebase user authentication** feature. With this feature, user registration and authentication will be handled by **Firebase**.


Data of Destinology's users will be saved on to firestore database. Here is the detail of the stored data on firestore database.
 
 - User Data
	 - Email
     - User name
     - Full name
     - Created time

 - Session Tokens

## Endpoints
Here are the endpoints used by 

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


*Note that this server will run on PEDOTAN environment and any data send or retrieve will  be from PEDOTAN firebase and PEDOTAN cloud storage.