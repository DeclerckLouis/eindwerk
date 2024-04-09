# Archived: GitLab CI/CD
## Why was it chosen?
GitLab CI/CD was chosen because it was the main CI/CD tool used in the company.  
It was also chosen because it was easy to setup and had a lot of integrations with GitLab itself. (Webhooks, etc.)  

## Why was it abandoned?  
The idea of using GitLab CI/CD as the main triggering system was abandoned because it was too complex for the current state of the project.  
When saying too complex, I don't mean it in the sense that it was complex to learn or understand, but in the sense that it required a lot of extra "secrets" management.  
It will most likely be introduced again in the future, once a centralized secret management system is in place. (HashiCorp Vault, most likely).  
In the current state of the project, every integration works with ansible-vault encrypted variables, which are only decrypted when needed.  
For more information, please refer to the [[RoadMap]].