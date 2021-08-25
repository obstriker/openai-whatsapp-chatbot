OpenAI Chatbot
==============================

A chatbot that uses the OpenAI API to leverage the power of their famous transformer-based language models such as GTP3 and Codex to reply to incoming messages from whatsapp or via http

Requires a valid key to OpenAI's API and access to their GTP3 or Codex engines.

Usage
---------

### Run from the command line:

To start the application that works with whatsapp: (requires a Twillio auth key)

```bash
python3 -m app whatsapp-app
```

To start the HTTP application:

```bash
python3 -m app webapp
```

### Run with Docker:

```bash
docker run container
```


--------