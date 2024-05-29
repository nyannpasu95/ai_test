/*global fetch*/

async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const response = await fetch('https://989r1licmb.execute-api.ap-northeast-1.amazonaws.com/v1/chat', {
        method: 'POST',
        body: JSON.stringify({ message: userMessage }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (!response.ok) {
        console.error('Network response was not ok', response.statusText);
        return;
    }

    // Assuming the response is plain text
    const data = await response.text();
    const chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatbox.innerHTML += `<p><strong>Bot:</strong> ${data}</p>`;
    document.getElementById('userMessage').value = '';
}
