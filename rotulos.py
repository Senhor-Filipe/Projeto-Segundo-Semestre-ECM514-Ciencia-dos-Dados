import requests
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

# Carregar os embeddings e rótulos previamente salvos
with open('embeddings.pkl', 'rb') as f:
    embeddings, labels = pickle.load(f)

# Carregar o modelo pré-treinado para embeddings
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")


def get_new_wikipedia_page_content(new_page_title):
    """
    Extrai o conteúdo da nova página da Wikipédia pelo título da página.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'explaintext': True,
        'titles': new_page_title
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data['query']['pages'].values()))
        return page.get('extract', None)
    else:
        return None


def get_embedding(new_text):
    """
    Obtém o embedding do texto usando um modelo pré-treinado.
    """
    inputs = tokenizer(new_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding


def calcular_similaridade(new_page_title):
    """
    Calcula a similaridade entre o texto da nova página e os embeddings existentes.
    """
    new_text = get_new_wikipedia_page_content(new_page_title)
    if not new_text:
        return None, None, None

    new_embedding = get_embedding(new_text)
    similarities = cosine_similarity([new_embedding], embeddings)

    # Rótulo sugerido
    most_similar_index = similarities.argmax()
    suggested_label = labels[most_similar_index]
    suggested_similarity = similarities[0, most_similar_index]

    # Top 10 rótulos mais similares
    top_indices = similarities.argsort()[0][-10:][::-1]
    top_labels = [labels[i] for i in top_indices]
    top_similarities = [similarities[0, i] for i in top_indices]

    return suggested_label, suggested_similarity, (top_labels, top_similarities)
