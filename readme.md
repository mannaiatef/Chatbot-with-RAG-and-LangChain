# Chatbot with RAG and LangChain

Un chatbot intelligent alimenté par **Retrieval-Augmented Generation (RAG)** et **LangChain**, capable de répondre à des questions basées sur des documents PDF personnalisés.

## 🎯 Caractéristiques

- **RAG (Retrieval-Augmented Generation)** : Combine recherche de documents et génération de réponses
- **LangChain** : Framework puissant pour construire des applications LLM
- **Chroma Vector Database** : Stockage et recherche efficace d'embeddings
- **OpenAI API** : Modèles de langage avancés (GPT-4o-mini, text-embedding-3-large)
- **Interface Gradio** : Interface web intuitive et conviviale
- **Support PDF** : Charge et traite automatiquement les fichiers PDF

## 📋 Prérequis

- **Python 3.10+** (recommandé 3.11+)
- **OpenAI API Key** - Obtenez une clé sur [platform.openai.com](https://platform.openai.com/api-keys)
- **Git** (pour cloner le repository)

## 🚀 Guide d'Installation

### 1. Cloner le repository

```bash
git clone https://github.com/mannaiatef/Chatbot-with-RAG-and-LangChain.git
cd Chatbot-with-RAG-and-LangChain
```

### 2. Créer un environnement virtuel

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\Activate
```

**Sur macOS/Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet :

```bash
# Copier le fichier d'exemple si disponible
cp .env.example .env

# Ou créer manuellement
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

**⚠️ Important** : Remplacez `your-api-key-here` par votre clé OpenAI réelle.

Vous pouvez obtenir votre clé OpenAI ici : https://platform.openai.com/api-keys

## 📚 Guide d'Utilisation

### Préparation des données

1. **Créez un dossier `data`** à la racine du projet s'il n'existe pas :
   ```bash
   mkdir data
   ```

2. **Ajoutez vos fichiers PDF** dans le dossier `data` :
   ```
   data/
   ├── document1.pdf
   ├── document2.pdf
   └── ...
   ```

### Étape 1 : Ingestion des données

Avant de lancer le chatbot, ingérez vos documents PDF dans la base de données vectorielle :

```bash
python ingest_database.py
```

**Qu'est-ce que cela fait ?**
- Charge tous les fichiers PDF du dossier `data`
- Divise les documents en chunks optimisés
- Crée des embeddings avec le modèle OpenAI
- Stocke les embeddings dans Chroma DB

### Étape 2 : Lancer le chatbot

Une fois l'ingestion terminée, démarrez l'interface web :

```bash
python chatbot.py
```

**Accédez à l'interface :**
- L'application ouvrira automatiquement sur `http://127.0.0.1:7860`
- Ou accédez manuellement à cette URL dans votre navigateur

### Utilisation du chatbot

1. **Posez des questions** relatives à vos documents PDF
2. **Le chatbot récupère** les passages pertinents de votre base de données
3. **Les réponses** sont basées uniquement sur vos documents (RAG)

**Exemple :**
- Documents contient : "La photosynthèse est le processus par lequel..."
- Question : "Qu'est-ce que la photosynthèse ?"
- Réponse : Basée sur le contenu de vos documents

## 📁 Structure du Projet

```
Chatbot-with-RAG-and-LangChain/
├── chatbot.py                 # Application chatbot (interface Gradio)
├── ingest_database.py         # Script d'ingestion des documents
├── requirements.txt           # Dépendances Python
├── .env                       # Variables d'environnement (non committée)
├── .env.example               # Template pour .env
├── .gitignore                 # Fichiers à ignorer par Git
├── data/                      # Dossier pour vos documents PDF
│   └── (vos fichiers PDF)
├── chroma_db/                 # Base de données vectorielle
│   └── chroma.sqlite3
└── README.md                  # Ce fichier
```

## 🔧 Configuration Avancée

### Modifier les paramètres

Dans `chatbot.py`, vous pouvez ajuster :

```python
# Modèle d'embeddings
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Modèle de langage
llm = ChatOpenAI(temperature=0.5, model='gpt-4o-mini')

# Nombre de résultats de recherche
num_results = 5
```

Dans `ingest_database.py`, vous pouvez modifier :

```python
# Taille des chunks de texte
chunk_size=300,
# Chevauchement entre chunks
chunk_overlap=100,
```

## 🐛 Dépannage

### Erreur : "OPENAI_API_KEY environment variable is not set"

**Solution :**
1. Vérifiez que votre fichier `.env` existe à la racine du projet
2. Vérifiez qu'il contient `OPENAI_API_KEY=votre_clé`
3. Assurez-vous que votre clé est valide sur https://platform.openai.com

### Erreur : "Error code: 429 - insufficient_quota"

**Solution :**
1. Votre quota OpenAI est épuisé
2. Ajoutez un moyen de paiement : https://platform.openai.com/account/billing/overview
3. Vérifiez votre plan de facturation

### Erreur : "No documents found in data folder"

**Solution :**
1. Créez le dossier `data` s'il n'existe pas
2. Ajoutez des fichiers PDF au dossier
3. Assurez-vous que les fichiers sont en format `.pdf`

### Le chatbot n'a pas accès à mes documents

**Solution :**
1. Vérifiez que vous avez exécuté `ingest_database.py` avant de lancer `chatbot.py`
2. Supprimez le dossier `chroma_db` et réexécutez l'ingestion si les documents ont changé
3. Vérifiez les logs pour les erreurs d'ingestion

## 📊 Flux de travail du RAG

```
PDF Documents
     ↓
PyPDFDirectoryLoader (Chargement)
     ↓
RecursiveCharacterTextSplitter (Division en chunks)
     ↓
OpenAI Embeddings (Conversion en vecteurs)
     ↓
Chroma Vector Store (Stockage)
     ↓
[Lors d'une question utilisateur]
     ↓
Similarity Search (Recherche des chunks pertinents)
     ↓
LLM Prompt Engineering (Construction du contexte)
     ↓
ChatOpenAI (Génération de réponse)
     ↓
Gradio UI (Affichage au utilisateur)
```

## 🔐 Sécurité

- **Ne committez jamais votre fichier `.env`** avec votre clé API
- Utilisez un `.gitignore` pour exclure `.env`
- Utilisez des secrets ou variables d'environnement en production
- Limitez vos clés API aux permissions minimales nécessaires

## 🛠️ Technologies Utilisées

| Technologie | Version | Utilisation |
|-------------|---------|-------------|
| LangChain | 0.3.23 | Framework RAG et gestion LLM |
| OpenAI API | 1.74.0 | Modèles de langage et embeddings |
| Chroma | 0.6.3 | Base de données vectorielle |
| Gradio | 5.25.1 | Interface web |
| LangChain Chroma | 0.2.3 | Intégration Chroma |
| PyPDF | 5.4.0 | Traitement de fichiers PDF |
| Python Dotenv | 1.1.0 | Gestion variables d'environnement |

## 📝 Améliorations Futures

- [ ] Support de multiples formats (DOCX, TXT, etc.)
- [ ] Historique conversationnel persistant
- [ ] Interface d'upload de fichiers
- [ ] Filtrage par métadonnées
- [ ] Modèles locaux alternatifs
- [ ] Mode batch pour traitement multiple
- [ ] API REST pour intégrations externes

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Support

Pour toute question ou problème :
1. Consultez la section [Dépannage](#-dépannage)
2. Vérifiez les issues GitHub existantes
3. Créez une nouvelle issue si besoin

## 🎓 Ressources Utiles

- [Documentation LangChain](https://python.langchain.com/)
- [Documentation OpenAI](https://platform.openai.com/docs/)
- [Documentation Chroma](https://docs.trychroma.com/)
- [Documentation Gradio](https://www.gradio.app/docs/)
- [RAG - Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)

---

**Créé avec ❤️ pour faciliter l'interaction avec vos documents**
