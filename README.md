## Description

Ce projet est un assistant vocal nommé Sophie. Elle est basée sur l'API OpenAI et utilise la reconnaissance vocale de Google pour transformer la voix en texte et pyttsx3 pour transformer le texte en voix. L'assistant vocal est capable d'effectuer des actions en fonction des instructions reçues, de sauvegarder des informations en mémoire et de gérer des fichiers texte.

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante :

pip install -r requirements.txt

## Configuration

Créez un fichier .env à la racine du projet avec les clés d'API OpenAI et les autres paramètres nécessaires. Voici un exemple de fichier .env :

### Utilisation

Pour utiliser Sophie, exécutez le fichier principal :

python gpt_speech.py

Sophie est initialement en mode d'écoute passive. Pour activer Sophie, dites "Sophie" dans votre phrase, par exemple : "Hey Sophie, ça va ?". Une fois activée, Sophie écoutera et répondra à vos instructions.

## Fonctions principales

Reconnaissance vocale : Sophie écoute et transcrit vos paroles en texte.

Génération de réponse : Sophie génère une réponse appropriée à partir du texte reçu.

Texte en parole : Sophie convertit la réponse générée en parole.

Actions : Sophie peut effectuer différentes actions, telles que rafraîchir la conversation, sauvegarder des informations dans un fichier texte ou en mémoire.

## Licence

Ce projet est sous licence MIT.
