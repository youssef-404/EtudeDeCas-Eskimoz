## Configuration

1. Créez un compte de service dans Google Cloud Platform et téléchargez le fichier JSON des informations d'identification.
2. Renommez le fichier `.env.example` en `.env` et mettez à jour le chemin vers votre fichier de clé JSON .
3. Ouvrez le fichier `.env` et modifiez la ligne pour inclure le chemin de votre fichier de clé JSON :

    ```plaintext
    GOOGLE_SHEETS_CREDENTIALS=path/to/your-service-account-file.json
    ```
