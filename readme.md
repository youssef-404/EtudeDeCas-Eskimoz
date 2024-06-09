# Étude de Cas : Analyse de texte et intégration avec Google Sheets

Ce projet contient des scripts Python pour effectuer une analyse n-gram sur des données textuelles et pour intégrer ces données avec Google Sheets via l'API Google Sheets.

## Configuration

1. **Créer un projet sur Google Cloud Platform et activer l'API Google Sheets**
    - Allez sur [Google Cloud Console](https://console.cloud.google.com/).
    - Créez un nouveau projet.
    - Activez l'API Google Sheets et l'API Google Drive pour ce projet.
    - Créez des informations d'identification pour un compte de service et téléchargez le fichier de clé JSON.

2. **Partager le Google Sheet avec le compte de service**

    - Ouvrez le Google Sheet que vous souhaitez utiliser.
    - Cliquez sur "Partager".
    - Partagez le Google Sheet avec l'adresse email du compte de service trouvée dans le fichier JSON des informations d'identification.

3. **Configurer l'environnement Python**
    ```bash
    pip install -r requirements.txt
    ```

4. **Renommez le fichier `.env.example` en `.env` et mettez à jour le chemin vers votre fichier de clé JSON**

    ```plaintext
    GOOGLE_SHEETS_CREDENTIALS=path/to/your-service-account-file.json
    ```

## Utilisation

Le script effectuera les tâches suivantes :

1. Connexion à l'API Google Sheets.
2. Analyse des n-grams sur les données textuelles et affichage n-grams les plus fréquents.
3. Remplissage d'un fichier Google Sheets spécifique avec les données du DataFrame.

## Données

Le fichier `data/data_science_phrases.csv` contient les données textuelles
