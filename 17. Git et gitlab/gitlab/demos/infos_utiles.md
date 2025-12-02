## Variables :

Settings => CI/CD => variables => add Variables

MA_VARIABLE_SECRETE

- Cochez "protected variable" (seulement sur les branches protégées)
- Cochez "Masked variables" (non visible dans les logs)

1. DOCKERHUB_USERNAME :
    - protected : True
    - Masked: False

2. DOCKERHUB_PASSWORD
    - protected : True
    - Masked: True