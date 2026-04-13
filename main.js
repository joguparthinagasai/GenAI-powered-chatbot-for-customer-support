(function () {
  const chatWindow = document.getElementById("chat-window");
  const input = document.getElementById("msg");
  const sendBtn = document.getElementById("sendBtn");

  const ws = new WebSocket(`ws://${location.host}/ws/chat`);

  ws.onopen = () => addBot("Welcome to GENAI Bike Chatbot 🚴");

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    addBot(data.text);
  };

  function addUser(text) {
    const div = document.createElement("div");
    div.className = "msg user";
    div.innerText = text;
    chatWindow.appendChild(div);
  }

  function addBot(text) {
    const div = document.createElement("div");
    div.className = "msg bot";
    div.innerText = text;
    chatWindow.appendChild(div);
  }

  sendBtn.onclick = () => {
    const text = input.value;
    addUser(text);

    ws.send(JSON.stringify({ text }));

    input.value = "";
  };
})();