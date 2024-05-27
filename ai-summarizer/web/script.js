/*global fetch*/

async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const response = await fetch('https://4y5jz8k57d.execute-api.ap-northeast-1.amazonaws.com/v1/chat', {
        method: 'POST',
        body: JSON.stringify({ message: userMessage }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    const chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
    document.getElementById('userMessage').value = '';
}
