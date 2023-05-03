## Description

Ce projet est un assistant vocal nommé Sophie. Elle est basée sur l'API OpenAI et utilise la reconnaissance vocale de Google pour transformer la voix en texte et pyttsx3 pour transformer le texte en voix. L'assistant vocal est capable d'effectuer des actions en fonction des instructions reçues, de sauvegarder des informations en mémoire et de gérer des fichiers texte.

This project is a voice assistant named Sophie. It is based on the OpenAI API and uses Google speech recognition to turn voice into text and pyttsx3 to turn text into voice. The voice assistant is able to perform actions according to the instructions received, save information in memory and manage text files.

## Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante :

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Créez un fichier .env à la racine du projet avec les clés d'API OpenAI et les autres paramètres nécessaires. Vous pouvez utiliser le fichier .env.example comme modèle :

Create an .env file in the root of the project with the OpenAI API keys and other necessary settings. You can use the .env.example file as a template:

```bash
OPENAI_API='API_Key'
NAME='Sophie'
CHARACTER_PROMPT='Ton personnage et ses caractéristiques | Your character and its characteristics'
RULES_PROMPT='Les règles pour votre personnage | The rules for your character'
MEMORY=True
SPEECH_LANGAGE='fr-FR | en-US'
```

## Utilisation

Pour utiliser Sophie, exécutez le fichier principal :

To use Sophie, run the main file:

```bash
python gpt_speech.py
```

Sophie est initialement en mode d'écoute passive. Pour activer Sophie, dites "Sophie" dans votre phrase, par exemple : "Hey Sophie, ça va ?". Une fois activée, Sophie écoutera et répondra à vos instructions.

Sophie is initially in passive listening mode. To activate Sophie, say "Sophie" in your sentence, for example: "Hey Sophie, how are you?". Once activated, Sophie will listen and respond to your instructions.

## Fonctions principales

Reconnaissance vocale : Sophie écoute et transcrit vos paroles en texte.
Speech recognition: Sophie listens and transcribes your words into text.

Génération de réponse : Sophie génère une réponse appropriée à partir du texte reçu.
Response generation: Sophie generates an appropriate response from the received text.

Texte en parole : Sophie convertit la réponse générée en parole.
Text to Speech: Sophie converts the generated response into speech.

Actions : Sophie peut effectuer différentes actions, telles que rafraîchir la conversation, sauvegarder des informations dans un fichier texte ou en mémoire.
Actions: Sophie can perform different actions, such as refreshing the conversation, saving information in a text file or in memory.