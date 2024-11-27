fetch('http://127.0.0.1:5000/query-model', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: 'Hello, can you explain how to use your API?' }),
})
    .then(response => response.json())
    .then(data => {
        console.log('Response from Ollama model:', data.response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
