$(document).ready(function () {
  const urlParams = new URLSearchParams(window.location.search);
  const sessionId = urlParams.get("session_id");
  const projectName = urlParams.get("name") || "Unnamed";

  $("#chat-project-name").text(`Project: ${projectName}`);

  $("#sendBtn").click(async function () {
    const question = $("#chatInput").val().trim();
    if (!question) return;

    $("#chat-window").append(`<div class="message user">🧑‍💻 ${question}</div>`);
    $("#chatInput").val("");

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: question,
          session_id: sessionId,
        }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Error fetching response");
      }

      const result = await response.json();
      $("#chat-window").append(`<div class="message bot">🤖 ${result.answer}</div>`);
    } catch (err) {
      console.error(err);
      $("#chat-window").append(`<div class="message bot error">⚠️ ${err.message}</div>`);
    }

    $("#chat-window").scrollTop($("#chat-window")[0].scrollHeight);
  });
});
