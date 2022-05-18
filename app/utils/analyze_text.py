from google.cloud import language_v1

def sample_analyze_entities(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    sentiment = client.analyze_sentiment(request={'document': document})

    entities_result = []
    for entity in response.entities:
        text_info = {
            'name': entity.name,
            'type': language_v1.Entity.Type(entity.type_).name,
            'salience': round(entity.salience * 100, 4),
            'metadata': []
        }

        for metadata_name, metadata_value in entity.metadata.items():
            if metadata_name != 'mid':
                text_info['metadata'].append({
                    'name': ' '.join(metadata_name.split('_')),
                    'value': metadata_value
                })
        
        entities_result.append(text_info)
    
    return {
        'sentiment': round(sentiment.document_sentiment.score * 100, 4),
        'magnitude': round(sentiment.document_sentiment.magnitude, 4),
        'entities': entities_result
    }
