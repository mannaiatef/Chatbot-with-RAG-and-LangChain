# Chatbot with RAG and LangChain

Un chatbot intelligent alimenté par **Retrieval-Augmented Generation (RAG)** et **LangChain**, capable de répondre à des questions basées sur des documents PDF personnalisés. 🚀 **100% LOCAL** avec Ollama et Mistral !

## 🎯 Caractéristiques

- **RAG (Retrieval-Augmented Generation)** : Combine recherche de documents et génération de réponses
- **LangChain** : Framework puissant pour construire des applications LLM
- **Chroma Vector Database** : Stockage et recherche efficace d'embeddings
- **Ollama + Mistral** : LLM local gratuit, sans API (100% privé) 🔒
- **HuggingFace Embeddings** : Embeddings locaux gratuits (sentence-transformers) 💰
- **Interface Gradio** : Interface web intuitive et conviviale
- **Support PDF** : Charge et traite automatiquement les fichiers PDF
- **Sans coûts** : Aucune clé API requise, tout s'exécute localement

## 📋 Prérequis

- **Python 3.10+** (recommandé 3.11+)
- **Ollama** - Téléchargez depuis [ollama.ai](https://ollama.ai)
- **Git** (pour cloner le repository)

### Installation d'Ollama

1. **Téléchargez Ollama** : https://ollama.ai
2. **Installez-le** selon votre OS
3. **Téléchargez le modèle Mistral** :
   ```bash
   ollama pull mistral
   ```
4. **Vérifiez l'installation** :
   ```bash
   ollama list
   ```

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

### 4. Configuration (Optionnelle)

**Aucune clé API requise !** Tout s'exécute localement.

⚠️ **Important** : Assurez-vous qu'Ollama est en cours d'exécution avant de lancer le chatbot :
```bash
# Sur Windows/macOS/Linux, vérifiez qu'Ollama s'exécute sur le port 11434
curl http://localhost:11434
```

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
- Crée des embeddings locaux avec HuggingFace (sentence-transformers)
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
# Modèle d'embeddings local (GRATUIT)
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Modèle de langage local (Ollama + Mistral)
llm = Ollama(model="mistral", temperature=0.5)

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

### Erreur : "Connection refused" ou "Failed to connect to Ollama"

**Solution :**
1. Vérifiez qu'Ollama est installé depuis [ollama.ai](https://ollama.ai)
2. Lancez Ollama (il devrait s'exécuter en arrière-plan)
3. Vérifiez qu'il est accessible : `curl http://localhost:11434`
4. Assurez-vous que le modèle Mistral est téléchargé : `ollama pull mistral`

### Erreur : "Model 'mistral' not found"

**Solution :**
```bash
# Téléchargez le modèle Mistral
ollama pull mistral

# Vérifiez qu'il est disponible
ollama list
```

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

### Performance lente du chatbot

**Solutions :**
1. Assurez-vous qu'Ollama a suffisamment de mémoire RAM
2. Réduisez la taille des chunks dans `ingest_database.py`
3. Diminuez le nombre de résultats de recherche (`num_results`)

## 📊 Flux de travail du RAG

```
PDF Documents
     ↓
PyPDFDirectoryLoader (Chargement)
     ↓
RecursiveCharacterTextSplitter (Division en chunks)
     ↓
HuggingFace Embeddings (Conversion en vecteurs) ✅ LOCAL & GRATUIT
     ↓
Chroma Vector Store (Stockage)
     ↓
[Lors d'une question utilisateur]
     ↓
Similarity Search (Recherche des chunks pertinents)
     ↓
LLM Prompt Engineering (Construction du contexte)
     ↓
Ollama + Mistral (Génération de réponse) ✅ LOCAL & GRATUIT
     ↓
Gradio UI (Affichage au utilisateur)
```

## 🔐 Sécurité

- ✅ **100% LOCAL** : Aucune donnée n'est envoyée à des serveurs externes
- ✅ **Pas de clé API** : Aucune exposition de credentials
- ✅ **Données privées** : Tout reste sur votre ordinateur
- Utilisez un `.gitignore` pour exclure les dossiers sensibles
- Limitez l'accès au dossier `chroma_db` contenant les embeddings

## 🛠️ Technologies Utilisées

| Technologie | Version | Utilisation | Coût |
|-------------|---------|-------------|------|
| LangChain | 0.3.23 | Framework RAG et gestion LLM | Gratuit |
| Ollama | Latest | Exécution locale de Mistral | Gratuit |
| Mistral | 7B | Modèle LLM local | Gratuit |
| HuggingFace Embeddings | 3.0.1 | Embeddings locaux | Gratuit 💰 |
| Chroma | 0.6.3 | Base de données vectorielle | Gratuit |
| Gradio | 5.25.1 | Interface web | Gratuit |
| LangChain Chroma | 0.2.3 | Intégration Chroma | Gratuit |
| PyPDF | 5.4.0 | Traitement de fichiers PDF | Gratuit |
| Python Dotenv | 1.1.0 | Gestion variables d'environnement | Gratuit |

## 💰 Coût Total

**$0.00** 🎉 - Aucun frais de API, tout s'exécute localement !

## 📝 Améliorations Futures

- [ ] Support de multiples formats (DOCX, TXT, etc.)
- [ ] Historique conversationnel persistant
- [ ] Interface d'upload de fichiers
- [ ] Filtrage par métadonnées
- [ ] Autres modèles Ollama (Llama2, Neural Chat, etc.)
- [ ] Mode batch pour traitement multiple


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
