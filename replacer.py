import sys

if sys.version_info[0] == 3:
	from io import StringIO
else:
	from cStringIO import StringIO


def replace_entities(text, grouped_entities, **replacers):
	entities = []
	for entity_type, entity_list in grouped_entities.items():
		replacer = replacers.get(entity_type)
		if replacer is None:
			continue
		for entity in entity_list:
			entity_pair = (entity['indices'], replacer(entity))
			entities.append(entity_pair)

	entities.sort(key = lambda x: x[0][0])

	output = StringIO()
	last_idx = 0

	for entity_pair in entities:
		indices, entity = entity_pair

		i, last_idx = indices

		output.write(text[: i])
		output.write(entity)


	output.write(text[last_idx :])

	return output.getvalue()

def tweet_replace_links(tweet):
	def url_replacer(url):
		return '<a href="%s">%s</a>' % (url['expanded_url'], url['display_url'])

	return replace_entities(tweet['text'].encode('utf-8'), tweet['entities'], urls = url_replacer)