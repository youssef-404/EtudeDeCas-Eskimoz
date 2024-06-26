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

### Fonction 1 : Connexion à l'API Google Sheets
La fonction `connect_to_google_sheets` permet de se connecter à l'API Google Sheets.

### Fonction 2 : Analyse n-gram
Les fonctions `pre_processing`, `generate_ngrams`, et `analyze_ngrams` permettent de nettoyer le texte, générer des n-grams et analyser leur fréquence.

### Fonction 3 : Remplir un Google Sheets à partir d'un DataFrame
La fonction `dataframe_to_sheet` permet de remplir un Google Sheets avec les données d'un DataFrame.

### Exemple d'Utilisation
Le script `main.py` comprend deux exemples d'utilisation, chacun effectuant différentes analyses et mettant à jour un Google Sheet spécifique.

La fonction `example1` effectue les tâches suivantes :
1. Charge les données du fichier `data/data_science_phrases.csv`.
2. Prétraite les données textuelles en supprimant les caractères spéciaux, les chiffres et les mots courants (stopwords).
3. Génère les 15 bi-grams les plus fréquents à partir des données textuelles prétraitées.
4. Crée un DataFrame Pandas avec les bi-grams et leurs fréquences.
5. Envoie le DataFrame vers un fichier Google Sheets.

La fonction `example2` effectue les tâches suivantes :
1. Charge les données du fichier `data/news_headline.csv`.
2. Prétraite les données textuelles en supprimant les caractères spéciaux, les chiffres et les mots courants (stopwords).
3. Sépare les données en trois DataFrames distincts selon le sentiment (positif, négatif, neutre).
4. Pour chaque DataFrame, génère les 15 bi-grams les plus fréquents.
5. Crée un DataFrame Pandas en concaténant les bi-grams et leurs fréquences pour chaque sentiment.
6. Envoie le DataFrame résultant vers un fichier Google Sheets.


**Remarque** : N'oubliez pas de changer le nom du Google Sheet et le nom de la feuille dans le script avant de l'exécuter. Modifiez les appels des fonctions `example1("data_science_phrases","Sheet1")` et `example2("data_science_phrases","Sheet1")` pour correspondre aux noms de votre Google Sheet partagé.

### Exécution du script
Pour exécuter le script, utilisez la commande suivante après avoir terminé la configuration :

```bash
python main.py
```
**Remarque** : Ce script exécute l'exemple `example1()`, qui analyse des phrases de science des données à partir d'un fichier CSV. Vous pouvez également commenter `example1()` et décommenter `example2()` pour analyser les titres de nouvelles avec différents sentiments.
