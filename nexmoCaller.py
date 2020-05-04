import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='ccfabc66-2223-47c7-a846-a6f6d72ce338',
  private_key='path\\private.key',
)
ncco = [
  {
    'action': 'talk',
    'voiceName': 'Jacek',
    'text': '''
Przykładowy tekst do powiezenia
'''
  }
]
response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '48'
  }],
  'from': {
    'type': 'phone',
    'number': '48507214973'
  },
  'ncco': ncco
})

pprint(response)
