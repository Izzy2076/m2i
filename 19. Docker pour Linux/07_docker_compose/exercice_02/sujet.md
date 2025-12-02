### Services à intégrer

1. **Base de données**

   - Image : `mysql:8.0`
   - Nom de base à créer : `employee`
   - Volume de persistance à ajouter
   - nom du service : db

2. **PhpMyAdmin**

   - Image : `phpmyadmin:latest`
   - Interface accessible via navigateur

3. **Backend (Spring Boot)**

   - Construit depuis le dossier `./back_employee`
   - Communique avec MySQL => depends_on : db
   - Variables d'environment :
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/employee
      SPRING_DATASOURCE_USERNAME: root
      SPRING_DATASOURCE_PASSWORD: root

4. **Frontend (React)**

   - Construit depuis le dossier `./front_employee`
   - Communique avec le backend
